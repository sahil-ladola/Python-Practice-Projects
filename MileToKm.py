from tkinter import *


def convert_mi_km():
    mi = float(MI_input.get())
    km = mi * 1.689
    result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(100, 100)
window.config(padx=16, pady=16)

MI_input = Entry(width=7)
MI_input.grid(column=1, row=0)

MI_label = Label(text="Miles")
MI_label.grid(column=2, row=0)

Equal_label = Label(text="is equal to")
Equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


cal_button = Button(text="Calculate", command=convert_mi_km)
cal_button.grid(column=1, row=2)

window.mainloop()
