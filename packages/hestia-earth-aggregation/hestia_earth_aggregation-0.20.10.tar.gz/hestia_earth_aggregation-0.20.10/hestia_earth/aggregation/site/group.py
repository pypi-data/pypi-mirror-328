from functools import reduce
from hestia_earth.schema import SchemaType
from hestia_earth.utils.tools import non_empty_list, flatten

from hestia_earth.aggregation.models.terms import map_blank_nodes
from hestia_earth.aggregation.utils.blank_node import filter_blank_nodes
from .management import filter_management


_FILTER_BLANK_NODES = {
    'management': lambda blank_nodes, start_year, end_year: filter_blank_nodes(
        filter_management(blank_nodes, start_year, end_year)
    )
}


def _filter_blank_nodes(node: dict, list_key: str, start_year: int = None, end_year: int = None):
    blank_nodes = node.get(list_key, [])
    return _FILTER_BLANK_NODES.get(list_key, filter_blank_nodes)(blank_nodes, start_year, end_year)


def _group_by_term(group: dict, blank_node: dict):
    key = '-'.join(non_empty_list([
        blank_node.get('term', {}).get('@id'),
        str(blank_node.get('depthUpper', '')),
        str(blank_node.get('depthLower', ''))
    ] + ([
        blank_node.get('startDate'),
        blank_node.get('endDate'),
    ] if blank_node.get('@type') == SchemaType.MANAGEMENT.value else [])))
    if key not in group:
        group[key] = []
    group[key].append(blank_node)
    return group


def group_sites(sites: list, props: list, start_year: int = None, end_year: int = None):
    key = 'site'
    groups = {key: {'nodes': []}}

    def group_by(group: dict, site: dict):
        group[key]['nodes'].append(site)

        def group_by_prop(list_key: str):
            blank_nodes = flatten(map(
                lambda v: v | {
                    'country': site.get('country'),
                    'completeness': True
                }, _filter_blank_nodes(site, list_key, start_year, end_year)))
            return reduce(_group_by_term, blank_nodes, group[key].get(list_key, {}))

        group[key] = reduce(lambda prev, curr: prev | {curr: group_by_prop(curr)}, props, group[key])
        return group

    return map_blank_nodes(props, reduce(group_by, sites, groups))
