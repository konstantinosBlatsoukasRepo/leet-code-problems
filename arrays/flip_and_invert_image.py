class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        reversed_res = [self.reverse(row) for row in A]
        return [self.invert(row) for row in reversed_res]

    def reverse(self, array):
        indexes = [-index for index in range(1, len(array) + 1)]
        return [array[index] for index in indexes]

    def invert(self, array):
        inverted = []
        for element in array:
            if element == 0:
                inverted.append(1)
            else:
                inverted.append(0)
        return inverted
