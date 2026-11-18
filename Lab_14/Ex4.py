# Get public liscense data from City of Chicago's data portal
# Kaili Takara
# November 18, 2026

import pandas as pd
from sodapy import Socrata


client = Socrata("data.cityofchicago.org", None)


# Specify the specific JSON dataset

json_file = "rr23-ymwb"

results = client.get(json_file, limit=500)
#convert to pandas dataframe
results_df = pd.DataFrame.from_records(results)
results_df.info()

vehicles = results_df[["public_vehicle_number", "vehicle_fuel_source"]]
print("Vehicles and fuel source:")

vehicles.info()
vehicles_by_fuel = vehicles.groupby("vehicle_fuel_source").count()
print(vehicles_by_fuel)