# Scrap names of ITM Falculty and grad students
# Kaili Takara
# November 18, 2026

import ssl
import urllib.request
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

itm_url = "https://shidler.hawaii.edu/itm/people"
print("Retrieving", itm_url)

itm_page = urllib.request.urlopen(itm_url)
itm_names = []

soup = BeautifulSoup(itm_page, "html.parser")
#Find all the faulty, which are in h2 tags with class="title"
faulty = soup.find_all("h2", class_="title")

for person in faulty:
    itm_names.append(person.text)
    print("Faulty:", person.text)

print("Total faulty:", len(itm_names))