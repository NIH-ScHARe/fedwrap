# AGENTS.md

Guidance for AI agents working in this repository.

## Project Overview

`fedwrap` is a Python library (published to PyPI) that wraps public US federal government APIs and data downloads. It returns data as pandas DataFrames. All data sources are fully public — no API keys or credentials are required or used anywhere in the codebase.

## Repository Structure

```
src/fedwrap/
├── __init__.py           # Re-exports all public functions via `from .module import *`
├── census_acs/           # American Community Survey (Census Bureau API)
├── cdc_places/           # CDC PLACES dataset
├── cdc_brfss/            # CDC BRFSS dataset
├── cdc_svi/              # CDC/ATSDR Social Vulnerability Index
└── widget/               # ipywidgets-based data explorer (display_explorer())
```

## Module Pattern

Every dataset module follows this structure. Use it when adding a new module:

| File | Purpose |
|---|---|
| `__init__.py` | Imports the public function(s) and lists them in `__all__` |
| `config.py` | Enums, `Literal` types, and API endpoint constants |
| `*_utils.py` | Private helper functions (prefixed with `_`) |
| `main.py` or `tools.py` | Public-facing function(s) that orchestrate the helpers |

The top-level `src/fedwrap/__init__.py` should also be updated to re-export any new public functions via `from .new_module import *`.

## Public API Conventions

- Each module exposes one primary function (e.g., `get_acs_data`, `get_places_data`, `get_svi`).
- Functions return a `pandas.DataFrame`.
- Parameters use `Literal` types or `Enum`s defined in the module's `config.py` to constrain valid inputs.
- Internal/private helpers are prefixed with `_`.

## Testing

There is no test suite yet. When adding one, use `pytest`. Note that all data comes from live public endpoints, so any tests against real APIs should either be marked to skip in CI or use cached/mocked responses.

## Dependencies

Declared in `pyproject.toml`. Current dependencies: `pandas`, `requests`, `beautifulsoup4`, `ipywidgets`. Add new dependencies there if needed.
