import re
from unidecode import unidecode
from hestia_earth.schema import SchemaType, TermTermType
from hestia_earth.utils.model import linked_node
from hestia_earth.utils.api import find_node, find_node_exact
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.tools import non_empty_list

SEARCH_LIMIT = 10000
DEFAULT_COUNTRY_ID = 'region-world'
DEFAULT_COUNTRY_NAME = 'World'
DEFAULT_COUNTRY = {'@id': 'region-world', 'name': DEFAULT_COUNTRY_NAME}
MODEL = 'aggregatedModels'
METHOD_MODEL = {'@type': SchemaType.TERM.value, '@id': MODEL}


def _fetch_all(term_type: TermTermType): return find_node(SchemaType.TERM, {'termType': term_type.value}, SEARCH_LIMIT)


def _fetch_single(term_name: str): return find_node_exact(SchemaType.TERM, {'name': term_name})


def _fetch_default_country(): return _fetch_single(DEFAULT_COUNTRY_NAME)


def _fetch_countries():
    return find_node(SchemaType.TERM, {
        'termType': TermTermType.REGION.value,
        'gadmLevel': 0
    }, SEARCH_LIMIT)


def _format_country_name(name: str):
    return re.sub(r'[\(\)\,\.\'\"]', '', unidecode(name).lower().replace(' ', '-')) if name else None


def _format_organic(organic: bool): return 'organic' if organic else 'conventional'


def _format_irrigated(irrigated: bool): return 'irrigated' if irrigated else 'non-irrigated'


def _is_global(country: dict): return country.get('@id', '').startswith('region-')


def should_aggregate(term: dict):
    lookup = download_lookup(f"{term.get('termType')}.csv", True)
    value = get_table_value(lookup, 'termid', term.get('@id'), column_name('skipAggregation'))
    return True if value is None or value == '' else not value


def _group_by_term_id(group_by_methodModel=False):
    def group_by(group: dict, node: dict):
        group_key = '-'.join(non_empty_list([
            node.get('methodModel', {}).get('@id') if group_by_methodModel else None,
            node.get('term', {}).get('@id')
        ]))
        if group_key not in group:
            group[group_key] = []
        group[group_key].append(node)
        return group
    return group_by


def _update_country(country_name: str):
    return linked_node({
        **(_fetch_single(country_name) if isinstance(country_name, str) else country_name),
        '@type': SchemaType.TERM.value
    })
