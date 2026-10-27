
class AlarmManager:

    def __init__(self):
        self.alarms = []#Lista med alla aktiva alarm som läggs till av användaren.

    def add_alarm(self, category, level):#Funktion för att addera larm i listan, Kategori och nivå.

        alarm = {"category": category, "level": level}
        self.alarms.append(alarm)
        self.alarms.sort(key=lambda x: (x["category"], x["level"]))
        return alarm

    def remove_alarm(self, index):#Funktion för borttagning av alarm, index för placering i listan som tas bort.

        if 0 <= index < len(self.alarms):
            removed_alarm = self.alarms.pop(index)
            return removed_alarm
        else:
            raise IndexError("Ogiltigt index för att ta bort alarm.")
        
    def show_alarms(self):#Funktion som returnar listan.
        return self.alarms

    def send_alarms(self, path):#Sparar alarm till en textfil som läses av Monitoreringssystemet.
        with open(path, "w", encoding="utf-8") as file:
            for alarm in self.alarms:
                file.write(f"{alarm['category']};{alarm['level']}\n")

    def saved_alarms(self, path):#Sparar alarm till en textfil
        with open(path, "w", encoding="utf-8") as file:
            for alarm in self.alarms:
                file.write(f"{alarm['category']};{alarm['level']}\n")
        
    def load_alarms(self, path):#laddar alarm från textfilen
        try:
            with open(path, "r", encoding="utf-8") as file:
                for i in file:
                    category, level = i.strip().split(";")
                    self.alarms.append({"category": category, "level":float(level)})
        except FileNotFoundError:#Felhantering ifall filen inte finns.
            pass

        