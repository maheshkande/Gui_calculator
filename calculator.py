import tkinter as tk

# --- Button Functions ---
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# --- Key Press Event ---
def key_press(event):
    key = event.char
    if key in '0123456789+-*/.':
        button_click(key)
    elif key == '\r':  # Enter key
        calculate()
    elif key == '\x08':  # Backspace
        entry.delete(len(entry.get())-1, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("🧮 Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: calculate() if x == '=' else button_click(x)
        tk.Button(frame, text=btn, font=("Arial", 18), command=action).pack(side="left", expand=True, fill="both")

# Clear Button
tk.Button(root, text="Clear", font=("Arial", 18), command=clear, bg="red", fg="white").pack(fill="both", padx=10, pady=10)

# Bind key events
root.bind("<Key>", key_press)

root.mainloop()

