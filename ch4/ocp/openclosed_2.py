class Event:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False


class UnknownEvent(Event):
    pass

class LoginEvent(Event):

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"]["session"] == 0
            and event_data["after"]["session"] == 1
        )


class LogoutEvent(Event):

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"]["session"] == 1
            and event_data["after"]["session"] == 0
        )


class SystemMonitor:
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)


## ===== test

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
