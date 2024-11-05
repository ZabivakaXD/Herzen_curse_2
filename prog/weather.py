import urllib.request
from bs4 import BeautifulSoup

url = "https://wttr.in/"
with urllib.request.urlopen(url) as request:
    html = request.read()

bs = BeautifulSoup(html, "html.parser")
print(bs)

print(bs.find("span", {"class":"ef118"}).string)
