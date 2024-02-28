from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


print(Solution().removeElement(nums=[3, 2, 2, 3], val=3))
