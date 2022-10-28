
board = []
for i in range(5):
    board.append(['-', '-', '-'])

board[1][2] = 'Y'

#print(board)
# Print this out in a much prettier way
for i in range(len(board)):
    print(board[i])
