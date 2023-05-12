from typing import List

from bottom_sheet.data_models import Context, BottomSheet
from bottom_sheet.factory.production_line import ProductionLine


class BottomSheetFactory:
    def __init__(self, context: Context, production_line: List[ProductionLine]):
        self.context = context
        self.production_line = production_line

    def produce(self) -> List[BottomSheet]:
        bottom_sheet_list = []

        for production_line in self.production_line:
            if production_line.is_pass(context=self.context):
                bottom_sheet_list.append(production_line.make(context=self.context))

        return bottom_sheet_list
