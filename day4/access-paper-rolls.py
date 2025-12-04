#!/usr/bin/python3


def display(grid):
    for row in grid:
        print(" ".join(str(x) for x in row))


def find_accessible_rolls(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                adjacent_rolls = (
                    grid[row -1][col -1] + grid[row -1][col] + grid[row-1][col+1] 
                    + grid[row][col-1] + grid[row][col+1]
                    + grid[row +1][col -1] + grid[row +1][col] + grid[row+1][col+1] 
                        )
                print(adjacent_rolls)







def main():

    grid = []

    with open("../puzzle-inputs/test-day4.txt") as f:
        for line in f:
            row = line.rstrip("\n")
            grid.append(list(row))

    display(grid)
    find_accessible_rolls(grid)


main()
