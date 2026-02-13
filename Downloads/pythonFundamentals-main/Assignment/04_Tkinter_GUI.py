import tkinter as tk
from tkinter import messagebox

board = [""] * 9
current_player = "X"
game_over = False

def check_winner():
    win_combinations = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]
    
    for combo in win_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    return None

#for status update
def update_status():
    if game_over:
        status_label.config(text="Game Over!", fg="red", font=("Arial", 16, "bold"))
    else:
        status_label.config(text=f"{current_player}'s Turn", fg="blue", font=("Arial", 16, "bold"))

def on_click(index):
    global current_player, game_over
    
    if game_over or board[index] != '':
        return
    
    board[index] == ""
    board[index] = current_player
    buttons[index]["text"] = current_player
    buttons[index].config(state='disabled')
        
    winner = check_winner()
    if winner:
        game_over = True
        status_label.config(text=f'{winner} Wins!', fg='green', font=('Arial"', 16, 'bold'))
        messagebox.showinfo("Game Over", f"{winner} wins!")
    elif "" not in board:
        status_label.config(text=f'Draw!', fg='orange', font=('Arial', 16, 'bold'))
        messagebox.showinfo("Game Over", "Draw!")
    else:
        current_player = "O" if current_player == "X" else "X"
        update_status()

def reset_game():
    global board, game_over, current_player
    board = [''] * 9
    current_player = 'X'
    game_over = False

    for button in buttons:
        button['text'] = ''
        button.confif(state='normal')

    update_status()

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []


for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)


#status label
status_label = tk.Label(root, text="X's Turn", fg="blue", font=("Arial", 16, "bold"))
status_label.grid(row=0, column=0, columnspan=3, pady=10)

root.mainloop()
