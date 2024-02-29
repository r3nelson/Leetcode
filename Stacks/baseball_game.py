from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in operations:
            if i == "C":
                result.pop()
            elif i == "D":
                result.append(result[-1] * 2)
            elif i == "+":
                result.append(result[-1] + result[-2])
            else:
                result.append(int(i))
            # print(result)

        return sum(result)


print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
