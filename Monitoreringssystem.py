import psutil
import time
import sys


#Ställ in larmnivåer
warning_limits = {
    "CPU": 5,
    "RAM": 40,
    "DISK": 60
}
def clear_terminal():
    sys.stdout.write("\033[H\033[J")

def monitoring_loop(limittype, maxvalue=None):

    writer = sys.stdout.write
    start_timer = time.monotonic()
    iterations = 0

    try:
        while True:
            
            clear_terminal()

            if limittype == "Tid" and (time.monotonic() - start_timer >= maxvalue):
                break
            if limittype == "Iteration" and iterations >= maxvalue:
                break
            if limittype == "Oändlig":
                writer("Tryck CTRL-C för att avbryta monitoreringen")
       
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory()
            disk = psutil.disk_usage("C:")
            
            clear_terminal()
            if cpu >= warning_limits["CPU"]:
                writer(f"CPU-användning är över {warning_limits['CPU']}%\n")

            if ram.percent >= warning_limits["RAM"]:
                writer(f"RAM-användning är över {warning_limits['RAM']}%\n")

            if disk.percent >= warning_limits["DISK"]:
                writer(f"Disk-användning är över {warning_limits['DISK']}%\n")

            writer(f"\nCPU: {cpu}% RAM: {ram.percent}% Disk: {disk.percent}%\r")
            sys.stdout.flush()
            time.sleep(1)
            iterations += 1
            if limittype == "Oändlig":
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitorering manuellt avbruten\n")
        main()

    print("Monitorering avslutad - återgår till huvudmenyn\n")
    main()

def start_monitor_session():
    
    clear_terminal()
    duration = 0
    choice = input("Hur vill du bestämma tid?\n" \
    "1. Tid\n" \
    "2. Iterationer\n"
    "3. Oändligt - Avbryts med CTRL-C\n"
    "Val: ")
    
    if choice == "1":
        clear_terminal()
        try:
            duration = int(input("Ange längd i sekunder\n"))
            if duration <= 0:
                print("Värdet måste vara högre än 0.")
                time.sleep(1)
                return

            print(f"Du har valt att starta en monitorering i {duration} sekunder")
            completed = monitoring_loop("Tid", duration)
            if completed:
                time.sleep(1)
        except ValueError:
            print("Felaktigt värde")
            main()
        except KeyboardInterrupt:
            print("\nMonitorering manuellt avbruten\n")
            main()
        
    elif choice == "2":
        clear_terminal()
        try:
            duration = int(
                input("Ange längd i antal iterationer: ")
                )
            if duration <= 0:
                print("Värdet måste vara högre än 0.")
                return
            print(f"Du har valt att starta en monitorering i {duration} iterationer")
            monitoring_loop("Iteration", duration)
            time.sleep(1)
        except ValueError:
            print("\nFelaktigt värde")
            main()
        except KeyboardInterrupt:
            print("\nMonitorering manuellt avbruten\n")
            main()
            
    elif choice == "3":
        monitoring_loop("Oändlig")
    else:
        main()

def main():
    choice = input("Vad vill du göra?\n" \
    "1. Ladda alarm.\n" \
    "2. Starta monitorsession.\n" \
    "3. Avsluta.\n")
    match choice:
        case "1":
            pass
        case "2":
            start_monitor_session()
        case "3":
            exit(0)
        case _:
            print("Du har angivit ett felaktikt val")
            clear_terminal()
            main()

if __name__ == "__main__":
    main()