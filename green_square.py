import git
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



#resultat
#print("Titre:", titre)
#print("Date:", date)
#print("Description:", description)
#print("PDF:", pdf)
#print("Alerte:", alerte)
#print("Detail:", detail)
#print("Lien vers le reste de l'article : <a href='" + detail + "'>Cliquez ici</a>")

content = f"""
Titre : {titre}
Date : {date}
Description : {description}
PDF : {pdf}
Alerte : {alerte}
Detail : {detail}
Lien vers le reste de l'article : <a href='{detail}'>Cliquez ici</a>

"""

# Ecriture dans le fichier resultat.md
with open("resultat.md", "w", encoding="utf-8") as f:
    f.write(content)


#    f.write(f"Titre: {titre}\n")
#    f.write(f"Date: {date}\n")
#    f.write(f"Description: {description}\n")
#    f.write(f"PDF: {pdf}\n")
#    f.write(f"Alerte: {alerte}\n")
#    f.write(f"Detail: {detail}\n")
#    f.write(f"Lien vers le reste de l'article : <a href='{detail}'>Cliquez ici</a>\n")

# Ajout du fichier resultat.md dans le repo
#repo = git.Repo("C:/Users/remid/OneDrive/Bureau/M1/ProjetAnnuel23/infrastructure/")
#repo.git.add(".")
#repo.index.commit("Mise à jour du fichier resultat.md")
#origin = repo.remote(name='remi')
#origin.push()
