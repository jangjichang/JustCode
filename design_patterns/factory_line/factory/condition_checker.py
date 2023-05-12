from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime

from bottom_sheet.data_models import Context
from bottom_sheet.service import get_event_by_name


class ConditionChecker(ABC):
    @abstractmethod
    def is_pass(self, context: Context) -> bool:
        return True


class PeriodConditionChecker(ConditionChecker):
    def __init__(self, display_start_at: datetime, display_end_at: datetime):
        self.display_start_at = display_start_at
        self.display_end_at = display_end_at

    def is_pass(self, context: Context) -> bool:
        if self.display_end_at is not None:
            if self.display_end_at < context.current_datetime:
                return False

        if self.display_start_at is not None:
            if context.current_datetime < self.display_start_at:
                return False

        return True


class BrokerConditionChecker(ConditionChecker):
    def __init__(self, broker: str):
        self.broker = broker

    def is_pass(self, context: Context) -> bool:
        return context.broker == self.broker


class EventApplyHistoryConditionChecker(ConditionChecker):
    def __init__(self, event_name: str):
        self.event_name = event_name

    def is_pass(self, context: Context) -> bool:
        event = get_event_by_name(event_name=self.event_name)
        if not event:
            return False
        return context.user_id in event.participant
