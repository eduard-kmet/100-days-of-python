# Úloha 1 - Správca kontaktov
# import json
# def uloz_kontakt(meno, telefon, email):
#     try:
#         with open("kontakty.json", "r", encoding="utf-8") as subor:
#             kontakt = json.load(subor)
#     except FileNotFoundError:
#         kontakt = {}

#     kontakt[meno] = {"telefon": telefon, "email": email}

#     with open("kontakty.json","w",encoding="utf-8") as subor:
#         json.dump(kontakt,subor,ensure_ascii=False, indent=4)

# def najdi_kontakt(meno):
#     try:
#         with open("kontakty.json", "r", encoding="utf-8") as subor:
#                 kontakt = json.load(subor)
#                 if meno in kontakt:
#                     print (kontakt[meno])
#                 else:
#                     print ("Chyba, takýto kontakt sa v zozname nenachádza")
#     except FileNotFoundError:
#         print("Chyba - žiadny súbor neexistuje, najprv ho vytvor")

    

# uloz_kontakt("Anna Nováková", "0912 345 678", "anna@email.sk")
# uloz_kontakt("Peter Kováč", "0900 111 222", "peter@email.sk")
# najdi_kontakt("Anna Nováková")
# najdi_kontakt("Ján Mrkvička")



# Úloha 2 – Analyzátor textu (Reťazce + Slovníky + Comprehensions)
# Napíš funkciu, ktorá analyzuje vstupný text a vráti štatistiky.
# Požiadavky:

# Počet slov, počet unikátnych slov, najčastejšie slovo
# Slovník s frekvenciou každého slova (malými písmenami, bez interpunkcie)
# Percento unikátnych slov (zaokrúhlené na 1 desatinné miesto)
# import string
# def analyzuj_text(text):

#     male_pismena = text.lower()
#     bez_interpunkcie = male_pismena
#     for znak in string.punctuation:
#         bez_interpunkcie = bez_interpunkcie.replace(znak,"")
#     zoznam_slov = bez_interpunkcie.split()

#     frekvencia = {}
#     for slovo in zoznam_slov:
#         frekvencia[slovo] = frekvencia.get(slovo,0) + 1

#     pocet_slov = len(zoznam_slov)
#     unikatne_slova = set(zoznam_slov)
#     najcastejsie_slovo = max(frekvencia,key=frekvencia.get)
#     percento_unikatnych = round(((len(unikatne_slova)/pocet_slov)*100),1)

#     return {
#         "pocet_slov": pocet_slov,
#         "unikatne": len(unikatne_slova),
#         "najcastejsie": najcastejsie_slovo,
#         "percento_unikatnych": percento_unikatnych,
#         "frekvencia": frekvencia
#     }


# # Test
# text = """Python je úžasný jazyk. Python sa používa všade.
# Jazyk Python je jednoduchý a jazyk je pekný."""

# vysledok = analyzuj_text(text)
# print(vysledok)

# Úloha 3 – Bezpečná kalkulačka (Exception Handling + OOP)
# Vytvor triedu Kalkulacka, ktorá bezpečne zvláda všetky bežné chyby.
# Požiadavky:

# Metódy: scitaj, odcitaj, nasob, vydel, mocnina
# Každá metóda ošetruje neplatné vstupy (TypeError, ValueError, ZeroDivisionError)
# Metóda historia() vráti zoznam posledných 5 výpočtov ako reťazce

# class Kalkulacka:
#     def __init__(self):
#         self.historia_vypoctov = []

#     def scitaj(self, a , b):
#         try:
#             vysledok_scitaj = a + b
#             self.historia_vypoctov.append(f"{a} + {b} = {vysledok_scitaj}")
#             return vysledok_scitaj
#         except TypeError:
#             print("Chyba - vstupom musia byt iba cisla")
#         except ValueError:
#             print("Neplatná hodnota")
#         except ZeroDivisionError:
#             print("Nulou nedelím")

#     def vydel(self, a , b):
#         try:
#             vysledok_vydel = a / b
#             self.historia_vypoctov.append(f"{a} / {b} = {vysledok_vydel}")
#             return vysledok_vydel
#         except TypeError:
#             print("Chyba - vstupom musia byt iba cisla")
#         except ValueError:
#             print("Neplatná hodnota")
#         except ZeroDivisionError:
#             print("Nulou nedelím")

#     def odcitaj(self, a , b):
#         try:
#             vysledok_odcitaj = a - b
#             self.historia_vypoctov.append(f"{a} - {b} = {vysledok_odcitaj}")
#             return vysledok_odcitaj
#         except TypeError:
#             print("Chyba - vstupom musia byt iba cisla")
#         except ValueError:
#             print("Neplatná hodnota")
#         except ZeroDivisionError:
#             print("Nulou nedelím")

#     def nasob(self, a , b):
#         try:
#             vysledok_nasob = a * b
#             self.historia_vypoctov.append(f"{a} * {b} = {vysledok_nasob}")
#             return vysledok_nasob
#         except TypeError:
#             print("Chyba - vstupom musia byt iba cisla")
#         except ValueError:
#             print("Neplatná hodnota")
#         except ZeroDivisionError:
#             print("Nulou nedelím")

#     def mocnina(self, a , b):
#         try:
#             vysledok_mocnina = a ** b
#             self.historia_vypoctov.append(f"{a} ** {b} = {vysledok_mocnina}")
#             return vysledok_mocnina
#         except TypeError:
#             print("Chyba - vstupom musia byt iba cisla")
#         except ValueError:
#             print("Neplatná hodnota")
#         except ZeroDivisionError:
#             print("Nulou nedelím")

#     def historia(self):
#         historia = self.historia_vypoctov
#         print(historia[-5:])


# k = Kalkulacka()
# print(k.scitaj(10, 5))
# print(k.vydel(10, 0))
# print(k.nasob("abc", 3))
# k.historia()

# import json

# class FilmovaBaza:
#     def __init__(self):

#        self.subor = "filmy.json"
            
        
#     def pridaj_film(self,nazov, rok, zaner):
#         try:
#             with open ("filmy.json", "r") as data:
#                 filmy = json.load(data)
#         except FileNotFoundError:
#             filmy = {}

#         if nazov in filmy:
#             print("Film už existuje")
#             return

#         filmy[nazov] = {"rok" : rok , "žáner" : zaner , "hodnotenie" : []}
#         with open("filmy.json","w") as data:
#             json.dump(filmy,data)


#     def ohodnotit(self, nazov, hodnotenie):
#         try:
#             with open("filmy.json","r") as data:
#                 filmy = json.load(data)
#         except FileNotFoundError:
#             print("Súbor neexistuje")
#             return

#         if nazov not in filmy:
#             print("Film neexistuje")
#             return
  
#         if hodnotenie < 1 or hodnotenie > 10:
#             print("Hodnotenie mimo rozsahu")
#             return


        
#         filmy[nazov]["hodnotenie"].append(hodnotenie)
#         with open("filmy.json","w") as data:
#             json.dump(filmy,data)


#     def priemer(self,nazov):
#         try:
#             with open("filmy.json","r") as data:
#                 filmy = json.load(data)
#         except FileNotFoundError:
#             print("Súbor neexistuje")
#             return

#         if nazov not in filmy:
#             print("Film neexistuje")
#             return
        
#         hodnotenie = filmy[nazov]["hodnotenie"]
#         if len(hodnotenie) == 0:
#             return 0
#         return round(sum(hodnotenie)/len(hodnotenie),1)
    
#     def najlepsie_filmy(self):
#         try:
#             with open("filmy.json","r") as data:
#                 filmy = json.load(data)
#         except FileNotFoundError:
#             print("Súbor neexistuje")
#             return
#         priemerky = {}
#         for film in filmy:
#             priemerky[film] = self.priemer(film)
#         zoradene = sorted(priemerky, key = priemerky.get, reverse=True)
#         return zoradene [:3]
        

#     def zanrove_statistiky(self):

#         try:
#             with open("filmy.json","r") as data:
#                 filmy = json.load(data)
#         except FileNotFoundError:
#             print("Súbor neexistuje")
#             return
        
#         slovnik = {}
#         for film in filmy:
#             zaner = filmy[film]["žáner"]
#             slovnik[zaner] = slovnik.get(zaner,0) + 1
            
#         return slovnik


# baza = FilmovaBaza()
# baza.pridaj_film("Inception", 2010, "sci-fi")
# baza.pridaj_film("Titanic", 1997, "drama")
# baza.ohodnotit("Inception", 9)
# baza.ohodnotit("Inception", 15)   # chyba
# print(baza.priemer("Inception"))
# print(baza.najlepsie_filmy())
# print(baza.zanrove_statistiky())
        



"""Úloha 5 – Systém úloh (JSON + OOP + Dátumy)

Vytvor triedu TodoManager, ktorá spravuje zoznam úloh v ulohy.json.

Požiadavky:

pridaj_ulohu(nazov, priorita, termin) – pridá úlohu (priorita: "vysoká"/"stredná"/"nízka", termin vo formáte "DD.MM.YYYY")
dokoncit(nazov) – označí úlohu ako dokončenú
zoznam_nedokoncenych() – vráti zoznam nedokončených úloh zoradených podľa priority (vysoká → stredná → nízka)
po_termine() – vráti úlohy kde termin už prešiel (porovnaj s dnešným dátumom)
Hint pre dátumy – nový modul:


from datetime import datetime
dnes = datetime.today()
datum = datetime.strptime("25.12.2024", "%d.%m.%Y")  # reťazec → datetime
Štruktúra JSON:


{
    "Nakúpiť": {
        "priorita": "vysoká",
        "termin": "01.01.2025",
        "dokoncena": false
    }
}
Test:


todo = TodoManager()
todo.pridaj_ulohu("Nakúpiť", "vysoká", "01.01.2025")
todo.pridaj_ulohu("Cvičiť", "nízka", "31.12.2026")
todo.dokoncit("Nakúpiť")
print(todo.zoznam_nedokoncenych())
print(todo.po_termine()"""

import json
class TodoManager:
    def __init__(self):
        self.subor = "ulohy.json"

    def pridaj_ulohu(self,nazov, priorita, termin):
        try:
            with open("ulohy.json","r") as data:
                ulohy = json.load(data)
        except FileNotFoundError:
            ulohy = {}

        ulohy[nazov] = {"priorita":priorita, "termin":termin, "dokončená":False}
        with open("ulohy.json","w") as data:
            json.dump(ulohy,data,indent=4)

    def dokoncit(self,nazov):
        try:
            with open("ulohy.json","r") as data:
                ulohy = json.load(data)
        except FileNotFoundError:
            ulohy = {}

        if nazov not in ulohy:
            print("Úloha neexistuje")
            return


        ulohy[nazov]["dokončená"] = True
        with open("ulohy.json","w") as data:
            json.dump(ulohy,data,indent=4)

    def zoznam_nedokoncenych(self):
        try:
            with open("ulohy.json","r") as data:
                ulohy = json.load(data)
        except FileNotFoundError:
            ulohy = {}

        poradie = {"vysoká": 1, "stredná": 2, "nízka": 3}
        nedokoncene = {}
        
        for nazov in ulohy:
            if ulohy[nazov]["dokončená"] == False:
                nedokoncene.append(nazov)

        return sorted(nedokoncene, key lambda n: poradie[ulohy[n]["priorita"]])

        