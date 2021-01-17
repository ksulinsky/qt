import mysql.connector
import hashlib
class Baza2:

        def __init__(self):
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            self.cur=self.db.cursor(dictionary=True)
        def get_tresc(self,nazwa):
            query = "select tresc from pojecia where tytul=%s"
            self.cur.execute(query,(nazwa,))

            fields = [x['tresc'] for x in self.cur.fetchall()]
            if not fields:
                tablica = []
                tablica.append("brak")
                return tablica

            else:
                return fields

        def get_tresc_akceptacja(self, nazwa):
            query = "select tresc from akceptacja where tytul=%s"
            self.cur.execute(query, (nazwa,))

            fields = [x['tresc'] for x in self.cur.fetchall()]
            if not fields:
                tablica = []
                tablica.append("brak")
                return tablica
            else:
                return fields



        def losowe_pojecie(self):
            query="select * from pojecia order by rand() limit 1"
            self.cur.execute(query)
            tytul = [x['tytul'] for x in self.cur.fetchall()]
            self.cur.execute(query)
            tresc=  [y['tresc'] for y in self.cur.fetchall()]
            return tytul[0], tresc[0]

        def lista_pojec(self):

            query = "select * from pojecia order by tytul"
            self.cur.execute(query)
            tytul = [x['tytul'] for x in self.cur.fetchall()]
            return tytul

        def wstaw_pojecie_user(self,title,content):

            self.cur = db.cursor(dictionary=True)
            query = "insert into akceptacja (id,tytul,tresc) values (NULL,%s,%s)"
            self.cur.execute(query, (title,content,))
            self.db.commit()
            return

        def wstaw_pojecie_admin(self, title, content):

            self.cur = db.cursor(dictionary=True)
            query = "insert into pojecia (id,tytul,tresc) values (NULL,%s,%s)"
            self.cur.execute(query, (title, content,))
            self.db.commit()
            return

        def usun_pojecie_admin(self,title):

            query = "delete from pojecia where tytul=%s"
            self.cur.execute(query, (title,))
            self.db.commit()
            return

        def zaloguj(self,logen,haselko):
            self.cur = self.db.cursor(dictionary=True)
            query = "select * from uzytkownicy where nazwa=%s"
            self.cur.execute(query, (logen,))
            fields = [x['haslo'] for x in self.cur.fetchall()]
            self.cur.execute(query, (logen,))
            fields2 = [x['uprawnienia'] for x in self.cur.fetchall()]
            if not fields:
                return 0,0
            else:
                porownanie=hashlib.md5(haselko.encode('utf-8')).hexdigest()

                if porownanie==fields[0]:
                    return 1,fields2[0]
                else:
                    return 0
        def zarejestruj(self,logen,haselko,email1):
            query = "insert into uzytkownicy(id,nazwa,haslo,uprawnienia,email) values (NULL,%s,md5(%s),1,%s)"
            self.cur.execute(query,(logen,haselko,email1,))
            self.db.commit()
            return
        def wyswietl_akceptacja(self):
            query = "select tytul from akceptacja"
            self.cur.execute(query)
            fields = [x['tytul'] for x in self.cur.fetchall()]
            if not fields:
                return 0
            return fields
        def decyzje_akceptacja(self,fields):
            if not fields:
                return 0
            for x in fields:
                query = "select * from akceptacja where id=%s"
                self.cur.execute(query, (x,))
                title = [z['tytul'] for z in self.cur.fetchall()]
                self.cur.execute(query, (x,))
                cont=[y['tresc'] for y in self.cur.fetchall()]
                print(title, cont)

                title1 = title[0]
                cont1 = cont[0]
                odp=input("Czy chcesz? ")
                if(odp=="tak"):
                    query5="insert into pojecia (id,tytul,tresc) values (NULL,%s,%s)"
                    self.cur.execute(query5, (title1,cont1,))
                    query3="delete from akceptacja where id=%s"
                    self.cur.execute(query3, (x,))
                    self.db.commit()
                elif odp=="nie":
                    query4 = "delete from akceptacja where id=%s"
                    self.cur.execute(query4, (x,))
                    self.db.commit()