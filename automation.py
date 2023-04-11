import git

# Initialiser le repo Git
repo = git.Repo('https://github.com/R-D-Y/alerte-anssi/anssi-alert.py')

# Récupérer la branche courante
current_branch = repo.active_branch

# Ouvrir le fichier resultats.md en mode écriture
with open('resultats.md', 'w') as f:
    f.write("Titre: {}\n".format(titre))
    f.write("Date: {}\n".format(date))
    f.write("Description: {}\n".format(description))
    f.write("PDF: {}\n".format(pdf))
    f.write("Alerte: {}\n".format(alerte))
    f.write("Detail: {}\n".format(detail))
    f.write("Lien vers le reste de l'article : <a href='" + detail + "'>Cliquez ici</a>\n")

# Ajouter le fichier resultats.md et valider les modifications
repo.index.add(['resultats.md'])
repo.index.commit("Dernière alerte de l'ANSSI")

# Pousser les modifications vers la branche courante
repo.git.push('origin', current_branch.name)
