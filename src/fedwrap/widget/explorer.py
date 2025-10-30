import ipywidgets as w
from IPython.display import display, FileLink
import tempfile, os

VARIABLE_CATALOG: dict[str, list[str]] = {
    "ACS": {
        "Variables" : [
            "HOUSEHOLD_TYPE",
            "HOUSEHOLD_RELATIONSHIP",
            "MALE_MARITAL_STATUS",
            "FEMALE_MARITAL_STATUS",
            "SCHOOL_ENROLLMENT",
            "EDUCATIONAL_ATTAINMENT",
            "VETERAN_STATUS",
            "RESIDENCE_YEAR_AGO",
            "PLACE_OF_BIRTH",
            "US_CITIZENSHIP_STATUS",
            "WORLD_REGION_OF_BIRTH_OF_FOREIGN_BORN",
            "LANGUAGE_SPOKEN_AT_HOME",
            "ANCESTRY",
            "COMPUTER_AND_INTERNET_USE",
            "EMPLOYMENT_STATUS",
            "COMMUTING_TO_WORK",
            "OCCUPATION",
            "INDUSTRY",
            "CLASS_OF_WORKER",
            "HOUSEHOLD_INCOME",
            "HOUSEHOLDS_WITH_EARNINGS",
            "HOUSEHOLDS_WITH_SOCIAL_SECURITY",
            "HOUSEHOLDS_WITH_RETIREMENT_INCOME",
            "HOUSEHOLDS_WITH_SUPPLEMENTAL_SECURITY_INCOME",
            "HOUSEHOLDS_WITH_CASH_PUBLIC_ASSISTANCE_INCOME",
            "HOUSEHOLDS_WITH_SNAP_BENEFITS",
            "FAMILY_INCOME",
            "HEALTH_INSURANCE_COVERAGE",
            "HOUSING_OCCUPANCY",
            "UNITS_IN_STRUCTURE",
            "YEAR_STRUCTURE_BUILT",
            "ROOMS",
            "BEDROOMS",
            "HOUSING_TENURE",
            "YEAR_HOUSEHOLDER_MOVED_INTO_UNIT",
            "VEHICLES_AVAILABLE",
            "HOUSE_HEATING_FUEL",
            "HOUSING_LACKING_COMPLETE_PLUMBING_FACILITIES",
            "HOUSING_LACKING_COMPLETE_KITCHEN_FACILITIES",
            "HOUSING_NO_TELEPHONE_SERVICE_AVAILABLE",
            "OCCUPANTS_PER_ROOM",
            "HOUSING_VALUE",
            "MORTGAGE_STATUS",
            "SELECTED_MONTHLY_OWNER_COSTS_WITH_MORTGAGE",
            "SELECTED_MONTHLY_OWNER_COSTS_WITHOUT_MORTGAGE",
            "SMOCAPI_WITH_MORTGAGE",
            "SMOCAPI_WITHOUT_MORTGAGE",
            "GROSS_RENT",
            "GRAPI",
            "TOTAL_POP",
            "POP_SEX",
            "AGE",
            "RACE",
        ],
        "Years": [
            "2009", "2010", "2011", "2012", "2013", 
            "2014", "2015", "2016", "2017", "2018",
            "2019", "2020", "2021", "2022", "2023"
        ],
        "Geographies": [
            "country",
            "state",
            "county",
            "census tract",
            "zip code",
            "congressional district",
            "MSA"
        ],
        "Options": {
            "measure": {
                "type": "toggle",                 # dropdown | toggle | multiselect | checkbox | text | int
                "label": "Measure",
                "choices": [("Absolute", "absolute"), ("Proportion", "proportion")],
                "default": "absolute",
            }
        },
    },
    "CDC PLACES": {
        "Variables" : [
            "ARTHRITIS",
            "BPHIGH",
            "CANCER",
            "CASTHMA",
            "CHD",
            "COPD",
            "DEPRESSION",
            "DIABETES",
            "HIGHCHOL",
            "KIDNEY",
            "OBESITY",
            "STROKE",
            "TEETHLOST",
            "BINGE",
            "CSMOKING",
            "LPA",
            "SLEEP",
            "GHLTH",
            "MHLTH",
            "PHLTH",
            "ACCESS2",
            "BPMED",
            "CERVICAL",
            "CHECKUP",
            "CHOLSCREEN",
            "COLON_SCREEN",
            "COREM",
            "COREW",
            "DENTAL",
            "MAMMOUSE",
            "HEARING",
            "VISION",
            "COGNITION",
            "MOBILITY",
            "SELFCARE",
            "INDEPLIVE",
            "DISABILITY",
            "ISOLATION",
            "FOODSTAMP",
            "FOODINSECU",
            "HOUSINSECU",
            "SHUTUTILITY",
            "LACKTRPT",
            "EMOTIONSPT"
        ],
        "Years": [
            "2018", "2019", "2020", "2021", "2022"
        ],
        "Geographies": [
            "state",
            "county",
            "census",
            "zcta",
            "places"
        ],
        "Options": {
            "measure_type": {
                "type": "toggle",                 # dropdown | toggle | multiselect | checkbox | text | int
                "label": "Measure Type",
                "choices": [("Crude", "crude"), ("Age-Adjusted", "age-adjusted")],
                "default": "crude",
            }
        },
    },
    "CDC BRFSS": {
        "Variables" : [  # ← rename to your actual third dataset ID
            'DRNKANY5', '_RFBING5', '_RFDRHV5', '_DRDXAR1',
            '_CASTHM1', '_LTASTH1', 'CVDINFR4', 'CVDSTRK3',
            'CVDCRHD4', 'CHCCOPD1', 'ADDEPEV2', 'DIABETE3',
            'CHCKIDNY', 'CHCOCNCR', 'CHCSCNCR', '_RFBLDS3',
            '_FOBTFS',  '_COL10YR', '_FS5YR',   '_CRCREC',
            'AGE',      'BLIND',    'DIFFALON', 'DIFFDRES',
            'DECIDE',   'DIFFWALK', 'EDUCA',    'EMPLOY1',
            'DEAF',     'INCOME',   'INTERNET', 'MARITAL',
            '_CHLDCNT', 'RACE8',    'RENTHOM1', 'SEX',
            'VETERAN3', '_CURECIG', '_ECIGSTS', 'MEDCOST',
            'HLTHPLN1', 'CHECKUP1', 'PERSDOC2', '_HCVU651',
            '_RFHLTH',  'GENHLTH',  'HIVTST6',  '_FLSHOT6',
            '_PNEUMO2', '_DRNKDRV', '_RFSEAT2', '_ALTETH2',
            '_DENVST2', '_EXTETH2', '_BMI5CAT', '_TOTINDA',
            '_RFPSA21', '_RFSMOK3', 'USENOW3', '_SMOKER3', 
            '_RFMAM2Y', '_MAM5021', '_RFPAP33', 'DRNKANY6', '_RFBING6', '_CHOLCH1',
            '_RFCHOL1', '_LMTACT1', '_LMTWRK1', '_LMTSCL1', '_MICHD', '_FRTLT1A',
            '_VEGLT1A', '_RFHYPE5', 'SHINGLE2', '_PAINDX1', '_PASTAE1', '_PASTRNG',
            '_RFDRHV6', 'CHCKDNY1', '_PNEUMO3', '_ALTETH3', '_DENVST3', '_EXTETH3',
            '_RFPSA22', '_RFMAM21', '_MAM5022', '_RFPAP34', '_RFDRHV7', '_CHOLCH2',
            '_RFCHOL2', '_DRDXAR2', '_LMTACT2', '_LMTWRK2', 'CHCCOPD2', 'ADDEPEV3',
            'DIABETE4', 'CHCKDNY2', '_MENT14D', '_PHYS14D', 'HIVTST7', '_FLSHOT7',
            'TETANUS1', '_PAINDX2', '_PASTAE2', '_RFDRHV8', '_CHOLCH3', '_RFCHOL3',
            'CHCCOPD3', 'CHCOCNC1', 'CHCSCNC1', 'INCOME1', '_CURECI2', 'ECIGNOW2',
            'MEDCOST1', '_HLTHPL1', 'PERSDOC3', '_HCVU653', '_RFHYPE6', '_PAINDX3',
            '_PASTAE3', '_RFBLDS5', '_CRCREC2', '_HLTHPLN', '_HCVU652'
        ],
        "Years": [
            "2011", "2012", "2013", "2014", "2015",
            "2016", "2017", "2018", "2019", "2020",
            "2021", "2022", "2023"
        ],
        "Geographies": [
            "state",
            "msa"
        ],
        "Options": {
            "measure_type": {
                "type": "toggle",                 # dropdown | toggle | multiselect | checkbox | text | int
                "label": "Measure Type",
                "choices": [("Crude", "crude"), ("Age-Adjusted", "age-adjusted")],
                "default": "crude",
            },
            "break_out": {
                "type": "dropdown",
                "label": "Breakout Category",
                "choices": [
                    ("Overall", "Overall"),
                    ("Sex", "Sex"),
                    ("Age Group", "Age Group"),
                    ("Race/Ethnicity", "Race/Ethnicity"),
                    ("Education Attained", "Education Attained"),
                    ("Household Income", "Household Income")
                ]
            }
        },
    }
}

class Explorer:
    """A small, dependency-light ipywidgets app."""

    def __init__(self):
        
        self.option_widgets = {}
        
        ds_ids = list(VARIABLE_CATALOG.keys())

        self.dataset = w.Dropdown(
            options=ds_ids,
            value=ds_ids[0],
            description="Dataset",
        )

        self.variable = w.Dropdown(
            options=VARIABLE_CATALOG[self.dataset.value]["Variables"],
            description="Variable",
        )

        self.year = w.Dropdown(
            options = VARIABLE_CATALOG[self.dataset.value]["Years"],
            description="Year",
        )

        self.geography = w.Dropdown(
            options = VARIABLE_CATALOG[self.dataset.value]["Geographies"],
            description="Geography",
        )
    
        # Dataset-specific options live here
        self.opts_box = w.VBox([])   # filled when dataset changes

        # Actions & outputs
        self.get_btn = w.Button(description="Get data", button_style="primary", icon="download")
        self.status = w.HTML()
        self.preview = w.Output()     # for df.head()
        self.download = w.Output()    # for a FileLink (or data-URI)

        # (Optional) A label showing the current selection
        self.selection = w.HTML()

        # Wire events
        self.dataset.observe(self._on_dataset_change, names="value")
        self.variable.observe(self._on_variable_change, names="value")
        self.year.observe(self._on_year_change, names="value")
        self.geography.observe(self._on_geography_change, names="value")
        self.get_btn.on_click(self._on_get_data)

        self.root = w.VBox(
            [
                w.HTML("<h3>Federal Data – Quick Picker</h3>"),
                self.dataset,
                self.variable,
                self.year,
                self.geography,
                self.opts_box,
                self.selection,
                w.HBox([self.get_btn, self.status]),
                self.preview,
                self.download,
            ]
        )

        # Initialize
        self._on_dataset_change({"new": self.dataset.value})

    # Auto-display in notebooks when the object is the last expression
    # def _ipython_display_(self):
    #     display(self.root)

    def _on_dataset_change(self, change):
        ds = change["new"]
        spec = VARIABLE_CATALOG.get(ds, {})

        # Update the variable dropdown options to match the dataset
        vars_for_ds = VARIABLE_CATALOG.get(ds, {}).get("Variables", [])
        # Preserve value if still valid, else fall back to first option
        new_value = self.variable.value if self.variable.value in vars_for_ds else (vars_for_ds[0] if vars_for_ds else None)
        self.variable.options = vars_for_ds
        self.variable.value = new_value

        # update year options 
        years_for_ds = VARIABLE_CATALOG.get(ds, {}).get("Years", [])
        # Preserve value if still valid, else fall back to first option
        new_value = self.year.value if self.year.value in years_for_ds else (years_for_ds[0] if years_for_ds else None)
        self.year.options = years_for_ds
        self.year.value = new_value

        # update year options 
        geographies_for_ds = VARIABLE_CATALOG.get(ds, {}).get("Geographies", [])
        # Preserve value if still valid, else fall back to first option
        new_value = self.geography.value if self.geography.value in geographies_for_ds else (geographies_for_ds[0] if geographies_for_ds else None)
        self.geography.options = geographies_for_ds
        self.geography.value = new_value

        self._build_options(spec.get("Options", {}))

        self._update_selection_label()

    def _build_options(self, options_spec: dict):
        """Create widgets from Options spec and place them in opts_box."""
        self.option_widgets = {}
        widgets = []
        for name, spec in options_spec.items():
            wid = self._make_option_widget(spec)
            self.option_widgets[name] = wid
            if hasattr(wid, "observe"):
                wid.observe(lambda _ : self._update_selection_label(), names="value")
            widgets.append(wid)
        self.opts_box.children = tuple(widgets)

    def _make_option_widget(self, spec: dict) -> w.Widget:
        kind = spec.get("type", "dropdown")
        label = spec.get("label", "Option")
        default = spec.get("default", None)

        # normalize choices; allow list[str] or list[(label, value)]
        raw_choices = spec.get("choices", [])
        if raw_choices and isinstance(raw_choices[0], (list, tuple)):
            options = raw_choices  # already (label, value) pairs
            default = default if default is not None else options[0][1]
        else:
            options = raw_choices  # simple list; Dropdown/ToggleButtons can take it

        if kind == "toggle":
            return w.ToggleButtons(description=label, options=options, value=default)
        if kind == "multiselect":
            # default may be list/tuple; SelectMultiple expects a tuple
            if default is None: default = []
            return w.SelectMultiple(description=label, options=options, value=tuple(default))
        if kind == "checkbox":
            return w.Checkbox(description=label, value=bool(default))
        if kind == "int":
            return w.IntText(description=label, value=int(default) if default is not None else 0)
        if kind == "text":
            return w.Text(description=label, value=str(default) if default is not None else "")
        # default: dropdown
        return w.Dropdown(description=label, options=options, value=default if default in (list(zip(*options))[1] if options and isinstance(options[0], (list, tuple)) else options) else (options[0][1] if options and isinstance(options[0], (list, tuple)) else (options[0] if options else None)))

    def _on_variable_change(self, _):
        self._update_selection_label()
    
    def _on_year_change(self, _):
        self._update_selection_label()

    def _on_geography_change(self, _):
        self._update_selection_label()

    # --- Fetch + preview + download -----------------------------------------

    def _on_get_data(self, _):
        self.status.value = "⏳ Querying…"
        self.preview.clear_output()
        self.download.clear_output()

        ds = self.dataset.value
        var = self.variable.value
        yr = self.year.value
        geo = self.geography.value
        opts = self._collect_options()  # dataset-specific kwargs

        try:
            df = self.fetch_fn(ds, var, yr, geo, **opts)

            # Preview
            with self.preview:
                import pandas as pd  # lazy import for safety
                display(df.head() if hasattr(df, "head") else pd.DataFrame(df))

            # Download link via temp file (robust in notebooks)
            fname = f"{ds}_{var}_{yr}_{geo}.csv".replace(" ", "_")
            tmpdir = tempfile.mkdtemp(prefix="feddata_")
            path = os.path.join(tmpdir, fname)
            # Write CSV
            df.to_csv(path, index=False)

            with self.download:
                display(FileLink(path, result_html_prefix="Download CSV: "))

            self.status.value = f"✅ Loaded {len(df):,} rows"
        except Exception as e:
            self.status.value = f"<span style='color:#b00020'>❌ {type(e).__name__}: {e}</span>"

    # --- Helpers -------------------------------------------------------------

    def _preserve_or_first(self, current, options):
        return current if (current in options) else (options[0] if options else None)

    def _collect_options(self) -> dict:
        out = {}
        for name, wid in self.option_widgets.items():
            val = getattr(wid, "value", None)
            # SelectMultiple returns a tuple -> convert to list
            if isinstance(wid, w.SelectMultiple):
                val = list(val)
            out[name] = val
        return out

    def _update_selection_label(self):
        ds = self.dataset.value
        var = self.variable.value
        yr = self.year.value
        geo = self.geography.value
        bits = [f"<b>Selected:</b> {ds}"]
        if var: bits.append(f"→ <code>{var}</code>")
        if yr:  bits.append(f"→ {yr}")
        if geo: bits.append(f"→ {geo}")
        # summarize options
        if self.option_widgets:
            opts = []
            for k, wid in self.option_widgets.items():
                v = getattr(wid, "value", None)
                if isinstance(wid, w.SelectMultiple):
                    v = ", ".join(map(str, v))
                opts.append(f"{k}={v}")
            bits.append(f"({'; '.join(opts)})")
        self.selection.value = " ".join(bits)

    def fetch_fn(self, dataset, variable, year, geography, **options):
        """
        Fallback to your package's fetch. Replace with your real import/signature if different.
        Expected to return a pandas.DataFrame.
        """

        if dataset == "ACS":
            from fedwrap import get_acs_data

            if options.get("measure") == "proportion":
                return get_acs_data(measureid=variable, year=year, geo=geography, as_percent=True)
            return get_acs_data(measureid=variable, year=year, geo=geography)
        
        elif dataset == "CDC PLACES":
            from fedwrap import get_places_data

            if options.get("measure_type") == "age-adjusted":
                datavaluetypeid = "AgeAdjPrv"
            else:
                datavaluetypeid = "CrdPrv"

            return get_places_data(measureid=variable, year=year, geo=geography, datavaluetypid=datavaluetypeid)
        
        elif dataset == "CDC BRFSS":
            from fedwrap import get_brfss_data

            if options.get("measure_type") == "age-adjusted":
                variable_type = "age-adjusted"
            else:
                variable_type = "crude"

            break_out = options.get("break_out", "Overall")

            return get_brfss_data(
                geo=geography, 
                measure=variable_type, 
                year=year,
                question_id=variable,
                break_out_category=break_out,
            )


def display_explorer() -> Explorer:
    """Build and display the explorer; return the object for further use."""
    ui = Explorer()
    display(ui.root)
    return ui