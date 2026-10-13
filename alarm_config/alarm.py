
class AlarmManager:

    def __init__(self):
        self.alarms = []

    def add_alarm(self, category, level):
        alarm = {"category": category, "level": level}
        self.alarms.append(alarm)
        return alarm

   # def remove_alarm(self, index):
      #  if 0 <= index < len(self.alarms):
      #      removed_alarm = self.alarms.pop(index)
      #      return removed_alarm
       # else:
       #     raise IndexError("Ogiltigt index för att ta bort alarm.")
        
    def show_alarms(self):
        list_sorted = sorted(self.alarms, key=lambda x: x['category'])
        return list_sorted