# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".

from collections import deque
from typing import List
import copy


class Solution:
    REAL_TARGET = [0, 0, 0, 0]

    def openLock(self, deadends: List[str], target: str) -> int:
        real_deadends = []
        for deadend in deadends:
            real_deadends.append([int(digit) for digit in list(deadend)])

        root = [int(digit) for digit in list(target)]

        print(root)
        total_trials = 0

        queue = deque([root])
        while queue:
            current_combo = queue.pop()
            if current_combo == self.REAL_TARGET:
                return total_trials

            inc_combos = self.inc_by_one(current_combo)
            for combo in inc_combos:
                if combo != real_deadends:
                    queue.appendleft(combo)

            dec_combos = self.dec_by_one(current_combo)
            for combo in dec_combos:
                if combo != real_deadends:
                    queue.appendleft(combo)

            total_trials += 1

    def inc_by_one(self, current_combo):
        inc_combos = []
        for i in range(4):
            combo_copy = copy.deepcopy(current_combo)
            print(combo_copy)
            if combo_copy[i] == 9:
                combo_copy[i] = 0
            else:
                combo_copy[i] += 1
            inc_combos.append(combo_copy)
        return inc_combos

    def dec_by_one(self, current_combo):
        dec_combos = []
        for i in range(4):
            combo_copy = copy.deepcopy(current_combo)
            if combo_copy[i] == 0:
                combo_copy[i] = 9
            else:
                combo_copy[i] -= 1
            dec_combos.append(combo_copy)
        return dec_combos


solution = Solution()

print(solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))

# print(solution.inc_by_one([1, 2, 3, 4]))
# print(solution.dec_by_one([1, 2, 3, 4]))
