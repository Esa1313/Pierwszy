def moje_menu():
    choice = None
    while choice != "q":
        print \
            ("""
        Kalkulator Ewy

        1 - dodawanie
        2 - odejmowanie
        3 - mnożenie
        4 - dzielenie
        
        q - koniec zabawy
        """)

        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli
        if choice == "q":
            print("Do widzenia.")

        # dodawanie
        elif choice == "1":
            print("1 powinno dodawać")
            dodajemy()

        # odejmowanie
        elif choice == "2":
            print("2 powinno odejmować")
            odejmujemy()

        # mnożenie
        elif choice == "3":
            print("3 powinno mnożyć")
            mnozymy()

        # dzielenie
        elif choice == "4":
            print("4 powinno dzielić")
            dzielimy()

        # nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


def dodajemy():
    l1 = input("Podaj pierwszą liczbę: ")
    l2 = input("Podaj drugą liczbę: ")
    print("LICZYMY " + l1 + " + " + l2 + " =", end=" ")
    wynik = float(l1) + float(l2)
    print(wynik)

def odejmujemy():
    l1 = input("Podaj pierwszą liczbę: ")
    l2 = input("Podaj drugą liczbę: ")
    print("LICZYMY " + l1 + " - " + l2 + " =", end=" ")
    wynik = float(l1) - float(l2)
    print(wynik)

def mnozymy():
    l1 = input("Podaj pierwszą liczbę: ")
    l2 = input("Podaj drugą liczbę: ")
    print("LICZYMY " + l1 + " * " + l2 + " =", end=" ")
    wynik = float(l1) * float(l2)
    print(wynik)

def dzielimy():
    l1 = input("Podaj pierwszą liczbę: ")
    l2 = input("Podaj drugą liczbę: ")
    print("LICZYMY " + l1 + " / " + l2 + " =", end=" ")
    wynik = float(l1) / float(l2)
    print(wynik)