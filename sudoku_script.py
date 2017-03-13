import sys
import numpy as np
import math

# ----------------------------- Quelques fonctions utilitaires pour le jeu de sudoku ---------------------------------

#convert sudoku config as a str to 2d numpy array
def str_to_grid(grid_str):
    grid = np.array(list(grid_str), dtype=int)
    grid_2d = grid.reshape(9,9)
    return grid_2d

#Verification de conflit sur ligne et colonne
def check_line(num,row,col,grid):
    if row ==0 | col == 0:
        print("rows and column must be between 1 and 9")
        return 0
    for x in range(0,9):
        if num == grid[row][x]:
            print("row not okay")
            return 0
    for y in range(0,9):
        if num == grid[y][col]:
            print("column not okay")
            return 0
    return 1

#Retourne le carre 3x3
def get_square(row,col,grid):
    x_square = math.floor((row) / 3)
    y_square = math.floor((col) / 3)

    sub_grid = grid[3 * x_square: 3 * x_square + 3]
    sub_grid = sub_grid[:, 3 * y_square: 3 * y_square + 3]
    return sub_grid

#Verification de conflit dans un carre 3x3
def check_square(num,row,col,grid):
    if row ==0 | col == 0:
        print("rows and column must be between 1 and 9")
        return 0

    sub_grid = get_square(row,col,grid)

    if num in sub_grid:
        print("error num is in square")
        return 0
    return 1

#Retourne la liste des possibilites pour un case
def eval_possibility(row,col,grid):
    if grid[row][col] != 0 :
        print("ERROR : no possiblities, this cell already contain a value")
        return []

    possible = [1,2,3,4,5,6,7,8,9]
    sub_grid = get_square(row,col,grid).flatten()
    row_val = grid[row].flatten()
    col_val = grid[:,col].flatten()
    all_val = np.concatenate([sub_grid,row_val,col_val])

    for item in all_val:
        if item in possible:
            possible.remove(item)

    return possible

def main (argument):
    grid = str_to_grid("200060000007004086000001300000000040090000000480000710900078000000050002020600501")
    print(grid)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))