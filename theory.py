
import tkinter as tk
from tkinter import ttk


class AlgorithmTheory:
    def __init__(self, root):
        self.root = root
        self.root.title("ChessMind - DAA Theory")
        self.root.geometry("800x650")
        self.root.configure(bg="#171526")

        self.create_interface()

    def create_interface(self):
        tk.Label(
            self.root,
            text="CHESSMIND - DAA THEORY",
            font=("Arial", 23, "bold"),
            fg="white",
            bg="#171526"
        ).pack(pady=20)

        notebook = ttk.Notebook(self.root)
        notebook.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        topics = [
            (
                "N-Queens",
                "The N-Queens problem places N queens on an N x N "
                "chessboard so that no two queens attack each other.\n\n"
                "Rules:\n"
                "1. No two queens share a row.\n"
                "2. No two queens share a column.\n"
                "3. No two queens share a diagonal."
            ),
            (
                "Backtracking",
                "Backtracking is an algorithmic technique that builds "
                "a solution step by step.\n\n"
                "If a choice cannot lead to a valid solution, the "
                "algorithm removes that choice and tries another.\n\n"
                "ChessMind uses backtracking to find valid queen positions."
            ),
            (
                "Recursion",
                "Recursion is a technique in which a function calls itself.\n\n"
                "In ChessMind, each recursive call attempts to place "
                "a queen in the next row.\n\n"
                "The base case is reached when all N queens are placed."
            ),
            (
                "Time Complexity",
                "The N-Queens problem has a factorial-scale search space.\n\n"
                "A commonly stated upper bound for backtracking is O(N!).\n\n"
                "In this implementation, safety checking also scans "
                "previous rows, so each check can take O(N) time."
            ),
            (
                "Space Complexity",
                "The board and recursion stack require O(N) "
                "auxiliary space.\n\n"
                "If all valid solutions are stored, additional memory "
                "is needed for the solution list."
            )
        ]

        for title, content in topics:
            frame = tk.Frame(
                notebook,
                bg="#29253e"
            )

            notebook.add(frame, text=title)

            tk.Label(
                frame,
                text=title,
                font=("Arial", 20, "bold"),
                fg="#c4a8ff",
                bg="#29253e"
            ).pack(pady=25)

            text = tk.Text(
                frame,
                wrap="word",
                font=("Arial", 12),
                bg="#29253e",
                fg="white",
                relief="flat",
                padx=25,
                pady=20
            )

            text.pack(
                fill="both",
                expand=True
            )

            text.insert("1.0", content)
            text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmTheory(root)
    root.mainloop()
