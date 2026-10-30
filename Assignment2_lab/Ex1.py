#
#
#

import pandas as pd


csv_file = 'https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'

try:
    df = pd.read_csv(csv_file,engine='pyarrow',on_bad_lines='skip')
    outfile = 'sales_data_test.csv'
    df.head(10).to_csv(outfile, index=False)
    print(f"Frist 10 rows of {csv_file} saved to {outfile}")
    
except Exception as e:
    print("Error reading the CSV file:", e)