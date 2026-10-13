from alarm_manager import AlarmManager

manager = AlarmManager()

def handle_add_alarm():

    print("Välj Larm-kategori:")
    print("1. CPU-alarm")
    print("2. RAM-alarm")
    print("3. Disk-alarm")
    choice = input("Val: ")

    if choice == "1":
        category = "cpu"
    elif choice == "2":
        category = "ram"
    elif choice == "3":
        category = "disk"
    else:
        print("Ogiltigt val. Försök igen.")
        return

    level = input(f"Procent nivå för alarm {category.upper()}: ")
    level = level.replace(",", ".")

    try:
        alarm = manager.add_alarm(category, level)
        print(f"Larm skapat: {alarm.category} {alarm.level} %")
    except ValueError as error:
        print(f"Fel: {error}")

def handle_remove_alarm():
    pass
def handle_show_alarms():
    pass
def handle_send_alarms():
    pass

def menu():

    while True:
        print("----Larm-konfigurationssystem----")
        print("1. Lägg till alarm")
        print("2. Ta bort alarm")
        print("3. Visa alla aktiva larm")
        print("4. Skicka larm till Monitoreringssystem")
        print("5. Avsluta")
        choice = input("Meny val: ")

        if choice == "1":
            handle_add_alarm()
        elif choice == "2":
            pass
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

