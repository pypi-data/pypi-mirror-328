from hestia_earth.schema import SchemaType, SiteDefaultMethodClassification
from hestia_earth.utils.tools import non_empty_list

from hestia_earth.aggregation.models.terms import aggregate as aggregate_by_term
from hestia_earth.aggregation.utils import _aggregated_node, sum_data, _aggregated_version, format_aggregated_list
from hestia_earth.aggregation.utils.term import _update_country, _format_country_name
from hestia_earth.aggregation.utils.blank_node import cleanup_blank_nodes
from hestia_earth.aggregation.utils.source import format_aggregated_sources
from .measurement import _new_measurement
from .management import _new_management
from .group import group_sites

AGGREGATION_KEYS = ['measurements', 'management']


def _format_aggregate(new_func: dict):
    def format(aggregate: dict):
        return _aggregated_version(new_func(aggregate))
    return format


def _format_site(site_data: dict, results: tuple):
    measurements, data = results.get('measurements')
    management, _ = results.get('management')
    sites = data.get('nodes', []) or data.get('node-ids', [])
    sources = data.get('source-ids')
    return create_site(site_data) | {
        'measurements': cleanup_blank_nodes(map(_format_aggregate(_new_measurement), measurements)),
        'management': cleanup_blank_nodes(map(_format_aggregate(_new_management), management)),
        'aggregatedSites': format_aggregated_list('Site', sites),
        'aggregatedSources': format_aggregated_list('Source', sources) if sources
        else format_aggregated_sources(sites, 'defaultSource'),
        'numberOfSites': data.get('numberOfSites', sum_data(data.get('nodes', []), 'numberOfSites'))
    } if len(sites) > 0 else None


def _extend_site(sites: list, start_year: int, end_year: int, combine_values: bool = False):
    groups = group_sites(sites, AGGREGATION_KEYS, start_year, end_year)
    aggregates = aggregate_by_term(AGGREGATION_KEYS, groups, combine_values=combine_values)
    site = create_site(sites[0]) if sites else {}
    return (_format_site(site, aggregates[0]) if len(aggregates) > 0 else None) or (site | {
        'aggregatedSites': format_aggregated_list('Site', sites),
        'aggregatedSources': format_aggregated_sources(sites, 'defaultSource'),
        'numberOfSites': sum_data(sites, 'numberOfSites')
    })


def aggregate_sites(cycles: dict, start_year: int, end_year: int):
    # cycles is a group of keys and list of data containing the sites
    def extend_site(value: dict):
        sites = value.get('sites', [])
        return value | {'site': _extend_site(sites, start_year, end_year)}

    return {key: extend_site(value) for key, value in cycles.items()}


def format_country_sites(sites: list):
    groups = group_sites(sites, AGGREGATION_KEYS)
    aggregates = aggregate_by_term(AGGREGATION_KEYS, groups, combine_values=True)
    measurements = aggregates[0].get('measurements')[0] if aggregates else []
    management = aggregates[0].get('management')[0] if aggregates else []
    return create_site(sites[0]) | {
        'measurements': cleanup_blank_nodes(map(_format_aggregate(_new_measurement), measurements)),
        'management': cleanup_blank_nodes(map(_format_aggregate(_new_management), management)),
        'aggregatedSites': format_aggregated_list('Site', sites),
        'aggregatedSources': format_aggregated_list('Source', sites),
        'numberOfSites': sum_data(sites, 'numberOfSites')
    }


def _site_id(n: dict, include_siteType: bool):
    return '-'.join(non_empty_list([
        _format_country_name(n.get('country', {}).get('name')),
        n.get('siteType') if include_siteType else None
    ]))


def _site_name(n: dict, include_siteType: bool):
    return ' - '.join(non_empty_list([
        n.get('country', {}).get('name'),
        n.get('siteType') if include_siteType else None
    ]))


def create_site(data: dict, include_siteType=True):
    site = {'type': SchemaType.SITE.value}
    site['country'] = data['country']
    site['siteType'] = data['siteType']
    site['name'] = _site_name(site, include_siteType)
    site['id'] = _site_id(site, include_siteType)
    site['defaultMethodClassification'] = SiteDefaultMethodClassification.MODELLED.value
    site['defaultMethodClassificationDescription'] = 'aggregated data'
    site['dataPrivate'] = False
    site['aggregatedDataValidated'] = False
    return _aggregated_node(site)


def update_site(country_name: str, source: dict = None, include_siteType=True):
    def update(site: dict):
        site['country'] = _update_country(country_name) if country_name else site.get('country')
        site['name'] = _site_name(site, include_siteType)
        site['id'] = _site_id(site, include_siteType)
        return site | ({} if source is None else {'defaultSource': source})
    return update
