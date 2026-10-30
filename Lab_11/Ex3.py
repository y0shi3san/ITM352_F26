# Create a dataframe from a csv file, create a pivot table aggregating sales by region and order_type
# Kaili Takara
# October 30, 2026

import pandas as pd
import numpy as np

# Tell pandas to print all colims when displaying a dataframe
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', "{:,.2f}" )

csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

try:
    df = pd.read_csv(csv_file, engine='pyarrow', on_bad_lines='skip')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', format='%Y-%n-%d')
    #print(df.head())

    # Calculate sales total per row, for later something
    df['sales'] = df['quantity']* df['unit_price']

    # Create a pivot table aggregating sales bu region and order_type
    pivot_table = pd.pivot_table(df,
                                 values='sales',
                                 index='customer_state',
                                 columns= ['customer_type', 'order_type'],
                                 aggfunc="mean",
                                 margin=True,
                                 margin_name='Total Sales')

    print(pivot_table)

except Exception as e:
    print(f"Error occurred while reading the CSV file: {e}")