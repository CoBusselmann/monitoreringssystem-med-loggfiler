import Monitoreringssystem
import menu
from loggsystem import Loggsystem

def main():
    log = Loggsystem()
    try:
        while True:
            Monitoreringssystem.clear_terminal()
            print("----Huvudmeny----")
            print("1. Starta Larm-konfigurationssystem")
            print("2. Starta Monitoreringssystem")
            print("3. Avsluta")
            choice = input("Meny val: ")
            if choice == "1":
                log.anvandarval("Huvudmeny", "Starta Larm-konfigurationssystem")
                log.info("Larm-konfigurationssystem startat")
                menu.menu(log)
            elif choice == "2":
                log.anvandarval("Huvudmeny", "Starta Monitoreringssystem")
                log.info("Monitoreringssystem startat")
                Monitoreringssystem.main(log)
            elif choice == "3":
                log.anvandarval("Huvudmeny", "Avsluta")
                log.info("Programmet avslutas")
                log.avsluta()
                print("Avslutar programmet")
                break
            else:
                print("Ogiltigt val, försök igen.")
                log.anvandarval("Huvudmeny", "Felaktigt val")
                log.fel("Felaktigt val i huvudmenyn")
    except KeyboardInterrupt:
        print("\nProgrammet avbrutet av användaren.")
        log.info("Programmet avbrutet av användaren.")

if __name__ == "__main__":
    main()