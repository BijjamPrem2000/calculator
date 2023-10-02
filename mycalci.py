import tkinter as tk


def evaluate_expression():
    try:
        expression = entry.get()
        result = str(eval(expression))
        result_label.config(text="Result: " + result)
    except Exception as e:
        result_label.config(text="Error")

# Create a new tkinter window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget for user input
entry = tk.Entry(window, width=50)
entry.grid(row=0, column=0, columnspan=5)

# Create buttons for numbers and operators
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]

row_num, col_num = 1, 0

for text in button_texts:
    if text == '=':
        tk.Button(window, text=text, command=evaluate_expression).grid(row=row_num, column=col_num, columnspan=2)
        col_num += 1
    else:
        tk.Button(window, text=text, command=lambda t=text: entry.insert(tk.END, t)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=row_num, column=0, columnspan=4)

# Run the tkinter main loop
window.mainloop()