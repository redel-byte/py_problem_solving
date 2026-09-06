Numeric = int | float


def division_securisee(a, b) -> Numeric:
    return a / b


# try:
#     # print(division_securisee(10, 2))
#     # print(division_securisee(10, 0))
# except ZeroDivisionError:
#     print("error : division par zero impossible.")
# 1.3 — convertir_entier(valeur)
def convertir_entier(number) -> Numeric:
    return int(number)


# try:
#     # print(convertir_entier(10))
#     # print(convertir_entier("abc"))
# except ValueError as e:
#     print(e.args)

notes = [12, 15, 9]


def acceder_element(liste, index) -> Numeric:
    try:
        return liste[index]
    except IndexError:
        print(
            f"Erreur : index {index} hors limites (taille de la liste : {len(liste)})."
        )


# acceder_element(notes, 1)
# acceder_element(notes, 10)


eleve = {"nom": "Sara", "age": 20}


def acceder_cle(dictionnaire, cle) -> str:
    try:
        return dictionnaire[cle]
    except KeyError:
        return f"Erreur : la cle {cle} n’existe pas."


# acceder_cle(eleve, "nom")
# acceder_cle(eleve, "email")


def traiter_valeur(valeur: str):
    try:
        return int(valeur)
    except ValueError:
        return f"Erreur : {valeur} n’est pas convertible."
    finally:
        print("Traitement termine.")


# traiter_valeur("8")
# traiter_valeur("x")

# --- block 2


def verifier_age(age):
    try:
        if age >= 18:
            print(f"Age Valide : {age}")
        else:
            raise ValueError()
    except ValueError:
        print(f"ValueError: l’age ne peut pas etre negatif ({age}).")


# verifier_age(25)
# verifier_age(-3)

nw_list = ["3", "9", "x", "5"]


def traiter_liste_de_valeurs(valeurs: list[str]) -> list[int]:
    resultat = []

    for valeur in valeurs:
        try:
            resultat.append(int(valeur))

        except ValueError:
            print(f'Log : valeur "{valeur}" invalide, exception relancee.')
            raise


# traiter_liste_de_valeurs(["3", "9", "x", "5"])


# except
class StockInsuffisantError(Exception):
    pass


def retirer_stock(stock: dict[str, int], produit: str, quantite: int) -> None:
    disponible = stock.get(produit, 0)

    if quantite > disponible:
        raise StockInsuffisantError(
            f'stock insuffisant pour "{produit}" '
            f"(demande : {quantite}, disponible : {disponible})"
        )

    stock[produit] -= quantite
    print(f"Retrait effectue : {quantite} {produit}.")


stock = {"pommes": 20, "bananes": 4}

# retirer_stock(stock, "pommes", 5)
# retirer_stock(stock, "bananes", 10)

# -------- block 3


# 3.1
def ecrire_liste_courses(chemin: str, articles: list[str]) -> None:
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write("\n".join(articles))


articles = ["pommes", "lait", "pain"]
# ecrire_liste_courses("courses.txt", articles)


# 3.2
def ajouter_article(chemin: str, article: str) -> None:
    with open(chemin, "a", encoding="utf-8") as fichier:
        fichier.write(f"\n{article}")


# ajouter_article("courses.txt", "oeufs")


# 3.3
def lire_fichier(chemin: str) -> list[str]:
    with open(chemin, "r", encoding="utf-8") as fichier:
        return fichier.readlines()


# print(lire_fichier("courses.txt"))


# 3.4
def compter_lignes(chemin: str) -> None:
    nombre_lignes = 0

    with open(chemin, "r", encoding="utf-8") as fichier:
        for _ in fichier:
            nombre_lignes += 1

    print(f"Nombre de lignes : {nombre_lignes}")


# compter_lignes("courses.txt")

# ---block 4


def lire_fichier_securise(fishier) -> None:
    try:
        with open(fishier, "r", encoding="utf-8") as f:
            content = f.readlines()
            content = [line.strip("\n") for line in content]
            print(content)
    except FileNotFoundError:
        print(f"Erreur : le fichier {fishier} n’existe pas.")


# lire_fichier_securise("courses.txt")
# lire_fichier_securise("inexistant.txt")

import csv


def claculate_moyenne(csv_content) -> Numeric:
    moyenne = 0
    for elem in csv_content:
        if elem[1].isdegit():
            moyenne += elem[1]
        else:
            raise ValueError(
                f"Attention : note invalide pour '{elem[0]}' ('{elem[1]}'), ligne ignoree."
            )
    return moyenne


def calculer_moyenne_csv(chemin: str) -> None:
    try:
        element = ["lina", "abc"]
        with open(chemin, encoding="utf-8") as f:
            content = csv.reader(f)
            print([elem for elem in content])
    except ValueError as error:
        print(error.args)


calculer_moyenne_csv("notes.csv")
