import json

nazwa_pliku = ('ocen.json',)
SKALA = (1,2,3,4,5,6)
PROGI = ((5.0,'celujący'),(4.5,'bardzo dobry'),(3.5,'dobry'),(2.5,'dostateczny'),(1.5,'dopuszczający'),(0,'niedostateczny'))



def num(typ,numer):
    while True:
        try:
            x = typ(input(numer))
            if x >= 0:
                return x
            else:
                raise ValueError
        except:
            print("Nieprawidłowa wartość")

def dodaj_ocene(oceny,opis,ocena,data):
    slownik = {'opis':opis,'ocena':ocena,'data':data}
    oceny.append(slownik)
    
def wyswietl_oceny(oceny):
    if not oceny:
        print('Lista jest pusta')
        return
    for i in oceny:
        print(f"Opis: {i['opis']}\nOcena: {i['ocena']}\nData: {i['data']}")

def statystyki(oceny):
    suma = 0
    licz = 0
    wartosci = []
    if not oceny:
        print('Lista jest pusta')
        return
    for i in oceny:
        suma += i['ocena']
        licz +=1
        wartosci.append(i['ocena'])
    srednia = suma/licz
    najlepsza = max(wartosci)
    najgorsza = min(wartosci)
    for prog,nazwa in PROGI:
        if srednia >= prog:
            print(f"Ocena: {nazwa}\nŚrednia: {srednia:.2f}\nNajlepsza ocena: {najlepsza}\nNajgorsza ocena: {najgorsza}") 
            break
            
def zapisz_plik(nazwa_pliku,oceny):
    with open(nazwa_pliku[0],'w') as plik:
        json.dump(oceny, plik, ensure_ascii=False)
        
def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku[0], 'r') as plik:
            return json.load(plik)
    except:
        return []
    
def main():
    oceny = wczytaj_plik(nazwa_pliku)
    while True:
        print()
        print(f'=== DZIENNIK OCEN ===','1.Dodaj ocenę','2.Lista ocen','3.Statystyki','0.Zapisz i wyjdź',sep='\n')
        decyzja = num(int,'Wybierz działanie: ')
        print()
        if decyzja == 1:
            while True:
                opis = input('Podaj opis: ').lower()
                if len(opis) >=1:
                    break
                else: 
                    print('Opis nie może być pusty')
            while True:
                ocena = round(num(int,'Podaj ocenę: '),2)
                if ocena in SKALA:
                    break
                else:
                    print('Nie ma takiej oceny')
            while True:
                data = input('Podaj datę: ')
                if len(data) ==10 and data.replace('-', '').isdigit():
                    break
                else:
                    print('Nieprawidłowy format (YYYY-MM-DD)')
            dodaj_ocene(oceny,opis,ocena,data)
        elif decyzja == 2:
            wyswietl_oceny(oceny)
        elif decyzja ==3:
            statystyki(oceny)
        elif decyzja == 0:
            zapisz_plik(nazwa_pliku,oceny)
            break
            
        
if __name__ == '__main__':
    main()
