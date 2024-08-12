from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
responce = requests.get(url)
html = responce.text

soup = BeautifulSoup(html, "html.parser")

text = soup.find_all("span", class_="text")
print(text)
author = soup.find_all("small", class_="author")
print(author)

for i in range(len(text)):
    print(f"Цитата № - {i+1}")
    print(text[i].text)
    print(f"Автор цитаты - {author[i].text}\n")
