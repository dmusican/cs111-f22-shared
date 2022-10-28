
board = []
for i in range(2):
    board.append(['-', '-', '-'])

board[1][2] = 'Y'

#print(board)
# Print this out in a much prettier way
#for i in range(len(board)):
#    print(board[i])
# Print this out in a much MORE prettier way
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=" ")
    print()

print(board)
