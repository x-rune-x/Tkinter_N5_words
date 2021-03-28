from tkinter import *


root = Tk()
root.title("Simple calculator")


total = 0


def button_click(number):
    current = entry_1.get()
    entry_1.delete(0, END)
    entry_1.insert(0, str(current) + str(number))


def clear_click():
    entry_1.delete(0, END)
    global total
    total = 0


def plus_click():
    current_num = int(entry_1.get())
    global total
    total = current_num + total
    entry_1.delete(0, END)


def equals_click():
    current_num = int(entry_1.get())
    global total
    total = current_num + total
    entry_1.delete(0, END)
    entry_1.insert(0, total)
    total = 0


entry_1 = Entry(root, width=40, borderwidth=5)
entry_1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create all the buttons for the calculator.
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_cl = Button(root, text="clear", padx=80, pady=20, command=clear_click)
button_equals = Button(root, text="=", padx=89, pady=20, command=equals_click)
button_plus = Button(root, text="+", padx=39, pady=20, command=plus_click)

# Put the buttons on the screen in the correct order.
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_cl.grid(row=4, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equals.grid(row=5, column=1, columnspan=2)

root.mainloop()
