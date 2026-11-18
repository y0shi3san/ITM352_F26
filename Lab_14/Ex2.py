# Grab 1 month interest rate data from the US treasury website
# Kaili Takara
# November 18, 2026

import ssl, lxml
import pandas as pd
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"
print("Retrieving", url)

webpage = urllib.request.urlopen(url)
df = pd.read_html(webpage)
print("columns:", df[0].columns)
