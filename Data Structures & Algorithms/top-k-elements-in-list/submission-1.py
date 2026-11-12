class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        sorted_hashmap = dict(sorted(hashmap.items(), key = lambda item:item[1], reverse=True))

        ans = []
        
        for key in sorted_hashmap:
            ans.append(key)
            k -= 1
            if k <= 0:
                break

        return ans