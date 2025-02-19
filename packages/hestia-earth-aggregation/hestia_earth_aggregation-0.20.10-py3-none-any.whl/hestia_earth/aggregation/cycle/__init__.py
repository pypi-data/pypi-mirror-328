from hestia_earth.utils.tools import non_empty_list

from hestia_earth.aggregation.log import logger
from hestia_earth.aggregation.utils.quality_score import calculate_score, filter_min_score
from hestia_earth.aggregation.models.terms import aggregate as aggregate_by_term, map_blank_nodes
from hestia_earth.aggregation.models.countries import aggregate as aggregate_by_country
from hestia_earth.aggregation.models.world import aggregate as aggregate_world
from hestia_earth.aggregation.site.utils import aggregate_sites
from .group import group_by_product
from .utils import (
    AGGREGATION_KEYS,
    aggregate_with_matrix,
    format_for_grouping, format_terms_results, format_country_results, _format_world_results,
    _update_cycle
)


def aggregate_country(country: dict, product: dict, cycles: list, source: dict, start_year: int, end_year: int) -> list:
    functional_unit = cycles[0].get('functionalUnit')

    include_matrix = aggregate_with_matrix(product)

    # step 1: aggregate all cycles indexed on the platform
    cycles = format_for_grouping(cycles)
    cycles: dict = group_by_product(product, cycles, AGGREGATION_KEYS, start_year, end_year, include_matrix)
    # current product might not be any primary product in cycles
    if len(cycles.keys()) == 0:
        logger.debug('1 - No cycles to run aggregation.')
        return []

    # aggregate sites and extend cycles
    cycles = aggregate_sites(cycles, start_year, end_year)
    # combine cycles into a "master" cycle with multiple values
    cycles = map_blank_nodes(AGGREGATION_KEYS, cycles)

    # TODO: once all cycles have been combined, aggregate
    aggregates = aggregate_by_term(AGGREGATION_KEYS, cycles)
    cycles = non_empty_list(map(format_terms_results, aggregates))
    cycles = non_empty_list(map(
        _update_cycle(country, start_year, end_year, source, functional_unit, include_matrix),
        cycles
    ))
    logger.debug(f"Found {len(cycles)} cycles at sub-country level")
    cycles = filter_min_score(map(calculate_score, cycles))
    if len(cycles) == 0:
        logger.debug('2 - No cycles to run aggregation.')
        return []

    # step 2: use aggregated cycles to calculate country-level cycles
    country_cycles = format_for_grouping(cycles)
    country_cycles = group_by_product(product, country_cycles, AGGREGATION_KEYS, start_year, end_year, False)
    aggregates = aggregate_by_country(AGGREGATION_KEYS, country_cycles)
    country_cycles = non_empty_list(map(format_country_results, aggregates))
    country_cycles = non_empty_list(map(
        _update_cycle(country, start_year, end_year, source, functional_unit, False),
        country_cycles
    ))
    logger.debug(f"Found {len(country_cycles)} cycles at country level")
    country_cycles = filter_min_score(map(calculate_score, country_cycles))

    # when not including matrix, cycles and country_cycles will be the same
    all_cycles = (cycles if include_matrix else []) + country_cycles
    return all_cycles


def aggregate_global(country: dict, product: dict, cycles: list, source: dict, start_year: int, end_year: int) -> list:
    functional_unit = cycles[0].get('functionalUnit')

    cycles = format_for_grouping(cycles)
    countries = [cycle.get('site', {}).get('country') for cycle in cycles]
    cycles = group_by_product(product, cycles, AGGREGATION_KEYS, start_year, end_year, False)
    # current product might not be any primary product in cycles
    if len(cycles.keys()) == 0:
        return []

    aggregates = aggregate_world(AGGREGATION_KEYS, cycles)
    cycles = non_empty_list(map(_format_world_results, aggregates))
    cycles = non_empty_list(map(
        _update_cycle(country, start_year, end_year, source, functional_unit, False),
        cycles
    ))
    cycles = filter_min_score([calculate_score(cycle, countries) for cycle in cycles])

    return cycles
