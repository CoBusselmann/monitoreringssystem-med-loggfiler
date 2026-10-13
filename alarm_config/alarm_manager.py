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
if __name__ == "__main__":
    manager = AlarmManager()
    manager.add_alarm("cpu", 80)
    manager.add_alarm("ram", 90.5)
    print(len(manager.alarms))   # ska skriva 2