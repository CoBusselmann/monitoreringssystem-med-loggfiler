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

        elif choice == "2":
            print("Vilket alarm vill du ta bort?")
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            print("Avslutar system.")
            break
        else:
            print("Ogiltigt meny val, försök igen.")
menu()

