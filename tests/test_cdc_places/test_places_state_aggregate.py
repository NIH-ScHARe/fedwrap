"""
Tests for the population-weighted state prevalence computation in
get_places_state_data. All external calls are mocked.
"""
import pytest
from unittest.mock import patch
import pandas as pd

from fedwrap.cdc_places.places_utils import get_places_state_data


@pytest.fixture
def county_df():
    """Two counties in NY, one in FL, one US aggregate row."""
    return pd.DataFrame({
        "locationid": ["36001", "36003", "12001", "00000"],
        "stateabbr": ["NY", "NY", "FL", "US"],
        "data_value": [10.0, 20.0, 40.0, 25.0],
    })


@pytest.fixture
def population_df():
    """Population data with full ucgid strings that need FIPS truncation."""
    return pd.DataFrame({
        "ucgid": ["0500000US36001", "0500000US36003", "0500000US12001", "0500000US00000"],
        "Total population": [1000.0, 3000.0, 2000.0, 6000.0],
    })


def _mock_both(county_df, population_df):
    """Context manager pair that mocks both upstream data sources."""
    return (
        patch("fedwrap.cdc_places.places_utils.get_places_data", return_value=county_df),
        patch("fedwrap.cdc_places.places_utils.get_acs_data", return_value=population_df),
    )


def test_weighted_prevalence_is_correct(county_df, population_df):
    # NY: (10.0*1000/100 + 20.0*3000/100) / (4000/100) * 100 = 17.5
    with _mock_both(county_df, population_df)[0], _mock_both(county_df, population_df)[1]:
        result = get_places_state_data(2022, "ARTHRITIS")
    ny_row = result[result["stateabbr"] == "NY"]
    assert not ny_row.empty
    assert ny_row["data_value"].iloc[0] == pytest.approx(17.5, abs=0.05)


def test_result_rounded_to_one_decimal(county_df, population_df):
    with _mock_both(county_df, population_df)[0], _mock_both(county_df, population_df)[1]:
        result = get_places_state_data(2022, "ARTHRITIS")
    for val in result["data_value"]:
        rounded = round(val, 1)
        assert val == pytest.approx(rounded, abs=1e-9)


def test_us_row_excluded(county_df, population_df):
    with _mock_both(county_df, population_df)[0], _mock_both(county_df, population_df)[1]:
        result = get_places_state_data(2022, "ARTHRITIS")
    assert "US" not in result["stateabbr"].values


def test_output_columns_are_stateabbr_and_data_value(county_df, population_df):
    with _mock_both(county_df, population_df)[0], _mock_both(county_df, population_df)[1]:
        result = get_places_state_data(2022, "ARTHRITIS")
    assert list(result.columns) == ["stateabbr", "data_value"]


def test_fips_truncation_applied_to_population_data(county_df, population_df):
    # population_df uses full GEO IDs; after truncation they should merge with county_df's 5-char locationids
    with _mock_both(county_df, population_df)[0], _mock_both(county_df, population_df)[1]:
        result = get_places_state_data(2022, "ARTHRITIS")
    # If truncation didn't happen, the merge would fail and data_value would be NaN
    assert result["data_value"].notna().all()


def test_missing_county_in_population_produces_nan_or_zero(county_df):
    """County present in PLACES but absent from population → graceful handling."""
    pop_df_incomplete = pd.DataFrame({
        "ucgid": ["0500000US36001"],  # only one county
        "Total population": [1000.0],
    })
    with (
        patch("fedwrap.cdc_places.places_utils.get_places_data", return_value=county_df),
        patch("fedwrap.cdc_places.places_utils.get_acs_data", return_value=pop_df_incomplete),
    ):
        result = get_places_state_data(2022, "ARTHRITIS")
    # Should not raise; result may contain NaN for unmatched counties
    assert isinstance(result, pd.DataFrame)
