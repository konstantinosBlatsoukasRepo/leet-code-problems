class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy = [height for height in heights]
        heights = sorted(heights)

        count = 0
        for index in range(0, len(heights)):
            if heights[index] != copy[index]:
                count += 1
        return count
