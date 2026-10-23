# Analyze an array of tuples using numpy
# Kaili Takara
# October 23, 2026

import numpy as np
import os

# Create an array of tuples of household income and percentiles
hh_income =[
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292),
]

hh_income_array = np.array(hh_income)

# Report the dimensions of the array and the number of elements in the array
print(f"Dimensions of the array: {hh_income_array.ndim}")
print(f"Number of elements in the array: {hh_income_array.size}")

for i in range(hh_income_array.shape[0]):
    percentile, income = hh_income_array[i]
    print(f"Percentile: {percentile}, Income: {income}")

for i in range(hh_income_array.shape[0]):
    print(hh_income_array[i, 0], hh_income_array[i, 1])

file_path = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "Lab_9", "names.txt")
)

if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
    try:
        with open(file_path, "r", encoding="utf-8"):
            print(f"File: {file_path}")
            print(f"Size: {os.path.getsize(file_path)} bytes")
    except OSError as error:
        print(f"Could not open {file_path}: {error}")
else:
    print(f"File does not exist or is not readable: {file_path}")
