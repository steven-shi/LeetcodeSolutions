'''
https://leetcode.com/problems/island-perimeter/
Island Perimeter
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
  [0,1,0,0],
   [1,1,0,0]]

   Answer: 16
   Explanation: The perimeter is the 16 yellow stripes in the image below:


'''


class Solution(object):
    def getNum(self, row, col):
        if row == -1 or row>= self.maxrow or col==-1 or col>=self.maxcol:
            return None
        return self.grid[row][col]
    
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.maxcol = len(grid[0])
        self.maxrow = len(grid)
        self.grid=grid
        result = 0
        for row, rowNums in enumerate(grid):
            for col, num in enumerate(rowNums):
                if num == 0:
                    continue
                left = self.getNum(row-1, col)
                if left == 0 or left is None:
                    result += 1
                right = self.getNum(row+1, col)
                if right == 0 or right is None:
                    result +=1
                top = self.getNum(row, col-1)
                if top == 0 or top is None:
                    result += 1
                bottom = self.getNum(row, col+1)
                if bottom == 0 or bottom is None:
                    result += 1
                
        return result
                
            
