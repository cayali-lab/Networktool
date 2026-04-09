
def validate_ip(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        number = int(part)
        if number < 0 or number > 255:
            return False

    return True


def main():
    while True:
        print("\n= NÄTVERKSVERKTYG =")
        print("1. Validera IP-adress")
        print("2. Validera port")
        print("3. Visa logg")
        print("4. Avsluta")

        choice = input("Val: ").strip()

        if choice == "1":
            ip = input("Ange IP-adress: ").strip()

            if validate_ip(ip):
                print(f"{ip} är en giltig IP-adress.")
            else:
                print(f"{ip} är inte en giltig IP-adress.")

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