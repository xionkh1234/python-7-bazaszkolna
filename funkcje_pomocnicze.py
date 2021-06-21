# def podziel_na_segmenty(l, n):
      
#     for i in range(0, len(l), n): 
#         yield l[i:i + n]

def get_wychowawca_by_name(imie_nazw, wychowawcy):
  for w in wychowawcy:
    if w.imie_nazw == imie_nazw:
      return w

def get_wychowawca_by_klasa(klasa, wychowawcy):
  for w in wychowawcy:
    if klasa in w.klasy:
      return w
  return ''

def get_nauczyciel_by_name(imie_nazw, nauczyciele):
  for n in nauczyciele:
    if n.imie_nazw == imie_nazw:
      return n
      
def get_uczniowie_by_klasa(klasa, uczniowie):
  uczniowie_return = []
  for u in uczniowie:
    if u.klasa == klasa:
      uczniowie_return.append(u.wyswietl())
  return uczniowie_return

def get_klasa_by_uczen(imie_nazw, uczniowie):
  for u in uczniowie:
    if u.imie_nazw == imie_nazw:
      return u.klasa

def get_lekcje_nauczyciel_by_klasa(klasa, nauczyciele):
  lekcje = []
  for n in nauczyciele:
    if klasa in n.klasy:
      lekcje.append(n.imie_nazw +' - '+n.przedmiot)
  return lekcje

def check_if_wychowawca(imie_nazw, wychowawcy):
  for w in wychowawcy:
    if w.imie_nazw == imie_nazw:
      return True
  return False

def check_if_nauczyciel(imie_nazw, nauczyciele):
  for n in nauczyciele:
    if n.imie_nazw == imie_nazw:
      return True
  return False

def check_if_uczen(imie_nazw, uczniowie):
  for u in uczniowie:
    if u.imie_nazw == imie_nazw:
      return True
  return False

