## Úloha 1 

# import requests

# response = requests.get("https://httpbin.org/get")
# status = response.status_code
# print(f"Status kód: {status}")
# print(f"Úspešné: {status == 200}")

## Úloha 2

# import requests

# response = requests.get("https://httpbin.org/get")
# data = response.json()
# print(f"URL: {data["url"]}")
# print(f"Origin: {data["origin"]}")

## Úloha 3

# import requests

# parametre = {
#     "amount" : 5,
#     "type" : "boolean",
# }

# response = requests.get("https://opentdb.com/api.php" , params=parametre)
# data = response.json()
# print(data["results"][0]["question"])
# print(data["results"][0]["correct_answer"])


# # Úloha 4

# class Auto:
#     def __init__(self,znacka,rok):
#         self.znacka = znacka
#         self.rok = rok

# a = Auto("BMW", 2020)
# b = Auto("Toyota", 2018)
# print(a.znacka,a.rok)
# print(b.znacka,b.rok)


# # Úloha 5 

# class Auto:
#     def __init__(self,znacka,rok):
#         self.znacka = znacka
#         self.rok = rok

#     def popis(self):
#         print(f"Toto auto je {self.znacka} z roku {self.rok}")

#     def je_stare(self):
#         return self.rok < 2016

# a = Auto("BMW", 2020)
# b = Auto("Toyota", 2015)
# a.popis()
# print(f"Je staré: {a.je_stare()}")
# b.popis()
# print(f"Je staré: {b.je_stare()}")


# # Úloha 6

# class Skore:
#     def __init__(self):
#         self.body = 0
#         self.pokusy = 0

#     def spravna_odpoved(self):
#         self.body += 1
#         self.pokusy += 1

#     def zla_odpoved(self):
#         self.pokusy += 1

#     def vypis(self):
#         return f"Skóre: {self.body}/{self.pokusy}"
    
# s = Skore()
# s.spravna_odpoved()
# s.spravna_odpoved()
# s.zla_odpoved()
# s.spravna_odpoved()
# s.zla_odpoved()
# print(s.vypis())


# # Úloha 7
# import json

# vysledky = [
#     {"meno": "Eduard", "skore": 7},
#     {"meno": "Anna", "skore": 9}
# ]


# with open("vysledky.json", "w", encoding="utf-8") as f:
#     json.dump(vysledky, f, indent=2)


# with open("vysledky.json","r",encoding="utf-8") as f:
#     data = json.load(f)
#     for hrac in data:
#         print(f"{hrac["meno"]}:{hrac["skore"]}")


# # Úloha 9

# import json

# vysledky = [
#     {"meno": "Eduard", "skore": 7},
#     {"meno": "Anna", "skore": 9}
# ]


# with open("vysledky.json","r",encoding="utf-8") as f:
#     data = json.load(f)
#     data.append({"meno": "Marek", "skore": 5})

# with open("vysledky.json", "w", encoding="utf-/") as f:
#     json.dump(data,f,indent=2)   

# with open("vysledky.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#     for hrac in data:
#         print(f"{hrac["meno"]} : {hrac["skore"]}")

# # Úloha 10

# cislo = input("Zadaj číslo:\n")
# try:
#     x = 100 /int(cislo)
#     print(f"Výsledok: {x}")
# except ZeroDivisionError:
#     print("Chyba: nulou deliť nemožno")


# # Úloha 11
# import requests

# try:
#     response = requests.get("https://toto-neexistuje-123.xyz")
# except requests.exceptions.ConnectionError:
#     print("Chyba: Nedá sa pripojiť k API")


# # Úloha 12

# import json

# try:
#     with open("neexistujuci.json", "r", encoding="utf-8") as f:
#         data = json.load(f)

# except FileNotFoundError:
#     data = []
#     print("Súbor neexistuje, začínam s prázdnym zoznamom")

# print(data)