from collections import deque


class Solution:
    LAND = '1'
    WATER = '0'

    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0

        total_rows = len(grid)
        total_columns = len(grid[0])

        visited = set()
        number_of_islands = 0
        for row in range(total_rows):
            for column in range(total_columns):
                grid_location = (row, column)
                if grid_location in visited or self.is_water(grid, grid_location):
                    continue
                if self.is_new_island(grid, grid_location, visited):
                    print(grid_location)
                    number_of_islands += 1
                    visited.add(grid_location)

        return number_of_islands

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

    def is_new_island(self, grid, direction, visited):
        queue = deque([direction])
        new_island = False
        while queue:
            row, column = queue.pop()

            valid_directions = []
            for (dir_row, dir_column) in self.DIRECTIONS:
                new_direction = (row + dir_row, column + dir_column)
                if self.is_valid_direction(grid, new_direction):
                    valid_directions.append(new_direction)

            surrounded_by_water = True
            for valid_direction in valid_directions:
                if self.is_land(grid, valid_direction):
                    surrounded_by_water = False

            if surrounded_by_water:
                return True

            for (dir_row, dir_column) in self.DIRECTIONS:
                new_direction = (row + dir_row, column + dir_column)
                if self.is_valid_direction(grid, new_direction) and new_direction not in visited and self.is_land(grid, new_direction):
                    visited.add(new_direction)
                    queue.appendleft(new_direction)
                    new_island = True

        return new_island
