"""
347. Top K Frequent Elements
Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.


Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        answer = c.most_common(k)

        return list(map(lambda x: x[0], answer))


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(s.topKFrequent(nums, k), "[1, 2]")
    nums = [1]
    k = 1
    print(s.topKFrequent(nums, k), "[1]")

"""
Runtime: 124 ms, faster than 13.56% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.8 MB, less than 28.71% of Python3 online submissions for Top K Frequent Elements.
"""