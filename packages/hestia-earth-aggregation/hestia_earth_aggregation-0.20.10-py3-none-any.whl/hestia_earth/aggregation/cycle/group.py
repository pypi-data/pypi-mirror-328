from functools import reduce
from hestia_earth.utils.tools import safe_parse_date

from ..utils.completeness import is_complete, group_completeness
from ..utils.term import _group_by_term_id
from ..utils.practice import filter_practices
from ..utils.blank_node import filter_blank_nodes, filter_aggregate


def _end_date_year(node: dict):
    date = safe_parse_date(node.get('endDate'))
    return date.year if date else None


def _same_product(product: dict):
    def compare(node: dict):
        np = node.get('product', {}) if node else {}
        return np.get('@id', np.get('term', {}).get('@id')) == product.get('@id')
    return compare


_GROUP_BY_METHOD_MODEL_PROP = [
    'emissionsResouceUse',
    'impacts',
    'endpoints'
]


_FILTER_BLANK_NODES = {
    'practices': lambda blank_nodes, start_year, end_year: filter_blank_nodes(
        filter_practices(blank_nodes), start_year, end_year
    ),
    'measurements': filter_blank_nodes,
    'emissions': lambda blank_nodes, *args: list(filter(filter_aggregate, blank_nodes))
}


def _filter_blank_nodes(node: dict, list_key: str, start_year: int, end_year: int):
    blank_nodes = node.get(list_key, [])
    return _FILTER_BLANK_NODES.get(list_key, lambda values, *args: values)(blank_nodes, start_year, end_year)


def group_by_product(product: dict, nodes: list, props: list, start_year: int, end_year: int, include_matrix=True):
    """
    Group a list of blank nodes filtering by the same product.
    """
    filtered_nodes = list(filter(_same_product(product), nodes))

    def group_by(group: dict, node: dict):
        node_id = node.get('@id', node.get('id'))
        end_date = _end_date_year(node)
        organic = node.get('organic', False)
        irrigated = node.get('irrigated', False)
        key = '-'.join([str(organic), str(irrigated)]) if include_matrix else 'default'
        data = {
            'organic': organic,
            'irrigated': irrigated,
            'country': node.get('country'),
            'year': end_date
        }
        if key not in group:
            group[key] = {
                'product': product,
                'nodes': [],
                'sites': [],
                'completeness': {},
                **data,
                **reduce(lambda prev, curr: {**prev, curr: {}}, props, {})
            }
        group[key]['nodes'].append({**node, **data})
        group[key]['sites'].append(node.get('site'))

        def group_by_prop(list_key: str):
            blank_nodes = _filter_blank_nodes(node, list_key, start_year, end_year)
            values = list(map(
                lambda v: v | data | {
                    'id': node_id,
                    'completeness': is_complete(node, product, v)
                }, blank_nodes))
            return reduce(_group_by_term_id(list_key in _GROUP_BY_METHOD_MODEL_PROP), values, group[key][list_key])

        group[key] = reduce(lambda prev, curr: prev | {curr: group_by_prop(curr)}, props, group[key])
        group[key]['completeness'] = group_completeness(group[key]['completeness'], node)
        return group

    return reduce(group_by, filtered_nodes, {})
