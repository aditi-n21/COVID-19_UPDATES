#covid updates
#use urlib and beautiful soup
from urllib.request import urlopen, Request 
from bs4 import BeautifulSoup as bs

# to get the notification
from win10toast import ToastNotifier

url = "https://www.mygov.in/covid-19"

#  Get the HTML
header ={"User-Agent":"Mozilla"}
req = Request("https://www.mygov.in/covid-19",headers=header)
html= urlopen(req)
# object of bs
soup=bs(html, features="html5lib")
# 1
case=soup.find("span",{"class":"icount"}).text
# 2
deaths=soup.find("div",{"class":"iblock death_case"}).span.text
# 3
cured=soup.find("div",{"class":"iblock discharge"}).span.text
# notification

notification = ToastNotifier()
message="Active - "+case+"\nDeaths - "+deaths+"\nCured - "+cured
notification.show_toast(title="COVID-19 Update",msg=message,duration=5,icon_path="virus.ico")