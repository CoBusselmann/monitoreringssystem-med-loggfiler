import psutil
import time
import sys


# Ställ in larmnivåer, kommer senare hämtas från larm-konfigurationssystem
warning_limits = {
    "CPU": 5,
    "RAM": 40,
    "DISK": 60
}

# Rensar terminalen - används för att presentera monitoreringsinformationen snyggare
def clear_terminal():
    sys.stdout.write("\033[H\033[J")


# Monitoreringsloop som körs tills användaren avbryter eller tills en viss tid/iterationer har passerat
def monitoring_loop(limittype, maxvalue=None):
    
    writer = sys.stdout.write

    # Mäter hur länge monitoreringen har pågått
    start_timer = time.monotonic()

    iterations = 0
    
    try:
        while True:
            
            clear_terminal()

            if limittype == "Tid" and (time.monotonic() - start_timer >= maxvalue):
                break
            if limittype == "Iteration" and iterations >= maxvalue:
                break

            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory()
            disk = psutil.disk_usage("C:")
            
            clear_terminal()
            if limittype == "Oändlig":
                writer(f"Tryck CTRL-C för att avbryta monitoreringen\n\n")

            if cpu >= warning_limits["CPU"]:
                writer(f"CPU-användning är över {warning_limits['CPU']}%\n")

            if ram.percent >= warning_limits["RAM"]:
                writer(f"RAM-användning är över {warning_limits['RAM']}%\n")

            if disk.percent >= warning_limits["DISK"]:
                writer(f"Disk-användning är över {warning_limits['DISK']}%\n")

            writer(f"\nCPU: {cpu}% RAM: {ram.percent}% Disk: {disk.percent}%\r")
            
            #Gör att texten skrivs ut direkt och buffras inte
            sys.stdout.flush()

            #time.sleep skapar en paus i X sekunder, för att användaren ska kunna se det som står i terminalen
            time.sleep(1)

            iterations += 1
                
    except KeyboardInterrupt:
        print("\n\nMonitorering manuellt avbruten\n")
        main()

    print("Monitorering avslutad - återgår till huvudmenyn\n")
    main()
# Startar monitoreringssessionen och frågar användaren om hur länge den ska köras
def start_monitor_session():
    
    clear_terminal()
    duration = 0
    choice = input("Hur vill du bestämma tid?\n" \
    "1. Tid\n" \
    "2. Iterationer\n"
    "3. Oändligt - Avbryts med CTRL-C\n"
    "Gör ett val (1-3): ")
    
    if choice == "1":
        clear_terminal()
        try:
            duration = int(input("Ange längd i sekunder\n"))
            if duration <= 0:
                print("Värdet måste vara högre än 0.")
                time.sleep(2)
                return

            print(f"Du har valt att starta en monitorering i {duration} sekunder")
            completed = monitoring_loop("Tid", duration)
            if completed:
                time.sleep(2)
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
                input("Ange längd i antal iterationer: \n")
                )
            if duration <= 0:
                print("Värdet måste vara högre än 0.")
                return
            print(f"Du har valt att starta en monitorering i {duration} iterationer")
            monitoring_loop("Iteration", duration)
            time.sleep(2)
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

# Huvudmeny
def main():
    choice = input("Vad vill du göra?\n" \
    "1. Ladda alarm.\n" \
    "2. Starta monitorsession.\n" \
    "3. Avsluta.\n"
    "Gör ett val (1-3): ")
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