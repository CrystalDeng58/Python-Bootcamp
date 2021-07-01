import bs4 as bs
import requests

page = requests.get("http://rss.weather.gov.hk/rss/CurrentWeather.xml")
soup = bs.BeautifulSoup(page.content, "lxml")

item = list(soup.find_all("td"))
temp = []

for i in range(len(item)):
    temp.append(item[i].get_text())

location = []
info = []

for i in range(0, len(temp), 2):
    location.append(temp[i])
    info.append(temp[i + 1])

print(location, "\n\n")
print(info)
