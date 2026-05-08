import json

PROGI = ((90,'celujący'),(75,'bardzo dobry'),(60,'dobry'),(45,'dostateczny'),(30,'dopuszczający'),(0,'niedostateczny'))
MIN_PUNKTY = (30,)
nazwa_pliku = ('wyniki_egzaminow.json',)

def num(typ,numer):
    while True:
        try:
            x = typ(input(numer))
            if x >=0:
                return x
            else:
                raise ValueError
        except ValueError:
            print('Nieprawidłowa wartość')
            
def dodaj_wynik(wyniki,uczen,egzamin,punkty,data):
    slownik = {'uczen':uczen,'egzamin':egzamin,'punkty':punkty,'data':data}
    wyniki.append(slownik)
    
def wyswietl_wyniki(wyniki):
    if not wyniki:
        print('Lista jest pusta')
        return
    licz = 0
    for i in wyniki:
        for prog,nazwa in PROGI:
            if i['punkty'] >=prog:
                slownie = nazwa
                break
        if i['punkty'] >= MIN_PUNKTY[0]:
            zdal = 'zdał'
        else:
            zdal = 'nie zdał'
        print(f"Uczeń: {i['uczen']}\nStopień: {slownie}, {zdal}\n ")
    
def statystyki(wyniki):
    if not wyniki:
        print('Lista jest pusta')
        return
    wynik = []
    suma = 0
    licz = 0
    for i in wyniki:
        licz +=1
        suma += i['punkty']
        wynik.append(i['punkty'])
    srednia = suma/licz
    najlepszy = max(wynik)
    najgorszy = min(wynik)
    print(f"Średni wynik: {srednia:.2f}\nNajlepszy wynik: {najlepszy}\nNajgorszy wynik: {najgorszy}")
def zapisz_plik(nazwa_plik,wyniki):
    with open(nazwa_pliku[0],'w') as plik:
        json.dump(wyniki,plik,ensure_ascii=False)
        
def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0],'r') as plik:
            return json.load(plik)
    except:
        return []

def main():
    wyniki = wczytaj_plik(nazwa_pliku)
    while True:
        print()
        print(f"=== WYNIKI EGZAMINÓW ===","1.Dodaj wynik","2.Lista wyników","3.Statystyki","0.Zapisz i wyjdź",sep="\n")
        decyzja = num(int, 'Wybierz działanie: ')
        print()
        if decyzja ==1:
            uczen = input('Podaj imie i nazwisko ucznia: ').title()
            egzamin = input('Z jakiego przedmiotu był egzamin: ').lower()
            while True:
                try:
                    punkty = num(int, 'Ile punktów zdobyłeś: ')
                    if 0 <= punkty <= 100:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('Nieprawidłowa wartość zakres punktów (0-100)')
            while True:
                data = input('Podaj datę: ')
                if len(data) == 10 and data.replace('-', '').isdigit():
                    break
                else:
                    print('Nieprawidłowa wartość format to (YYYY-MM-DD)')
            dodaj_wynik(wyniki,uczen,egzamin,punkty,data)
        elif decyzja == 2:
            wyswietl_wyniki(wyniki)
        elif decyzja == 3:
            statystyki(wyniki)
        elif decyzja == 0:
            zapisz_plik(nazwa_pliku,wyniki)
            break
        
if __name__ == '__main__':
    main()