from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        nums.sort()
        self.nums = nums

    def add(self, val: int) -> int:
        self._heapify(val=val)
        return self.nums[-self.k]

    def _heapify(self, val: int) -> None:
        if not self.nums:
            self.nums.append(val)

        left, right = 0, len(self.nums)
        mid = (left + right) // 2

        while left < right:
            mid = (left + right) // 2

            if self.nums[mid] == val:
                self.nums.insert(mid, val)
                val = None
                break
            elif self.nums[mid] > val:
                right = mid
            else:
                left = mid + 1

        if val is not None:
            if self.nums[mid] <= val:
                self.nums.insert(mid+1, val)
            else:
                self.nums.insert(mid, val)



def test_solution():
    k = KthLargest(3, [4, 5, 8, 2])
    assert k.add(3) == 4
    assert k.add(5) == 5
    assert k.add(10) == 5
    assert k.add(9) == 8
    assert k.add(4) == 8

    k = KthLargest(3, [5, -1])
    assert k.add(2) == -1
    assert k.add(1) == 1
    assert k.add(-1) == 1
    assert k.add(3) == 2
    assert k.add(4) == 3

    k = KthLargest(1, [])
    assert k.add(-3) == -3
    assert k.add(-2) == -2
    assert k.add(-4) == -2
    assert k.add(0) == 0
    assert k.add(4) == 4
