
import tkinter as tk
from tkinter import ttk

from backtracking import is_safe


class ChessBoard:

    def __init__(self, root):
        self.root = root
        self.root.title("ChessMind - Live Chessboard")
        self.root.geometry("700x760")
        self.root.configure(bg="#100e20")
        self.root.resizable(False, False)

        self.n = 8
        self.board = [-1] * self.n

        self.steps = 0
        self.solutions = 0

        self.running = False
        self.generator = None
        self.current_position = None
        self.after_id = None

        self.create_interface()
        self.draw_board()

    def create_interface(self):

        tk.Label(
            self.root,
            text="♛ CHESSMIND",
            font=("Arial", 27, "bold"),
            fg="white",
            bg="#100e20"
        ).pack(pady=(15, 5))

        tk.Label(
            self.root,
            text="LIVE BACKTRACKING VISUALIZATION",
            font=("Arial", 11, "bold"),
            fg="#c4a8ff",
            bg="#100e20"
        ).pack(pady=5)

        # Board Size Selection
        controls = tk.Frame(
            self.root,
            bg="#100e20"
        )
        controls.pack(pady=15)

        tk.Label(
            controls,
            text="Board Size:",
            fg="white",
            bg="#100e20",
            font=("Arial", 11)
        ).pack(side="left", padx=8)

        self.size = ttk.Combobox(
            controls,
            values=[4, 5, 6, 7, 8],
            width=6,
            state="readonly"
        )

        self.size.set(8)
        self.size.pack(side="left", padx=5)

        self.size.bind(
            "<<ComboboxSelected>>",
            self.change_size
        )

        # Chessboard Canvas
        self.canvas = tk.Canvas(
            self.root,
            width=480,
            height=480,
            bg="#100e20",
            highlightthickness=0
        )

        self.canvas.pack(pady=10)

        # Status
        self.status = tk.Label(
            self.root,
            text="Ready to solve!",
            font=("Arial", 12, "bold"),
            fg="#c4a8ff",
            bg="#100e20"
        )

        self.status.pack(pady=8)

        # Statistics
        stats = tk.Frame(
            self.root,
            bg="#211b38",
            padx=20,
            pady=12
        )

        stats.pack(pady=8)

        self.steps_label = tk.Label(
            stats,
            text="STEPS: 0",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#211b38"
        )

        self.steps_label.pack(side="left", padx=25)

        self.solutions_label = tk.Label(
            stats,
            text="SOLUTIONS: 0",
            font=("Arial", 12, "bold"),
            fg="#c4a8ff",
            bg="#211b38"
        )

        self.solutions_label.pack(side="left", padx=25)

        # Buttons
        buttons = tk.Frame(
            self.root,
            bg="#100e20"
        )

        buttons.pack(pady=15)

        tk.Button(
            buttons,
            text="START",
            command=self.start_animation,
            bg="#7655bd",
            fg="white",
            width=12,
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(side="left", padx=5)

        tk.Button(
            buttons,
            text="PAUSE",
            command=self.pause_animation,
            bg="#51427a",
            fg="white",
            width=12,
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(side="left", padx=5)

        tk.Button(
            buttons,
            text="RESET",
            command=self.reset,
            bg="#39334f",
            fg="white",
            width=12,
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(side="left", padx=5)

        # Animation Speed
        self.speed = tk.Scale(
            self.root,
            from_=50,
            to=1000,
            orient="horizontal",
            label="Animation Speed (milliseconds)",
            bg="#100e20",
            fg="white",
            troughcolor="#7655bd",
            highlightthickness=0,
            length=300
        )

        self.speed.set(300)
        self.speed.pack(pady=5)

        tk.Label(
            self.root,
            text="Purple Highlight = Current Checking Position",
            font=("Arial", 9),
            fg="#aaa4c5",
            bg="#100e20"
        ).pack(pady=5)

    def draw_board(self):

        self.canvas.delete("all")

        square = 60

        for row in range(self.n):
            for col in range(self.n):

                x1 = col * square
                y1 = row * square

                x2 = x1 + square
                y2 = y1 + square

                color = (
                    "#eee4d1"
                    if (row + col) % 2 == 0
                    else "#765b82"
                )

                if self.current_position == (row, col):
                    color = "#b58aff"

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="#29253e",
                    width=1
                )

                # Draw Queen
                if self.board[row] == col:

                    self.canvas.create_text(
                        x1 + 30,
                        y1 + 30,
                        text="♛",
                        font=("DejaVu Sans", 36),
                        fill="#21152e"
                    )

        self.steps_label.config(
            text=f"STEPS: {self.steps}"
        )

        self.solutions_label.config(
            text=f"SOLUTIONS: {self.solutions}"
        )

    def solve(self, row=0):

        if row == self.n:

            self.solutions += 1

            yield "Valid Solution Found!"

            return

        for col in range(self.n):

            self.steps += 1
            self.current_position = (row, col)

            yield f"Checking Row {row + 1}, Column {col + 1}"

            if is_safe(self.board, row, col, self.n):

                self.board[row] = col

                yield f"Queen placed at Row {row + 1}, Column {col + 1}"

                yield from self.solve(row + 1)

                # Backtracking
                self.board[row] = -1

                yield "Backtracking: Removing Queen"

        self.current_position = None

    def animate(self):

        if not self.running or self.generator is None:
            return

        try:

            message = next(self.generator)

            self.status.config(text=message)

            self.draw_board()

            self.after_id = self.root.after(
                self.speed.get(),
                self.animate
            )

        except StopIteration:

            self.running = False
            self.generator = None

            self.status.config(
                text="All Solutions Explored!"
            )

            self.current_position = None
            self.draw_board()

    def start_animation(self):

        if self.running:
            return

        if self.generator is None:

            self.board = [-1] * self.n
            self.steps = 0
            self.solutions = 0

            self.generator = self.solve()

        self.running = True
        self.animate()

    def pause_animation(self):

        self.running = False

        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.status.config(
            text="Animation Paused"
        )

    def reset(self):

        self.running = False

        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.generator = None

        self.board = [-1] * self.n

        self.steps = 0
        self.solutions = 0

        self.current_position = None

        self.status.config(
            text="Ready to solve!"
        )

        self.draw_board()

    def change_size(self, event=None):

        self.reset()

        self.n = int(self.size.get())

        self.canvas.config(
            width=self.n * 60,
            height=self.n * 60
        )

        self.board = [-1] * self.n

        self.draw_board()


if __name__ == "__main__":

    root = tk.Tk()

    app = ChessBoard(root)

    root.mainloop()
