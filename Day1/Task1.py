N = int(input("Enter a positive odd integer: "))
print(N)

#check that N is valid and prompt user to enter another value for N if it is not

while(N % 2 == 0):
    N = int(input("Try again and be sure to enter a correct int, postive odd number: "))
    print(N)
    
#set and print empty square 0 0 0 x3
square = [[0 for x in range(N)] for y in range(N)]


def magicSquareVerification(N):
    
    #Start with a 1 in the middle column of the first row.
    row = N - 3
    column = N - 2
 
    #starting number to full squares
    counter = 1
    
    #example N = 3, repeat until 3x3, num = 15 
    while counter <= (N * N):
        
        #checks
        
        #if row moves outside to the right up it wraps
        if row == -1 and column == N:
            column = N - 2
            row = 0
        else:
            if column == N:
                column = 0
            if row < 0:
                row = N -1
        
        #if number already there (positive) then set position back to column -2 and row +1
        if square[int(row)][int(column)]:
            column = column - 2
            row = row + 1
            continue
        else:
            square[int(row)][int(column)] = counter
            counter = counter + 1
            # put counter in square [][] and add 1
         #then move the position in the square on top and one right after placing counter number
        column = column + 1
        row = row  -1 
    #print square with counter included end = ' ' to help visualize
    for i in range(0, N):
        for j in range (0, N):
            print((square[i][j]), end= ' ')
            if j == N -1:
                print()
    print('verified')
magicSquareVerification(N)