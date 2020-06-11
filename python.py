import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import json
s = "wwww"
url = 'http://www.met.gov.my/forecast/weather/town'
response = requests.get(url)
result = BeautifulSoup(response.text, "html.parser")

title = result.find("h3",{"class":"met-man-toggle"}).text 
kota = result.find("caption").text
print(title, "|", kota)
oke = result.findAll('tbody')
x = []
for row in oke:
    for i in range(len(row)-1):
        formula_1 = (2 * i - 1)
        res = {}
        res['Tarikh'] = row("td",{"style":"text-align: center; vertical-align: middle;"})[formula_1 + 1].get_text(separator=" ").strip()
        cuaca = row("td",{"style":"text-align: center; vertical-align: middle;"})[formula_1 + 2].text
        res['Cuaca'] = re.sub(r'\n|\s+$', r'', cuaca)
        ramalan = row("td",{"style":"text-align: left; vertical-align: middle;"})[i].text
        ramalan_2 = re.sub(r'\u00b0|\s+$|^\W+', r'', ramalan)
        res['Ramalan'] = re.split(r'\n', ramalan_2)
        #xxx = res["Jam"].find("td",{"style":"text-align: center; vertical-align: middle;"})[i].text
        x.append(res)

print(json.dumps(x, indent=4))


# import bs4
# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup
# my_url= 'http://www.met.gov.my/forecast/weather/town'
# uClient= uReq(my_url)
# page_html = uClient.read() 
# uClient.close()
# page_soup = soup(page_html,"html.parser")
# containers = page_soup.find_all("div",{"style":"text-align: center; vertical-align: middle;"})
# #<div id="table-forecast-type" class="col-lg-3 col-md-3 col-xs-12">
# #print(containers[0])
# # print(page_soup.td.text)
# # table = page_soup.find("h3",{"class":"met-man-toggle"}).text

# # print(x[0].text)
# #print(table) 
# # l=[]
# # for items in table:
# # #     for i in range(len(items.find_all("td"))-1):
# #     d = {}  
# #     d["Tarikh"]=items.find_all("td",{"style":"date-time"})[i].text
# #     d["date"]=items.find_all("td",{"style":"day-detail"})[i].text
# #     d["desc"]=items.find_all("td",{"style":"description"})[i].text 
# #     d["temp"]=items.find_all("td",{"style":"temp"})[i].text 
# #     d["precip"]=items.find_all("td",{"style":"precip"})[i].text
# #     d["wind"]=items.find_all("td",{"style":"wind"})[i].text  
# #     d["humidity"]=items.find_all("td",{"style":"humidity"})[i].text 
# #     l.append(d)

        
# # page_soup.head
# # page_soup.body.spa
# # containers = page_soup.findAll("tr",{"style":"Pagi"})
# # print (containers)

# # contain = containers[0]
# # container = containers[0]
# # container.img["title"]
# # container.strong.text.strip()
# # print(f'The price : $ {priceC_0}')


# # table=page_soup.find_all("table",{"id":"twc-forecast_table"})
# # l=[]
# # for items in table:
# #  for i in items.find_all("tr"):

# #      d = {}  
# #      d["Tarikh"]=items.find_all("td",{"style":"text-align: center; vertical-align: middle;"})[i].text
# #      d["Cuaca"]=items.find_all("td",{"style":"text-align: center; vertical-align: middle;"})[i].tex
# #      d["Ramalan"]=items.find_all("td",{"style":"text-align: left; vertical-align: middle;"})[i].tex
# #      l.append(d)

# print(page_soup.find_all("td",{"style":"text-align: center; vertical-align: middle;"})[8].text)