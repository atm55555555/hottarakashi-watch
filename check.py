import requests
from bs4 import BeautifulSoup

URL = "https://www3.yadosys.com/reserve2/ja/room/calendar/147/ehejfcebejdheigbgihfgpdn/all"

r = requests.get(URL, timeout=30)
print(r.status_code)

soup = BeautifulSoup(r.text, "lxml")

tables = soup.find_all("table")

print("table:", len(tables))
