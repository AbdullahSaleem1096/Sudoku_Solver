import time
class Sudoku_Solver:
    def __init__(self):
        self.board = [
            [3, 0, 0, 0, 0, 0, 0, 1, 5],
            [0, 8, 6, 9, 0, 0, 0, 0, 0],
            [0, 7, 0, 2, 5, 0, 0, 0, 0],
            [0, 1, 5, 0, 0, 6, 3, 4, 9],
            [0, 6, 0, 3, 4, 5, 8, 0, 1],
            [0, 0, 7, 8, 9, 1, 0, 0, 0],
            [6, 5, 8, 0, 0, 0, 1, 0, 2],
            [2, 0, 0, 5, 0, 8, 0, 0, 4],
            [0, 0, 0, 0, 0, 2, 5, 9, 8],
        ]
        self.domain = {}
        self.backtracking_steps = 0

    def update_domain(self, digit, row, col):
        for i in range(9):
            # Update the column entries
            if (i, col) in self.domain and digit in self.domain[(i, col)]:
                self.domain[(i, col)].remove(digit)
            # Update the row entries
            if (row, i) in self.domain and digit in self.domain[(row, i)]:
                self.domain[(row, i)].remove(digit)
        
        # Subgrid calculation
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if (i, j) in self.domain and digit in self.domain[(i, j)]:
                    self.domain[(i, j)].remove(digit)


    def is_safe(self,digit,row,col):
        for i in range(9):
            # checking the column
            if self.board[row][i] == digit:
                return False
            # checking the row
            if self.board[i][col] == digit:
                return False
        # checking the box
        starting_row = (row // 3) * 3
        starting_col = (col // 3) * 3
        for i in range(starting_row,starting_row+3):
            for j in range(starting_col,starting_col+3):
                if self.board[i][j] == digit:
                    return False
        return True
    
    def helper(self, row, col):
        if row == 9:
            return True 
        
        if col == 9:  
            return self.helper(row + 1, 0)
        
        if self.board[row][col] != 0: 
            return self.helper(row, col + 1)
        
        for digit in range(1, 10):
            if self.is_safe(digit, row, col):
                self.board[row][col] = digit
                if self.helper(row, col + 1):
                    return True
                self.board[row][col] = 0 
                self.backtracking_steps += 1

        return False 

    def Sudoku_Solver(self):
        if (self.helper(0,0)):
            return True
        return False

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(len(self.board[i])):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i][j], end=" ")
            print()

    def initialize_domain(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    dom = []
                    for num in range(1, 10):
                        if self.is_safe(num, row, col):
                            dom.append(num)
                    self.domain[(row, col)] = dom
                #else:
                #    self.domain[(row,col)] = [self.board[row][col]]

    def print_domain(self):
        for pos,dom in self.domain.items():
            print(f"Cell {pos}: Domain = {dom}")

    def restore_domains(self, row, col, num):
        """Restore domains after backtracking."""
        for i in range(self.size):
            # Re-add 'num' to the row, column, and subgrid
            if self.board[row][i] == 0:
                self.domain[(row, i)].add(num)
            if self.board[i][col] == 0:
                self.domain[(i, col)].add(num)
        
        # Subgrid calculation
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if self.board[i][j] == 0:
                    self.domain[(i, j)].add(num)

    def find_cell_with_smallest_domain(self):
        """Find the coordinate (row, col) with the smallest domain."""
        smallest_cell = None
        smallest_domain_size = float('inf')  # Initialize with a very large value

        for cell in self.domain:
            domain_size = len(self.domain[cell])
            if domain_size > 0:  # Only consider cells with domain size greater than 0
                if domain_size < smallest_domain_size:
                    smallest_domain_size = domain_size
                    smallest_cell = cell

        return smallest_cell, smallest_domain_size
    
    def fill_board(self):
        cell,size = self.find_cell_with_smallest_domain()
        if size == 0:
            return False
        
        if self.board[row][col] != 0: 
            return self.helper(row, col + 1)
        
        row,col = cell
        for digit in self.domain[cell]:
            self.board[row][col] = digit
            if self.fill_board(row, col + 1):
                return True
            self.board[row][col] = 0 
        return False 

    def fill_board(self):
        # Find cell with smallest domain
        cell, domain_size = self.find_cell_with_smallest_domain()
        
        # If no cell is found, board is complete
        if cell is None:
            return True
            
        # If we find a domain of size 0, this branch is invalid
        if domain_size == 0:
            return False
        
        row, col = cell
        domain_copy = self.domain[cell].copy()  # Make a copy of domain values
        
        # Try each value in the domain of the selected cell
        for digit in domain_copy:
            # Make the move
            self.board[row][col] = digit
            
            # Store current domain state for backtracking
            old_domain = self.domain.copy()
            
            # Update domains and remove this cell from domain dictionary
            self.update_domain(digit, row, col)
            del self.domain[cell]
            
            # Recursively continue filling
            if self.fill_board():
                return True
                
            # If we reach here, we need to backtrack
            self.board[row][col] = 0
            self.domain = old_domain
            self.backtracking_steps += 1
        
        return False

if __name__ == "__main__":
    solver = Sudoku_Solver()
    print("Original Sudoku Board:")
    solver.print_board()
    
    user = int(input("How would you like to solve the Sudoku? (1: Backtracking, 2: Backtracking with Forward Checking): "))
    if user == 1:
        start_time = time.time()
        if solver.Sudoku_Solver():
            print("\nSolved Sudoku Board:")
            solver.print_board()
        else:
            print("\nNo solution exists")
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print(f"\nExecution time: {execution_time:.4f} milli-seconds")
        print(f"Backtracking steps: {solver.backtracking_steps}")
    elif user == 2:
        start_time = time.time()
        solver.initialize_domain()
        if solver.fill_board():
            print("\nSolved Sudoku Board:")
            solver.print_board()
        else:
            print("\nNo solution exists")
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print(f"\nExecution time: {execution_time:.4f} milli-seconds")
        print(f"Backtracking steps: {solver.backtracking_steps}")
    else:
        print("Invalid choice. Exiting...")


"""
    def fill_board(self):
        to_delete = []
        for pos, dom in self.domain.items():
            if len(dom) == 1:
                i, j = pos
                self.board[i][j] = dom[0]
                self.update_domain(dom[0],i,j)
                to_delete.append(pos)
        
        for pos in to_delete:
            del self.domain[pos]
"""