Sudoku_Solver

🧩 Sudoku Solver in Python

This is a Sudoku puzzle solver implemented in Python using two approaches:

1. Simple Backtracking
2. Backtracking with Forward Checking (using Domains & MRV heuristic)

---

📌 Features

- Solves a partially-filled 9x9 Sudoku board.
- Two solving strategies:
  - Classic Backtracking (brute-force DFS).
  - Forward Checking with dynamic domain tracking (more efficient).
- Displays number of backtracking steps and execution time.
- Pretty-printed Sudoku board for easy visualization.

---

🧠 Algorithms Used

1. Backtracking
- Classic depth-first search.
- Places digits and checks for safety recursively.
- Backtracks when no safe value is found.

2. Forward Checking with MRV (Minimum Remaining Values)
- Initializes domains of valid values per cell.
- Always chooses the cell with the smallest domain (heuristic).
- Updates domains as digits are placed (Forward Checking).
- Backtracks when any cell is left with an empty domain.

---

🧪 Sample Input Board

The default board is hardcoded:

