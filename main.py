import requests
from bs4 import BeautifulSoup
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

df = pd.read_csv("Stock List 16 Nov 2023.csv", index_col=1)
list_saham = []
for code in df.index:
    list_saham.append(code)

#print(list_saham)




#URL = "https://investasi.kontan.co.id/"
URL = "https://search.bisnis.com/?q=rekomendasi+saham"
headers ={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57",
    "Accept-Language" : "en-US,en;q=0.9,id;q=0.8"
}
try:
    response = requests.get(URL, headers=headers, timeout=5)
except:
    response="No Response"

website = response.text

soup = BeautifulSoup(website, "html.parser")
news = soup.find("a", class_="icon")

NEW_URL = news.get("href")
new_response = requests.get(NEW_URL, headers=headers)
new_website = new_response.text
soup2 = BeautifulSoup(new_website, "html.parser")

content = soup2.find("article", class_="detailsContent")
text_content = content.text
news_title = soup2.find("h1", class_="detailsTitleCaption")

recommended = False
rec_saham = []
for saham in list_saham:
    if saham in text_content:
        rec_saham.append(saham)
        recommended = True
    else:
        pass


my_email = "leonarduslaksmana1502@gmail.com"
#password = "ojejvftmdwswitjf"
password = "giruysojrhwpscib"

if recommended is True:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=["leonarduslaksmana1502@yahoo.com", "agnethavaleriame@gmail.com"],
                            msg=f"Subject: {news_title.text}\n\nList saham = {rec_saham}\nLink = {NEW_URL}")








