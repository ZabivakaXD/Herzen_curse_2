import urllib.request
from bs4 import BeautifulSoup

url = "https://wttr.in/"
with urllib.request.urlopen(url) as request:
    html = request.read()

bs = BeautifulSoup(html, "html.parser")
texts = bs.text

index_place = texts.find("Weather report:") + 15
index_end_place = index_place + 30
place = texts[index_place:index_end_place].strip()

index_weather = texts.find(" °C")
index_start_weather = index_weather - 8
weather = texts[index_start_weather:index_weather].strip().replace('(', ' ').replace(')', '').split(' ')

index_wind = texts.find("km/h")
index_start_wind = index_wind - 4
wind = texts[index_start_wind:index_wind].strip()

print(bs.text)
print("Погода в", place)
print("Температура", weather[0], "°C, ощущается как", weather[1],"°C", chr(127777))
print("Скорость ветра", wind, "км/ч", chr(127744))
# print("Температура", bs.find("span", {"class":"ef047"}).text, ", ощущается как", bs.find("span", {"class":"ef048"}).text, chr(127777))
# print("Скорость ветра", bs.find("span", {"class":"ef226"}).text, chr(127744))

# вывести 3 строки температура, скорость ветра, видимость и какие-нибудь эмодзи
