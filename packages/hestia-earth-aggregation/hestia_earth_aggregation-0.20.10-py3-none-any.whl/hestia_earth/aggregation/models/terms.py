from typing import List
from functools import reduce
from hestia_earth.utils.tools import non_empty_list, flatten, list_sum, safe_parse_float
from hestia_earth.utils.blank_node import get_node_value
from hestia_earth.utils.model import find_term_match
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.api import download_hestia

from hestia_earth.aggregation.log import logger
from hestia_earth.aggregation.utils import weighted_average, _min, _max, _sd, pick, sum_data
from hestia_earth.aggregation.utils.blank_node import default_missing_value
from hestia_earth.aggregation.utils.completeness import blank_node_completeness_key
from hestia_earth.aggregation.utils.emission import get_method_tier
from hestia_earth.aggregation.site.management import aggregated_dates

_DRY_MATTER_TERM_ID = 'dryMatter'


def _debugNodes(nodes: list):
    for node in nodes:
        if node.get('yield'):
            logger.debug(
                'id=%s, yield=%s, weight=%s, ratio=%s/%s, organic=%s, irrigated=%s',
                node.get('@id'),
                round(node.get('yield')),
                100/len(nodes),
                1,
                len(nodes),
                node.get('organic'),
                node.get('irrigated')
            )


def _term_lookup_dm(term: dict):
    lookup = download_lookup(f"{term.get('termType')}-lookup.csv")
    return safe_parse_float(get_table_value(lookup, 'termid', term.get('@id'), column_name(_DRY_MATTER_TERM_ID)))


def _term_dm(term: dict):
    data = download_hestia(term.get('@id'))
    return safe_parse_float(find_term_match(data.get('defaultProperties', []), _DRY_MATTER_TERM_ID).get('value'))


def _rescale_product_value_dm(node: dict, value: float):
    # for products with the `dryMatter` property, need to rescale using our default value
    node_dm = safe_parse_float(find_term_match(node.get('properties', []), _DRY_MATTER_TERM_ID).get('value'))
    default_dm = (_term_lookup_dm(node.get('term', {})) or _term_dm(node.get('term', {}))) if node_dm else 0
    return value * node_dm / default_dm if all([node_dm, default_dm]) else value


def _node_value(node: dict, key: str = 'value'):
    value = get_node_value(node, key, default=None)
    value = _rescale_product_value_dm(node, value) if all([
        node.get('@type') == 'Product',
        key == 'value',
        value
    ]) else value
    return value


def _completeness_count_missing(nodes: list, completeness: dict):
    first_node = nodes[0]
    completeness_key = blank_node_completeness_key(first_node)
    completeness_count = len([node for node in nodes if node.get('completeness', False)])
    completeness_count_total = completeness.get(completeness_key, 0)
    completeness_count_missing = (
        completeness_count_total - completeness_count
    ) if completeness_count_total > completeness_count else 0
    return completeness_count_missing


def _product_count_missing(complete_nodes: list):
    # add `0` values for complete products but wih no `value` (missing term or missing value)
    return len(list(filter(lambda node: len(node.get('value', [])) == 0, complete_nodes)))


def _blank_node_dates(blank_nodes: list):
    first_node = blank_nodes[0]
    return aggregated_dates(
        next((n for n in blank_nodes if n.get('endDate')), first_node)
    ) if first_node['@type'] == 'Management' else pick(first_node, ['startDate', 'endDate'])


def _map_blank_node(blank_nodes: list, completeness: dict):
    first_node = blank_nodes[0]
    term = first_node.get('term')
    is_product_aggregation = first_node['@type'] == 'Product'

    # only use nodes were completeness is True or not set
    complete_nodes = [node for node in blank_nodes if node.get('completeness') is not False]

    # for primary product, we can use the value only for incomplete products
    incomplete_products_with_value = [
        node for node in blank_nodes
        if all([not node.get('completeness', False), list_sum(node.get('value', [-1]), -1) >= 0])
    ] if is_product_aggregation and first_node.get('primary') else []
    incomplete_values = non_empty_list(map(_node_value, incomplete_products_with_value))

    missing_values = [default_missing_value(term)] * (
        (_product_count_missing(complete_nodes) if is_product_aggregation else 0) +
        _completeness_count_missing(blank_nodes, completeness)
    )

    economicValueShare_values = non_empty_list([_node_value(node, 'economicValueShare') for node in complete_nodes])
    economicValueShare = economicValueShare_values + missing_values

    complete_values = non_empty_list(map(_node_value, complete_nodes))
    values = complete_values + missing_values + incomplete_values

    if not values:
        logger.warning(f"No aggregated values found for '{term.get('@id')}'")

    all_nodes = complete_nodes + incomplete_products_with_value
    max_values = flatten([n.get('max', []) for n in all_nodes])
    min_values = flatten([n.get('min', []) for n in all_nodes])
    observations = flatten([n.get('observations', 1) for n in all_nodes])
    inputs = flatten([n.get('inputs', []) for n in all_nodes])
    methodTier = get_method_tier(all_nodes)

    return {
        'term': term,
        'economicValueShare': economicValueShare,
        'value': values,
        'max': max_values,
        'min': min_values,
        'observations': observations,
        'inputs': inputs,
        'methodTier': methodTier
    } | pick(first_node, ['depthUpper', 'depthLower']) | _blank_node_dates(blank_nodes) if len(values) > 0 else None


def _map_term(aggregates_map: dict, completeness: dict, term_id: str):
    blank_nodes = [node for node in aggregates_map.get(term_id, []) if not node.get('deleted')]
    return [_map_blank_node(blank_nodes, completeness)] if len(blank_nodes) > 0 else []


def _map_blank_nodes(aggregate_key: str, data: dict):
    completeness = data.get('completeness', {})
    aggregates_map = data.get(aggregate_key, {})
    terms = aggregates_map.keys()
    return {
        term_id: non_empty_list(_map_term(aggregates_map, completeness, term_id)) for term_id in terms
    }


def _map_blank_nodes_list(aggregate_keys: List[str], data: dict):
    nodes = data.get('nodes', [])
    _debugNodes(nodes)
    return {
        aggregate_key: _map_blank_nodes(aggregate_key, data) for aggregate_key in aggregate_keys
    } | pick(data, ['site', 'organic', 'irrigated']) | {
        'node-ids': [n.get('@id') for n in nodes],
        'source-ids': [n.get('defaultSource', {}).get('@id') for n in nodes],
        'site-ids': [n.get('site', {}).get('@id') for n in nodes],
        'completeness': [n.get('completeness') for n in nodes],
        'numberOfCycles': sum_data(nodes, 'numberOfCycles'),
        'numberOfSites': sum_data(nodes, 'numberOfSites')
    }


def map_blank_nodes(aggregate_keys: List[str], groups: dict):
    return {key: _map_blank_nodes_list(aggregate_keys, value) for key, value in groups.items()}


def _aggregate(blank_nodes: list, combine_values: bool):
    first_node = blank_nodes[0]
    term = first_node.get('term')

    economicValueShare_values = flatten(map(lambda v: v.get('economicValueShare', []), blank_nodes))
    economicValueShare = weighted_average([(v, 1) for v in economicValueShare_values])

    all_values = flatten(map(lambda v: v.get('value', []), blank_nodes))
    value = weighted_average([(v, 1) for v in all_values])

    max_value = _max(all_values) if not combine_values else _max(flatten([
        n.get('max', []) for n in blank_nodes
    ] + all_values), min_observations=len(all_values) or 1)
    min_value = _min(all_values) if not combine_values else _min(flatten([
        n.get('min', []) for n in blank_nodes
    ] + all_values), min_observations=len(all_values) or 1)
    observations = len(all_values) if not combine_values else sum(flatten([
        n.get('observations', 1) for n in blank_nodes
    ]))

    inputs = flatten([n.get('inputs', []) for n in blank_nodes])
    methodTier = get_method_tier(blank_nodes)

    return {
        'term': term,
        'economicValueShare': economicValueShare,
        'value': value,
        'max': max_value,
        'min': min_value,
        'sd': _sd(all_values),
        'observations': observations,
        'inputs': inputs,
        'methodTier': methodTier
    } | pick(first_node, ['depthUpper', 'depthLower', 'startDate', 'endDate']) if len(all_values) > 0 else None


def _aggregate_term(aggregates_map: dict, combine_values: bool):
    def aggregate(term_id: str):
        blank_nodes = [node for node in aggregates_map.get(term_id, []) if not node.get('deleted')]
        return _aggregate(blank_nodes, combine_values) if len(blank_nodes) > 0 else None
    return aggregate


def _aggregate_nodes(aggregate_keys: List[str], data: dict, combine_values: bool):
    def aggregate_single(key: str):
        aggregates_map: dict = data.get(key)
        terms = aggregates_map.keys()
        aggregates = non_empty_list(map(_aggregate_term(aggregates_map, combine_values), terms))
        return (aggregates, data) if len(aggregates) > 0 else ([], {})

    return reduce(lambda prev, curr: prev | {curr: aggregate_single(curr)}, aggregate_keys, {})


def aggregate(aggregate_keys: List[str], groups: dict, combine_values: bool = False) -> list:
    return non_empty_list([
        _aggregate_nodes(aggregate_keys, value, combine_values)
        for value in groups.values()
    ])
