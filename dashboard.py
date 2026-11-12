
import tkinter as tk

from chessboard import ChessBoard
from algorithm_analysis import PerformanceAnalyzer
from theory import AlgorithmTheory
from about import AboutProject


class Dashboard:

    def __init__(self, root):
        self.root = root

        self.root.title("ChessMind | Intelligent N-Queens Solver")
        self.root.geometry("1050x780")
        self.root.minsize(950, 750)
        self.root.configure(bg="#100e20")

        self.create_dashboard()

    def create_dashboard(self):

        # Main Container
        main = tk.Frame(
            self.root,
            bg="#100e20"
        )
        main.pack(fill="both", expand=True, padx=30, pady=15)

        # Header
        header = tk.Frame(main, bg="#100e20")
        header.pack(fill="x", pady=(5, 15))

        tk.Label(
            header,
            text="♛",
            font=("DejaVu Sans", 42),
            fg="#b58aff",
            bg="#100e20"
        ).pack(side="left", padx=(5, 15))

        title_frame = tk.Frame(header, bg="#100e20")
        title_frame.pack(side="left")

        tk.Label(
            title_frame,
            text="CHESSMIND",
            font=("Arial", 29, "bold"),
            fg="white",
            bg="#100e20"
        ).pack(anchor="w")

        tk.Label(
            title_frame,
            text="INTELLIGENT N-QUEENS PROBLEM SOLVER",
            font=("Arial", 10, "bold"),
            fg="#b58aff",
            bg="#100e20"
        ).pack(anchor="w", pady=3)

        tk.Label(
            main,
            text="Design and Analysis of Algorithms  |  Mini Project",
            font=("Arial", 11),
            fg="#aaa4c5",
            bg="#100e20"
        ).pack(anchor="w", pady=(0, 15))

        # Welcome Section
        welcome = tk.Frame(
            main,
            bg="#211b38",
            padx=15,
            pady=12
        )
        welcome.pack(fill="x", pady=5)

        tk.Label(
            welcome,
            text="Welcome to ChessMind",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#211b38"
        ).pack(anchor="w")

        tk.Label(
            welcome,
            text="Explore the power of Backtracking and Recursion.",
            font=("Arial", 11),
            fg="#c5b9df",
            bg="#211b38"
        ).pack(anchor="w", pady=(7, 0))

        # Statistics Heading
        tk.Label(
            main,
            text="PROJECT OVERVIEW",
            font=("Arial", 13, "bold"),
            fg="#c4a8ff",
            bg="#100e20"
        ).pack(anchor="w", pady=(18, 10))

        # Statistics Cards
        stats = tk.Frame(main, bg="#100e20")
        stats.pack(fill="x")

        stats.grid_columnconfigure(0, weight=1)
        stats.grid_columnconfigure(1, weight=1)
        stats.grid_columnconfigure(2, weight=1)

        self.create_stat(stats, "92", "8-Queens Solutions", 0)
        self.create_stat(stats, "O(N!)", "Search Complexity", 1)
        self.create_stat(stats, "O(N)", "Auxiliary Space", 2)

        # Modules Heading
        tk.Label(
            main,
            text="EXPLORE PROJECT MODULES",
            font=("Arial", 13, "bold"),
            fg="#c4a8ff",
            bg="#100e20"
        ).pack(anchor="w", pady=(20, 10))

        # Module Container
        modules = tk.Frame(main, bg="#100e20")
        modules.pack(fill="both", expand=True)

        modules.grid_columnconfigure(0, weight=1)
        modules.grid_columnconfigure(1, weight=1)
        modules.grid_rowconfigure(0, weight=1)
        modules.grid_rowconfigure(1, weight=1)

        # Module 1
        self.create_module(
            modules,
            "♟  Chessboard Visualization",
            "Watch queens being placed using the Backtracking algorithm.",
            self.open_chessboard,
            0, 0
        )

        # Module 2
        self.create_module(
            modules,
            "◈  Algorithm Analysis",
            "Analyze execution time and performance using graphs.",
            self.open_analysis,
            0, 1
        )

        # Module 3
        self.create_module(
            modules,
            "⌘  DAA Theory",
            "Learn recursion, backtracking and time and space complexity.",
            self.open_theory,
            1, 0
        )

        # Module 4
        self.create_module(
            modules,
            "ⓘ  About Project",
            "Explore project objectives, technologies and information.",
            self.open_about,
            1, 1
        )

        # Footer
        footer = tk.Frame(main, bg="#100e20")
        footer.pack(fill="x", pady=(10, 0))

        tk.Label(
            footer,
            text="CHESSMIND  •  PYTHON + TKINTER",
            font=("Arial", 9, "bold"),
            fg="#8e83aa",
            bg="#100e20"
        ).pack()

        tk.Label(
            footer,
            text="Developed by Harpreet Kaur",
            font=("Arial", 9),
            fg="#aaa4c5",
            bg="#100e20"
        ).pack(pady=3)

    # Create Statistics Card
    def create_stat(self, parent, value, label, column):

        card = tk.Frame(
            parent,
            bg="#211b38",
            height=90
        )

        card.grid(
            row=0,
            column=column,
            padx=7,
            sticky="nsew"
        )

        card.grid_propagate(False)

        tk.Label(
            card,
            text=value,
            font=("Arial", 24, "bold"),
            fg="#c4a8ff",
            bg="#211b38"
        ).pack(pady=(10, 3))

        tk.Label(
            card,
            text=label,
            font=("Arial", 10),
            fg="white",
            bg="#211b38"
        ).pack()

    # Create Module Card
    def create_module(
        self, parent, title, description,
        command, row, column
    ):

        card = tk.Frame(
            parent,
            bg="#211b38",
            padx=15,
            pady=12
        )

        card.grid(
            row=row,
            column=column,
            padx=7,
            pady=7,
            sticky="nsew"
        )

        tk.Label(
            card,
            text=title,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#211b38"
        ).pack(anchor="w")

        tk.Label(
            card,
            text=description,
            font=("Arial", 9),
            fg="#aaa4c5",
            bg="#211b38",
            wraplength=350,
            justify="left"
        ).pack(anchor="w", pady=7)

        tk.Button(
            card,
            text="OPEN MODULE  →",
            command=command,
            bg="#7655bd",
            fg="white",
            activebackground="#9672df",
            activeforeground="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=7
        ).pack(anchor="w")

    # Open Chessboard
    def open_chessboard(self):
        window = tk.Toplevel(self.root)
        ChessBoard(window)

    # Open Algorithm Analysis
    def open_analysis(self):
        window = tk.Toplevel(self.root)
        PerformanceAnalyzer(window)

    # Open DAA Theory
    def open_theory(self):
        window = tk.Toplevel(self.root)
        AlgorithmTheory(window)

    # Open About Project
    def open_about(self):
        window = tk.Toplevel(self.root)
        AboutProject(window)


if __name__ == "__main__":

    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
