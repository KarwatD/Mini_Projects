import json

GATUNEK = ('fantastyka','kryminał','romans','historyczna','popularnonaukowa','inne')
STATUS = ('przeczytana','do przeczytania','w trakcie')
nazwa_pliku = ('biblioteczka_ksiazek.json',)

# Walidacja danych
def num(typ,numer):
    while True:
        try:
            x = typ(input(numer))
            if x >=0:
                return x
            else:
                print('Wartość jest ujemna')
        except ValueError:
            print('Nieprawidłowa wartość')

# Dodawanie książek
def dodaj_ksiazke(kolekcja,tytul,autor,gatunek,status):
    slownik = {'tytul':tytul,'autor':autor,'gatunek':gatunek,'status':status}
    kolekcja.append(slownik)
    
# Wyswietlanie książek
def wyswietl_kolekcje(kolekcja):
    if not kolekcja:
        print('Biblioteka jest pusta')
        return
    for i in kolekcja:
        print(f"Tytuł: {i['tytul']}\nAutor: {i['autor']}\nGatunek: {i['gatunek']}\nStatus: {i['status']}")
    
# Wyswietlanie statystyk
def statystyki(kolekcja):
    if not kolekcja:
        print('Biblioteka jest pusta')
        return
    ulubiony = {'fantastyka':0,'kryminał':0,'romans':0,'historyczna':0,'popularnonaukowa':0,'inne':0}
    wszystkie = 0
    przeczytane = 0
    planowane = 0
    for i in kolekcja:
        wszystkie +=1
        if i['status'] == STATUS[0]:
            przeczytane +=1
            if i['gatunek'] == GATUNEK[0]:
                ulubiony['fantastyka'] +=1
            elif i['gatunek'] == GATUNEK[1]:
                ulubiony['kryminał'] +=1
            elif i['gatunek'] == GATUNEK[2]:
                ulubiony['romans'] +=1
            elif i['gatunek'] == GATUNEK[3]:
                ulubiony['historyczna'] +=1
            elif i['gatunek'] == GATUNEK[4]:
                ulubiony['popularnonaukowa'] +=1
            elif i['gatunek'] == GATUNEK[5]:
                ulubiony['inne'] +=1
            else:
                continue
        elif i['status'] == STATUS[1]:
            planowane +=1
        else:
            continue
    najwiecej = max(ulubiony,key=ulubiony.get)
    print(f"Wszystkie: {wszystkie}\nPrzeczytane: {przeczytane}\nPlanowane: {planowane}\nUlubiony gatunek: {najwiecej}, Przeczytane: {ulubiony[najwiecej]} " )
    
    
# Zapisywanie w pliku
def zapisz_plik(kolekcja,nazwa_pliku):
    with open(nazwa_pliku[0], 'w') as plik:
        json.dump(kolekcja,plik, ensure_ascii=False)
    
# Pobieranie z pliku
def wczytaj_plik(nazwa_pliku):
    try:    
        with open(nazwa_pliku[0],'r') as plik:
            return json.load(plik)
    except:
        return []
    
# Menu
def main():
    kolekcja = wczytaj_plik(nazwa_pliku)
    while True:
        print()
        print(f'=== MOJA BIBLIOTECZKA ===','1.Dodaj książkę','2.Lista książek','3.Statystyki','0.Zapisz i wyjdź', sep='\n')
        decyzja = num(int,'Wybierz działanie: ')
        print()
        if decyzja == 1:
            tytul = input('Podaj tytuł: ')
            autor = input('Podaj autora: ')
            while True:
                gatunek = input('Podaj gatunek: ')
                if gatunek in GATUNEK:
                    break
                else:
                    print()
                    print('Niepoprawny gatunek wybierz z poniższych:')
                    x = 0
                    for i in range(len(GATUNEK)):
                        x+=1
                        print(x,GATUNEK[i].capitalize())
            while True:
                status = input('Podaj status: ')
                if status in STATUS:
                    break
                else:
                    print()
                    print('Niepoprawny status wybierz z poniższych:')
                    x = 0
                    for i in range(len(STATUS)):
                        x+=1
                        print(x,STATUS[i].capitalize())
            dodaj_ksiazke(kolekcja,tytul,autor,gatunek,status)
        elif decyzja ==2:
            wyswietl_kolekcje(kolekcja)
        elif decyzja ==3:
            statystyki(kolekcja)
        elif decyzja == 0:
            zapisz_plik(kolekcja,nazwa_pliku)
            break
if __name__ == '__main__':
    main()