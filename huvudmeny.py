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
                log.user_choices("Huvudmeny", "Starta Larm-konfigurationssystem")
                log.info("Larm-konfigurationssystem startat")
                menu.menu(log)
            elif choice == "2":
                log.user_choices("Huvudmeny", "Starta Monitoreringssystem")
                log.info("Monitoreringssystem startat")
                Monitoreringssystem.main(log)
            elif choice == "3":
                log.user_choices("Huvudmeny", "Avsluta")
                log.info("Programmet avslutas")
                log.end_log()
                print("Avslutar programmet")
                break
            else:
                print("Ogiltigt val, försök igen.")
                log.user_choices("Huvudmeny", "Felaktigt val")
                log.log_error("Felaktigt val i huvudmenyn")
    except KeyboardInterrupt:
        print("\nProgrammet avbrutet av användaren.")
        log.info("Programmet avbrutet av användaren.")

if __name__ == "__main__":
    main()