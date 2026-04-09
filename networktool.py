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
    logg = []

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
                logg.append(f"IP {ip} - giltig")
            else:
                print(f"{ip} är inte en giltig IP-adress.")
                logg.append(f"IP {ip} - ogiltig")

        elif choice == "2":
            port_input = input("Ange port: ").strip()

            if not port_input.isdigit():
                print(f"{port_input} är inte en giltig port.")
                logg.append(f"Port {port_input} - ogiltig")
            else:
                port = int(port_input)
                if 1 <= port <= 65535:
                    print(f"{port} är en giltig port.")
                    logg.append(f"Port {port} - giltig")
                else:
                    print(f"{port} är inte en giltig port.")
                    logg.append(f"Port {port} - ogiltig")

        elif choice == "3":
            print("\n= LOGG =")
            if not logg:
                print("Ingen logg ännu.")
            else:
                for i, entry in enumerate(logg, 1):
                    print(f"{i}. {entry}")

        elif choice == "4":
            print(f"Totalt antal valideringar: {len(logg)}")
            print("Avslutar.")
            break

        else:
            print("Ogiltigt val")


if __name__ == "__main__":
    main()