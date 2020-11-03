class Kalkulator:
    arg1 = 0.0
    arg2 = 0.0
    znak =""
    wynik=0.0

    def __init__(self, arg1=None, arg2 = None, znak=None, wynik=None):
        self.arg1=arg1
        self.arg2=arg2
        self.znak=znak
        self.wynik=wynik

    def __str__(self):
        return "Dzialanie : {s.arg1} {s.znak} {s.arg2} = {s.wynik}".format(s = self)


    def dodawanie(self):
        class Error(Exception):
            """Base class for other exceptions"""
            pass

        class WrongOption(Error):
            """Zly znak"""

        try:
            if self.znak != "+":
                raise WrongOption
            else:
                self.wynik = self.arg1 + self.arg2
                print(f" {self.arg1} {self.znak} {self.arg2} = {self.wynik}")
        except WrongOption:
            print("nieodpowiedni znak")


    def odejmowanie(self):
        class Error(Exception):
            """Base class for other exceptions"""
            pass

        class WrongOption(Error):
            """Zly znak"""
            pass

        try:
            if self.znak != "-":
                raise WrongOption
            else:
                self.wynik = self.arg1 - self.arg2
                print(f" {self.arg1} {self.znak} {self.arg2} = {self.wynik}")
        except WrongOption:
            print("nieodpowiedni znak")


    def mnozenie(self):
        class Error(Exception):
            """Base class for other exceptions"""
            pass

        class WrongOption(Error):
            """Zly znak"""
            pass

        try:
            if self.znak != "*":
                raise WrongOption
            else:
                self.wynik = self.arg1 * self.arg2
                print(f" {self.arg1} {self.znak} {self.arg2} = {self.wynik}")
        except WrongOption:
            print("nieodpowiedni znak")


    def dzielenie(self):
        class Error(Exception):
            """Base class for other exceptions"""
            pass

        class WrongOption(Error):
            """Zly znak"""
            pass

        try:
            if self.znak != "/":
                raise WrongOption
            else:
                if self.arg2 !=0:
                    self.wynik = self.arg1 / self.arg2
                    print(f" {self.arg1} {self.znak} {self.arg2} = {self.wynik}")
                else:
                    print("dzielenie przez 0!")

        except WrongOption:
            print("nieodpowiedni znak")

    def dzialanie(self):
        class Error(Exception):
            """Base class for other exceptions"""
            pass

        class WrongOption(Error):
            """Zly znak"""
            pass
        try:
            if self.znak == "/":
                self.dzielenie()
            elif self.znak =="+":
                self.dodawanie()
            elif self.znak=="-":
                self.odejmowanie()
            elif self.znak=="*":
                self.mnozenie()
            else:
               raise WrongOption
        except WrongOption:
            print("nieodpowiedni znak")