import psutil
import time
import sys


#Ställ in larmnivåer
warning_limits = {
    "CPU": 5,
    "RAM": 40,
    "DISK": 60
}

def start_monitor_session():

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("C:")
    session = True
    duration = 0
    writer = sys.stdout.write

    choice = input("Hur vill du bestämma tid?\n" \
    "1. Tid\n" \
    "2. Iterationer\n"
    "3. Oändligt - Avbryts med CTRL-C\n"
    "Val: ")
    
    if choice == "1":
        try:
            duration = int(
                input("Ange längd i sekunder\n")
                )
            if duration <= 0:
                print("Värdet måste vara högre än 0.")
                return
            print(f"Du har valt att starta en monitorering i {duration} sekunder")

            start_timer = time.monotonic()

            while time.monotonic() - start_timer < duration:              
                for i in range(duration, 0, -1):
                    cpu = psutil.cpu_percent(interval=1)
                    ram = psutil.virtual_memory()
                    disk = psutil.disk_usage("C:")
                    
                    sys.stdout.write("\033[H\033[J")
                    if cpu >= warning_limits["CPU"]:
                        writer(f"CPU-användning är över {warning_limits["CPU"]}%\n")

                    if ram.percent >= warning_limits["RAM"]:
                          writer(f"RAM-användning är över {warning_limits["RAM"]}%\n")

                    if disk.percent >= warning_limits["DISK"]:
                        writer(f"Disk-användning är över {warning_limits["DISK"]}%\n")

                    writer(f"\nCPU: {cpu}% RAM: {ram.percent}% Disk: {disk.percent}%\r")
                    sys.stdout.flush()
                    time.sleep(1)

            print("\n\nMonitorering avslutad - återgår till huvudmenyn\n")
            main()

        except ValueError:
            print("Felaktigt värde")
            main()
        
    elif choice == "2":
        try:
            duration = int(
                input("Ange längd i antal iterationer: ")
                )
            if duration <= 0:
                print("Värdet måste vara högre än 0.")
                return
            print(f"Du har valt att starta en monitorering i {duration} iterationer")

            start_timer = time.monotonic()

            while time.monotonic() - start_timer < duration:              
                while time.monotonic() - start_timer < duration:              
                    for i in range(duration, 0, -1):
                        cpu = psutil.cpu_percent(interval=1)
                        ram = psutil.virtual_memory()
                        disk = psutil.disk_usage("C:")
                        
                        sys.stdout.write("\033[H\033[J")
                        if cpu >= warning_limits["CPU"]:
                            writer(f"CPU-användning är över {warning_limits["CPU"]}%\n")

                        if ram.percent >= warning_limits["RAM"]:
                            writer(f"RAM-användning är över {warning_limits["RAM"]}%\n")

                        if disk.percent >= warning_limits["DISK"]:
                            writer(f"Disk-användning är över {warning_limits["DISK"]}%\n")

                        writer(f"\nCPU: {cpu}% RAM: {ram.percent}% Disk: {disk.percent}%\r")
                        sys.stdout.flush()
                        time.sleep(1)

            print("\nMonitorering avslutad - återgår till huvudmenyn")
            main()

        except ValueError:
            print("\nFelaktigt värde")
            main()

        except KeyboardInterrupt:
            print("\nMonitorering manuellt avbruten")
            main()

    elif choice == "3":
        try:
            while session:
                cpu = psutil.cpu_percent(interval=1)
                ram = psutil.virtual_memory()
                disk = psutil.disk_usage("C:")
                
                sys.stdout.write("\033[H\033[J")
                writer("Tryck CTRL-C för att avbryta monitoreringen\n\n")
                if cpu >= warning_limits["CPU"]:
                    writer(f"CPU-användning är över {warning_limits["CPU"]}%\n")

                if ram.percent >= warning_limits["RAM"]:
                    writer(f"RAM-användning är över {warning_limits["RAM"]}%\n")

                if disk.percent >= warning_limits["DISK"]:
                    writer(f"Disk-användning är över {warning_limits["DISK"]}%\n")

                writer(f"\nCPU: {cpu}% RAM: {ram.percent}% Disk: {disk.percent}%\r")
                sys.stdout.flush()
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nMonitorering manuellt avbruten")
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

if __name__ == "__main__":
    main()