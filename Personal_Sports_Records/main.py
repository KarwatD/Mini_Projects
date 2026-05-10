import json

DYSCYPLINY = ('bieg 5km', 'bieg 10km','pompki','podciąganie','plank','rower 20km')
nazwa_pliku = ('rekordy_osobiste.json',)


def num(typ,numer,wyn=True):
    while True:
        try:
            x = typ(input(numer))
            if x >= 0 and not wyn:
                return x
            elif x > 0 and wyn:
                return x
            else:
                raise ValueError
        except ValueError:
            print('Nieprawidłowa wartość')
            

def dodaj_wynik(wyniki,data,dyscyplina,wynik):
    nowy_rekord = True
    if 'bieg' in dyscyplina or 'rower' in dyscyplina:
        jednostka = 'mins'
    else:
            jednostka = 'reps'
    for i in wyniki:
        if dyscyplina == i['dyscyplina'] and i['rekord']:
            if jednostka == 'mins':
                if wynik < i['wynik']:
                    i['rekord'] = False
                else:
                    nowy_rekord = False
            elif jednostka == 'reps':
                if wynik > i['wynik']:
                    i['rekord'] = False
                else:
                    nowy_rekord = False
    slownik = {'data':data,'dyscyplina':dyscyplina,'wynik':wynik,'jednostka':jednostka,'rekord':nowy_rekord}
    wyniki.append(slownik)

        
            
    
def wyswietl_wyniki(wyniki,dyscyplina=None):
    for i in wyniki:
        if not dyscyplina:
            if i['rekord']:
                print(f"Data: {i['data']}\nDyscyplina: {i['dyscyplina']}\nWynik: {i['wynik']}\n")
                print(f" !!! REKORD !!!\n")
        else:
            if dyscyplina == i['dyscyplina']:
                if i['rekord']:
                    print(f"Data: {i['data']}\nDyscyplina: {i['dyscyplina']}\nWynik: {i['wynik']}\n")
                    print(f" !!! REKORD !!!\n")
                    
                
    
    
def aktualne_rekordy(wyniki):
    print('=== REKORDY ===')
    for i in wyniki:
        if i['rekord']:
            print(f"Data: {i['data']}\nDyscyplina: {i['dyscyplina']}\nWynik: {i['wynik']}")
    
    
def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0],'r') as plik:
            return json.load(plik)
    except:
        return []
        
        
def zapisz_plik(wyniki,nazwa_pliku):
    with open(nazwa_pliku[0],'w') as plik:
        json.dump(wyniki,plik,ensure_ascii=False)
        

def main():
    wyniki= wczytaj_plik(nazwa_pliku)
    while True:
        print(f"\n=== MOJE REKORDY ===",'1.Dodaj wynik','2.Lista wyników','3.Aktualne rekordy','0.Zapisz i wyjdź',sep='\n')
        decyzja = num(int,'Wybierz działanie: ',wyn=False)
        print()
        if decyzja == 1:
            while True:
                data = input('Podaj date: ')
                if len(data) ==10 and data.replace('-', '').isdigit():
                    break
            while True:
                dyscyplina = input('Podaj dyscypline: ')
                if dyscyplina in DYSCYPLINY:
                    break
            wynik = num(float,'Podaj wynik w minutach lub liczbę powtórzeń: ')
            dodaj_wynik(wyniki,data,dyscyplina,wynik)
        elif decyzja ==2:
            while True:
                print(f'\n=== FILTR ===','1.Wyświetl wszystko','2.Filtruj po dyscyplinie','0.Cofnij',sep='\n')
                decyzja2 = num(int,'Wybierz działanie: ')
                print()
                if decyzja2 == 1:
                    wyswietl_wyniki(wyniki)
                elif decyzja2 == 2:
                    while True:
                        filtr = input('Podaj dyscypline po której chcesz filtrować: ')
                        if filtr in DYSCYPLINY:
                            break
                    wyswietl_wyniki(wyniki,dyscyplina=filtr)
                elif decyzja2 == 0:
                    break
        elif decyzja == 3:
            aktualne_rekordy(wyniki)
        elif decyzja == 0:
            zapisz_plik(wyniki,nazwa_pliku)
            break
        
if __name__ == '__main__':
    main()