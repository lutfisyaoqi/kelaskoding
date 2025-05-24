import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 32), width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)

            if self.check_winner(self.player):
                messagebox.showinfo("Game Over", f"Pemain {self.player} menang!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "Seri!")
                self.reset_game()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self, player):
        win_combinations = [
            [0,1,2], [3,4,5], [6,7,8],  # baris
            [0,3,6], [1,4,7], [2,5,8],  # kolom
            [0,4,8], [2,4,6]            # diagonal
        ]
        return any(all(self.board[i] == player for i in combo) for combo in win_combinations)

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
