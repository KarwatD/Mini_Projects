import json

KATEGORIE = ("jedzenie","transport","rozrywka","zdrowie","ubrania","inne")
nazwa_pliku = ('wydatki.json',)

# Data validation
def num(typ, numer):
    while True:
        try:
            x = typ(input(numer))
            if x >=0:
                return x
            else:
                print('Wartość jest ujemna')
        except ValueError:
            print('Nieprawidłowa wartość')

# Dodawanie wydatków
def dodaj_wydatek(wydatki,opis,data,kwota,kategoria):
    lista = {'data':data, 'opis':opis, 'kwota':kwota,'kategoria':kategoria}
    wydatki.append(lista)

# Wyswietlanie wydatków
def wyswietl_wydatki(wydatki):
    print()
    if not wydatki:
        print('Brak wpisów w pliku')
        return
    for i in wydatki:
        print(f"Data: {i['data']}\nOpis: {i['opis']}\nKwota: {i['kwota']:.2f}\nKategoria: {i['kategoria']}\n")

# Podsumowuje wydatki z danej kategorii
def podsumowanie(wydatki):
    if not wydatki:
        print('Brak wpisów w pliku')
        return
    wydatki_calkowite = 0
    jedzenie = 0
    transport = 0
    rozrywka = 0
    zdrowie = 0
    ubrania = 0
    inne = 0
    print()
    for i in wydatki:
        wydatki_calkowite += i['kwota']
        if i['kategoria'] == 'jedzenie':
            jedzenie += i['kwota']
        elif i['kategoria'] == 'transport':
            transport += i['kwota']
        elif i['kategoria'] == 'rozrywka':
            rozrywka += i['kwota']
        elif i['kategoria'] == 'zdrowie':
            zdrowie += i['kwota']
        elif i['kategoria'] == 'ubrania':
            ubrania += i['kwota']
        elif i['kategoria'] == 'inne':
            inne += i['kwota']
    print(f'Wydałeś łącznie: {wydatki_calkowite:.2f}\n Na jedzenie: {jedzenie:.2f}\n Na transport: {transport:.2f}\n Na rozrywke: {rozrywka:.2f}\n Na zdrowie: {zdrowie:.2f}\n Na ubrania: {ubrania:.2f}\n Inne wydatki: {inne:.2f}')

# Zapisywanie
def zapisz_plik(wydatki,nazwa_pliku):
    with open(nazwa_pliku[0], 'w') as plik:
        json.dump(wydatki,plik, ensure_ascii=False)

# Wczytywanie
def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0], 'r') as plik:
            return json.load(plik)
    except:
        return []
    
# Menu
def main():
    wydatki = wczytaj_plik(nazwa_pliku)
    while True:
        print()
        print(f'===DZIENNIK WYDATKÓW===','1.Dodaj wydatek','2.Lista wydatków','3.Podsumowanie kategorii','0.Zapisz i wyjdź',sep='\n')
        decyzja = num(int,'Wybierz działanie: ')
        if decyzja ==1:
            while True:
                data = input('Podaj date: ')
                if len(data) == 10 and data.replace('-', '').isdigit():
                    break
            opis = input('Opisz wydatek: ').lower()
            kwota = num(float,'Podaj kwote: ')
            while True:
                kategoria = input('Podaj kategorie: ').lower()
                if kategoria in KATEGORIE:
                    break
            dodaj_wydatek(wydatki,opis,data,kwota,kategoria)
        elif decyzja ==2:
            wyswietl_wydatki(wydatki)
        elif decyzja ==3:
            podsumowanie(wydatki)
        elif decyzja ==0:
            zapisz_plik(wydatki,nazwa_pliku)
            break

if __name__ == "__main__":
    main()