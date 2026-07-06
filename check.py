import requests
from bs4 import BeautifulSoup

URL = "https://hottarakashi-camping.com/reserve/?ym=202607"

r = requests.get(URL, timeout=30)
print(r.status_code)

soup = BeautifulSoup(r.text, "lxml")

tables = soup.find_all("table")

print("table:", len(tables))
