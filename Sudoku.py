# Sudolu board as a list of lists
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]


# printing the board
def print_board(new):
    for i in range(len(new)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - ")
        
        for j in range (len(new[i])):
            if j%3==0 and j!=0:
                print(" | ",end="")
            
            if j==8:
                print(new[i][j])
            else:
                print(str(new[i][j]) + " ",end="")

# function to check an empty cell on the board
def check_empty(new):
    for i in range(len(new)):
        for j in range(len(new)):
            if (new[i][j]==0):
                row=i
                col=j
                return (row,col)

    return False

# function to check if the number already exists in a row
def check_row(new,row,num):

    for i in range(len(new)):
        if new[row][i]==num:
            return True
    
    return False

# function to check if the number already exists in a column
def check_col(new,col,num):
    for i in range(len(new)):
        if new[i][col]==num:
            return True
    
    return False

# # function to check if the number already exists in a 3x3 box
def check_box(new,row,col,num):
    for i in range(3):
        for j in range(3):
            if (new[row][col]==num):
                return True
    return False

# function to check if its valid to place a number in the cell
def valid(new,num,row,col):
    return (not check_row(new,row,num) and (not check_col(new,col,num) and (not check_box(new,row,col,num))))

# the main function to solve the sudoku using backtracking 
def solve(new):
    
    # checking if there is an emmpty cell on the board and assigning the value to a variable 
    find=check_empty(new)

    if not find:
        return True
    else:
        # the check_empty returns (row,col) which is store in find
        # we are using the values in find to assign values to row and column
        row,col=find
    
    for num in range(1,len(new)+1):
        if (valid(new,num,row,col)):
            new[row][col]=num

            if (solve(new)):
                # if it is solved recursively, then return true
                return True
            else:
                # backtrack if it is not valid
                new[row][col]=0

    return False

print("BEFORE SOLVING\n")
print_board(board)
print("\n**************************************************************************\n")
if(solve(board)):
    print("AFTER SOLVING\n")
    print_board(board)
else:
    print("No solution!")