from tkinter import *
from tkinter import ttk 

C = Tk() 
C.title("DIABETE'S A BITCH, BUT MY UI AIN'T ONE")
C.geometry("800x600")

columns = ("Date", "Time", "Level", "Note")

tree = ttk.Treeview(C, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width= 100)
tree.pack(pady=10)

#my stuff that i wanna write: 
L = Label(C, text="Bulletin Entry: ", bg="#c0c0c0", font=("Terminal", 14))
L.pack()
T = Text(C, height=10, width=80, font=("Terminal", 14)) 
T.pack()

def add_entry(date, time, level):  
    tree.insert("", "end", values=(date, time, level)) 

def sum():
    total, count = 0, 0
    for child in tree.get_children():
        val = tree.item(child)["values"][2]
        try: 
            total += float(val)
            count += 1
        except: continue 
    average = total / count if count else o 
    messagebox.showinfo("summary", f"Toatal: {total} \n average: {average:.2f}") 

Button(C, text="Add Entry", command=add_entry("2025", "10:30", 123)).pack(pady=5) 
Button(C, text="Calculate sum", command=sum).pack(pady=5)


C.mainloop()
