"""
Pure validation logic tests for the BRFSS module.
check_question makes one network call; everything else is pure logic.
"""
import pytest
from unittest.mock import patch, MagicMock
import requests

from fedwrap.cdc_brfss.brfss_utils import check_question, check_breakout, get_endpoint
from fedwrap.cdc_brfss.config import BRFSS_ENDPOINTS


# ---------------------------------------------------------------------------
# check_question
# ---------------------------------------------------------------------------

def _make_question_response(question_ids):
    mock_resp = MagicMock()
    mock_resp.json.return_value = [{"variablename": qid} for qid in question_ids]
    return mock_resp


def test_check_question_returns_true_for_valid_id():
    mock_resp = _make_question_response(["CHECKUP1", "HLTHPLN1"])
    with patch("fedwrap.cdc_brfss.brfss_utils.requests.get", return_value=mock_resp):
        assert check_question("CHECKUP1", 2022) is True


def test_check_question_returns_false_for_invalid_id():
    mock_resp = _make_question_response(["CHECKUP1"])
    with patch("fedwrap.cdc_brfss.brfss_utils.requests.get", return_value=mock_resp):
        assert check_question("NOTAREAL", 2022) is False


def test_check_question_returns_false_on_request_exception():
    with patch(
        "fedwrap.cdc_brfss.brfss_utils.requests.get",
        side_effect=requests.RequestException("timeout"),
    ):
        assert check_question("CHECKUP1", 2022) is False


def test_check_question_sends_year_as_param():
    mock_resp = _make_question_response(["CHECKUP1"])
    with patch("fedwrap.cdc_brfss.brfss_utils.requests.get", return_value=mock_resp) as mock_get:
        check_question("CHECKUP1", 2022)
        _, kwargs = mock_get.call_args
        assert kwargs["params"] == {"year": 2022}


# ---------------------------------------------------------------------------
# check_breakout
# ---------------------------------------------------------------------------

def test_overall_is_always_valid_for_state_crude():
    assert check_breakout("state", "crude", "Overall") is True


def test_overall_is_always_valid_for_msa_crude():
    assert check_breakout("msa", "crude", "Overall") is True


def test_overall_is_always_valid_for_state_age_adjusted():
    assert check_breakout("state", "age-adjusted", "Overall") is True


def test_non_overall_valid_only_for_state_crude():
    assert check_breakout("state", "crude", "Sex") is True


def test_non_overall_invalid_for_msa_crude():
    assert check_breakout("msa", "crude", "Sex") is False


def test_non_overall_invalid_for_state_age_adjusted():
    assert check_breakout("state", "age-adjusted", "Sex") is False


def test_non_overall_invalid_for_msa_age_adjusted():
    assert check_breakout("msa", "age-adjusted", "Sex") is False


# ---------------------------------------------------------------------------
# get_endpoint
# ---------------------------------------------------------------------------

def test_get_endpoint_state_crude_returns_url():
    url = get_endpoint("state", "crude")
    assert isinstance(url, str) and url.startswith("https://")


def test_get_endpoint_state_age_adjusted_returns_url():
    url = get_endpoint("state", "age-adjusted")
    assert isinstance(url, str) and url.startswith("https://")


def test_get_endpoint_msa_crude_returns_url():
    url = get_endpoint("msa", "crude")
    assert isinstance(url, str) and url.startswith("https://")


def test_get_endpoint_msa_age_adjusted_returns_url():
    url = get_endpoint("msa", "age-adjusted")
    assert isinstance(url, str) and url.startswith("https://")


def test_get_endpoint_invalid_geo_raises_value_error():
    with pytest.raises(ValueError, match="country"):
        get_endpoint("country", "crude")


def test_get_endpoint_invalid_measure_raises_value_error():
    with pytest.raises(ValueError, match="unadjusted"):
        get_endpoint("state", "unadjusted")
