class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mult = 1;
        answer = [];
        for idx, x in enumerate(nums):
            answer.append(mult);
            mult *= x;
        mult = 1;
        for x in range(len(nums)-1,-1,-1):
            answer[x] *= mult;
            mult *= nums[x];
        return answer;
        