class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0 for _ in range(len(temperatures))]

        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                temp, index = stack.pop()
                result[index] = i - index
            
            stack.append((v, i))

        return result