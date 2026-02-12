import pandas as pd
from .svi_utils import _build_url, _download_if_needed, _load_svi_csv, _filter_state

def get_svi(
    year: int,
    geography: str = "tract",
    state: str | None = None,
    refresh: bool = False,
) -> pd.DataFrame:
    """
    Return CDC/ATSDR SVI data for a given year and geography.

    Parameters
    ----------
    year : int
        SVI release year (e.g. 2022).
    geography : {"tract", "county"}
        Level of geography.
    state : str, optional
        State FIPS or 2-letter postal code. If None, returns all states.
    refresh : bool
        If True, force re-download, ignoring cached file.
    """

    url  = _build_url(year, geography)
    path = _download_if_needed(url, refresh=refresh)
    df   = _load_svi_csv(path, year)
    df   = _filter_state(df, state, year)

    return df
