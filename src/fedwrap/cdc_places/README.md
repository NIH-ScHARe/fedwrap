🧭 **Overivew** 

A Python wrapper for the CDC's PLACES API. Simplifies fetching PLACES data.

🛠️ **Installation** 

```bash
pip install fedwrap
```

📝 **Instructions**

Calls to cdc_places occur through the get_places_data function. 

``` python
from fedwrap.cdc_places import get_places_data

get_places_data(GEO, YEAR, MEASUREID, DATAVALUETYPID)
```

🌐 *GEO*

The GEO parameter sets the geographical division for the data. The PLACES dataset supports the following geographies:
* county
* census
* zcta
* places

📆 *YEAR* 

The year parameter sets the year for which the data was collected. Note that release year of CDC PLACES data and the year of the underlying data are not the same. The YEAR parameter captures the actual year of the underlying data. 2018-2022 are supported for most variables. 

📏 *MEASUREID* 

The MEASUREID parameter sets the variable which is extracted from the PLACES dataset. The values and corresponding names are as follows: 

| MEASUREID | Measure Full Name |
|-|-|
ARTHRITIS | Arthritis among adults
BPHIGH | High blood pressure among adults
CANCER | Cancer (non-skin) or melanoma among adults
CASTHMA | Current asthma among adults
CHD | Coronary heart disease among adults
COPD | Chronic obstructive pulmonary disease among adults
DEPRESSION | Depression among adults
DIABETES | Diagnosed diabetes among adults
HIGHCHOL | High cholesterol among adults who have ever been screened
KIDNEY | Chronic kidney disease among adults aged &gt;=18 years
OBESITY	| Obesity among adults
STROKE	| Stroke among adults
TEETHLOST |	All teeth lost among adults aged >=65 years
BINGE |	Binge drinking among adults
CSMOKING |	Current cigarette smoking among adults
LPA |	No leisure-time physical activity among adults
SLEEP |	Short sleep duration among adults
GHLTH |	Fair or poor self-rated health status among adults
MHLTH |	Frequent mental distress among adults
PHLTH |	Frequent physical distress among adults
ACCESS2 |	Lack of health insurance among adults aged 18â€“64 years
BPMED |	Taking medicine to control high blood pressure among adults with high blood pressure
CERVICAL |	Cervical cancer screening among adult women aged 21â€“65 years
CHECKUP | 	Routine checkup within the past year among adults
CHOLSCREEN |	Cholesterol screening in the past 5 years among adults
COLON_SCREEN |	Colorectal cancer screening among adults aged 45â€“75 years
COREM |	Older adult men aged >=65 years who are up to date on a core set of clinical preventive services: Flu shot past year, PPV shot ever, Colorectal cancer screening
COREW |	Older adult women aged >=65 years who are up to date on a core set of clinical preventive services: Flu shot past year, PPV shot ever, Colorectal cancer screening, and Mammogram past 2 years
DENTAL |	Visited dentist or dental clinic in the past year among adult
MAMMOUSE |	Mammography use among women aged 50â€“74 years
HEARING |	Hearing disability among adults
VISION |	Vision disability among adults
COGNITION |	Cognitive disability among adults
MOBILITY |	Mobility disability among adults
SELFCARE |	Self-care disability among adults
INDEPLIVE |	Independent living disability among adults
DISABILITY |	Any disability among adults
ISOLATION |	Feeling socially isolated among adults
FOODSTAMP |	Received food stamps in the past 12 months among adults
FOODINSECU |	Food insecurity in the past 12 months among adults
HOUSINSECU |	Housing insecurity in the past 12 months among adults
SHUTUTILITY |	Utility services threat in the past 12 months among adults
LACKTRPT |	Lack of reliable transportation in the past 12 months among adults
EMOTIONSPT |	Lack of social and emotional support among adults

🆔 *DATAVALUETYPID*

The DATAVALUETYPID parameter sets the data value measurement to pull from the dataset. The two options are: 
* CrvPrv - crude prevalance 
* AgeAdjPrv - Age-adjusted prevalance 