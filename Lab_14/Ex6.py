# Use request package to retrive a page of morgage rate info.
# Kaili Takara
# November 18, 2026

import requests

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
print("Retrieving", url)

response = requests.get(url, timeout=10)
response.raise_for_status()

print(response.text)



