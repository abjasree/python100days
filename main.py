from tkinter import *
from tkinter import Tk


def button_click():
    miles = entry.get()
    km = float(miles)*1.689
    label3.config(text=f"{round(km)}")



window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=10, pady=20)

# Label
label = Label(text="Miles", font=("Arial", 15, "normal"))
label.grid(column=2, row=0)
label.config(padx=5,pady=5)

label1 = Label(text="Km", font=("Arial", 15, "normal"))
label1.grid(column=2, row=1)
label1.config(padx=5,pady=5)

label2 = Label(text="is equal to ", font=("Arial", 15, "normal"))
label2.grid(column=0, row=1)
label2.config(padx=5,pady=5)

label3 = Label(text="0", font=("Arial", 15, "normal"))
label3.grid(column=1, row=1)
label3.config(padx=5,pady=5)


# Button
button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


# Entry
entry = Entry(width=12, font=("Arial", 15, "normal"))
entry.insert(END, string="0")
entry.grid(column=1, row=0)





window.mainloop()
