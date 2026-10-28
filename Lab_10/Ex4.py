# Read a json file of taxi trip data and create a data frame and some simple stats
# Kaili Takara
# October 28, 2026

import pandas as pd

# Read the json dile into a data frame
results_df = pd.read_json('taxi_trips.json')

# Display the first few rows of the data frame
print(results_df.head(6))

# Displays basic statistics abou the data frame
print(results_df.describe())

median = results_df['fare'].median()
print("The median fare value is: ", median)
