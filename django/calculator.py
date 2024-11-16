import tkinter as tk
from tkinter import messagebox

# Function to update the entry box when buttons are clicked
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the entry box
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.config(bg="#282c34")
root.resizable(False, False)

# Create an entry widget to show the input/output
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief="sunken", justify="right", bg="#f4f4f4")
entry.grid(row=0, column=0, columnspan=4)

# Define button layout and create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Loop to create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, bg="#4caf50", command=button_equal)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, bg="#f44336", command=button_clear)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, bg="#f1f1f1", command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col, padx=10, pady=10)

# Run the main event loop
root.mainloop()
