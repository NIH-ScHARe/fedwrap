"""
Spot-checks of year-branching logic in DP02/DP05 measure functions.
get_demo_data is patched so no network calls are made; we capture the
`labels` argument that would have been passed to the Census API.
"""
import pytest
from unittest.mock import patch, call
import pandas as pd

SENTINEL_DF = pd.DataFrame({"ucgid": ["geo1"], "Total population": [1000.0]})


# ---------------------------------------------------------------------------
# get_total_pop (DP05) — simplest function, no as_percent param
# ---------------------------------------------------------------------------

def test_total_pop_year_2009_uses_number_prefix():
    with patch(
        "fedwrap.census_acs.DP05_functions.get_demo_data", return_value=SENTINEL_DF
    ) as mock_gd:
        from fedwrap.census_acs.DP05_functions import get_total_pop
        get_total_pop("2009", "county")
        labels = mock_gd.call_args[0][3]
        assert any(lbl.startswith("Number!!") for lbl in labels)


def test_total_pop_year_2022_uses_estimate_prefix():
    with patch(
        "fedwrap.census_acs.DP05_functions.get_demo_data", return_value=SENTINEL_DF
    ) as mock_gd:
        from fedwrap.census_acs.DP05_functions import get_total_pop
        get_total_pop("2022", "county")
        labels = mock_gd.call_args[0][3]
        assert any(lbl.startswith("Estimate!!") for lbl in labels)


# ---------------------------------------------------------------------------
# get_race (DP05) — 2023 capitalisation change
# ---------------------------------------------------------------------------

def test_race_2022_has_lowercase_some_other_race():
    with patch(
        "fedwrap.census_acs.DP05_functions.get_demo_data", return_value=SENTINEL_DF
    ) as mock_gd:
        from fedwrap.census_acs.DP05_functions import get_race
        get_race("2022", "county")
        labels = mock_gd.call_args[0][3]
        assert any("Some other race" in lbl for lbl in labels)
        assert not any("Some Other Race" in lbl for lbl in labels)


def test_race_2023_has_capitalised_some_other_race():
    with patch(
        "fedwrap.census_acs.DP05_functions.get_demo_data", return_value=SENTINEL_DF
    ) as mock_gd:
        from fedwrap.census_acs.DP05_functions import get_race
        get_race("2023", "county")
        labels = mock_gd.call_args[0][3]
        assert any("Some Other Race" in lbl for lbl in labels)


def test_race_unsupported_year_returns_none():
    result = None
    with patch("fedwrap.census_acs.DP05_functions.get_demo_data", return_value=SENTINEL_DF):
        from fedwrap.census_acs.DP05_functions import get_race
        result = get_race("2024", "county")
    assert result is None


# ---------------------------------------------------------------------------
# get_household_type (DP02) — year-era label differences
# ---------------------------------------------------------------------------

def test_household_type_2009_uses_number_prefix():
    with patch(
        "fedwrap.census_acs.DP02_functions.get_demo_data", return_value=SENTINEL_DF
    ) as mock_gd:
        from fedwrap.census_acs.DP02_functions import get_household_type
        get_household_type("2009", "county")
        labels = mock_gd.call_args[0][3]
        assert any(lbl.startswith("Number!!") for lbl in labels)


def test_household_type_2019_includes_cohabiting():
    with patch(
        "fedwrap.census_acs.DP02_functions.get_demo_data", return_value=SENTINEL_DF
    ) as mock_gd:
        from fedwrap.census_acs.DP02_functions import get_household_type
        get_household_type("2019", "county")
        labels = mock_gd.call_args[0][3]
        assert any("Cohabiting couple household" in lbl for lbl in labels)


def test_household_type_2022_uses_married_couple_household():
    with patch(
        "fedwrap.census_acs.DP02_functions.get_demo_data", return_value=SENTINEL_DF
    ) as mock_gd:
        from fedwrap.census_acs.DP02_functions import get_household_type
        get_household_type("2022", "county")
        labels = mock_gd.call_args[0][3]
        assert any("Married-couple household" in lbl for lbl in labels)


def test_household_type_unsupported_year_returns_none():
    with patch("fedwrap.census_acs.DP02_functions.get_demo_data", return_value=SENTINEL_DF):
        from fedwrap.census_acs.DP02_functions import get_household_type
        result = get_household_type("2024", "county")
    assert result is None


# ---------------------------------------------------------------------------
# get_health_insurance_coverage (DP03) — confirms DP03 table arg
# ---------------------------------------------------------------------------

def test_health_insurance_uses_dp03_table():
    with patch(
        "fedwrap.census_acs.DP03_functions.get_demo_data", return_value=SENTINEL_DF
    ) as mock_gd:
        from fedwrap.census_acs.DP03_functions import get_health_insurance_coverage
        get_health_insurance_coverage("2022", "county")
        table_arg = mock_gd.call_args[0][0]
        assert table_arg == "DP03"
