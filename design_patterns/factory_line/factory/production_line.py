from abc import ABC
from datetime import datetime
from typing import List

from bottom_sheet.data_models import Context, BottomSheet
from bottom_sheet.factory.condition_checker import ConditionChecker, PeriodConditionChecker, BrokerConditionChecker, \
    EventApplyHistoryConditionChecker
from bottom_sheet.factory.maker import Maker, HanaReleaseEventMaker


class ProductionLine(ABC):
    def __init__(self, condition_checker_list: List[ConditionChecker], maker: Maker):
        self.condition_checker_list = condition_checker_list
        self.maker = maker

    def is_pass(self, context: Context) -> bool:
        for condition_checker in self.condition_checker_list:
            if not condition_checker.is_pass(context):
                return False
        return True

    def make(self, context: Context) -> BottomSheet:
        return self.maker.make(context=context)



hana_release_event_production_line = ProductionLine(
    condition_checker_list=[
        PeriodConditionChecker(
            display_start_at=datetime(2023, 5, 2),
            display_end_at=datetime(2023, 6, 2)
        ),
        BrokerConditionChecker(
            broker='HANA'
        ),
        EventApplyHistoryConditionChecker(
            event_name='hana-release-event'
        ),
    ],
    maker=HanaReleaseEventMaker()
)