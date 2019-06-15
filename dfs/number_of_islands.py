from collections import deque
from typing import List


class Solution:
    LAND = '1'
    WATER = '0'

    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0

        visited = set()
        number_of_islands = 0

        total_rows = len(grid)
        total_columns = len(grid[0])

        for row in range(total_rows):
            for column in range(total_columns):
                grid_location = (row, column)
                if grid_location in visited or self.is_water(grid, grid_location):
                    continue
                else:
                    self.dfs(grid_location, visited, grid)
                    number_of_islands += 1
        print(visited)
        return number_of_islands

    def dfs(self, grid_location, visited, grid):
        if grid_location in visited or self.is_water(grid, grid_location):
            return

        visited.add(grid_location)
        valid_directions = self.get_valid_locations(grid_location, grid)

        if valid_directions == []:
            return

        if self.is_sourrounded_by_water(grid, valid_directions):
            return

        for valid_direction in valid_directions:
            self.dfs(valid_direction, visited, grid)

    def is_sourrounded_by_water(self, grid, valid_directions):
        surrounded_by_water = True
        for valid_direction in valid_directions:
            if self.is_land(grid, valid_direction):
                surrounded_by_water = False
        return surrounded_by_water

    def get_valid_locations(self, grid_location, grid):
        row, column = grid_location
        valid_directions = []
        for dir_row, dir_column in self.DIRECTIONS:
            new_direction = (row + dir_row, column + dir_column)
            if self.is_valid_direction(grid, new_direction):
                valid_directions.append(new_direction)
        return valid_directions

    def is_land(self, grid, grid_location):
        row, column = grid_location
        return grid[row][column] == self.LAND

    def is_water(self, grid, grid_location):
        row, column = grid_location
        return grid[row][column] == self.WATER

    def is_valid_direction(self, grid, direction):
        row, column = direction
        total_rows = len(grid)
        total_columns = len(grid[0])
        return row >= 0 and column >= 0 and row <= total_rows - 1 and column <= total_columns - 1


input = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]

solution = Solution()
print(solution.numIslands(input))
