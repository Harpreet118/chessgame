# ChessMind – Intelligent N-Queens Problem Solver

## Project Overview
ChessMind is a Python-based graphical application that solves the N-Queens Problem using the Backtracking Algorithm. It provides an interactive chessboard visualization and demonstrates important Design and Analysis of Algorithms (DAA) concepts.

## Project Objectives
- Understand the N-Queens Problem.
- Implement the Backtracking Algorithm.
- Visualize queen placement on a chessboard.
- Demonstrate recursion and backtracking.
- Analyze execution time for different board sizes.

## Technologies Used
- Python
- Tkinter – Graphical User Interface
- Matplotlib – Performance Graphs
- VS Code – Development Environment

## Main Features
1. **Chessboard Visualization:** Shows queen placement step by step.
2. **Algorithm Analysis:** Measures execution time and displays performance graphs.
3. **DAA Theory:** Explains recursion, backtracking, and complexity.
4. **About Project:** Displays project information.

## Algorithm Used: Backtracking
The Backtracking algorithm places one queen in each row. Before placing a queen, it checks whether the position is safe.

A position is safe when:
- No other queen exists in the same column.
- No other queen exists on the left diagonal.
- No other queen exists on the right diagonal.

If a safe position is found, the algorithm places the queen and moves to the next row. If no safe position is available, it removes the previously placed queen and tries another position.

## Complexity Analysis
- Time Complexity: Factorial-scale search; commonly described as O(N!) for the optimized N-Queens search.
- Auxiliary Space Complexity: O(N) for the board and recursive call stack, excluding stored solutions.

Note: The current implementation checks previously placed queens while testing a position, which adds up to O(N) work per safety check.

## Supported Board Sizes

| Board Size | Total Solutions |
|---|---:|
| 4 × 4 | 2 |
| 5 × 5 | 10 |
| 6 × 6 | 4 |
| 7 × 7 | 40 |
| 8 × 8 | 92 |

## Project Structure
- main.py – Main application file
- dashboard.py – Main dashboard
- chessboard.py – Chessboard visualization
- backtracking.py – Backtracking algorithm
- n_queens.py – N-Queens solver
- algorithm_analysis.py – Performance analysis
- theory.py – DAA theory
- about.py – Project information

## Installation and Execution

Install Matplotlib:

```bash
python -m pip install matplotlib
```

Run the application:

```bash
python main.py
```

## Developed By
**Harpreet Kaur**

Chandigarh University

**Project:** Design and Analysis of Algorithms (DAA) Mini Project