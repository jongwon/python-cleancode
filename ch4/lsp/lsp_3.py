
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data:dict) -> bool:
        return False

    @staticmethod
    def meets_condition_pre(event_data: dict):
        assert isinstance(event_data, dict), f"{event_data!r} is not a dict"
        for moment in ("before", "after"):
            assert moment in event_data, f"{moment} not in {event_data}"
            assert isinstance(event_data[moment], dict)


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


class TransactionEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["after"].get("transaction") is not None


class SystemMonitor:
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        Event.meets_condition_pre(self.event_data)
        event_cls = next(
            (
                event_cls
                for event_cls in Event.__subclasses__()
                if event_cls.meets_condition(self.event_data)
            ),
            UnknownEvent,
        )
        return event_cls(self.event_data)


## ==== test

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

log4 = SystemMonitor({
    "before": {"session": 1},
    "after": {"session":3, "transaction": "Tx001" }
});

print(log4.identify_event().__class__.__name__)
