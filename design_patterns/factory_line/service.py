from typing import Optional

from bottom_sheet.data_models import Event


def get_event_by_name(event_name: str) -> Optional[Event]:
    if event_name == 'hana-release-event':
        return Event(event_name=event_name, participant=[1, 2, 3])
    else:
        return None
