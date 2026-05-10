import json

PRZEDMIOTY = ('matematyka','fizyka','programowanie','angielski','historia','inne')
nazwa_pliku = ('tracker_nauki.json',)

def num(typ,numer,wart=None):
    while True:
        try:
            x = typ(input(numer))
            if not wart and x>=0:
                return x
            elif wart and x >0:
                return x
            else:
                raise ValueError
        except ValueError:
            print('Nieprawidłowa wartość')
            
    
def dodaj_sesje(sesje,data,przedmiot,czas_min,notatka):
    slownik = {'data':data,'przedmiot':przedmiot,'czas_min':czas_min,'notatka':notatka}
    sesje.append(slownik)
    
    
def wyswietl_sesje(sesje, przedmiot=None):
    if not sesje:
        print("Lista jest pusta")
        return
    for i in sesje:
        if przedmiot == i['przedmiot'] or not przedmiot:
            print(f"Data: {i['data']}\nPrzedmiot: {i['przedmiot']}\nCzas: {i['czas_min']}min\nNotatka: {i['notatka']}")


def statystyki(sesje):
    if not sesje:
        print("Lista jest pusta")
        return
    suma = 0
    slownik = {'matematyka':0,'fizyka':0,'programowanie':0,'angielski':0,'historia':0,'inne':0}
    for i in sesje:
        suma += i['czas_min']
        slownik[i['przedmiot']] += i['czas_min']
    
    najmniej = min(slownik,key=slownik.get)
    najwiecej = max(slownik,key=slownik.get)
    print(f"Czas łącznie: {suma}\n")
    for nazwa2,wartosc2 in slownik.items():
        print(f"Przedmiot: {nazwa2} | Czas: {wartosc2}min")
    print(f"Najwięcej czasu spędziłeś na nauce: {najwiecej}\nNajmniej czasu spędziłeś na nauce: {najmniej}")
    
    
    
def zapisz_plik(sesje,nazwa_pliku):
    with open(nazwa_pliku[0],'w') as plik:
        json.dump(sesje,plik,ensure_ascii=False)
        
        
def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0],'r') as plik:
            return json.load(plik)
    except:
        return []
    
def main():
    sesje = wczytaj_plik(nazwa_pliku)
    while True:
        print(f"\n=== TRACKER NAUKI ===","1.Dodaj sesje nauki","2.Lista sesji","3.Statystyki","0.Zapisz i wyjdź",sep="\n")
        decyzja = num(int,'Wybierz działanie: ')
        print()
        if decyzja == 1:
            while True:
                data = input("Podaj date: ")
                if len(data) == 10 and data.replace('-', '').isdigit():
                    break
            while True:
                przedmiot = input("Podaj przedmiot: ").lower()
                if przedmiot in PRZEDMIOTY:
                    break
                else:
                    print('Nie ma takiego przedmiotu')
            czas_min = num(int,'Ile się uczyłeś?: ',wart=True)
            notatka = input("Miejsce na notatke (opcjonalne): ")
            if not notatka:
                notatka = None
            dodaj_sesje(sesje,data,przedmiot,czas_min,notatka)
        elif decyzja == 2:
            while True:
                print(f'\n=== FILTROWANIE ===','1.Wyświetl wszystko','2.Filtruj po przedmiocie','0.Cofnij',sep='\n')
                decyzja2 = num(int,'Wybierz działanie: ')
                print()
                if decyzja2 == 1:
                    wyswietl_sesje(sesje)
                elif decyzja2 == 2:
                    while True:
                        filtr = input('Podaj przedmiot który cie interesuje: ').lower()
                        if filtr in PRZEDMIOTY:
                            break
                        else:
                            print('Nie ma takiego przedmiotu')
                    wyswietl_sesje(sesje,przedmiot=filtr)
                elif decyzja2 == 0:
                    break
        elif decyzja == 3:
            statystyki(sesje)
        elif decyzja == 0:
            zapisz_plik(sesje,nazwa_pliku)
            break
        
if __name__ == '__main__':
    main()