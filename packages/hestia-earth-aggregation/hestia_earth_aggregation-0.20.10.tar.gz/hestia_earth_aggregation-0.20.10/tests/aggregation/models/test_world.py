import os
import json
import pytest
from unittest.mock import Mock, patch

from tests.utils import (
    overwrite_expected,
    PRODUCT_BY_FILENAME, SOURCE, WORLD, fixtures_path, start_year, end_year,
    fake_download, fake_aggregated_version, filter_cycles
)
from hestia_earth.aggregation.cycle.group import group_by_product
from hestia_earth.aggregation.cycle.utils import (
    AGGREGATION_KEYS, format_for_grouping, _update_cycle, _format_world_results
)
from hestia_earth.aggregation.utils.quality_score import calculate_score
from hestia_earth.aggregation.models.world import aggregate

class_path = 'hestia_earth.aggregation.models.world'
fixtures_folder = os.path.join(fixtures_path, 'cycle', 'world')

_files = [f for f in os.listdir(fixtures_folder) if os.path.isfile(os.path.join(fixtures_folder, f))]


@pytest.mark.parametrize('filename', _files)
@patch('hestia_earth.aggregation.cycle.practice.download_hestia', side_effect=fake_download)
@patch('hestia_earth.aggregation.cycle.utils._aggregated_version', side_effect=fake_aggregated_version)
@patch('hestia_earth.aggregation.cycle.utils._aggregated_node', side_effect=fake_aggregated_version)
@patch('hestia_earth.aggregation.site.utils._aggregated_version', side_effect=fake_aggregated_version)
@patch('hestia_earth.aggregation.site.utils._aggregated_node', side_effect=fake_aggregated_version)
@patch('hestia_earth.aggregation.utils.queries.download_hestia', side_effect=fake_download)
@patch('hestia_earth.aggregation.site.management._current_date', return_value='2025-01-01')
@patch('hestia_earth.aggregation.utils.queries._current_date', return_value='2025-01-01')
@patch('hestia_earth.aggregation.cycle.utils._timestamp', return_value='')
def test_aggregate(
    mock_1: Mock,
    mock_2: Mock,
    mock_3: Mock,
    mock_4: Mock,
    mock_5: Mock,
    mock_6: Mock,
    mock_7: Mock,
    mock_8: Mock,
    mock_9: Mock,
    filename: str
):
    expected_path = os.path.join(fixtures_folder, filename)
    with open(os.path.join(fixtures_path, 'cycle', 'countries', filename), encoding='utf-8') as f:
        cycles = json.load(f)
    with open(expected_path, encoding='utf-8') as f:
        expected = json.load(f)

    functional_unit = cycles[0].get('functionalUnit')
    cycles = format_for_grouping(filter_cycles(cycles))
    product_name = filename.replace('-aggregated.jsonld', '')
    product = PRODUCT_BY_FILENAME[product_name]
    results = aggregate(AGGREGATION_KEYS, group_by_product(product, cycles, AGGREGATION_KEYS, 1950, 2050, False))
    results = list(map(_format_world_results, results))
    results = list(map(_update_cycle(WORLD, start_year, end_year, SOURCE, functional_unit, False), results))
    results = list(map(calculate_score, results))
    results = results
    overwrite_expected(expected_path, results)
    assert results == expected
