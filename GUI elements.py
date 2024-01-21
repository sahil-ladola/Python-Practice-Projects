from tkinter import *
# to get window like Turtle screen
window = Tk()
window.title("First GUI program")
window.minsize(width=400, height=300)

label = Label(text="Hello to Tkinter", font=("Arial", 18, "bold"))
label1 = Label(text="Hello to Tkinter", font=("Arial", 18, "bold"))
# mandatory display label on screen , place it on the screen & center it
label.pack() # side, expand
label1.pack()


# Button click event
def button_click():
    label.config(text="Button Clicked")
    label1.config(text=entry.get())


# Button
button = Button(text="Click", command=button_click)
button.pack()


# Entry
entry = Entry(width=16)
entry.pack()
# default value
entry.insert(END, string="Some Text")

# text
text = Text(height=5, width=30)
text.focus() # Cursor start with that element
text.insert(END, "Some Text")
print(text.get("1.0", END)) # First line, First character
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# checkbutton
def checkbutton_used():
    # 1 if button checked, otherwise 0
    print(checked_state.get())


# IntVar to get value of checkbox ,it's variable
checked_state = IntVar()
checkbutton = Checkbutton(text="On?", variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# IntVar to get value of radiobutton ,it's variable
radio_state = IntVar()
radiobutton1 = Radiobutton(text="1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="2", value=2, variable=radio_state, command=radio_used)
radiobutton2.pack()
radiobutton1.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


# Listbox
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
# keep window open
window.mainloop()
