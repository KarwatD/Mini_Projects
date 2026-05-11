import json

nazwa_pliku = ('planer_wyjsc.json',)
MIEJSCA = ('restauracja','kino','dom','park','kawiarnia','klub','inne')
STATUSY = ('planowane','odbyło się','odwołane')


def num(typ,numer):
    while True:
        try:
            x = typ(input(numer))
            if x >=0:
                return x
            else:
                raise ValueError
        except ValueError:
            print("Niepoprawna wartość")
            
            
def dodaj_wydarzenie(planer,nazwa,data,miejsce,zaproszeni):
    slownik = {'nazwa':nazwa,'data':data,'miejsce':miejsce,'zaproszeni':zaproszeni,'status':'planowane'}
    planer.append(slownik)
    
    
def zmien_status(planer,nazwa,nowy_status):
    if not planer:
        print('Lista jest pusta')
        return
    for i in planer:
        if nazwa.lower() == i['nazwa'].lower():
            i['status'] = nowy_status
    
    
def wyswietl_planer(planer, status= None):
    if not planer:
        print('Lista jest pusta')
        return
    print()
    for i in planer:
        if not status or status == i['status']:
            print(f"Nazwa: {i['nazwa']}\nData: {i['data']}\nMiejsce: {i['miejsce']}\nLista gości: {i['zaproszeni']}\nStatus: {i['status']}\n")
    
    
def zapisz_plik(nazwa_pliku,planer):
    with open(nazwa_pliku[0],'w') as plik:
        json.dump(planer,plik,ensure_ascii=False)
        

def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0], 'r') as plik:
            return json.load(plik)
    except:
        return []
    
    
def main():
    planer = wczytaj_plik(nazwa_pliku)
    while True:
        print(f'\n=== PLANER WYJŚĆ ===','1.Dodaj wydarzenie','2.Zmień status wydarzenia','3.Lista wydarzeń','0.Zapisz i wyjdź',sep='\n')
        decyzja = num(int,'Wybierz działanie: ')
        if decyzja == 1:
            while True:
                nazwa = input('Podaj nazwe wydarzenia: ')
                if nazwa:
                    break
            while True:
                data = input('Podaj date: ')
                if '-' in data:
                    rok,miesiac,dzien = data.split('-')
                elif '.' in data:
                    rok,miesiac,dzien = data.split('.')
                    data = data.replace('.', '-')
                if len(rok) == 4 and len(miesiac) == 2 and len(dzien)==2 and 0< int(miesiac) <=12 and 0 < int(dzien) <=31:
                    break
                else:
                    print('Niepoprawna data ')
            while True:
                miejsce = input('Podaj miejsce wydarzenia: ').lower()
                if miejsce in MIEJSCA:
                    break
            zaproszeni = input('Kto jest zaproszony? (podaj po ,): ')
            dodaj_wydarzenie(planer,nazwa,data,miejsce,zaproszeni)
        elif decyzja == 2:
            while True:
                nazwa = input('Podaj nazwe wydarzenia: ')
                if nazwa:
                    break
            while True:
                nowy_status = input('Podaj nowy status: ').lower()
                if nowy_status in STATUSY:
                    break
            zmien_status(planer, nazwa,nowy_status)
        elif decyzja == 3:
            while True:
                print(f'\n=== FILTROWANIE ===','1.Wyświetl wszystko','2.Filtruj po statusie','0.Cofnij',sep='\n')
                decyzja2 = num(int,'Wybierz działanie: ')
                print()
                if decyzja2 == 1:
                    wyswietl_planer(planer)
                elif decyzja2 == 2:
                    while True:
                        filtr = input('Podaj status: ').lower()
                        if filtr in STATUSY:
                            break
                    wyswietl_planer(planer,status=filtr)
                elif decyzja2 == 0:
                    break
        elif decyzja == 0:
            zapisz_plik(nazwa_pliku,planer)
            break
        
        
if __name__ == '__main__':
    main()