import tkinter as tk
import math

#Głowne okno
root = tk.Tk()
root.title("Kalkulator")
root.geometry("400x500")
root.resizable(False, False)

#Pole tekstowe
entry = tk.Entry(root, width=20, font=("Arial", 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

#Pole historii
history = tk.Text(root, height=5, width=30, font=("Arial", 10),
            state="disabled")
history.grid(row=6, column=0, columnspan=4, padx=10, pady=10,
            sticky="ew")

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))
    root.update()

def button_clear():
    entry.delete(0, tk.END)
    root.update()

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return None

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        entry.delete(0, tk.END)
        entry.insert(0 , str(result))
        history.config(state="normal")
        history.insert(tk.END, f"{expression} = {result}\n")
        history.config(state="disabled")
        history.see(tk.END)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Błąd: Dzielenie przez 0")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Błąd")
    root.update()


def button_operator(op):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + op)
    root.update()

def clear_history():
    history.config(state="normal")
    history.delete(1.0, tk.END)
    history.config(state="disabled")
    root.update()

def button_sqrt():
    try:
        value = float(entry.get())
        if value < 0:
            entry.delete(0, tk.END)
            entry.insert(0, "błąd: Ujemna liczba")
        else:
            result = math.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Błąd")
    root.update()

#Lista przycisków
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0), ('(', 5, 1), (')', 5, 2), ('√', 5, 3)
]

for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, padx=40, pady=20, font=("Arial", 12),
                        bg="lightgreen", command=button_equal)

    elif text == 'C':
        btn = tk.Button(root, text=text, padx=40, pady=20, font=("Arial", 12),
                        bg="lightcoral", command=button_clear)

    elif text in ['+', '-', '/', '*']:
        btn = tk.Button(root, text=text, padx=40, pady= 20, font=("Arial", 12),
                        bg="lightblue", command=lambda op=text: button_operator(op))

    elif text == "√":
        btn = tk.Button(root, text=text, padx=40, pady=20, font=("Arial",12),
                         bg="lightyellow", command=button_sqrt)

    else:
        btn = tk.Button(root, text=text, padx=40, pady=20, font=("Arial", 12),
                        bg="lightgrey", command=lambda num=text: button_click(num))
    btn.grid(row=row, column=col, sticky='nsew')

#Przycisk czyszczenia historii
btn_clear_hist = tk.Button(root, text="Clear History", padx=20,
            pady=10, font=("Arial", 10), bg="orange", command=clear_history)
btn_clear_hist.grid(row=7, column=0, columnspan=4, padx=10,
            pady=5, sticky="ew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
root.mainloop()

