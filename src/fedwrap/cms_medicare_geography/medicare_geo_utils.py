import requests
import pandas as pd
from .config import API_ENDPOINT, Geography, Measure, MEASURE_COLS

_ID_COLS = ["BENE_GEO_DESC", "BENE_GEO_CD", "YEAR"]


def _resolve_geo(geo: Geography | str) -> str:
    if isinstance(geo, Geography):
        return geo.value
    try:
        return Geography(geo.capitalize()).value
    except ValueError:
        valid = [g.value for g in Geography]
        raise ValueError(f"Invalid geography '{geo}'. Valid options: {valid}")


def _fetch_all(params: dict) -> list[dict]:
    params = {**params, "size": 10000, "offset": 0}
    results = []
    while True:
        response = requests.get(API_ENDPOINT, params=params)
        response.raise_for_status()
        page = response.json()
        if not page:
            break
        results.extend(page)
        if len(page) < params["size"]:
            break
        params["offset"] += params["size"]
    return results


def _resolve_measure(measure: Measure | str) -> Measure:
    if isinstance(measure, Measure):
        return measure
    try:
        return Measure(measure.lower())
    except ValueError:
        valid = [m.value for m in Measure]
        raise ValueError(f"Invalid measure '{measure}'. Valid options: {valid}")


def get_medicare_geography_data(
    geo: Geography | str,
    year: int,
    measure: Measure | str,
) -> pd.DataFrame | None:
    try:
        geo_value = _resolve_geo(geo)
        measure_key = _resolve_measure(measure)
        params = {
            "filter[BENE_GEO_LVL]": geo_value,
            "filter[YEAR]": year,
            "filter[BENE_AGE_LVL]": "All",
        }
        records = _fetch_all(params)
        df = pd.DataFrame(records)
        return df[_ID_COLS + MEASURE_COLS[measure_key]]
    except requests.RequestException as e:
        print(f"Error querying API: {e}")
        return None
