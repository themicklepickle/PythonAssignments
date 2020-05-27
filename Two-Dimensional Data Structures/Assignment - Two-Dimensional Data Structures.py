# Assignment - Two-Dimensional Data Structures
# Michael Xu
# May 22, 2020


# Q1 - [2] What is meant by a ‘two-dimensional list’? Give an example of how to create one.
"""
A two-dimensional list is a list that contains lists. It is referred to as being 2D
because the data structure can displayed in a way that resembles a 2D grid/matrix.
Here is an example of how to create one:
matrix = [[0 for col in range(4)] for row in range(3)]
which creates the 2D list:
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
displayed as a grid/matrix:
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
"""


# Q2 - [1] Write a code snippet that asks the user for two numbers, r and c, and generates a 2 dimensional r
# by c list where the element in position i, j is a space (‘ ’). Use list comprehension.
def Q2():
    r = int(input("Please enter the number of rows: "))
    c = int(input("Please enter the number of columns: "))
    matrix = [[" " for col in range(c)] for row in range(r)]
    print(matrix)
# uncomment line below to run code snippet:
# Q2()


# Q3 - [2] Given a list of lists (say x), use list comprehension to create the flattened equivalent of x.
# e.g. [[1, 2], [3, 4]] → [1, 2, 3, 4]
def flatten(x):
    return [col for row in x for col in row]
# uncomment lines below to run code snippet:
# x = [[1, 2], [3, 4]]
# print(flatten(x))


# Q4 - [3] Write a function out of bounds that takes a 2D list and a pair of int variables representing
# the row and column, and then decides whether the element indicated by the int variables are inside
# the list (i.e. are they valid indices).
def is_valid(matrix, row, col):
    if row < len(matrix) and col < len(matrix[row]):
        return True
    return False


# Programs
# Q1 - [10] This program will have you simulate a snail crawling around the bottom of a (rectangular) box
# leaving a trail of slime. The snail should be represented by the ‘@’ character, initially at the top left
# corner, and its slime should be represented by ‘_’. You should first ask the user for the dimensions
# (length and height) of the box, and then allow them to enter ‘a’ to move the snail left, ‘d’ to move right,
# ‘w’ to move up, and ‘s’ to move down. The character ‘q’ should exit the program. The trail of slime
# showing where the snail has been should be displayed at each step. However, the snail should not be
# able to move past the edge of the box! e.g.
def print_grid(grid):
    print("\n" + "—" * ((len(grid[0]) + 2) * 3 - 2) + "\n")
    print("*  " * (len(grid[0]) + 2))
    for row in grid:
        print("*  ", "  ".join(row), "  *", sep="")
    print("*  " * (len(grid[0]) + 2))


def valid(grid, row, col):
    if row < 0 or col < 0:
        return False
    if row < len(grid) and col < len(grid[row]):
        return True
    return False


def move(grid, location, axis, change):
    col, row = location
    if axis == "x":
        new_location = (col + change, row)
    if axis == "y":
        new_location = (col, row + change)
    new_col, new_row = new_location
    if valid(grid, new_row, new_col):
        grid[row][col] = "_"
        grid[new_row][new_col] = "@"
        return grid, new_location
    else:
        print("Can't move there!")
    return grid, location


def snail():
    cols = int(input("Please enter the length of the grid: "))
    rows = int(input("Please enter the height of the grid: "))
    grid = [[" " for col in range(cols)] for row in range(rows)]
    grid[0][0] = "@"
    coordinates = (0, 0)
    direction = None
    while direction != "q":
        print_grid(grid)
        direction = input("Direction: ")
        if direction == "a":  # left
            grid, coordinates = move(grid, coordinates, "x", -1)
        if direction == "d":  # right
            grid, coordinates = move(grid, coordinates, "x", 1)
        if direction == "w":  # up
            grid, coordinates = move(grid, coordinates, "y", -1)
        if direction == "s":  # down
            grid, coordinates = move(grid, coordinates, "y", 1)

# uncomment line below to run code snippet:
# snail()
