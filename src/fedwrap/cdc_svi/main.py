from pathlib import Path
import pandas as pd

VALID_YEARS = {2000, 2010, 2014, 2016, 2018, 2020, 2022}
VALID_GEOS  = {"tract", "county"}

def list_years():
    return sorted(VALID_YEARS)

def list_states():
    return sorted(STATE_FIPS.keys())

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
    if year not in VALID_YEARS:
        raise ValueError(f"Unsupported year={year}; valid options are {sorted(VALID_YEARS)}")
    if geography not in VALID_GEOS:
        raise ValueError(f"Unsupported geography={geography}; valid options are {VALID_GEOS}")

    url  = _build_url(year, geography)
    path = _download_if_needed(url, refresh=refresh)
    df   = _load_svi_csv(path)
    df   = _postprocess(df, geography)
    df   = _filter_state(df, state)

    return df
