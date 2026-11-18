class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0 for _ in range(len(temperatures))]

        stack = []

        for i, v in enumerate(temperatures):
            if not stack or v <= stack[-1][0]:
                stack.append((v, i))
            else:
                while stack and stack[-1][0] < v:
                    temp = stack.pop()
                    result[temp[1]] = i - temp[1]

                
                stack.append((v, i))

        
        return result