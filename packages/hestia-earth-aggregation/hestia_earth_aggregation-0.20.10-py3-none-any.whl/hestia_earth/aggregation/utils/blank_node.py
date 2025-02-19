from typing import List
from functools import reduce
from hestia_earth.schema import SchemaType
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.tools import non_empty_list, flatten, list_sum, is_number

from hestia_earth.aggregation.log import logger
from hestia_earth.aggregation.site.management import aggregated_dates
from . import pick, match_dates
from .term import should_aggregate


def _formatDepth(depth: str):
    # handle float values
    return str(int(depth)) if is_number(depth) else ''


def default_missing_value(term: dict):
    # value can be string, number or boolean
    # use lookup `valueType` to determine which value to add
    lookup = download_lookup(f"{term.get('termType')}.csv")
    value_type = get_table_value(lookup, 'termid', term.get('@id'), column_name('valueType'))
    return {'boolean': False}.get(value_type, 0)


def _blank_node_dates(blank_node: dict):
    return aggregated_dates(blank_node) if blank_node.get('@type') == SchemaType.MANAGEMENT.value else (
        pick(blank_node, ['startDate', 'endDate'])
    )


def group_blank_nodes(nodes: list):
    """
    Group a list of blank nodes using:
    - `termType`
    - the `depthUpper` and `depthLower`
    - the `startDate` and `endDate`
    - the lookup group `sumMax100Group` or `sumIs100Group` or `booleanGroup` if specified

    Parameters
    ----------
    nodes : list
        List of blank nodes with their index.
    """
    def group_by(group: dict, blank_node: dict):
        term = blank_node.get('term', {})
        term_type = term.get('termType')
        lookup = download_lookup(f"{term_type}.csv")
        sum_below_100_group = get_table_value(lookup, 'termid', term.get('@id'), column_name('sumMax100Group')) \
            if lookup is not None else None
        sum_equal_100_group = get_table_value(lookup, 'termid', term.get('@id'), column_name('sumIs100Group')) \
            if lookup is not None else None
        boolean_group = get_table_value(lookup, 'termid', term.get('@id'), column_name('booleanGroup')) \
            if lookup is not None else None

        keys = non_empty_list([
            term_type,
            _formatDepth(blank_node.get('depthUpper')),
            _formatDepth(blank_node.get('depthLower')),
            blank_node.get('startDate'),
            blank_node.get('endDate'),
            sum_below_100_group,
            sum_equal_100_group,
            boolean_group
        ])
        key = '-'.join(keys)

        group[key] = group.get(key, []) + [{
            'key': key,
            'node': blank_node,
            'sumMax100Group': sum_below_100_group,
            'sumIs100Group': sum_equal_100_group,
            'booleanGroup': boolean_group
        }]

        return group

    return reduce(group_by, nodes, {})


def _filter_by_array_treatment(blank_node: dict):
    term = blank_node.get('term', {})
    lookup = download_lookup(f"{term.get('termType')}.csv")
    value = get_table_value(lookup, 'termid', term.get('@id'), column_name('arrayTreatmentLargerUnitOfTime'))
    # ignore any blank node with time-split data
    return not value


def _filter_needs_depth(blank_node: dict):
    term = blank_node.get('term', {})
    lookup = download_lookup(f"{term.get('termType')}.csv")
    needs_depth = get_table_value(lookup, 'termid', term.get('@id'), column_name('recommendAddingDepth'))
    return not needs_depth or all([blank_node.get('depthUpper') is not None, blank_node.get('depthLower') is not None])


def _missing_blank_node(node_type: str, term_type: str, term_id: str, units: str):
    term = {'@type': 'Term', 'termType': term_type, '@id': term_id, 'units': units}
    return {
        '@type': node_type,
        'term': term,
        'value': [default_missing_value(term)]
    }


def _add_missing_blank_nodes(blank_nodes: List[dict]):
    existing_ids = [v.get('node').get('term', {}).get('@id') for v in blank_nodes]
    group_id = blank_nodes[0].get('sumIs100Group')
    blank_node = blank_nodes[0].get('node')
    node_type = blank_node.get('@type')
    term = blank_node.get('term', {})
    term_type = term.get('termType')
    units = term.get('units')
    lookup = download_lookup(f"{term_type}.csv")
    term_ids = list(lookup[lookup[column_name('sumIs100Group')] == group_id].termid)
    missing_term_ids = [term_id for term_id in term_ids if term_id not in existing_ids]
    return [
        _missing_blank_node(node_type, term_type, term_id, units) | pick(blank_node, ['startDate', 'endDate'])
        for term_id in missing_term_ids
    ]


def _filter_grouped_nodes(blank_nodes: List[dict]):
    values = flatten([v.get('node').get('value', []) for v in blank_nodes])
    total_value = list_sum(values)
    blank_node = blank_nodes[0]
    sum_equal_100 = any([blank_node.get('sumMax100Group'), blank_node.get('sumIs100Group')])
    valid = not sum_equal_100 or 99.5 <= total_value <= 100.5
    if not valid and total_value > 0:
        logger.debug('Sum of group %s equal to %s, skipping.', blank_node.get('key'), total_value)
    # for every group that should be 100%, add all missing blank nodes in the same group with value=0
    dates = _blank_node_dates(blank_node.get('node'))
    results = [
        v.get('node') for v in blank_nodes
    ] + (
        _add_missing_blank_nodes(blank_nodes) if blank_node.get('sumIs100Group') else []
    ) if valid else []
    return [r | dates for r in results]


def filter_aggregate(blank_node: dict): return should_aggregate(blank_node.get('term', {}))


def filter_blank_nodes(blank_nodes: List[dict], start_year: int = None, end_year: int = None):
    nodes = [v for v in blank_nodes if all([
        filter_aggregate(v),
        _filter_by_array_treatment(v),
        # _filter_needs_depth(v),  # allow measurements without depths to be aggregated together
        not start_year or not end_year or match_dates(v, start_year, end_year)
    ])]

    grouped_values = group_blank_nodes(nodes)
    return flatten(map(_filter_grouped_nodes, grouped_values.values()))


def _is_value_zero(value):
    return value == [0] if isinstance(value, list) else (value == 0 or value == 0.0) if value is not None else False


def _remove_value_zero(blank_node: dict):
    term = blank_node.get('term', {})
    units = term.get('units')
    value = blank_node.get('value')
    term_type = term.get('termType')
    lookup = download_lookup(f"{term_type}.csv")
    return all([
        units == '% area',
        _is_value_zero(value)
    ]) and bool(get_table_value(lookup, 'termid', term.get('@id'), column_name('sumIs100Group')))


def cleanup_blank_nodes(blank_nodes: List[dict]):
    # remove all blank nodes with `0` as value to reduce the node count
    return list(filter(lambda v: not _remove_value_zero(v), non_empty_list(blank_nodes)))
