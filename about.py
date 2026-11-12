
import tkinter as tk


class AboutProject:
    def __init__(self, root):
        self.root = root
        self.root.title("ChessMind - About Project")
        self.root.geometry("800x650")
        self.root.configure(bg="#171526")

        self.create_interface()

    def create_interface(self):
        tk.Label(
            self.root,
            text="♛ ABOUT CHESSMIND",
            font=("Arial", 25, "bold"),
            fg="white",
            bg="#171526"
        ).pack(pady=20)

        content = tk.Frame(
            self.root,
            bg="#29253e",
            padx=25,
            pady=20
        )
        content.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=15
        )

        sections = [
            (
                "Project Introduction",
                "ChessMind is an Intelligent N-Queens Problem Solver. "
                "It uses the Backtracking algorithm to find valid "
                "arrangements of queens on a chessboard."
            ),
            (
                "Project Objectives",
                "1. Understand the Backtracking algorithm.\n"
                "2. Apply recursion to solve a problem.\n"
                "3. Visualize queen placement on a chessboard.\n"
                "4. Analyze algorithm performance."
            ),
            (
                "Technologies Used",
                "Programming Language: Python\n"
                "GUI Framework: Tkinter\n"
                "Visualization: Matplotlib\n"
                "Algorithm: Backtracking and Recursion"
            ),
            (
                "Algorithm Details",
                "Problem: N-Queens Problem\n"
                "Approach: Backtracking\n"
                "Search Complexity: Factorial-scale, commonly O(N!)\n"
                "Auxiliary Space: O(N), excluding stored solutions"
            ),
            (
                "Project Information",
                "Project Name: ChessMind\n"
                "Project Type: DAA Mini Project\n"
                "Developed By: Harpreet Kaur\n"
                "University: Chandigarh University"
            )
        ]

        for heading, description in sections:
            tk.Label(
                content,
                text=heading,
                font=("Arial", 14, "bold"),
                fg="#c4a8ff",
                bg="#29253e",
                anchor="w"
            ).pack(fill="x", pady=(10, 4))

            tk.Label(
                content,
                text=description,
                font=("Arial", 10),
                fg="white",
                bg="#29253e",
                justify="left",
                anchor="w",
                wraplength=680
            ).pack(fill="x", pady=3)


if __name__ == "__main__":
    root = tk.Tk()
    app = AboutProject(root)
    root.mainloop()
