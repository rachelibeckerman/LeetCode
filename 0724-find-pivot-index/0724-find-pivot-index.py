class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = []
        sumRight = []
        tmpSum = 0
        for i in nums:
            sumLeft.append(tmpSum)
            tmpSum += i
        tmpSum = 0
        for i in range(len(nums)-1,-1,-1):
            sumRight.append(tmpSum)
            tmpSum += nums[i]
        for i in range(len(nums)):
            if(sumLeft[i] == sumRight[-i-1]):
                return i
        return -1