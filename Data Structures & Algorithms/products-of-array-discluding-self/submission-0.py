class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] * len(nums)
        postfix = [nums[len(nums) - 1]] * len(nums)

        res = []
        for i in range (1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        
        for i in range (len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        for i in range(0, len(nums)):
            prefix_value = prefix[i - 1] if i > 0 else 1
            postfix_value = postfix[i + 1] if i < len(nums) - 1 else 1
            res.append(prefix_value * postfix_value)

        return res