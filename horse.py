def to_board(matrix):
    a = len(matrix)
    b = len(matrix[0])
    output = ""
    for i in range(a):
        output += ("{:<3} " * b).format(*matrix[i]) + "\n"
    return output.rstrip()


steps = [[2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]  # Ходы коня


def allow_moves(x, y):
    possible = []
    for step in steps:
        if (0 <= x + step[0] < N) and (0 <= y + step[1] < M) and (board[y + step[1]][x + step[0]]) == 0:
            possible.append(step)
    return possible


def solution():
    x = X - 1
    y = Y - 1
    for i in range(1, M * N + 1):
        board[y][x] = i
        next_step = []
        min = 9
        for move in allow_moves(x, y):
            count = len(allow_moves(x + move[0], y + move[1]))
            if count < min and (count != 0 or i == N * M - 1):
                min = count
                next_step = move
        if len(next_step) == 0:
            break
        x += next_step[0]
        y += next_step[1]
    if i != M * N:
        print("Маршрут не существует")


file = open("input.txt", "r")
read = file.read().split()
M, N = int(read[0]), int(read[1])
X, Y = int(read[2]), int(read[3])
file.close()

board = [[0 for j in range(N)] for i in range(M)]
solution()
file = open("result.txt", 'w')
file.write(to_board(board))
file.close()
