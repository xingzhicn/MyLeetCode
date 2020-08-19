"""
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。

 

示例 1：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9
示例 2：

输入：grid = [[1,1,0,0]]
输出：1
 

提示：

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] 为 0 或 1
"""

"""
[
[1,1,1],
[1,0,1],
[1,1,1]
]
"""


class Solution(object):
    def is_cube(self, grid, x, y, max_side_length):
        return None
    def find_max_square(self, grid, x, y):
        # 向右遍历寻找最大的边长
        # x1,y 是正方形右上的顶点
        # x,y1 是正方形左下的顶点
        # x1,y1 是正方形右下的顶点
        max_side_length = 0
        for x1 in range(x, len(grid)):
            if grid[x1][y] == 1:
                if x1 - x > max_side_length:
                    max_side_length += 1
                # 判断该边长能否组成正方体
            elif grid[x1][y] == 0:
                self.is_cube(grid, x, y, max_side_length)

        return max_side_length

    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 最大边长
        max_side_length = 0
        # 遍历每个顶点
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    square = self.find_max_square(grid, x, y)
                    if square > max_side_length:
                        max_side_length = square
        return max_side_length ** 2


assert 9 == Solution().largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
