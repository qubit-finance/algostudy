"""
240. Search a 2D Matrix II
Write an efficient algorithm that searches for a target value in an m x n integer matrix.
The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9

"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(s.searchMatrix(matrix, target), True)
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 20
    print(s.searchMatrix(matrix, target), False)


"""
Runtime: 608 ms, faster than 63.38% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 36.1 MB, less than 6.69% of Python3 online submissions for Find the Duplicate Number.
"""
















"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = False
        for lst in matrix:
            for x in lst:
                if x==target:
                    return True
        
        
        return ans

"""


"""
Runtime: 184 ms, faster than 13.87% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.4 MB, less than 98.75% of Python3 online submissions for Search a 2D Matrix II.
"""