from EventTypes import EventType
from datetime import datetime


class Event:
    def __init__(
        self,
        start_time: datetime = None,
        end_time: datetime = None,
        event_type: EventType = None,
        event_name: str = None,
        event_id: int = None,
    ):
        if (
            start_time is None
            or end_time is None
            or event_type is None
            or event_name is None
            or event_id is None
        ):
            raise ValueError("All parameters must be set.")

        self.start_time = start_time
        self.end_time = end_time
        self.event_type = event_type
        self.event_name = event_name
        self.event_id = event_id

    def get_time_delta(self):
        return self.end_time - self.start_time

    def get_event_name(self):
        return self.event_name

    def get_event_type(self):
        return self.event_type

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_event_id(self):
        return self.event_id


class EventContainer:
    def __init__(
        self,
        date: datetime = None,
        events: list = None,
        container_id: int = None,
        container_locked: bool = False,
        container_archived: bool = False,
    ):
        if date is None or events is None or container_id is None:
            raise ValueError("All parameters must be set.")

        self.date = date
        self.events = []
        self.container_id = container_id
        self.container_locked = container_locked
        self.container_archived = container_archived

    def lock(self):
        self.container_locked = True

    def add_event(self, event: Event):
        if not self.container_locked:
            self.events.append(event)
        else:
            raise Exception("Container is locked.")

    def _internal_replace_event(self, event: Event, index: int):
        if not self.container_locked:
            self.events[index] = event
        else:
            raise Exception("Container is locked.")

    def replace_event(self, event: Event, event_id: int):
        for index, event_ in enumerate(self.events):
            if event_id == event_.get_event_id():
                self._internal_replace_event(event, index)
                return
        raise Exception(
            "Event with id {} not found in collection with id {}".format(
                event_id, self.container_id
            )
        )

    def get_event_by_id(self, event_id: int):
        for index, event_ in enumerate(self.events):
            if event_id == event_.get_event_id():
                return event_
        raise Exception(
            "Event with id {} not found in collection with id {}".format(
                event_id, self.container_id
            )
        )

    def get_event_by_index(self, index: int):
        return events[index]

    def remove_event(self, event_id: int):
        if not self.container_locked:
            for index, event_ in enumerate(self.events):
                if event_id == event_.get_event_id():
                    self.events.pop(index)
                    return
            raise Exception(
                "Event with id {} not found in collection with id {}".format(
                    event_id, self.container_id
                )
            )

    def archive(self):
        self.container_archive = True

    def check_archived(self):
        return self.container_archived

    def check_locked(self):
        return self.container_locked

    def get_total_events(self):
        return len(self.events)

    def get_all_events(self):
        return self.events
