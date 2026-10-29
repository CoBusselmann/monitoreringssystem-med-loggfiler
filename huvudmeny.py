import Monitoreringssystem
import menu
import sys
import argparse
from loggsystem import Loggsystem

def run_cli(log, argv):
    parser = argparse.ArgumentParser(
        description="Kör monitoreringssystemet från kommandoraden"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Ladda befintliga larmgränser
    subparsers.add_parser("load-alarms")

    # Starta monitorering
    monitor_parser = subparsers.add_parser("monitor")
    monitor_parser.add_argument(
        "--mode",
        choices=["time", "iterations", "infinite"],
        required=True
    )
    monitor_parser.add_argument(
        "--value",
        type=int,
        help="Sekunder eller antal iterationer"
    )

    args = parser.parse_args(argv)
    monitor = Monitoreringssystem.Monitoreringssystem(log)

    if args.command == "load-alarms":
        log.user_choices("Kommandorad", "Ladda alarm")
        monitor.load_alarms()

    elif args.command == "monitor":
        monitor.load_alarms()
        if args.mode == "time":
            if args.value is None or args.value <= 0:
                parser.error("Ange ett positivt --value för --mode time.")
            log.user_choices("Kommandorad", f"Monitorera i {args.value} sekunder")
            monitor.monitoring_loop("Tid", args.value)

        elif args.mode == "iterations":
            if args.value is None or args.value <= 0:
                parser.error("Ange ett positivt --value för --mode iterations.")
            log.user_choices("Kommandorad", f"Monitorera i {args.value} iterationer")
            monitor.monitoring_loop("Iteration", args.value)

        elif args.mode == "infinite":
            log.user_choices("Kommandorad", "Oändlig monitorering")
            monitor.monitoring_loop("Oändlig")

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
    if len(sys.argv) > 1:
        log = Loggsystem()
        try:
            run_cli(log, sys.argv[1:])
        finally:
            log.end_log()
    else:
        main()