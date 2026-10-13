
class AlarmManager:

    def __init__(self):
        self.alarms = []

    def add_alarm(self, category, level):
        alarm = {"category": category, "level": level}
        self.alarms.append(alarm)
        self.alarms.sort(key=lambda x: (x["category"], x["level"]))
        return alarm

    def remove_alarm(self, index):
        if 0 <= index < len(self.alarms):
            removed_alarm = self.alarms.pop(index)
            return removed_alarm
        else:
            raise IndexError("Ogiltigt index för att ta bort alarm.")
        
    def show_alarms(self):
        return self.alarms

    def send_alarms(self, path):
        with open(path, "w", encoding="utf-8") as file:
            for alarm in self.alarms:
                file.write(f"{alarm['category']};{alarm['level']}\n")

    def saved_alarms():
        pass
    def load_alarms():
        pass