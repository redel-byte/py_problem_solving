# --- block1/listes

notes = [12, 18, 7, 15, 9, 20, 3, 14]


def max_min(notes) -> str:
    max = min = notes[0]
    for num in notes:
        if max < num:
            max = num
        if min > num:
            min = num

    return f"Note min {min}\nNote max: {max}"


# print(max_min(notes))

notes = [8, 14, 6, 17, 11, 20]


def seuil(list) -> str:
    index = int(input("seuil: "))
    new_notes = []
    for num in list:
        if num >= index:
            new_notes.append(num)
    return f"result : {new_notes}"


# print(seuil(notes))

fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]


def Comptage(fruits) -> list:
    unique_fuits = set()
    count = 0
    comtage = []
    for fruit in fruits:
        for fruit2 in fruits:
            if fruit == fruit2:
                count += 1
        if fruit in unique_fuits:
            count = 0
            continue
        comtage.append((fruit, count))
        unique_fuits.add(fruit)
        count = 0
    return comtage


liste = [1, 2, 4, 4, 9]


def Inversion(liste) -> list:
    reverse_list = []
    for i in range(len(liste) - 1, -1, -1):
        reverse_list.append(liste[i])
    return reverse_list


# print(Inversion(liste))

liste_a = [1, 4, 7]
liste_b = [2, 3, 8, 9]


def Fusion(liste_a, liste_b) -> list:
    new_list = liste_a + liste_b
    return sort(new_list)


# 1, 4, 7, 2, 3, 8, 9


def sort(array) -> list:
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


# print(Fusion(liste_a, liste_b))
nombres = [3, 12, 7, 25, 8, 19, 2]


def Compréhension(nombers) -> list:
    return [element**2 for element in nombers if element % 2 == 0]


# print(Compréhension(nombres))

stock = {"pommes": 50, "bananes": 30, "oranges": 0}


# ------ block/Dictionaires


def vendre(stock: dict, fruit: str, quantite: int) -> str | tuple:
    if fruit in stock:
        if stock[fruit] > quantite:
            stock[fruit] -= quantite
            return f"Vente enregistree : {quantite} {fruit}."
        return f"Stock insuffisant pour {fruit} (disponible : {stock[fruit]})."
    return f"{fruit} not found."


vendre(stock, "pommes", 20)
vendre(stock, "oranges", 5)


stock = {"pommes": 30, "bananes": 0, "oranges": 0, "kiwis": 12}


def produits_epuises(stock) -> list:
    empty = []
    for key in stock:
        if stock[key] != 0:
            continue
        empty.append(key)
    return empty


produits_epuises(stock)

commandes = [
    {"client": "Ali", "produit": "pommes", "quantite": 5},
    {"client": "Sara", "produit": "bananes", "quantite": 10},
    {"client": "Ali", "produit": "oranges", "quantite": 2},
    {"client": "Ali", "produit": "oranges", "quantite": 1},
]


def Total_par_client(commandes):
    new_commands = []

    for command in commandes:
        existing = next(
            (obj for obj in new_commands if obj["client"] == command["client"]),
            None,
        )

        if existing:
            existing["quantite"] += command["quantite"]
        else:
            new_commands.append(command.copy())

    return new_commands


Total_par_client(commandes)

d = {"a": 1, "b": 2, "c": 3}


def Inversion(d) -> dict:
    keys = d.keys()
    reverse_dict = {}
    for key in keys:
        reverse_dict[d[key]] = key
    return reverse_dict


mots = ["chat", "elephant", "abeille", "riz"]


def diclen(mots) -> dict:
    new_dic = {}
    for mot in mots:
        new_dic[mot] = len(mot)
    return new_dic


diclen(mots)

entreprise = {
    "IT": ["Ali", "Sara", "Omar"],
    "RH": ["Lina"],
    "Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
}


def imbreqe(entreprise) -> dict:
    client_num = {}
    for grp in entreprise:
        client_num[grp] = len(entreprise[grp])
    return client_num


imbreqe(entreprise)

# --- block3/Sets
# Inscrits aux deux ateliers : {"Sara", "Lina"}
# Inscrits a au moins un atelier : {"Ali","Sara","Lina","Karim","Omar","Yasmine"}
# Uniquement Python : {"Ali", "Karim"}

atelier_python = ["Ali", "Sara", "Lina", "Karim"]
atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]


def Intersection_union_différence(atelier_java, atelier_python) -> tuple:
    atelier_python = set(atelier_python)
    atelier_java = set(atelier_java)
    intersection = atelier_python & atelier_java
    deference = atelier_python - atelier_java
    union = atelier_java | atelier_python
    return (intersection, deference, union)


Intersection_union_différence(atelier_java, atelier_python)

liste_1 = ["Ali", "Sara", "Lina"]
liste_2 = ["Ali", "Sara", "Ali"]


def a_des_doublons(liste) -> bool:
    liste_set = set(liste)
    return len(liste_set) != len(liste)


a_des_doublons(liste_1)
a_des_doublons(liste_2)


tags_articles = [
    ["python", "web", "api"],
    ["python", "data"],
    ["web", "css"],
]


def unique(tags_articles) -> set:
    all_lists = []
    for liste in tags_articles:
        all_lists += liste
    return set(all_lists)


unique(tags_articles)

coordonnees = {(1, 2), (3, 4)}


# ---- Bloc 4 — Combinaison listes / dicts / sets
