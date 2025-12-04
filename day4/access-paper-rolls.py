#!/usr/bin/python3

grid = []

def display(grid):
    for row in grid:
        print(" ".join(str(x) for x in row))
    print("\n")


def find_accessible_rolls(grid):

    total = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                if row == 0 :
                    if col == 0 or col == len(grid) -1:
                        adjacent_rolls = "@@@@@@"
                    else:
                        # top of grid
                        adjacent_rolls = (
                        grid[row][col-1] + grid[row][col+1]
                        + grid[row +1][col -1] + grid[row +1][col] + grid[row+1][col+1] 
                            )

                elif row == len(grid)-1:
                    # bottom of grid
                    if col == 0 or col == len(grid) -1:
                        adjacent_rolls = "@@@@@@"
                    else:
                        adjacent_rolls = (
                        grid[row -1][col -1] + grid[row -1][col] + grid[row-1][col+1] 
                        + grid[row][col-1] + grid[row][col+1]
                            )

                if col == 0:
                    # leftmost wall
                    if row == 0 or row == len(grid[row]) -1:
                        adjacent_rolls = "@"
                    else:
                        adjacent_rolls = (
                        grid[row -1][col] + grid[row-1][col+1] 
                        + grid[row][col+1]
                        + grid[row +1][col] + grid[row+1][col+1] 
                            )


                elif col == len(grid[row]) -1:
                    # rightmost wall
                    if row == 0 or row == len(grid[row]) -1:
                        adjacent_rolls = "@"
                    else:
                        adjacent_rolls = (
                        grid[row -1][col -1] + grid[row -1][col]
                        + grid[row][col-1] 
                        + grid[row +1][col -1] + grid[row +1][col]
                            )

                if not row == 0 and not row == len(grid) -1 and not col == 0 and not col == len(grid[row]) - 1: 
                    # not on the border
                    adjacent_rolls = (
                    grid[row -1][col -1] + grid[row -1][col] + grid[row-1][col+1] 
                    + grid[row][col-1] + grid[row][col+1]
                    + grid[row +1][col -1] + grid[row +1][col] + grid[row+1][col+1] 
                        )

                num = adjacent_rolls.count("@")
                if num < 4:
                    #print("grid:", row, " ", col, " adjacent_rolls:", adjacent_rolls)
                    grid[row][col] = "."
                    total += 1
    return total

def main():

    with open("../puzzle-inputs/bunch-of-rolls.txt") as f:
        for line in f:
            row = line.rstrip("\n")
            grid.append(list(row))

    #display(grid)
    count = 1
    final_answer = 0
    while count > 0:
        print("test")
        count = find_accessible_rolls(grid)
        print(count)
        final_answer += count

    print(final_answer)



main()
