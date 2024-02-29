## Sudoku Board Representation

The Sudoku board is represented as a 9x9 grid using a list of lists in Python. Empty cells are represented by `0`.

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


## Functions

- `print_board(new)`: Prints the Sudoku board in a readable format.
- `check_empty(new)`: Checks if there are any empty cells on the board.
- `check_row(new, row, num)`: Checks if the number `num` already exists in the specified row.
- `check_col(new, col, num)`: Checks if the number `num` already exists in the specified column.
- `check_box(new, row, col, num)`: Checks if the number `num` already exists in the 3x3 box containing the cell at `(row, col)`.
- `valid(new, num, row, col)`: Checks if it's valid to place the number `num` in the cell at `(row, col)`.
- `solve(new)`: Solves the Sudoku puzzle using backtracking.


## How to Run

To run the game, follow these steps:

1. Ensure you have python3 is installed on your machine.
2. Compile and run using `python3 Sudoku.py`.

   
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

