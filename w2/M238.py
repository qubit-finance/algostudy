"""
238. Product of Array Except Self

Given an integer array nums,
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 하나 뽑는데 O(1)이여야함. 그러면 미리 뭔가 해서 저장하는거밖에 없음.


        right_prod = [1]
        left_prod = [1]
        for i in range(len(nums)):
            right_prod.append(right_prod[-1]*nums[-i-1])
            left_prod.append(left_prod[-1]*nums[i])

        # left_prod[0]*right_prod[len(nums)-0]
        # left_prod[1]*right_prod[len(nums)-1]

        answer = [left_prod[i]*right_prod[len(nums)-i-1] for i in range(len(nums))]


        return answer


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4]
    print(s.productExceptSelf(nums), "[24,12,8,6]")
    nums = [-1,1,0,-3,3]
    print(s.productExceptSelf(nums), "[0,0,9,0,0]")


"""

Runtime: 260 ms, faster than 21.75% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 22.6 MB, less than 6.59% of Python3 online submissions for Product of Array Except Self.
"""