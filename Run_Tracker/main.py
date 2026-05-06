import json


MINIMALNY_DYSTANS = (1.0,)

# Data validation
def num(typ,numer):
    while True:
        try:
            x = typ(input(numer))
            if x >=0:
                return x
            else:
                print('Ta liczba jest ujemna')
        except ValueError:
            print('Nieprawidłowa wartość')


# Menu
def main():
    historia = wczytaj_plik('dziennik_biegania.json')
    while True:
        print()
        print(f'=== DZIENNIK BIEGANIA ===','1. Dodaj bieg','2. Historia biegów','3. Statystyki','0. Zapisz i wyjdź',sep='\n')
        decyzja = num(int,'Wybierz działanie: ')
        print()
        if decyzja == 1:
            while True:
                data = input('Podaj date (Y-m-d): ')
                if len(data) == 10 and data.replace('-', '').isdigit():
                    break
            while True:
                dystans = round(num(float,'Podaj dystans: '),2)
                if dystans >=MINIMALNY_DYSTANS[0]:
                    break
            czas = (num(int,'Podaj czas w minutach: '))
            dodaj_bieg(historia,data,dystans,czas)
        elif decyzja == 2 :
            wyswietl_historie(historia)
        elif decyzja == 3:
            statystyki(historia)
        elif decyzja == 0:
            zapisz_plik(historia,'dziennik_biegania.json')
            break
        else:
            print('Niepoprawna wartość')
            
    

# Dodawanie biegu
def dodaj_bieg(historia,data,dystans,czas):
    tempo = round(czas/dystans,2)
    trening = {'data':data, 'dystans_km':dystans, 'czas_min':czas, 'tempo_min_km':tempo}
    historia.append(trening)
    
# Wyświetlanie historii
def wyswietl_historie(historia):
    for i in historia:
        print(f"Data: {i['data']}\nDystans: {i['dystans_km']}\nCzas: {int(i['czas_min'])}\nTempo: {i['tempo_min_km']}\n")
        
    
# Wyświetla statystyki
def statystyki(historia):
    if not historia:
        print('Brak danych')
        return
    treningi = 0
    dystans_caly = 0
    srednie_tempo = 0
    for i in historia:
        dystans_caly += i['dystans_km']
        treningi +=1
        srednie_tempo += i['tempo_min_km']
    srednie_tempo = round(srednie_tempo/treningi,2)
    print(f'Całkowity dystans: {dystans_caly}\nŚrednie tempo: {srednie_tempo}\nLiczba treningów: {treningi}')

# Zapisywanie pliku
def zapisz_plik(historia,nazwa_pliku):
    with open(nazwa_pliku, 'w') as plik:
        json.dump(historia,plik)
        

# Wczytywanie pliku
def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            return json.load(plik)
    except:
        return []

main()