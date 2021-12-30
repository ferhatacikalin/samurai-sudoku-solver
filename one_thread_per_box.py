from create_board import *
import threading
import time
import copy
import board_to_file
to_pickle = []
adimsayisi = 0
sqr3_block_list = [(12, 12), (12, 13), (12, 14), (13, 12), (13, 13),
                   (13, 14), (14, 12), (14, 13), (14, 14)]
sqr3_block_list = sqr3_block_list + [(6, 12), (6, 13), (6, 14), (7, 12), (7, 13),
                                     (7, 14), (8, 12), (8, 13), (8, 14), ]
sqr3_block_list = sqr3_block_list + [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7),
                                     (7, 8), (8, 6), (8, 7), (8, 8), ]
sqr3_block_list = sqr3_block_list + [(12, 6), (12, 7), (12, 8), (13, 6), (14, 7),
                                     (13, 8), (14, 6), (14, 7), (14, 8), ]

Board = create_array_board()
print("-----------------------------------------------------------------------------------------------------------")
event4complete_1 = threading.Event()
event4complete_1and3 = threading.Event()
threads = []

def find_empty(bo, sqr):
    bound_row_start, bound_row_end, bound_col_start, bound_col_end = 0, 0, 0, 0
    if sqr == 1:
        bound_row_start = 0
        bound_row_end = 9
        bound_col_start = 0
        bound_col_end = 9
    elif sqr == 2:
        bound_row_start = 0
        bound_row_end = 9
        bound_col_start = 12
        bound_col_end = 21
    elif sqr == 3:
        bound_row_start = 6
        bound_row_end = 15
        bound_col_start = 6
        bound_col_end = 15
    elif sqr == 4:
        bound_row_start = 12
        bound_row_end = 21
        bound_col_start = 0
        bound_col_end = 9
    elif sqr == 5:
        bound_row_start = 12
        bound_row_end = 21
        bound_col_start = 12
        bound_col_end = 21

    for i in range(bound_row_start, bound_row_end):
        for j in range(bound_col_start, bound_col_end):
            if False:
                pass
            else:
                if bo[i][j] == "*":
                    return (i, j)  # row, col

    return None


def valid(bo, num, pos, sqr):
    bound_row_start, bound_row_end, bound_col_start, bound_col_end = 0, 0, 0, 0
    if sqr == 1:
        bound_row_start = 0
        bound_row_end = 9
        bound_col_start = 0
        bound_col_end = 9


    elif sqr == 2:
        bound_row_start = 0
        bound_row_end = 9
        bound_col_start = 12
        bound_col_end = 21

    elif sqr == 3:
        bound_row_start = 6
        bound_row_end = 15
        bound_col_start = 6
        bound_col_end = 15
    elif sqr == 4:
        bound_row_start = 12
        bound_row_end = 21
        bound_col_start = 0
        bound_col_end = 9
    elif sqr == 5:
        bound_row_start = 12
        bound_row_end = 21
        bound_col_start = 12
        bound_col_end = 21
    # check rows in col
    for i in range(bound_col_start, bound_col_end):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column in row
    for i in range(bound_row_start, bound_row_end):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    check_list1 = []
    if sqr == 3 and pos in sqr3_block_list:
        if pos in [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]:
            for i in range(0, 9):
                if bo[pos[0]][i] == num:
                    return False
            for i in range(0, 9):
                if bo[i][pos[1]] == num:
                    return False
        if pos in [(12, 12), (12, 13), (12, 14), (13, 12), (13, 13),
                   (13, 14), (14, 12), (14, 13), (14, 14)]:
            for i in range(12, 21):
                if bo[pos[0]][i] == num:
                    return False
            for i in range(12, 21):
                if bo[i][pos[1]] == num:
                    return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo, sqr):
    find = find_empty(bo, sqr)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):

        if valid(bo, i, (row, col), sqr):

            bo[row][col] = i
            if solve(bo, sqr):
                return True

            bo[row][col] = "*"

    return False


class solverThread(threading.Thread):
    def __init__(self, bo, sqr):
        threading.Thread.__init__(self)
        self.bo = bo
        self.sqr = sqr

    def run(self):

        if self.sqr == 3:
            event4complete_1.wait()
        if self.sqr == 2 or self.sqr == 4 or self.sqr == 5:
            event4complete_1and3.wait()

        find = find_empty(self.bo, self.sqr)

        if not find:
            if self.sqr == 1:
                event4complete_1.set()
            if self.sqr == 3:
                event4complete_1and3.set()

            return True

        else:
            row, col = find

        for i in range(1, 10):

            if valid(self.bo, i, (row, col), self.sqr):

                self.bo[row][col] = i


                global adimsayisi
                adimsayisi=adimsayisi+1
                to_pickle.append(copy.deepcopy([row, col, i]))
                if self.run():
                    return True

                self.bo[row][col] = "*"

        return False


def start():

    start=time.time()
    to_solve = [1, 2, 3, 4, 5]
    for i in to_solve:
        threads.append(solverThread(Board, i))
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    end=time.time()
    board_to_file.board_to_pickle(to_pickle)

    print(adimsayisi)
    print(end-start)
    return {"runtime": end - start, "adimsayisi": adimsayisi}