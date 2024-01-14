izbire=['1', '2', '3', '4', '5', '6', '7']
plosca=[['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', '*', '*', '*', '*'], ]
stolpci=7
vrstice=7 ### ups 6 je
def legitimen_igralec(igralec):
  if len(igralec)==1: ### simbol igralca predstavlja v polju
    return True
def igralec_ena():
  u1=input('Igralec 1, izberi simbol ki te bo predstavljal: ')
  while not legitimen_igralec(u1): ### dokler ne izbere z dolzino 1
      print('Tvoje ime mora imeti dolzino 1!')
      u1=input('Igralec 1, izberi simbol ki te bo predstavljal: ') 
  return u1 ### vrne simbol igralca
ena=igralec_ena()
def legitimen_igralec_2(igralec1, igralec2):
  if igralec2==igralec1:
    print('Ime je zasedeno!')
    return False
  else:
    return True
def igralec_dva():
  u2=input('Igralec 2, izberi simbol ki te bo predstavljal: ')
  while (not legitimen_igralec(u2)) or (not legitimen_igralec_2(ena,u2)): ### dokler ne izbere z dolzino 1 in ne izbere zasedeno ime
    print('Ime je zasedeno!')
    u2 = input('Igralec 2, izberi simbol ki te bo predstavljal: ')
  return u2
dva=igralec_dva()
crka=None
poteze=0
def print_plosca():
          print('  '.join(izbire)) ### zdruzi elemente iz izbire v string kjer so loceni z dvema presledkoma
          print('\n'.join(map('  '.join, plosca))) ### map vzame elemente plosce in jih transformira v string skozi vseh 7 stolpcev. \n je za presledke med vrsticami
          print('\n') ###dodatni presledek ki locuje naslednju output
def preveripoteze(poteze): 
          poteze+=1
def izberi_polje(poteze): ### poteze je stevilo potez
  try:
    s=int(input('Izberi potezo: ')) ### izberi potezo
    print('\n') ### presledek
    x=6
    while plosca[x][s-1] !='*': ### dokler je stolpec prazen
      x-=1
    plosca[x][s-1]=crka
    return True
  except IndexError: ### Vnos ni stevilka
    print('To polje ni na voljo. Poskusi se enkrat.')
  except ValueError: ### Stevilka izven dovoljenih parametrov
    print('To polje ni na voljo. Poskusi se enkrat.')
def stolp_zmaga(crka): ###zmaga v stolpcu
  for x in range(6,-1,-1): ### zadnji indeks je 0
    for y in range(7): ### 7 stolpcev
      try:
        if plosca[x][y]==plosca[x-1][y]==plosca[x-2][y]==plosca[x-3][y]==crka: ### 4 zaporedni enaki elementi v stolpcu
          return True
        else:
          continue
      except IndexError:
        continue
def vrsta_zmaga(crka): ### zmaga v vrstici
  for x in range(6,-1,-1):
    for y in range(7):
      try:
        if plosca[x][y]==plosca[x][y+1] ==plosca[x][y+2]==plosca[x][y+3]==crka: ### 4 zaporedni enaki elementi v vrstici
          return True
        else:
          continue
      except IndexError: #dobil sem indexerror
        continue
def diag_zmaga(crka): ###zmaga v diagonali 
  for x in range(6,-1,-1):
    for y in range(7):
      try:
        if plosca[x][y]==plosca[x-1][y+1]==plosca[x-2][y+2]==plosca[x-3][y+3]==crka: ### x-1, y+1 je zato ker je diagonala od gor levo do dol desno
          return True
        elif plosca[x][y]==plosca[x-1][y-1]==plosca[x-2][y-2]==plosca[x-3][y-3]==crka: ### diagonala od gor desno do dol levo
          return True
      except IndexError:
        continue
while True: ### igra se zanka
  print_plosca() ### izpise plosca
  if stolp_zmaga(crka): ### zmaga v stolpcu
    print(crka,'Je zmagal po stolpcu!')
    break
  elif vrsta_zmaga(crka): ### zmaga v vrstici
    print(crka,'Je zmagal po vrstici!')
    break
  elif diag_zmaga(crka): ### zmaga v diagonali
    print(crka,'Je zmagal po diagonali!')
    break
  if poteze%2==0: ### ce je poteza soda ali liha se doloci naslednjega na potezi
    crka=ena
  else:
    crka=dva
  if izberi_polje(poteze): ### izberi_polje je True samo v primeru da je polje prosto
    poteze+=1