# Задача
# Получить сегодняшний день, число, месяц, температуру, погоду, записать результаты в файлик csv

import requests
from bs4 import BeautifulSoup

doc_for_parser = open('homework_parser/doc_for_parser.csv', 'w')

url = 'https://www.meteoprog.ua/ru/weather/Kyiv/'
source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

div = soup.find("div", {'id':'reviewforecast_pjax_container'})
title = div.find("h2", {'class':'detailTitle'}).text
print (title)
doc_for_parser.write(title + '\n')
day = div.find("div", {"class": "dayoffWeek"}).text.replace(" ", "")
day = day[1:8]
print (day)
doc_for_parser.write(day + '\n')
date = div.find("div", {"class": "dayoffMonth"}).text.strip()
print (date)
doc_for_parser.write(date + '\n')
natural_phenomena = div.find("ul", {"class":"UlSlider"}).findAll("li", {"data-daynumber":"0"})
for pogodnie_uslovia in natural_phenomena:
     pogodnie_uslovia = pogodnie_uslovia["title"]
     print(pogodnie_uslovia)
     doc_for_parser.write(pogodnie_uslovia + '\n')

doc_for_parser.close()




