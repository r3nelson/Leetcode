class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hash_map = {")": "(", "}": "{", "]": "["}

        for c in s:
            # if c is a close value
            if c in hash_map:
                # make sure last value is open value of c
                if stack and stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    return False
            # if open value
            else:
                stack.append(c)

        return True if not stack else False


print(Solution().isValid(s="()"))
