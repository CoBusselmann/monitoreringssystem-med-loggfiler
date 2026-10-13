
class AlarmManager:

    def __init__(self):
        self.alarms = []

    def add_alarm(self, category, level):
        alarm = {"category": category, "level": level}
        self.alarms.append(alarm)
        return alarm