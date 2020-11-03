import Kalkulator

if __name__ == '__main__':

    print("------KALKULATOR------")
    kalk = Kalkulator.Kalkulator()
x=10
while x>0:

    kalk.arg1 = (int)(input("Podaj pierwszą liczbę: "))
    kalk.znak = (input("Podaj znak dzialania: "))
    kalk.arg2 = (int)(input("Podaj drugą liczbę: "))

    kalk.dzialanie()
    x=x-1