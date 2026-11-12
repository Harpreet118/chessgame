from backtracking import solve_n_queens

def get_solutions(n):
    if n < 4 or n > 8:
        return []

    return solve_n_queens(n)


if __name__ == "__main__":
    n = 8
    solutions = get_solutions(n)

    print("ChessMind - N Queens Solver")
    print("Board Size:", n)
    print("Total Solutions:", len(solutions))
    print("First Solution:", solutions[0])
