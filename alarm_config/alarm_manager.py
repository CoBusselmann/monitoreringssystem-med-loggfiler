from alarm import AlarmRule

class AlarmManager:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, category, level):
        alarm = AlarmRule(category, level)
        self.alarms.append(alarm)
        return alarm

    def remove_alarm(self, index):
        pass
    def show_alarms(self):
        pass