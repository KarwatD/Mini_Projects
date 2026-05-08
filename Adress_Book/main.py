import json

GRUPY = ('rodzina','przyjaciele','praca','znajomi','inne')
nazwa_pliku = ('ksiazka_adresowa.json',)


def num(typ,numer):
    while True:
        try:
            x = typ(input(numer))
            if x >=0:
                return x
            else:
                raise ValueError
        except ValueError:
            print("Nieprawidłowa wartość")
           
            
def dodaj_kontakt(kontakty,imie_nazwisko,telefon,email,grupa):
    slownik = {'imie_nazwisko':imie_nazwisko,'telefon':telefon,'email':email,'grupa':grupa}
    kontakty.append(slownik)


def wyswietl_kontakty(kontakty, grupa = None):
    if not kontakty:
        print('Lista jest pusta')
    for i in kontakty:
        if grupa and i['grupa'] != grupa:
            continue
        print(f"Kontakt: {i['imie_nazwisko']}\nTelefon: {i['telefon']}\nEmail: {i['email']}\nGrupa: {i['grupa']}\n")


def szukaj(kontakty,fraza):
    if not kontakty:
        print('Lista jest pusta')
        return
    print()
    for i in kontakty:
        if fraza.lower() in i['imie_nazwisko'].lower():
            print(f"Kontakt: {i['imie_nazwisko']}\nTelefon: {i['telefon']}\nEmail: {i['email']}\nGrupa: {i['grupa']}\n")
    
    
def zapisz_plik(kontakty,nazwa_pliku):
    with open(nazwa_pliku[0],'w') as plik:
        json.dump(kontakty,plik,ensure_ascii=False)
        

def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0],'r') as plik:
            return json.load(plik)
    except:
        return []
    
def main():
    kontakty = wczytaj_plik(nazwa_pliku)
    while True:
        print()
        print(f'=== KSIĄŻKA ADRESOWA ===','1.Dodaj kontakt','2.Lista kontaktów (wszystkie lub z grupy)','3.Szukaj kontaktu','0.Zapisz i wyjdź',sep='\n')
        decyzja = num(int,'Wybierz działanie: ')
        print()
        if decyzja ==1:
            imie_nazwisko = input('Podaj imie i nazwisko ').title()
            while True:
                telefon = input('Podaj numer telefonu format(xxx-xxx-xxx): ')
                if len(telefon) == 11 and telefon.replace('-', '').isdigit():
                    break
                else:
                    print('Nieprawidłowa wartość')
            while True:
                email = input('Podaj email: ')
                if '@' in email:
                    break
                else:
                    print('Nieprawidłowa wartość')
            while True:
                grupa = input('Podaj grupe: ').lower()
                if grupa in GRUPY:
                    break
                else:
                    print('Nie ma takiej grupy')
            dodaj_kontakt(kontakty,imie_nazwisko,telefon,email,grupa)
        elif decyzja == 2:
            while True:
                print(f'== FILTR ==', '1.Wyświetl wszystkie','2.Filtruj po grupie','0.Cofnij',sep='\n')
                decyzja2 = num(int, 'Wybierz działanie: ')
                print()
                if decyzja2 == 1:
                    wyswietl_kontakty(kontakty)
                elif decyzja2 == 2:
                    grupa = input('Podaj grupe: ').lower()
                    print()
                    if grupa in GRUPY:
                        wyswietl_kontakty(kontakty,grupa)
                        break
                    else:
                        print('Nie ma takiej grupy')
                elif decyzja2 ==0:
                    break
        elif decyzja == 3:
            fraza = input('Podaj dane po których będziemy szukać: ').title()
            szukaj(kontakty,fraza)
        elif decyzja == 0:
            zapisz_plik(kontakty,nazwa_pliku)
            break
        
if __name__ == '__main__':
    main()