import Monitoreringssystem
import menu

def main():
    try:
            while True:
                print("----Huvudmeny----")
                print("1. Starta Monitoreringssystem")
                print("2. Starta Larm-konfigurationssystem")
                print("3. Avsluta")
                choice = input("Meny val: ")
                if choice == "1":
                    Monitoreringssystem.main()
                elif choice == "2":
                    menu.menu()
                elif choice == "3":
                    print("Avslutar programmet...")
                    break
                else:
                    print("Ogiltigt val, försök igen.")
    except KeyboardInterrupt:
        print("\nProgrammet avbrutet av användaren.")