class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        
        for c in t:
            if c in hashmap and hashmap[c] > 0:
                hashmap[c] -= 1
            else:
                return False

        for v in hashmap.values():
            if v != 0:
                return False

        return True