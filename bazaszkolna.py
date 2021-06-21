import sys
from funkcje_pomocnicze import *

BAZA_WYCHOWAWCA = 'wychowawca'
BAZA_NAUCZYCIEL = 'nauczyciel'
BAZA_UCZEN = 'uczen'

wychowawcy = []
uczniowie = []
nauczyciele = []

class Wychowawca:
    def __init__(self):
        self.imie_nazw = ''
        self.klasy = []

    def wyswietl(self):
        print(self.imie_nazw)


class Nauczyciel:
    def __init__(self):
        self.imie_nazw = ''
        self.przedmiot = ''
        self.klasy = []

    def wyswietl(self):
        print(self.imie_nazw)


class Uczen:
    def __init__(self):
        self.imie_nazw = ''
        self.klasa = []

    def wyswietl(self):
        print(self.imie_nazw)

def get_by_class(klasa):
  wychowawca = get_wychowawca_by_klasa(klasa, wychowawcy)
  if wychowawca == '':
    print('W: Brak wychowawcy')
  else:
    print('W: '+ wychowawca.imie_nazw)
  for u in uczniowie:
    if klasa in u.klasa:
      print("U: "+u.imie_nazw)

def get_by_wychowawca(imie_nazw):
  wychowawca = get_wychowawca_by_name(imie_nazw, wychowawcy)
  for klasa in wychowawca.klasy:
    get_uczniowie_by_klasa(klasa, uczniowie)

def get_by_nauczyciel(imie_nazw):
  nauczyciel = get_nauczyciel_by_name(imie_nazw, nauczyciele)
  wychowawcy_local = []
  for klasa in nauczyciel.klasy:
    wychowawcy_local.append(get_wychowawca_by_klasa(klasa, wychowawcy).imie_nazw)
  for item in list(dict.fromkeys(wychowawcy_local)):  #eliminacja duplikatow gdy wychowawca ma kilka klas
    print(item)

def get_by_uczen(imie_nazw):
  klasa = get_klasa_by_uczen(imie_nazw, uczniowie)
  lekcje_nauczyciel = get_lekcje_nauczyciel_by_klasa(klasa, nauczyciele)
  for item in lekcje_nauczyciel:
    print(item)

calosc_baza = []
jeden_wiersz = []
baza = open('in.txt', 'r', encoding='utf-8')
while True:
  typ = baza.readline().strip()
  #sprawdzenie czy jestesmy na koncu bazy
  if typ == 'koniec':
    break

  if typ == BAZA_WYCHOWAWCA:
    wychowawca = Wychowawca()
    wychowawca.imie_nazw = baza.readline().strip()
    while True:
      klasa = baza.readline().strip()
      if klasa:
        wychowawca.klasy.append(klasa)
      else:
        break
    wychowawcy.append(wychowawca)

  if typ == BAZA_NAUCZYCIEL:
    nauczyciel = Nauczyciel()
    nauczyciel.imie_nazw = baza.readline().strip()
    nauczyciel.przedmiot = baza.readline().strip()
    while True:
      klasa = baza.readline().strip()
      if klasa:
        nauczyciel.klasy.append(klasa)
      else:
        break
    nauczyciele.append(nauczyciel)

  if typ == BAZA_UCZEN:
    uczen = Uczen()
    uczen.imie_nazw = baza.readline().strip()
    uczen.klasa = baza.readline().strip()
    uczniowie.append(uczen)

  #odczytanie pliku i konwersja na tablice
  # if wiersz:
  #   jeden_wiersz.append(wiersz)
  # else:
  #   if BAZA_UCZEN in jeden_wiersz: # rozdzielenie uczniow na grupy po 3 wiersze
  #     x = list(podziel_na_segmenty(jeden_wiersz, 3))
  #     calosc_baza.extend(x)
  #   else:
  #     calosc_baza.append(jeden_wiersz.copy())
  #     jeden_wiersz.clear()

baza.close()

#konwersja tablicy na obiekty
# for rekord in calosc_baza:
#   print(rekord)
#   if rekord[0] == BAZA_WYCHOWAWCA:
#     wychowawcy.append(Wychowawca(rekord[1], rekord[2:]))
#   if rekord[0] == BAZA_NAUCZYCIEL:
#     nauczyciele.append(Nauczyciel(rekord[1], rekord[2], rekord[3:]))
#   if rekord[0] == BAZA_UCZEN:
#     uczniowie.append(Uczen(rekord[1], rekord[2]))

# get_by_class('2c')
# print("#####################")
# get_by_wychowawca('Krzysztof Baczynski')
# print("#####################")
# get_by_nauczyciel('Jan Dlugosz')
# print("#####################")
# get_by_uczen('Andrzej Kowalski')
# print("#####################")

if sys.argv[1]:
  if len(sys.argv)-1 == 1:
    dane = sys.argv[1]
  else:
    dane = sys.argv[1] + ' ' + sys.argv[2]

  if len(dane) == 2:
    get_by_class(dane)

  elif check_if_wychowawca(dane, wychowawcy):
    get_by_wychowawca(dane)

  elif check_if_nauczyciel(dane, nauczyciele):
    get_by_nauczyciel(dane)

  elif check_if_uczen(dane, uczniowie):
    get_by_uczen(dane)