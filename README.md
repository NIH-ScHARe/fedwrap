# fedwrap

A Python package providing convenient wrappers for accessing and working with US federal datasets, including the American Community Survey and CDC PLACES.

---

## Table of Contents

- [fedwrap](#fedwrap)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
  - [Modules](#modules)
  - [Dependencies](#dependencies)
  - [License](#license)
  - [Contact](#contact)
---

## Overview

`fedwrap` simplifies access to federal datasets by providing Pythonic wrappers for public APIs and data downloads. The package is designed for researchers, analysts, and developers who need streamlined access to high-value US government data.

---

## Features

- Easy access to the American Community Survey (ACS) and the CDC PLACES dataset 
- Data returned as pandas DataFrames for easy analysis

---

## Installation

```bash
pip install fedwrap
```

## Quick Start

```python
from fedwrap import census_acs, cdc_places

# Example: Fetch ACS data
acs_df = census_acs.get_education_data(year=2022, geography="county")

# Example: Fetch CDC PLACES data
places_df = data = get_places_data(
    geo='county',
    year='2022',
    measureid='ARTHRITIS',
    datavaluetypid='CrdPrv'
)
```
## Modules

- census_acs provides functions for accessing data from the American Community Survey API
- cdc-places provides functions for accessing data from the CDC PLACES dataset 

## Dependencies

- pandas
- requests
- beautifulsoup4

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, open an issue or contact Mark Aronson. 