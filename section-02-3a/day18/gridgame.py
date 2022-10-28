
board = []
for row in range(5):
    board.append(['-', '-', '-'])

board[0][2] = 'Y'
print(board)
print()
# Print nicely
for row in range(5):
    for col in len(board[row]):
        print(board[row][col], end=" ")
    print()
