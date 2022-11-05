from tkinter import *


def button_clicked():
    miles = float(input1.get())

    print(type(miles))
    label2['text'] = f"{miles} miles is {miles *1.6} kilometers"


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="How many kilometers?")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=50)

input1 = Entry(width=10)
input1.grid(column=1, row=0)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=0)


label2 = Label(text="... miles is ... kilometers", font=("Arial", 24, "bold"))
label2.grid(column=0, row=2)
# button


button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)
# Entry


window.mainloop()
