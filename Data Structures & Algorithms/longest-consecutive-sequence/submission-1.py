class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for num in nums:
            if num - 1 in nums_set:
                continue
            else:
                current_len = 1
                current_num = num
                while current_num + 1 in nums_set:
                    current_len += 1
                    current_num += 1
                
                longest = max(longest, current_len)

        return longest