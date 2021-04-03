class Items:
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)


items = Items(1, 1, 2, 3, 5, 8, 13, 21)
print(items[2:5])
