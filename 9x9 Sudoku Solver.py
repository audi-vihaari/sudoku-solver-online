Unsolved_sudoku = [[5, 6, 0, 0, 0, 3, 0, 0, 0],
                   [1, 0, 0, 2, 5, 4, 0, 8, 0],
                   [0, 4, 2, 6, 8, 0, 9, 0, 0],
                   [0, 5, 0, 0, 2, 0, 0, 0, 9],
                   [0, 7, 3, 8, 0, 0, 0, 5, 6],
                   [9, 2, 6, 3, 4, 0, 0, 0, 1],
                   [2, 0, 9, 0, 0, 8, 7, 0, 0],
                   [0, 3, 4, 0, 6, 0, 0, 0, 0],
                   [6, 0, 0, 4, 0, 0, 1, 0, 2]]

prob = Unsolved_sudoku
s = prob
t = False


def print_sudoku(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-----------------------------")
        for j in range(8):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(bo[i][j], " ", end="")
        print(bo[i][8])
    return


def check(bo, i, j, k):
    for h in range(9):
        if bo[i][h] == k:
            return False
        if bo[h][j] == k:
            return False
    a = (i // 3)*3
    b = (j // 3)*3
    for x in range(3):
        for y in range(3):
            if bo[a+x][b+y] == k:
                return False
    return True


def solve():
    global prob, s, t
    for i in range(9):
        for j in range(9):
            if prob[i][j] == 0:
                for k in range(1,10):
                    if check(prob, i, j, k):
                        prob[i][j] = k
                        solve()
                        if t:
                            return
                        prob[i][j] = 0
                return
            if i == 8 and j == 8 and prob[8][8] != 0:
                t = True
    return


print("Unsolved Sudoku:")
print_sudoku(prob)
print("=============================")
print("Solution:")
solve()
print_sudoku(prob)
