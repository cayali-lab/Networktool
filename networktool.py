def main():
    while True:
        print("\n= NÄTVERKSVERKTYG =")
        print("1. Validera IP-adress")
        print("2. Validera port")
        print("3. Visa logg")
        print("4. Avsluta")

        choice = input("Val: ").strip()

        if choice == "1":
            print("IP validering kommer snart")
        elif choice == "2":
            print("Port validering kommer snart")
        elif choice == "3":
            print("Logg kommer snart")
        elif choice == "4":
            print("Totalt antal valideringar: 0")
            print("Avslutar.")
            break
        else:
            print("Ogiltigt val")


if __name__ == "__main__":
    main()