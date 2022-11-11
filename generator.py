import random

import numpy as np


def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validateGrid(grid, row, col, i):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0
    return False


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def printGrid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()


def validateGrid(grid, row, col, num):

    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    block_x = col//3
    block_y = row//3
    for i in range(block_y*3, block_y*3 + 3):
        for j in range(block_x*3, block_x*3 + 3):
            if grid[i][j] == num and (i, j) != (row, col):
                return False

    return True


def getNum(grid):
    row = random.randrange(9)
    column = random.randrange(9)
    num = random.randrange(1, 10)
    same = 0

    if validateGrid(grid, row, column, num):
        if grid[row][column] == 0:
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == num:
                        same += 1
            if same < 9:
                grid[row][column] = num
                return
                # print(grid[row])
                # print(grid[row][column])
        else:
            getNum(grid)
    else:
        getNum(grid)


def createGrid():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    xy_00 = random.randrange(10)
    if xy_00 < 8:
        num = random.randrange(3, 10)
        grid[0][0] = num
    for i in range(5):
        getNum(grid)

    return grid


def deleteValue(grid):
    row = random.randrange(9)
    col = random.randrange(9)
    if grid[row][col] != 0:
        grid[row][col] = 0
    else:
        deleteValue(grid)


def getGrid():
    grid = createGrid()

    if solve(grid):
        for i in range(43):
            deleteValue(grid)
        return grid
    else:
        getGrid()
