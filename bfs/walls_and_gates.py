
from collections import deque
from typing import List


class Solution:
    WALL = -1
    GATE = 0
    INFINITY = 2147483647
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        total_rows = len(rooms)
        total_columns = len(rooms[0])

        gates = deque([])
        for row in range(total_rows):
            for column in range(total_columns):
                if rooms[row][column] == self.GATE:
                    gates.appendleft((row, column))

        print(gates)


solution = Solution()
solution.wallsAndGates([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
                        [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]])
