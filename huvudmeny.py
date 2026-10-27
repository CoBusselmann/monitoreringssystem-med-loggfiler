import Monitoreringssystem
import menu

def main():
    try:
            while True:
                Monitoreringssystem.clear_terminal()
                print("----Huvudmeny----")
                print("1. Starta Larm-konfigurationssystem")
                print("2. Starta Monitoreringssystem")
                print("3. Avsluta")
                choice = input("Meny val: ")
                if choice == "1":
                    menu.menu()
                elif choice == "2":
                    Monitoreringssystem.main()
                elif choice == "3":
                    print("Avslutar programmet...")
                    break
                else:
                    print("Ogiltigt val, försök igen.")
    except KeyboardInterrupt:
        print("\nProgrammet avbrutet av användaren.")

main()