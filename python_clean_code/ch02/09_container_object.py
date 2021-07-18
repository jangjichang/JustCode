from typing import Tuple


class Boundaries:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __contains__(self, coord: Tuple[int, int]):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)
        self.grid = [[False for _ in range(self.width)][:] for _ in range(self.height)]

    def __contains__(self, coord: Tuple[int, int]):
        return coord in self.limits

    def __getitem__(self, coord: Tuple[int, int]):
        x, y = coord
        if coord in self.limits:
            return self.grid[x][y]
        raise IndexError(f"{x}, {y} is outside the coordinates")

    def __setitem__(self, coord: Tuple[int, int], marked: bool):
        if not isinstance(marked, bool):
            raise TypeError("Invalid type has been entered.")

        x, y = coord
        if coord in self.limits:
            self.grid[x][y] = marked
        else:
            raise IndexError(f"{x}, {y} is outside the coordinates")

    def __str__(self):
        marked_coordinate = ""
        for row in self.grid:
            for element in row:
                if element:
                    marked_coordinate += "O "
                else:
                    marked_coordinate += "X "
            marked_coordinate += "\n"
        return marked_coordinate


"""
구성이 간단하다. 위임을 통해 문제를 해결한다.
두 객체 모두 최소한의 논리를 사용했다. 메서드는 짧고 응집력이 있다.
coord in self.limits는 의도를 직관적으로 표현하여 더 이상의 설명이 필요 없다.
외부에서 사용할 때도 이점이 있다.
"""
MARKED = True


def mark_coordinate(grid, coord):
    grid[coord] = MARKED


if __name__ == "__main__":
    grid = Grid(3, 3)
    coords = [(1, 1), (2, 2), (1, 2)]

    for coord in coords:
        mark_coordinate(grid, coord)

    print(grid)

    # 지도에서 범위 바깥을 표시할 때 에러 발생
    # coord = (4, 5)
    # mark_coordinate(grid, coord)

    # 지도에서 범위 바깥의 값에 접근할 때 에러 발생
    # print(grid[5, 8])
