# Get a URL from the user, clean it, and extract the domanin name and the TLD (Top-Level Domain)
# Kaili Takara
# Date: Sept 18, 2026

url = input("Enter a URL: ")

clean_url = url.replace("https://","")
cleaned_url = clean_url.replace("/","")
print ("Cleaned URL:", cleaned_url)

parts = cleaned_url.split(".")
print("The parts are:", parts)

domain_name = parts[1]
tld = parts[2]
print("Domain name:", domain_name)
print("TLD:", tld)