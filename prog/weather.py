import urllib.request
from bs4 import BeautifulSoup

url = "https://wttr.in/"
with urllib.request.urlopen(url) as request:
    html = request.read()

bs = BeautifulSoup(html, "html.parser")

#print(bs.text)
print("Температура", bs.find("span", {"class":"ef050"}).text, ", ощущается как", bs.find("span", {"class":"ef051"}).text, chr(127777))
print("Скорость ветра", bs.find("span", {"class":"ef118"}).text, chr(127744))

# вывести 3 строки температура, скорость ветра, видимость и какие-нибудь эмодзи
# для 2.3 sabplots данные погоды
