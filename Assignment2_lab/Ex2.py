#
#
#

import pandas as pd
import time

csv_file = 'https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'


def load_csv(filepath):
    print(f"Loading CSV filr from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(csv_file,engine='pyarrow',on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Numbers of rows: {len(df)}")
        
    except Exception as e:
        print("Error reading the CSV file:", e)


try:
    df = pd.read_csv(csv_file,engine='pyarrow',on_bad_lines='skip')
    print(df.head())
except Exception as e:
    print("Error reading the CSV file:", e)

# Call load_csv to lead the data and print the first 10 rows
csv_file = 'https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'
sales_data = load_csv(csv_file)

# Check if the data frame was loaded successfully before attempting to print the first 10 rows
if sales_data is not None:
    print(sales_data.head(10))
