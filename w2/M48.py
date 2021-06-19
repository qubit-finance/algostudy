"""
48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # rotate를 수식으로 표현해보자.
        # for N X N
        # i,j =>
        # mid = (N-1)/2
        # (0 -1 1 0 )

        # ex : 1 : 0,0 mid = 1
        # 7 -> (-1, -1)
        # x = 0 * -1 + -1 * -1 = 1
        # y = 1 * -1 + 9 = -1
        # 1씩 더하면ㅡ 2,0 0


        def _rotate(i, j):
            return len(matrix) - 1 - j, i

        # 2 : 1 3: 1 4: 2
        for i in range((len(matrix)-1)//2+1):
            for j in range(len(matrix) // 2):
                temp_x = i
                temp_y = j
                temp_val = matrix[j][i]
                if (i, j) == _rotate(i, j):
                    break

                for _ in range(4):
                    temp_x, temp_y = _rotate(temp_x, temp_y)
                    temp = matrix[temp_y][temp_x]
                    matrix[temp_y][temp_x] = temp_val
                    temp_val = temp

        # 좌측 상단 1/4
        # 0 ~ (len(s)-1)//2
        # 1 0 2 0 3 1

        # 돌리고, 혹시 본인이면 break.
if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(matrix)
    print(matrix, "[[7,4,1],[8,5,2],[9,6,3]]")
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(s.rotate(matrix), matrix, "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]")
    matrix = [[1]]
    print(s.rotate(matrix), matrix, "[[1]]")
    matrix = [[1,2],[3,4]]
    print(s.rotate(matrix), matrix, "[[3,1],[4,2]]")


"""

Runtime: 60 ms, faster than 5.43% of Python3 online submissions for Rotate Image.
Memory Usage: 14.1 MB, less than 82.83% of Python3 online submissions for Rotate Image.

"""