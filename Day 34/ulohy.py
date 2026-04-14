import requests
import json
import html
from datetime import date

ENDPOINT = "https://opentdb.com/api.php"
parametre= {
    "amount" : 10,
    "type" : "boolean"
}

class OtazkaModel:
    def __init__(self, text, odpoved):
        self.text = text
        self.odpoved = odpoved

class KvizBrain:
    def __init__(self, zoznam_otazok):
        self.zoznam_otazok = zoznam_otazok
        self.skore = 0
        self.cislo_otazky = 0

    def ma_dalsu_otazku(self):
        return self.cislo_otazky < len(self.zoznam_otazok)

    def poloz_otazku(self):
        otazka = self.zoznam_otazok[self.cislo_otazky]
        print(f"Otázka {self.cislo_otazky + 1}: {otazka.text}")
        odpoved = input("Tvoja odpoved (True/False): \n")
        if odpoved.lower() == otazka.odpoved.lower():
            print("Správne")
            self.skore +=1
        else:
            print(f"Zle! Správna odpoveď bola: {otazka.odpoved}")

        self.cislo_otazky +=1

def nacitaj_otazky():
    response = requests.get(ENDPOINT, params= parametre)
    data = response.json()
    otazky = []
    for item in data["results"]:
        text = html.unescape(item["question"])
        odpoved = item["correct_answer"]
        otazky.append(OtazkaModel(text,odpoved))

    return otazky
    # TODO: osetr pripady ked API nevrati 200
    pass

def uloz_vysledok(meno, skore):
    try:
        with open("vysledok.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    except FileNotFoundError:
        data = []       

    data.append({"meno": meno,"skore": skore,"datum": str(date.today())})

    with open("vysledok.json", "w", encoding="utf-8") as f:
        json.dump(data,f,indent=2)

def zobraz_rebricek():
    try:
        with open("vysledky.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Žiadne výsledky zatiaľ.")
        return

    zoradene = sorted(data, key=lambda x: x["skore"], reverse=True)
    print("\n--- TOP 3 ---")
    for hrac in zoradene[:3]:
        print(f"{hrac['meno']}: {hrac['skore']} ({hrac['datum']})")


# --- Hlavný program ---
meno = input("Zadaj svoje meno: ")
otazky = nacitaj_otazky()

# TODO: vytvor KvizBrain, spusti hru v cykle
# TODO: po skonceni uloz vysledok a zobraz rebricek


kviz = KvizBrain(otazky)
while kviz.ma_dalsu_otazku():
    kviz.poloz_otazku()
print(f"Koniec! Tvoje skóre: {kviz.skore}/10")
uloz_vysledok(meno, kviz.skore)
zobraz_rebricek()
