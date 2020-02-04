
class Event:

    def meets_condition(self, event_data:dict) -> bool:
        return False


class LoginEvent(Event):
    def meets_condition(self, event_data:dict, override: bool) -> bool:
        return bool(event_data)


print("Hello")
