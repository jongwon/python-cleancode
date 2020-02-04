class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

class LoginEvent(Event):
    pass

class LogoutEvent(Event):
    pass

class UnknownEvent(Event):
    pass

class SystemMonitor:
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if(self.event_data["before"]["session"] == 0
                and self.event_data["after"]["session"] == 1):
            return LoginEvent(self.event_data)
        if(self.event_data["before"]["session"] == 1
                and self.event_data["after"]["session"] == 0):
            return LogoutEvent(self.event_data)
        return UnknownEvent(self.event_data)

log1 = SystemMonitor({
    "before": {"session": 0},
    "after": {"session": 1}
});

print(log1.identify_event().__class__.__name__)

log2 = SystemMonitor({
    "before": {"session": 1},
    "after": {"session": 0}
});

print(log2.identify_event().__class__.__name__)

log3 = SystemMonitor({
    "before": {"session": 1},
    "after": {"session": 1}
});

print(log3.identify_event().__class__.__name__)
