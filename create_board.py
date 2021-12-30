def read_txt():
    list_board = []
    text_file = open("Board.txt", "r")
    for line in text_file:
        list_board.append(line.strip())
    return list_board


def create_array_board():
    list = read_txt()
    array_board = [[-1 for x in range(21)] for y in range(21)]  # 1-6
    for i in range(len(list)):
        for j in range(len(list[i])):
            if (i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5) and (
                    j == 9 or j == 10 or j == 11 or j == 12 or j == 13 or j == 14 or j == 15 or j == 16 or j == 17):
                if list[i][j] == "*":
                    array_board[i][j + 3] = "*"
                else:
                    array_board[i][j + 3] = int(list[i][j])
            elif i == 9 or i == 10 or i == 11:
                if list[i][j]=="*":
                    array_board[i][j + 6] = "*"
                else:
                    array_board[i][j + 6] = int(list[i][j])
            elif (i == 15 or i == 16 or i == 17 or i == 18 or i == 19 or i == 20) and (
                    j == 9 or j == 10 or j == 11 or j == 12 or j == 13 or j == 14 or j == 15 or j == 16 or j == 17):
                if list[i][j]=="*":
                    array_board[i][j + 3] = "*"
                else:
                    array_board[i][j + 3] = int(list[i][j])

            else:
                if list[i][j]=="*":
                    array_board[i][j] = "*"
                else:
                    array_board[i][j] = int(list[i][j])

    return array_board


if __name__ == "__main__":
    create_array_board()
