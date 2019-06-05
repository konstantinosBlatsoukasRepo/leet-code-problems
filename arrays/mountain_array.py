class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and A[i] > A[i+1]:
                return i