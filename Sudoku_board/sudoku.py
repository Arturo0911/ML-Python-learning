#!/usr/bin/python3


sudoku = [[0,0,0,4,5,6,7,8,9],[1,0,0,3,2,6,7,8,5],[0,0,0,9,1,6,7,8,0],
          [0,0,0,9,0,6,7,8,2],[0,0,0,4,5,6,7,8,9],[0,0,0,4,5,6,7,8,9],
          [0,0,0,4,5,6,7,8,9],[0,0,0,4,5,6,7,8,9],[0,0,0,4,5,6,7,8,9]]




def print_board(m):

    if m is None:
        print("No solutions!")
        return

    if m == []:

        print("Empty matrix!")

    line = "-"*25
    num_rows = len(m)
    num_cols = len(m[0])

    for x in range(num_rows):

        if x % 3 == 0:
            print(line)

        row_to_print = ""

        for y in range(num_cols):

            if y % 3 == 0:
                row_to_print += "| "

            value = str(m[x][y]) if m[x][y] > 0 else " "
            row_to_print += value + " "
        row_to_print += "|"
        print(row_to_print)
    print(line)
if __name__ == '__main__':


    print_board(sudoku)