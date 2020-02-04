

class Event:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(self, event_data: dict) -> bool:
        return False



class LoginEvent(Event):

    def meets_condition(self, event_data: dict) -> bool:
        return bool(event_data)


class LogoutEvent(Event):

    def meets_condition(self, event_data: dict, override: bool) -> bool:
        if override:
            return True
        return False

