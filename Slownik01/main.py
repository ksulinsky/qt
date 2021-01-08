
from baza2 import Baza2

if __name__ == '__main__':

    baza=Baza2()

fields=baza.get_tresc("pojecie")
print(fields[0])
# baza.wstaw_pojecie_user("tablica","Tablica to struktura danych, która przechowuje wartości tego samego typu danych")

string1, string2= baza.losowe_pojecie()
tr = baza.get_tresc(string2[0])
print(string1, string2, tr[0])
tab=baza.lista_pojec()
print(tab[0])
#print(tab)
# baza.wstaw_pojecie_user("pojecie","getter jak w c++")
#baza.usun_pojecie_admin("pojeci2e")
#fields22=baza.wyswietl_akceptacja()
#baza.decyzje_akceptacja(fields22)