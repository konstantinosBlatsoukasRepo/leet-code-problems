from collections import deque


class Solution(object):
    def hammingDistance(self, x: int, y: int) -> int:
        x = deque(bin(x)[2:])
        y = deque(bin(y)[2:])

        length_diff = abs(len(y) - len(x))
        if len(x) < len(y):
            for i in range(0, length_diff):
                x.appendleft('0')
        else:
            for i in range(0, length_diff):
                y.appendleft('0')

        distance = 0
        for index in range(0, len(y)):
            if x[index] != y[index]:
                distance += 1

        return distance


solution = Solution()
print(solution.hammingDistance(1, 4))
