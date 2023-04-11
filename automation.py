import git

# Récupération des résultats
titre = "..."
date = "..."
description = "..."
pdf = "..."
alerte = "..."
detail = "..."
resultat = (
    f"Titre: {titre}\n"
    f"Date: {date}\n"
    f"Description: {description}\n"
    f"PDF: {pdf}\n"
    f"Alerte: {alerte}\n"
    f"Detail: {detail}\n"
    f"Lien vers le reste de l'article : <a href='{detail}'>Cliquez ici</a>"
)

# Récupération du dépôt Git
repo = git.Repo("https://github.com/R-D-Y/alerte-anssi")

# Écriture des résultats dans le fichier resultat.md
with open("resultat.md", "w") as f:
    f.write(resultat)

# Ajout et envoi des modifications
repo.git.add("resultat.md")
repo.index.commit("Mise à jour du fichier resultat.md")
origin = repo.remote(name="origin")
origin.push()
