
import tkinter as tk
from tkinter import ttk
from time import perf_counter

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from n_queens import get_solutions


class PerformanceAnalyzer:

    def __init__(self, root):
        self.root = root
        self.root.title("ChessMind - Performance Analysis")
        self.root.geometry("950x720")
        self.root.configure(bg="#100e20")

        self.results = []

        self.create_interface()

    def create_interface(self):

        tk.Label(
            self.root,
            text="ALGORITHM PERFORMANCE ANALYSIS",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="#100e20"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="Analyze N-Queens Backtracking Algorithm",
            font=("Arial", 11),
            fg="#c4a8ff",
            bg="#100e20"
        ).pack()

        # Selection Area
        controls = tk.Frame(
            self.root,
            bg="#211b38",
            padx=20,
            pady=15
        )
        controls.pack(pady=20)

        tk.Label(
            controls,
            text="Select Board Size:",
            font=("Arial", 11, "bold"),
            fg="white",
            bg="#211b38"
        ).pack(side="left", padx=10)

        self.size = ttk.Combobox(
            controls,
            values=[4, 5, 6, 7, 8],
            state="readonly",
            width=8
        )

        self.size.set(8)
        self.size.pack(side="left", padx=10)

        tk.Button(
            controls,
            text="RUN ANALYSIS",
            command=self.analyze,
            bg="#7655bd",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8,
            relief="flat"
        ).pack(side="left", padx=10)

        # Result Area
        result_frame = tk.Frame(
            self.root,
            bg="#100e20"
        )
        result_frame.pack(fill="x", padx=25, pady=10)

        self.create_result_card(
            result_frame, "0", "Solutions", 0
        )

        self.create_result_card(
            result_frame, "0 ms", "Execution Time", 1
        )

        self.create_result_card(
            result_frame, "0", "Board Size", 2
        )

        # Status
        self.result_label = tk.Label(
            self.root,
            text="Select a board size and run analysis.",
            font=("Arial", 11, "bold"),
            fg="#c4a8ff",
            bg="#100e20"
        )
        self.result_label.pack(pady=8)

        # Graph
        self.graph_frame = tk.Frame(
            self.root,
            bg="#211b38"
        )
        self.graph_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=15
        )

        # History
        tk.Label(
            self.root,
            text="ANALYSIS HISTORY",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#100e20"
        ).pack(pady=5)

        self.history = tk.Listbox(
            self.root,
            height=4,
            bg="#211b38",
            fg="white",
            font=("Arial", 10),
            relief="flat"
        )

        self.history.pack(
            fill="x",
            padx=25,
            pady=(0, 15)
        )

    def create_result_card(
        self, parent, value, label, column
    ):

        card = tk.Frame(
            parent,
            bg="#211b38",
            width=250,
            height=90
        )

        card.grid(
            row=0,
            column=column,
            padx=8,
            sticky="nsew"
        )

        parent.grid_columnconfigure(
            column,
            weight=1
        )

        card.pack_propagate(False)

        value_label = tk.Label(
            card,
            text=value,
            font=("Arial", 20, "bold"),
            fg="#c4a8ff",
            bg="#211b38"
        )

        value_label.pack(pady=10)

        tk.Label(
            card,
            text=label,
            font=("Arial", 10),
            fg="white",
            bg="#211b38"
        ).pack()

        if not hasattr(self, "result_values"):
            self.result_values = []

        self.result_values.append(value_label)

    def analyze(self):

        n = int(self.size.get())

        self.result_label.config(
            text="Calculating... Please wait."
        )

        self.root.update_idletasks()

        start = perf_counter()

        solutions = get_solutions(n)

        end = perf_counter()

        elapsed = (end - start) * 1000

        total = len(solutions)

        self.results.append(
            (n, total, elapsed)
        )

        # Update Cards
        self.result_values[0].config(
            text=str(total)
        )

        self.result_values[1].config(
            text=f"{elapsed:.4f} ms"
        )

        self.result_values[2].config(
            text=f"{n} x {n}"
        )

        self.result_label.config(
            text=f"Analysis completed successfully for {n} x {n} board."
        )

        self.history.insert(
            "end",
            f"Board: {n}x{n} | Solutions: {total} | Time: {elapsed:.4f} ms"
        )

        self.draw_graph()

    def draw_graph(self):

        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        figure = Figure(
            figsize=(7, 3.2),
            dpi=100
        )

        axis = figure.add_subplot(111)

        sizes = [
            item[0] for item in self.results
        ]

        times = [
            item[2] for item in self.results
        ]

        axis.plot(
            range(1, len(times) + 1),
            times,
            marker="o",
            linewidth=2,
            label="Execution Time"
        )

        axis.set_title(
            "Algorithm Execution Time"
        )

        axis.set_xlabel(
            "Analysis Number"
        )

        axis.set_ylabel(
            "Time (Milliseconds)"
        )

        axis.grid(True)
        axis.legend()

        figure.tight_layout()

        chart = FigureCanvasTkAgg(
            figure,
            master=self.graph_frame
        )

        chart.draw()

        chart.get_tk_widget().pack(
            fill="both",
            expand=True
        )


if __name__ == "__main__":

    root = tk.Tk()

    app = PerformanceAnalyzer(root)

    root.mainloop()
