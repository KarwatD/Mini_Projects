import json

nazwa_pliku = ('lista_zadan.json',)
PRIORYTETY = ('niski','normalny','wysoki','pilne')
def num(numer):
    while True:
        try:
            x = int(input(numer))
            if x >=0:
                return x
            else:
                raise ValueError
        except:
            print('Niepoprawna wartość')
            
            
def dodaj_zadanie(zadania,tresc,priorytet):
    slownik = {'tresc':tresc,'priorytet':priorytet,'wykonane':False}
    zadania.append(slownik)
    
    
def oznacz_wykonane(zadania,numer):
    try:
        indeks = numer -1
        if 0 <= indeks < len(zadania):
            zadania[indeks]['wykonane'] = True
        else:
            print(f'Nieprawidłowa wartość zakres to (1 - {len(zadania)})')    
    except:
        print('Nieprawidłowa wartość')
    
def wyswietl_zadania(zadania, tylko_niewykonane=False):
    licz = 0
    if not zadania:
        print("Lista jest pusta")
    for i in zadania:
        if tylko_niewykonane and i['wykonane']:
            continue
        licz+=1
        if i['wykonane']:
            status = '[X]'
        else:
            status = '[ ]'
        print(f"{licz}.Treść zadania: {i['tresc']:<20} |  Priorytet: {i['priorytet']:<10} |  Status: {status:<10}")
    
    
def zapisz_plik(zadania,nazwa_pliku):
    with open(nazwa_pliku[0],'w') as plik:
        json.dump(zadania,plik, ensure_ascii=False)
    
    
def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0],'r') as plik:
            return json.load(plik)
    except:
        return []
    
    
def main():
    zadania = wczytaj_plik(nazwa_pliku)
    while True:
        print()
        print(f'=== LISTA ZADAŃ ===','1.Dodaj zadanie','2.Oznacz jako wykonane','3.Pokaż wszystkie zadania','4.Pokaż tylko niewykonane','0.Zapisz i wyjdź',sep='\n')
        decyzja = num('Wybierz działanie: ')
        print()
        if decyzja ==1:
            tresc = input('Podaj treść zadania: ')
            while True:
                priorytet = input('Podaj priorytet: ')
                if priorytet in PRIORYTETY:
                    break
                else:
                    print('Nieprawidłowa wartosc wybierz z poniższych:')
                    licz =1
                    for i in PRIORYTETY:
                        print(licz,i)
                        licz+=1
            dodaj_zadanie(zadania,tresc,priorytet)
        elif decyzja ==2:
            wyswietl_zadania(zadania)
            numer = num('Podaj numer zadania: ')
            oznacz_wykonane(zadania,numer)
        elif decyzja ==3:
            wyswietl_zadania(zadania)
        elif decyzja == 4:
            wyswietl_zadania(zadania,tylko_niewykonane=True)
        elif decyzja ==0:
            zapisz_plik(zadania,nazwa_pliku)
            break
        else:
            print('Niepoprawna wartość')
          
            
if __name__ == '__main__':
    main()