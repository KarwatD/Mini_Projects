import json

WARUNKI = ('słonecznie','pochmurno','deszcz','śnieg','mgła','burza')
nazwa_pliku = ('dziennik_pogody.json',)

def num (typ,numer):
    while True:
        try:
            x = typ(input(numer))
            return x
        except ValueError:
            print('Nieprawidłowa wartość')
            

def dodaj_wpis(dziennik,data,temperatura,warunki,wilgotnosc):
    slownik = {'data':data,'temperatura':temperatura,'warunki':warunki,'wilgotnosc':wilgotnosc}
    dziennik.append(slownik)
    
    
def wyswietl_wpisy(dziennik):
    for i in dziennik:
        print(f"Data: {i['data']}\nTemperatura: {i['temperatura']}\nPogoda: {i['warunki']}\nWilgotność: {i['wilgotnosc']}\n")


def statystyki(dziennik):
    suma = 0
    lista = []
    slownik = {WARUNKI[0]:0,WARUNKI[1]:0,WARUNKI[2]:0,WARUNKI[3]:0,WARUNKI[4]:0,WARUNKI[5]:0}
    for i in dziennik:
        suma += i['temperatura']
        lista.append(i['temperatura'])
        slownik[i['warunki']] +=1
    srednia = suma/len(dziennik)
    najwyzsza = max(lista)
    najnizsza = min(lista)
    dominanta = max(slownik,key=slownik.get)
    print(f"Średnia temperatura: {srednia:.2f}\nNajwyższa temperatura: {najwyzsza}\nNajniższa temperatura: {najnizsza}\nNajczęstsza pogoda: {dominanta}")
    
def zapisz_plik(nazwa_pliku,dziennik):
    with open(nazwa_pliku[0], 'w') as plik:
        json.dump(dziennik,plik, ensure_ascii=False)

def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0], 'r') as plik:
            return json.load(plik)
    except:
        return []
    

def main():
    dziennik = wczytaj_plik(nazwa_pliku)
    while True:
        print()
        print(f"=== DZIENNIK POGODY ===",'1.Dodaj wpis pogodowy','2.Historia obserwacji','3.Statystyki','0.Zapisz i wyjdź',sep='\n')
        decyzja = num(int,'Wybierz działanie: ')
        print()
        if decyzja == 1:
            while True:
                data = input('Podaj date: ')
                if len(data) ==10 and data.replace('-', '').isdigit():
                    break
            temperatura = num(float, 'Podaj temperature: ')
            while True:
                warunki = input('Jaka jest pogoda: ')
                if warunki in WARUNKI:
                    break
                else:
                    print('Nie ma takiej pogody na liście')
            while True:
                try:
                    wilgotnosc = num(int, 'Jaka jest wilgotność: ')
                    if 0 <= wilgotnosc <= 100:
                        break
                except:
                    print("Nieprawidłowa wartość")      
            dodaj_wpis(dziennik,data,temperatura,warunki,wilgotnosc)
        elif decyzja == 2:
            wyswietl_wpisy(dziennik)
        elif decyzja == 3:
            statystyki(dziennik)
        elif decyzja == 0:
            zapisz_plik(nazwa_pliku,dziennik)
            break

if __name__ == '__main__':
    main()