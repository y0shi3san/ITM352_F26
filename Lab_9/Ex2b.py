#
#
# Kaili Takara
# October 21, 2026

import csv
import os

#check if the file exist and is readable
if not os.path.exists("windows_cleaning_employer.csv"):
    print("Error: File windows_cleaning_employer.csv not found")
    exit(1)
else:
    file_size = os.path.getsize("windows_cleaning_employer.csv")
    print(f"File exist and is readable. Size: {file_size} bytes")


csv_filename = "windows_cleaning_employer.csv"
salaries = []

# Read the CSV file and store the salaries in a list
with open(csv_filename, "r") as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Skip the header row
    print(f"Headers: {headers}")
    salary_index = headers.index("Annual_Salary")  # Find the index of the "Salary" column
    for row in reader:
        salary = float(row[salary_index])  # Assuming the salary is in the identified column
        salaries.append(salary)
