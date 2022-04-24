from typing import List

from schema import Or, Schema

schema = Schema({"category": Or(str, None), "options": list, "barcode": str, "images": list})

if __name__ == "__main__":
    test_data = [{"category": None, "options": [], "barcode": "", "images": []}]

    for data in test_data:
        assert schema.is_valid(data)
