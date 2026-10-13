from alarm import AlarmManager

def menu():

    manager = AlarmManager()
    while True:
        print("----Larm-konfigurationssystem----")
        print("1. Lägg till alarm")
        print("2. Ta bort alarm")
        print("3. Visa alla aktiva larm")
        print("4. Skicka larm till Monitoreringssystem")
        print("5. Avsluta")
        choice = input("Meny val: ")

        if choice == "1":

            print("Vilket alarm vill du lägga till?")
            print("1. CPU")
            print("2. RAM")
            print("3. Disk")
            category = input("Alarm val: ")
            if category == "1":
                category = "cpu"
            elif category == "2":
                category = "ram"
            elif category == "3":
                category = "disk"
            else: 
                print("Ogiltigt val, försök igen.")
                continue
            try:
                level = float(input("Ange larmnivå: "))
            except ValueError:
                print("Du måste ange en siffra för larmnivån. Försök igen.")
                continue
            if level < 0 or level > 100:
                print("Larmnivån måste vara mellan 0 och 100. Försök igen.")
                continue

            manager.add_alarm(category, level)
            print(f"Du har lagt till ett {category.upper()} larm med nivå {level}%.")

        elif choice == "2":
            alarms = manager.show_alarms()
            if not alarms: 
                print("Inga alarm finns att ta bort.")
            else:
                print("Vilket alarm vill du ta bort?")
                for i, alarm in enumerate(alarms, start=1):
                    print(f"{i}. {alarm['category'].upper()} - {alarm['level']}%")
                try:
                    index = int(input("Ange numret på alarmet du vill ta bort: ")) - 1
                    removed_alarm = manager.remove_alarm(index)
                    print(f"Du har tagit bort ett {removed_alarm['category'].upper()} larm med nivå {removed_alarm['level']}%.")
                except (ValueError, IndexError):
                    print("Ogiltigt val, försök igen.")

        elif choice == "3":
                   
            alarms = manager.show_alarms()

            if not alarms:
                print("Inga alarm är finns.")
            else:
                print("Aktiva alarm:")
                for i, alarm in enumerate(alarms, start=1):
                    print(f"{i}. {alarm['category'].upper()} - {alarm['level']}%")

        elif choice == "4":
            pass
        elif choice == "5":
            print("Avslutar system.")
            break
        else:
            print("Ogiltigt meny val, försök igen.")
menu()

