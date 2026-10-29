
class AlarmManager:

    def __init__(self):
        
        #Lista med alla aktiva alarm som läggs till av användaren.
        self.alarms = []

    #Funktion för att addera larm i listan, Kategori och nivå.
    def add_alarm(self, category, level):
        alarm = {"category": category, "level": level}
        self.alarms.append(alarm)
        self.alarms.sort(key=lambda x: (x["category"], x["level"]))
        return alarm
    
    #Funktion för borttagning av alarm, index för placering i listan som tas bort.
    def remove_alarm(self, index):

        if 0 <= index < len(self.alarms):
            removed_alarm = self.alarms.pop(index)
            return removed_alarm
        else:
            raise IndexError("Ogiltigt index för att ta bort alarm.")
        
    #Funktion som returnar listan.
    def show_alarms(self):
        return self.alarms

    #Sparar alarm till en textfil som läses av Monitoreringssystemet. används vid avslutning av programmet också.
    def send_alarms(self, path):
        with open(path, "w", encoding="utf-8") as file:
            for alarm in self.alarms:
                file.write(f"{alarm['category']};{alarm['level']}\n")


    #laddar alarm från textfilen
    def load_alarms(self, path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                for i in file:
                    category, level = i.strip().split(";")
                    self.alarms.append({"category": category, "level":float(level)})
        #Felhantering ifall filen inte finns.
        except FileNotFoundError:
            pass

        