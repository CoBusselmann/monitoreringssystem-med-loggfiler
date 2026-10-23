from alarm import AlarmManager
from loggsystem import Loggsystem

#Hämtar AlarmManager klassen från alarm.py filen
def menu():

    logg = Loggsystem()
    manager = AlarmManager()
    manager.load_alarms("alarm_doc.txt")
    logg.data_laddad("alarm_doc.txt")
    logg.funktion("meny")
    #Hämtar sparade alarm från filen alarm_doc.txt
    while True:
        
        print("----Larm-konfigurationssystem----")
        print("1. Lägg till alarm")
        print("2. Ta bort alarm")
        print("3. Visa alla aktiva larm")
        print("4. Skicka larm till Monitoreringssystem")
        print("5. Avsluta")
        choice = input("Meny val: ")
        logg.anvandarval("Meny", choice)
        #Meny vid start av programmet
        if choice == "1":

            print("Vilket alarm vill du lägga till?")
            print("1. CPU")
            print("2. RAM")
            print("3. Disk")

            category = input("Alarm val: ")
            logg.anvandarval("Alarm kategori", category)
            if category == "1":
                category = "cpu"
            elif category == "2":
                category = "ram"
            elif category == "3":
                category = "disk"
            else: 
                print("Ogiltigt val, försök igen.")
                logg.fel(f"Ogiltigt alarm kategori {category}")
                continue
            try:
                level = float(input("Ange larmnivå: "))
                logg.anvandarval("Larm nivå,", level)
            except ValueError:
                print("Du måste ange en siffra för larmnivån. Försök igen.")
                logg.fel(f"Ogiltig Larm nivå, {level}")
                continue
                
            if level < 0 or level > 100:
                print("Larmnivån måste vara mellan 0 och 100. Försök igen.")
                logg.fel(f"Ogiltig Larm nivå {level}")
                continue

            manager.add_alarm(category, level)
            print(f"Du har lagt till ett {category.upper()} larm med nivå {level}%.")
            

        elif choice == "2":

            logg.funktion("Ta bort alarm startat.")
            alarms = manager.show_alarms()
            if not alarms: 
                print("Inga alarm finns att ta bort.")
                logg.info("Inga alarm finns att ta bort")
            else:
                print("Vilket alarm vill du ta bort?")
                for i, alarm in enumerate(alarms, start=1):
                    print(f"{i}. {alarm['category'].upper()} - {alarm['level']}%")
                try:
                    index = int(input("Ange numret på alarmet du vill ta bort: ")) - 1
                    logg.anvandarval(f"Tar bort larm {index}")
                    removed_alarm = manager.remove_alarm(index)
                    print(f"Du har tagit bort ett {removed_alarm['category'].upper()} larm med nivå {removed_alarm['level']}%.")
                except (ValueError, IndexError):
                    logg.info("Ogiltigt val vid borttagning av alarm")
                    print("Ogiltigt val, försök igen.")

        elif choice == "3":

            logg.funktion("Visa alarm, startat.")
            alarms = manager.show_alarms()

            if not alarms:
                logg.info("Inga alarm finns.")
                print("Inga alarm är finns.")
            else:
                logg.info("Aktiva alarm visas.")
                print("Aktiva alarm:")
                for i, alarm in enumerate(alarms, start=1):
                    print(f"{i}. {alarm['category'].upper()} - {alarm['level']}%")

        elif choice == "4":

            logg.funktion("Funktion, skicka larm till Monitoreringssystem.")
            try:
                manager.send_alarms("alarm_doc.txt")
                print("Larmen har skickats till Monitoreringssystemet.")
            except OSError:#Felhantering ifall filen inte kan sparas
                print("Kunde inte spara filen.")
                logg.fel("Fil kunde ej sparas.")

        elif choice == "5":

            logg.funktion("Avslutar Larm-system.")
            logg.data_sparad("Sparat larm i alarm_doc.txt")
            manager.saved_alarms("alarm_doc.txt")
            print("Avslutar system.")
            break

        else:

            logg.fel("Ogiltigt meny val")
            print("Ogiltigt meny val, försök igen.")

menu()

