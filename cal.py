import tkinter as tk

def add(a, b):
    return a + b

def subtract(a, b):
    return b - a

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: cannot divide by zero!"
    return a / b

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    oper = operator_var.get()

    if oper == '+':
        result.set(add(num1, num2))
    elif oper == '-':
        result.set(subtract(num1, num2))
    elif oper == '*':
        result.set(multi(num1, num2))
    elif oper == '/':
        result.set(div(num1, num2))

# Create the GUI window
root = tk.Tk()
root.title("Calculator")

# Create and place GUI elements
entry_num1 = tk.Entry(root)
entry_num1.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

operator_var = tk.StringVar()
operator_var.set('+')  # Default operator

operator_choices = ['+', '-', '*', '/']
operator_menu = tk.OptionMenu(root, operator_var, *operator_choices)
operator_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Start the GUI event loop
root.mainloop()
