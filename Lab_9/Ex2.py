#
#
#

import csv
csv_filename = "windows_cleaning_employer.csv"
salaries = []

# Read the CSV file and strore the salaries in a list
with open(csv_filename, "r") as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Skip the header row
    print(f"Headers: {headers}")
    salary_index = headers.index("Annual_Salary")  # Find the index of the "Salary" column
    for row in reader:
        salary = float(row[salary_index])  # Assuming the salary is in the identified column
        salaries.append(salary)


# Compute Salary Stats
avg_salary = sum(salaries) / len(salaries)
min_salary = min(salaries)
max_salary = max(salaries)

# Print the stats
print(f"Average Salary: ${avg_salary:,.2f}")
print(f"Minimum Salary: ${min_salary:,.2f}")
print(f"Maximum Salary: ${max_salary:,.2f}")
