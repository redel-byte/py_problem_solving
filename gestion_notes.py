nom = "Karim"
prenom = "Ben Ali"
notes = [12, 15, 9]

total = notes[0] + notes[1] + notes[2]
moyenne = total / 3

print(f"{nom} moyenne : {moyenne:>6.2f}")
print()


def calculer_moyenne(notes):
    if len(notes) == 0:
        print("Attention : aucune note fournie.")
        return None

    return round(sum(notes) / len(notes), 1)


def appreciation(moyenne):
    if moyenne is None:
        return "Non calcule"
    if moyenne < 10:
        return "Insuffisant"
    if moyenne < 12:
        return "Passable"
    if moyenne < 16:
        return "Bien"
    return "Tres bien"


etudiants = [
    {"nom": "Karim", "notes": [12, 15, 9]},
    {"nom": "Sara", "notes": [18, 17, 16]},
    {"nom": "Lina", "notes": [6, 8, 5]},
]

meilleur_etudiant = None
moins_bon_etudiant = None


for etudiant in etudiants:
    moyenne = calculer_moyenne(etudiant["notes"])
    mention = appreciation(moyenne)

    print(f"{etudiant['nom']} {moyenne:.2f} {mention}")

    if meilleur_etudiant is None or moyenne > meilleur_etudiant["moyenne"]:
        meilleur_etudiant = {"nom": etudiant["nom"], "moyenne": moyenne}

    if moins_bon_etudiant is None or moyenne < moins_bon_etudiant["moyenne"]:
        moins_bon_etudiant = {"nom": etudiant["nom"], "moyenne": moyenne}

print(f"meilleur etudiant : {meilleur_etudiant['nom']}")
print(f"moins bon etudiant : {moins_bon_etudiant['nom']}")



def construire_resultats(etudiants):
    resultats = {}
    noms_deja_vus = set()

    for etudiant in etudiants:
        nom = etudiant["nom"]
        notes = etudiant["notes"]

        if nom in noms_deja_vus:
            print(f"attntion, doublon detecte : {nom}")
            continue

        noms_deja_vus.add(nom)
        moyenne = calculer_moyenne(notes)

        if moyenne is not None:
            resultats[nom] = {
                "moyenne": moyenne,
                "mention": appreciation(moyenne),
            }

    return resultats


def classer_par_moyenne(resultats):
    return sorted(
        resultats.items(),
        key=lambda item: item[1]["moyenne"],
        reverse=True,
    )


def etudiants_en_echec(resultats):
    return [
        (nom, infos["moyenne"])
        for nom, infos in resultats.items()
        if infos["moyenne"] < 10
    ]


etudiants_test = [
    {"nom": "karim", "notes": [12, 8, 16]},
    {"nom": "sara", "notes": [18, 17, 19]},
    {"nom": "lina", "notes": [5, 6, 4]},
    {"nom": "youssef", "notes": [10, 10, 10]},
    {"nom": "nadia", "notes": [16, 16, 16]},
    {"nom": "aarim", "notes": [11, 12, 13]},
    {"nom": "hicham", "notes": []},
]


resultats = construire_resultats(etudiants_test)

print("resultats :")
print(resultats)

print("classement :")
classement = classer_par_moyenne(resultats)
for position, (nom, infos) in enumerate(classement, start=1):
    print(f"{position}. {nom} - {infos['moyenne']}")

print(etudiants_en_echec(resultats))
