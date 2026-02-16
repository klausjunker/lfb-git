from app import jkadd
from app import jksub
from app import jkmul
from app import jkdiv
def main():
    print("=== Grundrechenarten Rechner ===")
    
    try:
        a = float(input("Erste Zahl eingeben: "))
        b = float(input("Zweite Zahl eingeben: "))
    except ValueError:
        print("Ungültige Eingabe! Bitte Zahlen eingeben.")
        return

    print("\nWähle eine Operation:")
    print("1 = Addition (+)")
    print("2 = Subtraktion (-)")
    print("3 = Multiplikation (*)")
    print("4 = Division (/)")

    choice = input("Deine Wahl (1-4): ")

    if choice == "1":
        print("Ergebnis:", jkadd(a, b))
    elif choice == "2":
        print("Ergebnis:", jksub(a, b))
    elif choice == "3":
        print("Ergebnis:", jkmul(a, b))
    elif choice == "4":
        print("Ergebnis:", jkdiv(a, b))
    else:
        print("Ungültige Auswahl!")


if __name__ == "__main__":
    print("Debug:")
    main()
