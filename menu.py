from alarm import AlarmManager

#Hämtar AlarmManager klassen från alarm.py.
def menu(log):

    #instanser av loggsystem och AlarmManager klasserna
    manager = AlarmManager()
    manager.load_alarms("alarm_doc.txt")
    log.log_file_data("alarm_doc.txt")
    log.log_function("Startmeny Larm-system")

    while True:
        #Första meny vid start av Larm-konf.
        print("----Larm-konfigurationssystem----")
        print("1. Lägg till alarm")
        print("2. Ta bort alarm")
        print("3. Visa alla aktiva larm")
        print("4. Skicka larm till Monitoreringssystem")
        print("5. Avsluta")
        choice = input("Meny val: ")
        log.user_choices("Startmeny Larm-larmsystem", choice)
        
        if choice == "1":
            #kategori och nivå för alarmet som ska läggas till
            print("Vilket alarm vill du lägga till?")
            print("1. CPU")
            print("2. RAM")
            print("3. Disk")

            category = input("Alarm val: ")
            log.user_choices("Valt Larm:", category)

            if category == "1":
                category = "cpu"
            elif category == "2":
                category = "ram"
            elif category == "3":
                category = "disk"
            else: 
                print("Ogiltigt val, försök igen.")
                log.log_error(f"Ogiltigt alarm kategori {category}")
                continue
            try:
                level = float(input("Ange larmnivå: "))
                log.user_choices("Larm nivå:", level)
                #felhantering ifall användaren inte anger en siffra för larmnivån
            except ValueError:
                print("Du måste ange en siffra för larmnivån. Försök igen.")
                log.log_error(f"Ogiltig Larm nivå, {level}")
                continue
                #felhantering ifall användaren anger en larmnivå som inte är mellan 0 och 100
            if level < 0 or level > 100:
                print("Larmnivån måste vara mellan 0 och 100. Försök igen.")
                log.log_error(f"Ogiltig Larm nivå {level}")
                continue
                
            manager.add_alarm(category, level)
            print(f"Du har lagt till ett {category.upper()} larm med nivå {level}%.")
            

        elif choice == "2":
            #Val vid borttagning av alarm
            #Visar lista på alla aktiva alarm om det finns några.
            log.log_function("Ta bort alarm startat.")
            alarms = manager.show_alarms()

            if not alarms: 

                print("Inga alarm finns att ta bort.")
                log.info("Inga alarm finns att ta bort")

            else:

                print("Vilket alarm vill du ta bort?")
                log.info("Visar lista på alarm som kan tas bort.")
                for i, alarm in enumerate(alarms, start=1):
                    print(f"{i}. {alarm['category'].upper()} - {alarm['level']}%")
                    #Går igenom listan med alarm och visar dem för användaren med index för att matcha användarens val +1.

                try:

                    index = int(input("Ange numret på alarmet du vill ta bort: ")) - 1
                    removed_alarm = manager.remove_alarm(index)
                    print(f"Du har tagit bort ett {removed_alarm['category'].upper()} larm med nivå {removed_alarm['level']}%.")
                    log.info(f"Tar bort larm {removed_alarm['category'].upper()} med nivå {removed_alarm['level']}%")
                    #felhantering vid ogiltigt val av index.
                except (ValueError, IndexError):
                    log.log_error("Ogiltigt val vid borttagning av alarm")
                    print("Ogiltigt val, försök igen.")

        elif choice == "3":
            #Meny val för att visa alla aktiva alarm om det finns några.
            log.log_function("Visa alarm, startat.")
            alarms = manager.show_alarms()#s

            if not alarms:
                log.info("Inga alarm finns.")
                print("Inga alarm är finns.")
            else:
                log.info("Aktiva alarm visas.")
                print("Aktiva alarm:")
                for i, alarm in enumerate(alarms, start=1):
                    print(f"{i}. {alarm['category'].upper()} - {alarm['level']}%")

        elif choice == "4":
            #Meny val för att skicka alla larm till alarm_doc.txt, där filen läses av Monitoreringssystemet.
            log.log_function("Funktion, skicka larm till Monitoreringssystem.")
            try:
                manager.send_alarms("alarm_doc.txt")
                print("Larmen har skickats till Monitoreringssystemet.")
            except OSError:#Felhantering ifall filen inte kan sparas
                print("Kunde inte spara filen.")
                log.log_error("Fil kunde ej sparas.")

        elif choice == "5":
            #avslutar och sparar alla aktiva alarm i alarm_doc.txt filen.
            log.log_function("Avslutar Larm-system.")
            log.info("Sparat larm i alarm_doc.txt")
            manager.saved_alarms("alarm_doc.txt")
            print("Avslutar system.")
            break

        else:

            log.log_error("Ogiltigt meny val")
            print("Ogiltigt meny val, försök igen.")

if __name__ == "__main__":
    menu()

