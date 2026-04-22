"""
End-to-end pipeline tests for get_brfss_data and pivot_response_columns.
"""
import pytest
from unittest.mock import patch
import pandas as pd

from fedwrap.cdc_brfss.brfss_utils import pivot_response_columns, get_brfss_data
from fedwrap.cdc_brfss.config import BRFSS_ENDPOINTS


# ---------------------------------------------------------------------------
# pivot_response_columns
# ---------------------------------------------------------------------------

@pytest.fixture
def overall_df():
    return pd.DataFrame({
        "locationabbr": ["AL", "AL", "AK", "AK"],
        "response": ["Yes", "No", "Yes", "No"],
        "data_value": ["60.5", "39.5", "55.0", "45.0"],
        "break_out": ["Overall", "Overall", "Overall", "Overall"],
    })


@pytest.fixture
def sex_breakout_df():
    return pd.DataFrame({
        "locationabbr": ["AL", "AL", "AL", "AL"],
        "response": ["Yes", "Yes", "No", "No"],
        "data_value": ["65.0", "55.0", "35.0", "45.0"],
        "break_out": ["Male", "Female", "Male", "Female"],
    })


def test_overall_pivots_on_response_only(overall_df):
    result = pivot_response_columns(overall_df, "Overall")
    assert "Yes" in result.columns
    assert "No" in result.columns
    assert "locationabbr" in result.columns


def test_non_overall_creates_compound_column_names(sex_breakout_df):
    result = pivot_response_columns(sex_breakout_df, "Sex")
    compound_cols = [c for c in result.columns if " - " in c]
    assert len(compound_cols) > 0


def test_nan_filled_with_zero(overall_df):
    # Add a location that only has one response (creates NaN for missing response)
    extra = pd.DataFrame({
        "locationabbr": ["TX"],
        "response": ["Yes"],
        "data_value": ["70.0"],
        "break_out": ["Overall"],
    })
    df = pd.concat([overall_df, extra], ignore_index=True)
    result = pivot_response_columns(df, "Overall")
    tx_no = result.loc[result["locationabbr"] == "TX", "No"].iloc[0]
    assert tx_no == 0


def test_data_value_coerced_to_numeric():
    df = pd.DataFrame({
        "locationabbr": ["AL"],
        "response": ["Yes"],
        "data_value": ["N/A"],
        "break_out": ["Overall"],
    })
    result = pivot_response_columns(df, "Overall")
    # N/A becomes NaN then 0
    assert result["Yes"].iloc[0] == 0


def test_locationabbr_is_regular_column(overall_df):
    result = pivot_response_columns(overall_df, "Overall")
    assert "locationabbr" in result.columns
    assert result.index.name != "locationabbr"


# ---------------------------------------------------------------------------
# get_brfss_data — full pipeline
# ---------------------------------------------------------------------------

def test_raises_if_question_invalid():
    with (
        patch("fedwrap.cdc_brfss.brfss_utils.check_question", return_value=False),
        pytest.raises(ValueError, match="BADID"),
    ):
        get_brfss_data("state", "crude", 2022, "BADID")


def test_raises_if_breakout_invalid_for_non_state_crude():
    with (
        patch("fedwrap.cdc_brfss.brfss_utils.check_question", return_value=True),
        pytest.raises(ValueError),
    ):
        get_brfss_data("msa", "crude", 2022, "CHECKUP1", break_out_category="Sex")


def test_calls_correct_endpoint_for_state_crude():
    expected_url = BRFSS_ENDPOINTS["state"]["crude"]
    raw = pd.DataFrame({
        "locationabbr": ["AL"], "response": ["Yes"],
        "data_value": ["60.0"], "break_out": ["Overall"],
    })
    with (
        patch("fedwrap.cdc_brfss.brfss_utils.check_question", return_value=True),
        patch("fedwrap.cdc_brfss.brfss_utils.api_call", return_value=raw) as mock_api,
    ):
        get_brfss_data("state", "crude", 2022, "CHECKUP1")
        url_used = mock_api.call_args[0][0]
    assert url_used == expected_url


def test_passes_year_and_questionid_as_params():
    raw = pd.DataFrame({
        "locationabbr": ["AL"], "response": ["Yes"],
        "data_value": ["60.0"], "break_out": ["Overall"],
    })
    with (
        patch("fedwrap.cdc_brfss.brfss_utils.check_question", return_value=True),
        patch("fedwrap.cdc_brfss.brfss_utils.api_call", return_value=raw) as mock_api,
    ):
        get_brfss_data("state", "crude", 2022, "CHECKUP1")
        params = mock_api.call_args[0][1]
    assert "year" in params
    assert "questionid" in params


def test_returns_dataframe():
    raw = pd.DataFrame({
        "locationabbr": ["AL", "AL"],
        "response": ["Yes", "No"],
        "data_value": ["60.0", "40.0"],
        "break_out": ["Overall", "Overall"],
    })
    with (
        patch("fedwrap.cdc_brfss.brfss_utils.check_question", return_value=True),
        patch("fedwrap.cdc_brfss.brfss_utils.api_call", return_value=raw),
    ):
        result = get_brfss_data("state", "crude", 2022, "CHECKUP1")
    assert isinstance(result, pd.DataFrame)
