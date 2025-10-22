import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Diabetes Manager - Windows 98 Edition")
root.geometry("800x600")
root.configure(bg="#C0C0C0")  # Classic gray

# Style
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="#FFFFFF", foreground="black", fieldbackground="#FFFFFF")
style.configure("TButton", font=("MS Sans Serif", 10), padding=5)

# Blood Sugar Table
columns = ("Date", "Time", "Level", "Note")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(pady=10)

# Diary Section
diary_label = tk.Label(root, text="Diary Entry", bg="#C0C0C0", font=("MS Sans Serif", 10))
diary_label.pack()
diary_text = tk.Text(root, height=10, width=80, font=("MS Sans Serif", 10))
diary_text.pack()

# Buttons
def add_entry():
    # Placeholder logic
    tree.insert("", "end", values=("2025-10-22", "08:00", "120", "Felt good"))

def calculate_sum():
    total = 0
    count = 0
    for child in tree.get_children():
        val = tree.item(child)["values"][2]
        try:
            total += float(val)
            count += 1
        except:
            continue
    avg = total / count if count else 0
    messagebox.showinfo("Summary", f"Total: {total}\nAverage: {avg:.2f}")

ttk.Button(root, text="Add Entry", command=add_entry).pack(pady=5)
ttk.Button(root, text="Calculate Sum", command=calculate_sum).pack(pady=5)

root.mainloop()
