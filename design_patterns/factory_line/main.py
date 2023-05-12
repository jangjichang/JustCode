from datetime import datetime

from factory.production_line import hana_release_event_production_line
from data_models import Context
from factory.operator import BottomSheetFactory

if __name__ == '__main__':
    context1 = Context(
        current_datetime=datetime(2023, 5, 4, 18, 0),
        broker='HANA',
        user_id=1,
        account_id=2,
        action='withdraw',
    )

    bottom_sheet_factory = BottomSheetFactory(
        context=context1,
        production_line=[hana_release_event_production_line]
    )

    context1_bottom_sheet_list = bottom_sheet_factory.produce()

    print(f'context1: {context1_bottom_sheet_list}')
