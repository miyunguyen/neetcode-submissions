class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in hashmap:
                hashmap[''.join(sorted(s))] = 0

        i = 0
        for key in hashmap:
            hashmap[key] = i
            i += 1

        ans = [[] for _ in range(len(hashmap))]


        for s in strs:
            key = ''.join(sorted(s))
            if key in hashmap:
                ans[hashmap[key]].append(s)

        # print(hashmap)
        return ans