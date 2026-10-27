import psutil
import time
import sys
from loggsystem import Loggsystem



# Rensar terminalen - används för att presentera monitoreringsinformationen snyggare
def clear_terminal():
    sys.stdout.write("\033[H\033[J")

# Kontrollerar om ett mätvärde har nått eller passerat en larmgräns och returnerar True eller False.
def alarm_triggered(value, limit):
    return limit is not None and value >= limit

# Skapar en klass för monitoreringssystemet
class Monitoreringssystem:
    def __init__(self):
        self.log = Loggsystem()
        # Ställ in larmnivåer, värden hämtas från alarm_doc.txt via load_alarms()
        self.warning_limits = {
            "CPU": None,
            "RAM": None,
            "DISK": None
        }

    # Laddar larmnivåer från alarm_doc.txt och uppdaterar self.warning_limits
    def load_alarms(self):
        try:
            self.log.funktion("load_alarms")
            # Rensar terminalen
            clear_terminal()

            print("Följande alarm har ställts in:")
            
            with open("alarm_doc.txt") as f:
                for i in f:
                    value = i.strip().split(";", 1)
                    if "cpu;" in i and float(value[1]) >= 0 and float(value[1]) <= 100:
                        self.warning_limits["CPU"] = float(value[1])
                        print(f"CPU-alarm inställt till: {self.warning_limits["CPU"]}%")
                    elif "ram;" in i and float(value[1]) >= 0 and float(value[1]) <= 100:
                        self.warning_limits["RAM"] = float(value[1])
                        print(f"RAM-alarm inställt till: {self.warning_limits["RAM"]}%")
                    elif "disk;" in i and float(value[1]) >= 0 and float(value[1])<= 100:
                        self.warning_limits["DISK"] = float(value[1])
                        print(f"DISK-alarm inställt till: {self.warning_limits["DISK"]}%")
            
            self.log.info("Alarm har laddats från alarm_doc.txt")    
            print("Återgår till huvudmenyn om 5 sekunder")
            self.log.info("Återgår till huvudmenyn om 5 sekunder")
            time.sleep(5)
        except OSError as e:
            print(f"Fel vid läsning av alarm_doc.txt: {e}")
            self.log.fel(f"Fel vid läsning av alarm_doc.txt: {e}")
        except ValueError as e:
            print(f"Felaktigt värde i alarm_doc.txt: {e}")
            self.log.fel(f"Felaktigt värde i alarm_doc.txt: {e}")
        

    # Monitoreringsloop som körs tills användaren avbryter eller tills en viss tid/iterationer har passerat
    def monitoring_loop(self, limittype, maxvalue=None):
        self.log.funktion("monitoring_loop")
        writer = sys.stdout.write

        # Mäter hur länge monitoreringen har pågått
        start_timer = time.monotonic()

        iterations = 0
        
        try:
            while True:
                
                clear_terminal()

                # Kollar om monitoreringen ska avbrytas baserat på tid eller antal iterationer
                if limittype == "Tid" and (time.monotonic() - start_timer >= maxvalue):
                    break
                if limittype == "Iteration" and iterations >= maxvalue:
                    break

                # Hämtar CPU, RAM och Disk-användning
                cpu = psutil.cpu_percent(interval=1)
                ram = psutil.virtual_memory()
                disk = psutil.disk_usage("C:")
                
                clear_terminal()
                
                if limittype == "Oändlig":
                    writer(f"Tryck CTRL-C för att avbryta monitoreringen\n\n")

                # Kollar om CPU, RAM eller Disk har passerat larmgränsen och loggar det i loggsystemet - True om larmet har passerat, annars False
                if alarm_triggered(cpu, self.warning_limits["CPU"]):
                    writer(f"CPU-användning är över {self.warning_limits['CPU']}%\n")
                    self.log.larm("CPU", self.warning_limits["CPU"])

                if alarm_triggered(ram.percent, self.warning_limits["RAM"]):
                    writer(f"RAM-användning är över {self.warning_limits['RAM']}%\n")
                    self.log.larm("RAM", self.warning_limits["RAM"])
            
                if alarm_triggered(disk.percent, self.warning_limits["DISK"]):
                    writer(f"Disk-användning är över {self.warning_limits['DISK']}%\n")
                    self.log.larm("DISK", self.warning_limits["DISK"])

                writer(f"\nCPU: {cpu}% | RAM: {ram.percent}% | Disk: {disk.percent}%\r")
                
                #Gör att texten skrivs ut direkt och buffras inte
                sys.stdout.flush()

                #time.sleep skapar en paus i X sekunder, för att användaren ska kunna se det som står i terminalen
                time.sleep(2)

                iterations += 1
                    
        except KeyboardInterrupt:
            clear_terminal()
            print("Monitorering manuellt avbruten - återgår till huvudmenyn")
            self.log.info("Monitorering manuellt avbruten")
            time.sleep(3)
            return
            

        print("Monitorering avslutad - återgår till huvudmenyn")
        time.sleep(3)
        
    # Startar monitoreringssessionen och frågar användaren om hur länge den ska köras
    def start_monitor_session(self):
        self.log.funktion("start_monitor_session")
        clear_terminal()
        duration = 0
        choice = input("Hur vill du bestämma tid?\n" \
        "1. Tid\n" \
        "2. Iterationer\n"
        "3. Oändligt - Avbryts med CTRL-C\n"
        "Gör ett val (1-3): ")
        
        if choice == "1":
            self.log.anvandarval("Monitoreringssession", "Tid")
            clear_terminal()
            try:
                duration = int(input("Ange längd i sekunder: "))

                if duration <= 0:
                    print("Värdet måste vara högre än 0.")
                    self.log.fel("Felaktigt värde för sekunder")
                    time.sleep(2)
                    return

                print(f"Du har valt att starta en monitorering i {duration} sekunder")
                self.log.info(f"Monitorering startad i {duration} sekunder")
                self.monitoring_loop("Tid", duration)
                time.sleep(2)
                
            except ValueError as e:
                print(f"Felaktigt värde: {e}")
                self.log.fel("Felaktigt värde för sekunder")
                time.sleep(2)

            except KeyboardInterrupt:
                print("\nMonitorering manuellt avbruten\n")
                self.log.info("Monitorering manuellt avbruten")
                time.sleep(2)

        elif choice == "2":
            self.log.anvandarval("Monitoreringssession", "Iterationer")
            clear_terminal()
            try:
                duration = int(
                    input("Ange längd i antal iterationer: ")
                    )
                if duration <= 0:
                    print("Värdet måste vara högre än 0.")
                    self.log.fel("Felaktigt värde för iterationer")
                    time.sleep(2)
                    return
                
                print(f"Du har valt att starta en monitorering i {duration} iterationer")
                self.log.info(f"Monitorering startad i {duration} iterationer")
                self.monitoring_loop("Iteration", duration)
                time.sleep(2)

            except ValueError as e:
                print(f"Felaktigt värde: {e}")
                self.log.fel("Felaktigt värde för iterationer")
                time.sleep(2)
        
            except KeyboardInterrupt:
                print("\nMonitorering manuellt avbruten\n")
                self.log.info("Monitorering manuellt avbruten")
                time.sleep(2)

        elif choice == "3":
            self.log.anvandarval("Monitoreringssession", "Oändlig")
            self.log.info("Oändlig monitorering startad")
            self.monitoring_loop("Oändlig")

# Huvudmeny
def main():
    monitor = Monitoreringssystem()
    while True:
        clear_terminal()
        choice = input("Vad vill du göra?\n" \
        "1. Ladda alarm.\n" \
        "2. Starta monitorsession.\n" \
        "3. Avsluta.\n"
        "Gör ett val (1-3): ")
        match choice:
            case "1":
                monitor.log.anvandarval("Huvudmeny", "Ladda alarm")
                monitor.load_alarms()
            case "2":
                monitor.log.anvandarval("Huvudmeny", "Starta monitorsession")
                monitor.log.info("Monitoreringssession har startats")
                monitor.start_monitor_session()
            case "3":
                monitor.log.anvandarval("Huvudmeny", "Avsluta")
                monitor.log.info("Programmet avslutas")
                monitor.log.avsluta()
                exit(0)
            case _:
                print("Du har angivit ett felaktikt val")
                monitor.log.anvandarval("Huvudmeny", "Felaktigt val")
                monitor.log.fel("Felaktigt val i huvudmenyn")
                time.sleep(2)

if __name__ == "__main__":
    main()