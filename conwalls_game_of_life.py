# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 08:20:34 2018

 This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of
square cells. Each cell is either dead or alive, and at each tick, the
following rules apply:

    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or
diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a
starting list of live cell coordinates and the number of steps it should run
for. Once initialized, it should print out the board state at each step. Since
it's an infinite board, print out only the relevant coordinates, i.e. from the
top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot
(.).
@author: carlgval
"""


import numpy as np
from copy import deepcopy


def game_of_life(list_of_cells, steps):
    cols, rows = zip(*list_of_cells)
    grid = [[0 for i in range(max(cols))] for j in range(max(rows))]
    for j, i in list_of_cells:
        grid[i-1][j-1] = 1
    plot_grid(grid)
    for s in range(steps):
        grid = step(grid)


def plot_grid(grid):
    g = np.array(grid)
    if any([any(row) for row in grid]):
        starting_col = int(np.argwhere(np.sum(g, axis=0))[0])
        ending_col = int(np.argwhere(np.sum(g, axis=0))[-1]) + 1
        starting_row = int(np.argwhere(np.sum(g, axis=1))[0])
        ending_row = int(np.argwhere(np.sum(g, axis=1))[-1]) + 1

        for row in grid[starting_row:ending_row]:
            s = [str(r) for r in row[starting_col:ending_col]]
            print(' '.join(s).replace('0', '.').replace('1', '*'))
        print('')


def step(grid):
    if any(grid[0]):
        grid.insert(0, [0 for i in range(len(grid[0]))])
    if any(grid[-1]):
        grid.append([0 for i in range(len(grid[0]))])
    if any([row[0] for row in grid]):
        for row in grid:
            row.insert(0, 0)
    if any([row[-1] for row in grid]):
        for row in grid:
            row.append(0)
    p_grid = deepcopy(grid)
    for i, row in enumerate(p_grid[1:len(p_grid)]):
        for j, piece in enumerate(p_grid[i][1:len(p_grid[0])]):
            neighbours = 0
            neighbours += sum(p_grid[(i-1)][(j-1):(j+2)])
            neighbours += p_grid[(i)][(j-1)] + p_grid[(i)][(j+1)]
            neighbours += sum(p_grid[(i+1)][(j-1):(j+2)])
            if neighbours < 2:
                grid[i][j] = 0
            elif neighbours == 3:
                grid[i][j] = 1
            elif neighbours > 3:
                grid[i][j] = 0

    plot_grid(grid)
    return grid

if __name__ == '__main__':
    cells = [[2, 3],
             [3, 3],
             [1, 4],
             [2, 4],
             [3, 4],
             [3, 5],
             [4, 5],
             [5, 5],
             [6, 6],
             [4, 6],
             [3, 7]]
    game_of_life(cells, 5)
