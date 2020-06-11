import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import json

url = 'http://www.met.gov.my/forecast/weather/town'
response = requests.get(url)
result = BeautifulSoup(response.text, "html.parser")

title = result.find("h3",{"class":"met-man-toggle"}).text 
kota = result.find("caption").text
print(title, "|", kota)
oke = result.findAll('tbody')
x = []
for row in oke:
    for i in range(len(row)):
        formula_1 = (2 * i - 1)
        res = {}
        res['Tarikh'] = row("td",{"style":"text-align: center; vertical-align: middle;"})[formula_1 - 1].get_text(separator=" ").strip()
        cuaca = row("td",{"style":"text-align: center; vertical-align: middle;"})[formula_1].text
        res['Cuaca'] = re.sub(r'\n|\s+$', r'', cuaca)
        ramalan = row("td",{"style":"text-align: left; vertical-align: middle;"})[i].text
        ramalan_2 = re.sub(r'\u00b0|\s+$|^\W+', r'', ramalan)
        res['Ramalan'] = re.split(r'\n', ramalan_2)
        x.append(res)

print(json.dumps(x, indent=4))