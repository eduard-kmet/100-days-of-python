# Úloha 1 - slovníky


# nakupy = ["chlieb", "mlieko", "chlieb", "vajcia", "mlieko", "chlieb"]

# def spocitaj(nakupy):
#     opakovane = {}
#     for polozka in nakupy:
#         if polozka in opakovane:
#             opakovane[polozka] += 1
#         else:
#             opakovane[polozka] = 1



# znamky = [
#     ("Peter", 2),
#     ("Jana", 1),
#     ("Peter", 3),
#     ("Jana", 2),
#     ("Tomáš", 1),
#     ("Peter", 1),
# ]

# def priemer_znamok(znamky):
#     priemer = {}
#     for meno, znamka in znamky:
#         if meno in priemer:
#             priemer[meno].append(znamka)
#         else:
#             priemer[meno] = [znamka] 
#     for meno,zoznam in priemer.items():
#         priemer[meno] = sum(zoznam) / len(zoznam)
#     return priemer

# print(priemer_znamok(znamky))

# predaje = [
#     ("január", 1500),
#     ("február", 2300),
#     ("január", 800),
#     ("marec", 1200),
#     ("február", 900),
#     ("marec", 600),
# ]


# def celkove_predaje(predaje):
#     celkovo = {}
#     for mesiac,predaj in predaje:
#         if mesiac in celkovo:
#             celkovo[mesiac].append(predaj)
#         else:
#             celkovo[mesiac] = [predaj]

#     for mesiac, spolu in celkovo.items():
#         celkovo [mesiac] = sum(spolu)
#     return celkovo

# print(celkove_predaje(predaje))

# slova = ["auto", "dom", "pes", "kot", "or", "les", "ok", "strom", "more"]

# def podla_dlzky(slova):
#     dlzka = {}
#     for slovo in slova:
#         dlzka_slova = len(slovo)
#         if dlzka_slova in dlzka:
#             dlzka[dlzka_slova].append(slovo)
#         else:
#             dlzka[dlzka_slova] = [slovo]
#     return dlzka

# print(podla_dlzky(slova))

# studenti = {
#     "Peter": 85,
#     "Jana": 92,
#     "Tomáš": 61,
#     "Mária": 78,
#     "Lukáš": 55,
#     "Zuzana": 90,
# }


# def hodnotenie(studenti):
#     znamky = {}
#     for meno, vysledok in studenti.items():
#         if vysledok < 60:
#             znamky[meno] = "D"
#         elif 60 <= vysledok <= 74:
#             znamky[meno] = "C"
#         elif 75 <= vysledok <= 89:
#             znamky[meno] = "B"
#         else:
#             znamky[meno] = "A"
#     return znamky

# print(hodnotenie(studenti))


# class Auto:
#     def __init__(self, znacka, rok, km):
#         self.znacka = znacka
#         self.rok = rok
#         self.km = km

#     def info(self):
#         return f"{self.znacka} ({self.rok}) - {self.km} km"
    
# a1 = Auto("BMW", 2020, 50000)
# a2 = Auto("Audi", 2000, 150000)
# print(a1.info())
# print(a2.info())

# class BankovyUcet:
#     def __init__(self,majitel):
#         self.majitel = majitel
#         self.zostatok = 0

#     def vloz(self,suma):
#         self.zostatok += suma
#         return self.zostatok
    
#     def vyber(self,suma):
#         if self.zostatok < suma:
#             print("Nedostatok prostriedkov")
#             return self.zostatok
#         else:
#             self.zostatok -= suma
#         return self.zostatok
    
#     def info(self):
#         return f"Účet: {self.majitel}, Zostatok: {self.zostatok}"
    
    
# ucet = BankovyUcet("Peter")
# ucet.vloz(200)
# ucet.vyber(50)
# print(ucet.info())
# ucet.vyber(500)


# class Playlist:
#     def __init__(self,nazov):
#         self.nazov = nazov
#         self.piesne = []  

#     def pridaj_piesne(self,piesne):
#         self.piesne.append(piesne)

#     def odstran_piesne(self,piesne):
#         if piesne in self.piesne:
#             self.piesne.remove(piesne)
#         else:
#             print("Pieseň nenájdená")

#     def vypis(self):
#         for n, piesne in enumerate(self.piesne, start = 1):
#             print(f"{n}. {piesne}")

# p = Playlist("Obľúbené")
# p.pridaj_piesne("Bohemian Rhapsody")
# p.pridaj_piesne("Hotel California")
# p.pridaj_piesne("Stairway to Heaven")
# p.vypis()
# p.odstran_piesne("Hotel California")
# p.vypis()
# p.odstran_piesne("Neexistujuca")



# class Sklad:
#     def __init__(self):
#         self.produkty = {}

#     def pridaj(self,nazov,mnozstvo):
#         if nazov in self.produkty:
#             self.produkty[nazov] += mnozstvo

#         else:
#             self.produkty[nazov] = mnozstvo
        
#     def vyber(self,nazov,mnozstvo):
#         if nazov not in self.produkty:
#             print("Produkt nenájdený")
#         else:
#             if self.produkty[nazov] < mnozstvo:
#                 print("Nedostatok na sklade")
#             else:
#                 self.produkty[nazov] -= mnozstvo

#     def vypis(self):
#         for nazov, mnozstvo in self.produkty.items():
#             print(f"Produkt: {nazov} - množstvo: {mnozstvo}")
            

# s = Sklad()
# s.pridaj("jablká", 50)
# s.pridaj("hrušky", 30)
# s.pridaj("jablká", 20)  # teraz 70
# s.vyber("jablká", 10)   # teraz 60
# s.vyber("jablká", 100)  # Nedostatok na sklade
# s.vyber("banány", 5)    # Produkt nenájdený
# s.vypis()


# class Kniznica:
#     def __init__(self):
#         self.knihy = []

#     def pridaj(self,nazov,autor,rok):
#         self.knihy.append(Kniha(nazov,autor,rok))

#     def vypis(self):
#         for kniha in self.knihy:
#             print(f"{kniha.nazov} - {kniha.autor} - {kniha.rok}")

#     def podla_autora(self):
#         slovnik = {}
#         for kniha in self.knihy:
#             if kniha.autor in slovnik:
#                 slovnik[kniha.autor].append(kniha.nazov)
#             else:
#                 slovnik[kniha.autor] = [kniha.nazov]
#         return slovnik

#     def najstarsia(self):
#         return min(self.knihy, key = lambda k:k.rok)

# class Kniha:
#     def __init__(self, nazov, autor, rok):
#         self.nazov = nazov
#         self.autor = autor
#         self.rok = rok
        
# k = Kniznica()
# k.pridaj("1984", "Orwell", 1949)
# k.pridaj("Farma zvierat", "Orwell", 1945)
# k.pridaj("Malý princ", "Saint-Exupéry", 1943)
# k.vypis()
# print(k.podla_autora())
# print(k.najstarsia().nazov)
    

# class Poznamky:
#     def __init__(self):
#         self.poznamky = []

#     def pridaj(self,text):
#         self.poznamky.append(text)

#     def uloz(self,nazov_suboru):
#         with open(nazov_suboru,"w",encoding="utf-8") as f:
#             for poznamka in self.poznamky:
#                 f.write(poznamka + "\n")

#     def nacitaj(self,nazov_suboru):
#         with open(nazov_suboru,"r",encoding="utf-8") as f:
#             obsah = f.read() 
#             self.poznamky = obsah.splitlines()

#     def vypis(self):
#         for n , poznamka in enumerate(self.poznamky, start = 1):
#             print(f"{n}.{poznamka}")

# p = Poznamky()
# p.pridaj("Kúpiť mlieko")
# p.pridaj("Zavolať doktorovi")
# p.pridaj("Cvičiť o 18:00")
# p.uloz("poznamky.txt")

# p2 = Poznamky()
# p2.nacitaj("poznamky.txt")
# p2.vypis()


# class Kontakt:
#     def __init__(self, meno, telefon, email):
#         self.meno = meno
#         self.telefon = telefon
#         self.email = email

# class Kontakty:
#     def __init__(self):
#         self.zoznam = []


#     def pridaj(self,meno,telefon,email):
#         self.zoznam.append(Kontakt(meno,telefon,email))

#     def uloz(self,nazov_suboru):
#         with open(nazov_suboru,"w",encoding="utf-8") as f:
#             for kontakt in self.zoznam:
#                 f.write(f"{kontakt.meno},{kontakt.telefon},{kontakt.email}\n")


#     def nacitaj(self,nazov_suboru):
#         with open(nazov_suboru,"r",encoding="utf-8") as f:
#             for riadok in f.read().splitlines():
#                 meno, telefon, email = riadok.split(",")
#                 self.zoznam.append(Kontakt(meno,telefon,email))

#     def vypis(self):
#         for k in self.zoznam:
#             print(f"{k.meno} - {k.telefon} - {k.email}")

# k = Kontakty()
# k.pridaj("Peter", "0901123456", "peter@email.com")
# k.pridaj("Jana", "0902234567", "jana@email.com")
# k.uloz("kontakty.txt")

# k2 = Kontakty()
# k2.nacitaj("kontakty.txt")
# k2.vypis()



# class Produkt:
#     def __init__(self,nazov,cena,kategoria):
#         self.cena = cena
#         self.nazov = nazov
#         self.kategoria = kategoria

# class Obchod:
#     def __init__(self):
#         self.produkty = []

#     def pridaj(self,nazov,cena, kategoria):
#         self.produkty.append(Produkt(nazov,cena,kategoria))
    
#     def uloz(self,nazov_suboru):
#         with open(nazov_suboru,"w",encoding="utf-8") as f:
#             for p in self.produkty:
#                 f.write(f"{p.nazov},{p.cena},{p.kategoria}\n")

#     def nacitaj(self,nazov_suboru):
#         with open(nazov_suboru,"r",encoding="utf-8") as f:
#             for p in f.read().splitlines():
#                 nazov, cena, kategoria = p.split(",")
#                 self.produkty.append(Produkt(nazov,float(cena),kategoria))

#     def vypis(self):
#         for p in self.produkty:
#             print(f"{p.nazov} - {p.cena} - {p.kategoria}")

#     def najdrahsi(self):
#         return max(self.produkty, key = lambda p: p.cena)
    

# o = Obchod()
# o.pridaj("Laptop", 999.99, "Elektronika")
# o.pridaj("Kniha", 12.50, "Vzdelávanie")
# o.pridaj("Slúchadlá", 49.99, "Elektronika")
# o.uloz("obchod.txt")

# o2 = Obchod()
# o2.nacitaj("obchod.txt")
# o2.vypis()
# print(o2.najdrahsi().nazov)


# cisla = [4, 17, 3, 22, 8, 31, 15, 6, 28, 11]
# velke = [x for x in cisla if x > 10]
# parne = [x for x in cisla if x % 2 == 0]
# kvadraty = [x**2 for x in cisla]

# print(velke)
# print(parne)
# print(kvadraty)

# zamestnanci = [
#     ("Anna", "IT", 2800),
#     ("Peter", "HR", 2100),
#     ("Jana", "IT", 3200),
#     ("Marek", "Financie", 2600),
#     ("Lucia", "IT", 2950),
# ]

# it_zamestnanci = [meno for meno, oddelenie, plat in zamestnanci if oddelenie == "IT"]  
# vysoke_platy = [meno for meno, oddelenie, plat in zamestnanci if plat > 2700]
# vsetky_mena_velkym = [meno.upper() for meno,oddelenie, plat in zamestnanci]

# print(it_zamestnanci)
# print(vysoke_platy)
# print(vsetky_mena_velkym)
    
# zamestnanci = [
#     ("Anna", "IT", 2800),
#     ("Peter", "HR", 2100),
#     ("Jana", "IT", 3200),
#     ("Marek", "Financie", 2600),
#     ("Lucia", "IT", 2950),
#     ("Tomáš", "HR", 1950),
# ]        

# it_s_vysokym_platom = [meno for meno,oddelenie,plat in zamestnanci if oddelenie == "IT" and plat > 2700]
# nie_hr = [meno for meno,oddelenie,_ in zamestnanci if oddelenie != "HR"]

# print(it_s_vysokym_platom)
# print(nie_hr)





# df = pd.read_csv("Day 31/zamestnanci.csv")
# print(df.head())
# print(df["meno"])
# print(df[df["oddelenie"] == "IT"])

# df = pd.read_csv("Day 31/zamestnanci.csv")
# it_nad_2700 = [row["meno"] for _, row in df.iterrows() if row["oddelenie"] == "IT" and row["plat"] > 2700]

# print(it_nad_2700)
# print(df["plat"].mean())
# print(df["plat"].max())
# plat_v_oddeleni = df.groupby("oddelenie")["plat"].mean()
# print(plat_v_oddeleni)
# zamsestnanci_v_oddeleni = df.groupby("oddelenie")["meno"].count()
# print(zamsestnanci_v_oddeleni)
# df["bonus"] = df.apply(lambda row: row["plat"] * 0.05 if row["roky_v_firme"] > 3 else row["plat"] * 0.02, axis=1)
# df.to_csv("Day 31/zamestnanci_bonus.csv", index=False)
# najviac = df.loc[df.groupby("oddelenie")["roky_v_firme"].idxmax()]

# print(df)
# print(najviac)


# df = pd.read_csv("Day 31/zamestnanci.csv")
# priemerny_plat = df.groupby("oddelenie")["plat"].mean()
# it_nad = [row["meno"] for index,row in df.iterrows() if row["oddelenie"] == "IT" and row["plat"] > 2700]
# staz = df.groupby("oddelenie")["roky_v_firme"].max()
# df["mesacny_bonus"] = df.apply(lambda row: row["plat"] * 0.05 if row["roky_v_firme"] > 3 else row["plat"] * 0.02, axis = 1)
# df.to_csv("Day 31/zamestnanci.csv", index= False)


# import pandas as pd

# df = pd.read_csv("Day 31/studenti.csv")
# print(df)

# znamka_predmety = df.groupby("predmet")["znamka"].mean()
# mat = [row["meno"] for index,row in df.iterrows() if row["predmet"] == "Matematika" and row["znamka"] > 80]
# najlepsi = df.loc[df.groupby("predmet")["znamka"].idxmax()]

# df["prospel"] = df.apply(lambda row: "Áno" if row["znamka"] >= 70 else "Nie", axis=1)

# df.to_csv("Day 31/studenti_vysledky.csv", index = False)


class Ziak:
    def __init__(self,meno, rocnik):
        self.meno = meno
        self.rocnik = rocnik
        self.znamky = []

class Trieda:
    def __init__(self):
        self.ziaci = []

    
    def pridaj(self,meno,rocnik):
        self.ziaci.append(Ziak(meno,rocnik))

    def pridaj_znamku(self,meno,znamka):
        for ziak in self.ziaci:
            if ziak.meno == meno:
                ziak.znamky.append(znamka)

    def priemery(self):
        priemer = {}
        for ziak in self.ziaci:
            priemer[ziak.meno] = sum(ziak.znamky) / len(ziak.znamky)
        return priemer

    def najlepsi(self):
        return max(self.ziaci, key=lambda z:sum(z.znamky) / len(z.znamky))
    
    def uloz(self,nazov_suboru):
        with open(nazov_suboru,"w",encoding="utf-8") as f:
            for ziak in self.ziaci:
                f.write(f"{ziak.meno},{ziak.rocnik},{','.join(str(z) for z in ziak.znamky)}\n")


    def vypis(self):
        for ziak in self.ziaci:
            priemer = sum(ziak.znamky) / len(ziak.znamky)
            print(f"{ziak.meno} (rocnik {ziak.rocnik}) — priemer: {priemer:.1f}")



t = Trieda()
t.pridaj("Anna", 2)
t.pridaj("Peter", 1)
t.pridaj("Jana", 2)
t.pridaj_znamku("Anna", 90)
t.pridaj_znamku("Anna", 85)
t.pridaj_znamku("Peter", 70)
t.pridaj_znamku("Peter", 75)
t.pridaj_znamku("Jana", 95)
t.pridaj_znamku("Jana", 88)
t.vypis()
print(t.priemery())
print(t.najlepsi().meno)
t.uloz("trieda.txt")


