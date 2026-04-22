"""
Tests for _download_if_needed: cache hit, miss, refresh, and error paths.
All tests use an isolated temp directory via MYPKG_CACHE_DIR env var.
"""
import pytest
from unittest.mock import patch, MagicMock, call
import requests

from fedwrap.cdc_svi.svi_utils import _download_if_needed

FAKE_URL = "https://svi.cdc.gov/Documents/Data/2022/csv/states/SVI_2022_US.csv"
FAKE_FILENAME = "SVI_2022_US.csv"
FAKE_CONTENT = b"ST_ABBR,STCNTY\nMD,24001\n"


def _make_streaming_response(content=FAKE_CONTENT):
    mock_resp = MagicMock()
    mock_resp.iter_content.return_value = [content]
    return mock_resp


@pytest.fixture(autouse=True)
def isolate_cache(tmp_path, monkeypatch):
    """Point MYPKG_CACHE_DIR to a fresh temp dir for every test."""
    monkeypatch.setenv("MYPKG_CACHE_DIR", str(tmp_path))
    return tmp_path


# ---------------------------------------------------------------------------
# Cache miss
# ---------------------------------------------------------------------------

def test_cache_miss_calls_requests_get(tmp_path):
    mock_resp = _make_streaming_response()
    with patch("fedwrap.cdc_svi.svi_utils.requests.get", return_value=mock_resp) as mock_get:
        _download_if_needed(FAKE_URL)
        mock_get.assert_called_once()


def test_cache_miss_creates_file(tmp_path):
    mock_resp = _make_streaming_response()
    with patch("fedwrap.cdc_svi.svi_utils.requests.get", return_value=mock_resp):
        path = _download_if_needed(FAKE_URL)
    assert path.exists()


def test_cache_miss_returns_path_to_new_file(tmp_path):
    mock_resp = _make_streaming_response()
    with patch("fedwrap.cdc_svi.svi_utils.requests.get", return_value=mock_resp):
        path = _download_if_needed(FAKE_URL)
    assert path.is_file()


# ---------------------------------------------------------------------------
# Cache hit
# ---------------------------------------------------------------------------

def test_cache_hit_skips_download(tmp_path):
    # Pre-create the cached file
    cached = tmp_path / FAKE_FILENAME
    cached.write_bytes(FAKE_CONTENT)

    with patch("fedwrap.cdc_svi.svi_utils.requests.get") as mock_get:
        _download_if_needed(FAKE_URL, refresh=False)
        mock_get.assert_not_called()


def test_cache_hit_returns_existing_path(tmp_path):
    cached = tmp_path / FAKE_FILENAME
    cached.write_bytes(FAKE_CONTENT)

    with patch("fedwrap.cdc_svi.svi_utils.requests.get"):
        path = _download_if_needed(FAKE_URL, refresh=False)
    assert path == cached


# ---------------------------------------------------------------------------
# Refresh
# ---------------------------------------------------------------------------

def test_refresh_true_redownloads_when_cached(tmp_path):
    cached = tmp_path / FAKE_FILENAME
    cached.write_bytes(FAKE_CONTENT)

    mock_resp = _make_streaming_response()
    with patch("fedwrap.cdc_svi.svi_utils.requests.get", return_value=mock_resp) as mock_get:
        _download_if_needed(FAKE_URL, refresh=True)
        mock_get.assert_called_once()


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def test_http_error_propagates(tmp_path):
    mock_resp = MagicMock()
    mock_resp.raise_for_status.side_effect = requests.HTTPError("404")
    with (
        patch("fedwrap.cdc_svi.svi_utils.requests.get", return_value=mock_resp),
        pytest.raises(requests.HTTPError),
    ):
        _download_if_needed(FAKE_URL)


# ---------------------------------------------------------------------------
# Cache dir creation
# ---------------------------------------------------------------------------

def test_cache_dir_created_if_missing(tmp_path, monkeypatch):
    nested = tmp_path / "new" / "subdir"
    monkeypatch.setenv("MYPKG_CACHE_DIR", str(nested))

    mock_resp = _make_streaming_response()
    with patch("fedwrap.cdc_svi.svi_utils.requests.get", return_value=mock_resp):
        _download_if_needed(FAKE_URL)
    assert nested.exists()


# ---------------------------------------------------------------------------
# Filename and env var
# ---------------------------------------------------------------------------

def test_filename_derived_from_url_last_segment(tmp_path):
    mock_resp = _make_streaming_response()
    with patch("fedwrap.cdc_svi.svi_utils.requests.get", return_value=mock_resp):
        path = _download_if_needed(FAKE_URL)
    assert path.name == FAKE_FILENAME


def test_env_var_controls_cache_location(tmp_path, monkeypatch):
    custom = tmp_path / "custom_cache"
    monkeypatch.setenv("MYPKG_CACHE_DIR", str(custom))

    mock_resp = _make_streaming_response()
    with patch("fedwrap.cdc_svi.svi_utils.requests.get", return_value=mock_resp):
        path = _download_if_needed(FAKE_URL)
    assert str(path).startswith(str(custom))
