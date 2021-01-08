import mysql.connector
import hashlib
class Baza2:

        def get_tresc(self,nazwa):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            cur = db.cursor(dictionary=True)
            cur2 = db.cursor()

            query = "select tresc from pojecia where tytul=%s"
            cur = db.cursor(dictionary=True)
            cur.execute(query,(nazwa,))

            fields = [x['tresc'] for x in cur.fetchall()]
            if not fields:
                tablica = []
                tablica.append("brak")
                return tablica

            else:
                return fields

        def losowe_pojecie(self):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            cur = db.cursor(dictionary=True)
            query="select * from pojecia order by rand() limit 1"
            cur.execute(query)
            tytul = [x['tytul'] for x in cur.fetchall()]
            cur.execute(query)
            tresc=  [y['tresc'] for y in cur.fetchall()]
            return tytul[0], tresc[0]

        def lista_pojec(self):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            cur = db.cursor(dictionary=True)
            query = "select * from pojecia order by tytul"
            cur.execute(query)
            tytul = [x['tytul'] for x in cur.fetchall()]
            return tytul

        def wstaw_pojecie_user(self,title,content):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            cur = db.cursor(dictionary=True)
            query = "insert into akceptacja (id,tytul,tresc) values (NULL,%s,%s)"
            cur.execute(query, (title,content,))
            db.commit()
            return

        def usun_pojecie_admin(self,title):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            cur = db.cursor(dictionary=True)
            query = "delete from pojecia where tytul=%s"
            cur.execute(query, (title,))
            db.commit()
            return

        def zaloguj(self,logen,haselko):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            cur = db.cursor(dictionary=True)
            query = "select haslo from uzytkownicy where nazwa=%s"
            cur.execute(query, (logen,))
            fields = [x['haslo'] for x in cur.fetchall()]
            if not fields:
                return 0
            else:
                porownanie=hashlib.md5(haselko.encode('utf-8')).hexdigest()

                if porownanie==fields[0]:

                    return 1
                else:
                    print("nope")
                    return 0
        def zarejestruj(self,logen,haselko,email1):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            cur = db.cursor(dictionary=True)
            query = "insert into uzytkownicy(id,nazwa,haslo,uprawnienia,email) values (NULL,%s,md5(%s),1,%s)"
            cur.execute(query,(logen,haselko,email1,))
            db.commit()
            return
        def wyswietl_akceptacja(self):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            cur = db.cursor(dictionary=True)
            query = "select id from akceptacja"
            cur.execute(query)
            fields = [x['id'] for x in cur.fetchall()]
            if not fields:
                return 0
            return fields
        def decyzje_akceptacja(self,fields):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="slownik"
            )
            cur = db.cursor(dictionary=True)

            for x in fields:
                query = "select * from akceptacja where id=%s"
                cur.execute(query, (x,))
                title = [z['tytul'] for z in cur.fetchall()]
                cur.execute(query, (x,))
                cont=[y['tresc'] for y in cur.fetchall()]
                print(title, cont)
                odp=input("Czy chcesz? ")
                if(odp=="tak"):
                    query2="SELECT * FROM akceptacja WHERE id=%s"
                    cur.execute(query2, (x,))
                    query5="(insert into pojecia (id,tytul,tresc) values(NULL,%s,%s)"
                    cur.execute(query5,(title,cont,))
                    query3="delete from akceptacja where id=%s"
                    cur.execute(query3, (x,))
                    db.commit()
                elif odp=="nie":
                    query4 = "delete from akceptacja where id=%s"
                    cur.execute(query4, (x,))
                    db.commit()