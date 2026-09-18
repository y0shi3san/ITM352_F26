# simply dictionary excample

country_capitals = {
    "Germany": {"capital": "Berlin", "population": 84700000},
    "Canada": {"capital": "Ottawa", "population": 41300000},
    "France": {"capital": "Paris", "population": 68600000},
}

print("Country capitals:", country_capitals)
print(country_capitals["Canada"])

country_capitals["England"] = {"capital": "London", "population": 57700000}
print(country_capitals["England"])

print("Germany" in country_capitals)
print("Spain" not in country_capitals)