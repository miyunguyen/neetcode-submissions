class Solution:

    def encode(self, strs: List[str]) -> str:
        s_list = []

        for s in strs:
            s_list.append(f"{len(s)}#{s}")
        
        return "".join(s_list)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []
        while i < len(s):
            j = s.find('#', i)

            length = int(s[i:j])

            decoded_strs.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length
        
        return decoded_strs
