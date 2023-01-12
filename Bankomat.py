from dataclasses import dataclass

@dataclass
class Konto:
    stan_konta: float

    def __init__(self, stan_konta):
        self.__stan_konta = 2500.0

    def wyplata(self, ile, stan_konta):
        if ile > stan_konta:
            print("Nie ma tyle na koncie. Wypłata nie może być zrealizowana.")
        else:
            self.__stan_konta -= ile

    def wplata(self, ile):
        self.__stan_konta += ile

    def ile_zostalo(self):
        saldo = self.__stan_konta
        return saldo

b1 = Konto(2500)
choice = None
while choice != "q":
    print \
        ("""
    Bankomat Ewy

    1 - wypłata
    2 - wpłata
    3 - saldo

    q - koniec zabawy
    """)

    choice = input("Wybierasz: ")
    print()

    # wyjdź z pętli
    if choice == "q":
        print("Do widzenia.")

    # wypłata
    elif choice == "1":
        print("1 wypłata")

        odejmowanie = float(input("Ile chcesz wypłacić? "))
        saldo = b1.ile_zostalo()

        b1.wyplata(ile=odejmowanie, stan_konta=saldo)

        respose = input("Potrzebujesz wydruk? t/n ")
        if respose=="t":
            if odejmowanie>saldo:
                tytul1="Zadeklarowane do wypłaty: "
                tytyl2="Saldo: "
            else:
                tytul1="Wypłacone: "
                tytyl2="Saldo po operacji: "
            print(tytul1, end=" ")
            print(odejmowanie)
            print(tytyl2, end=" ")
            print(b1.ile_zostalo())

    # wpłata
    elif choice == "2":
        print("2 wpłata")
        dodawanie = float(input("Ile wpłacasz? "))
        b1.wplata(dodawanie)

        respose = input("Potrzebujesz wydruk? t/n ")
        if respose=="t":
            print("Wpłacono: ", end=" ")
            print(dodawanie)
            print("Saldo po operacji: ", end=" ")
            print(b1.ile_zostalo())

    # saldo
    elif choice == "3":
        print("saldo", end=" ")
        print(b1.ile_zostalo())


    # nieznany wybór
    else:
        print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")
