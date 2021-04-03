class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)
        self.grid = [[False for _ in range(self.width)][:] for _ in range(self.height)]

    def __contains__(self, coord):
        return coord in self.limits

    def __getitem__(self, coord):
        if coord in self.limits:
            x, y = coord
            return self.grid[x][y]
        return IndexError

    def __setitem__(self, coord, marked):
        if not isinstance(marked, bool):
            raise TypeError

        if coord in self.limits:
            x, y = coord
            self.grid[x][y] = marked
        else:
            raise IndexError

    def __str__(self):
        readable_str = ""
        for row in self.grid:
            for element in row:
                if element:
                    readable_str += "O "
                else:
                    readable_str += "X "
            readable_str += "\n"
        return readable_str


"""
구성이 간단하다. 위임을 통해 문제를 해결한다.
두 객체 모두 최소한의 논리를 사용했다. 메서드는 짧고 응집력이 있다.
coord in self.limits는 의도를 직관적으로 표현하여 더 이상의 설명이 필요 없다.
외부에서 사용할 때도 이점이 있다.
"""
MARKED = True

# TODO: grid, coords로 좌표를 마킹하는 클래스를 구현할 때, 외부에서 인덱스를 체크하는게 맞는지, 클래스에서 체크하는게 맞는지?
def mark_coordinate(grid, coord):
    if coord in grid:
        grid[coord] = MARKED


grid = Grid(3, 3)
coords = [(1, 1), (2, 2), (4, 5)]
for coord in coords:
    mark_coordinate(grid, coord)

print(grid)
