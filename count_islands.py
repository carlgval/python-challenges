# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 08:43:28 2018

 Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
 A 1 represents land and 0 represents water, so an island is a group of 1s
 that are neighboring and their perimiter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1

@author: carlgval
"""


valid_neighbours = [(-1, 0), (1, 0), (-1, -1), (-1, 1),
                    (1, 1), (1, -1), (0, 1), (0, -1)]


def count_islands(matrix):
    visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                visited[i][j] = 1
            elif visited[i][j] == 0:
                count += 1
                matrix, visited = visit(i, j, matrix, visited)
    return count


def visit(i, j, matrix, visited):
    visited[i][j] = 1
    neighbours = [(i+a, j+b) for a, b in valid_neighbours]
    for neighbour in neighbours:
        i_n, j_n = neighbour
        if is_valid(i_n, j_n, len(matrix), len(matrix[0])):
            if visited[i_n][j_n] == 0 and matrix[i_n][j_n] == 1:
                matrix, visited = visit(i_n, j_n, matrix, visited)
    return matrix, visited


def is_valid(i, j, i_lim, j_lim):
    if i >= 0 and i < i_lim and j >= 0 and j < j_lim:
        return True
    return False


if __name__ == '__main__':
    m = [[1, 0, 0, 0, 0],
         [0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 0, 0, 1],
         [1, 1, 0, 0, 1]]

    print(count_islands(m))
