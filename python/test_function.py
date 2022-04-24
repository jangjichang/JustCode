from typing import Tuple


def get_row_and_column_from_cell(cell: str) -> Tuple[str, str]:
    """
    cell에서 row, column을 반환합니다.

    Example:
    cell: C9
    row: 9
    column: C
    """
    row = ""
    column = ""

    for character in cell:
        try:
            row_first_character = str(int(character))
            row_index = cell.find(row_first_character)
            row = cell[row_index:]
            break
        except ValueError:
            column = f"{column}{character}"

    return row, column


print(get_row_and_column_from_cell("C94"))
