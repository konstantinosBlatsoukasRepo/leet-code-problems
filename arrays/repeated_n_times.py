"""
array - hash map
"""


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A) / 2

        number_frequencies = {}
        for number in A:
            if number in number_frequencies:
                number_frequencies[number] += 1
            else:
                number_frequencies[number] = 1

            if number_frequencies[number] == N:
                return number
