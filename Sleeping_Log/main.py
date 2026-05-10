import json


nazwa_pliku = ('dziennik_snu.json',)
JAKOSCI = ((1,'bardzo zły'),(2,'zły'),(3,'przeciętny'),(4,'dobry'),(5,'bardzo dobry'))


def num(typ,numer,uzycie='jakosc'):
    while True:
        try:
            x = typ(input(numer))
            if uzycie == 'menu' and (x ==0 or 3 >= x >=1):
                return x
            elif uzycie == 'jakosc' and 5 >= x >= 1:
                return x
            else:
                print('Nie ma takiej opcji w menu')
        except ValueError:
            print('Błąd typu')
            
            
def dodaj_wpis(dziennik,data,godzina_snu,godzina_pobudki,jakosc):
    godz_pobudki,min_pobudki = godzina_pobudki.split(':')
    godz_snu,min_snu = godzina_snu.split(':')
    godz_pobudki = int(godz_pobudki)
    min_pobudki = int(min_pobudki)
    czas_pobudki = (godz_pobudki*60)+min_pobudki
    godz_snu = int(godz_snu)
    min_snu = int(min_snu)
    czas_snu = (godz_snu*60)+min_snu
    if czas_pobudki > czas_snu:
        dlugosc_min = czas_pobudki - czas_snu
    else:
        dlugosc_min = (24*60)-czas_snu+czas_pobudki
    dlugosc_h = dlugosc_min/60
    slownik = {'data':data,'godzina_snu':godzina_snu,'godzina_pobudki':godzina_pobudki,'dlugosc_h':round(dlugosc_h,2),'jakosc':jakosc}
    dziennik.append(slownik)
    
    
def wyswietl_dziennik(dziennik):
    if not dziennik:
        print('Lista jest pusta')
        return
    for i in dziennik:
        for wartosc,nazwa in JAKOSCI:
            if i['jakosc'] == wartosc:
                break
        print(f"Data: {i['data']}\nGodzina zaśnięcia: {i['godzina_snu']}\nGodzina pobudki: {i['godzina_pobudki']}\nDługość snu: {i['dlugosc_h']}\nJakość: {nazwa}\n")
        

def statystyki(dziennik):
    if not dziennik:
        print('Lista jest pusta')
        return
    licz = 0
    suma_snu = 0
    suma_jakosc = 0
    ilosc_zlych = 0
    for i in dziennik:
        if i['dlugosc_h'] < 7:
            ilosc_zlych +=1
        suma_snu += i['dlugosc_h']
        suma_jakosc += i['jakosc']
        licz +=1
    srednia_snu = suma_snu/licz
    srednia_jakosc = suma_jakosc/licz
    for wartosc, nazwa in JAKOSCI:
        if wartosc == round(srednia_jakosc,0):
            opis1 = nazwa
            opis2 = wartosc
            break
    print(f"Średnia długość snu: {round(srednia_snu,2)}\nŚrednia jakość snu: {opis1} | Numerycznie: {opis2}\nLiczba nocy gdzie spałeś poniżej 7 godzin: {ilosc_zlych}")
    
    
def zapisz_plik(nazwa_pliku,dziennik):
    with open(nazwa_pliku[0],'w') as plik:
        json.dump(dziennik,plik,ensure_ascii=False)
        

def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0],'r') as plik:
            return json.load(plik)
    except:
        return []


def main():
    dziennik = wczytaj_plik(nazwa_pliku)
    while True:
        print(f'\n=== DZIENNIK SNU ===','1.Dodaj wpis snu','2.Historia snu','3.Statystyki','0.Zapisz i wyjdź',sep='\n')
        decyzja = num(int,'Wybierz działanie: ',uzycie='menu')
        print()
        if decyzja == 1:
            while True:
                data = input('Podaj date: ')
                if len(data) ==10 and data.replace('-', '').isdigit():
                    break
            while True:
                godzina_snu = input('Podaj godzine zaśnięcia format (XX:XX): ')
                if len(godzina_snu) == 5 and godzina_snu.replace(':', '').isdigit():
                    break
                else:
                    print('Nieprawidłowe dane prawidłowy format to (XX:XX)')
            while True:
                godzina_pobudki = input('Podaj godzine pobudki format (XX:XX): ')
                if len(godzina_pobudki) == 5 and godzina_pobudki.replace(':', '').isdigit():
                    break
                else:
                    print('Nieprawidłowe dane prawidłowy format to (XX:XX)')
            while True:
                jakosc = num(int,'Podaj jakość snu: ')
                for wartosc, nazwa in JAKOSCI:
                    if jakosc == wartosc:
                        break
                break
            dodaj_wpis(dziennik,data,godzina_snu,godzina_pobudki,jakosc)
        elif decyzja == 2:
            wyswietl_dziennik(dziennik)
        elif decyzja == 3:
            statystyki(dziennik)
        elif decyzja == 0:
            zapisz_plik(nazwa_pliku,dziennik)
            break
        

if __name__ == '__main__':
    main()