import requests
from bs4 import BeautifulSoup

url = "https://www.cert.ssi.gouv.fr/alerte/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


#Description de l'article
description = soup.select_one("body > div > div > section > div:nth-child(2) > div > div.cards > section > article:nth-child(1) > section.item-excerpt > p").text.strip()

#Lien vers le reste de l'article
detail= soup.select_one("body > div > div > section > div:nth-child(2) > div > div.cards > section > article:nth-child(1) > section.item-header > div.item-title > h3 > a")['href']

#date de l'article
date = soup.select_one("body > div > div > section > div:nth-child(2) > div > div.cards > section > article:nth-child(1) > section.item-header > div.item-meta > span.item-date").text.strip()

#titre de l'article
titre = soup.select_one("body > div > div > section > div:nth-child(2) > div > div.cards > section > article:nth-child(1) > section.item-header > div.item-title > h3 > a").text.strip()

#lien vers le pdf
pdf = soup.select_one("body > div > div > section > div:nth-child(2) > div > div.cards > section > article:nth-child(1) > section.item-header > div.item-meta > a")["href"]

#etat de l'alerte
alerte = soup.select_one("body > div > div > section > div:nth-child(2) > div > div.cards > section > article:nth-child(1) > section.item-header > div.item-meta > span.item-status").text.strip()

#> print on a readme
print("Titre:", titre)
print("Date:", date)
print("Description:", description)
print("PDF:", pdf)
print("Alerte:", alerte)
print("Detail:", detail)
print("Lien vers le reste de l'article : <a href='" + detail + "'>Cliquez ici</a>")


