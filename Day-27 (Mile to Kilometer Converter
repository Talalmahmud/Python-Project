from tkinter import *


kilotext = 0
window = Tk()
window.minsize(height=400,width=400)
window.title("Mile to Kilometer Converter")

def mileTokilo():
     result_label.config(text= float(mileEntry.get()) * 1.609)

mileEntry = Entry()
mileEntry.grid(column=5, row=0)
mile_label = Label(text= "Mile")
mile_label.grid(column=9, row=0)
equal_label = Label(text= "equal to")
equal_label.grid(column=2, row=2)

result_label = Label(text="0")
result_label.grid(column=5, row=2)

kilo_label = Label(text= "KM")
kilo_label.grid(column=9, row=2)

buttton = Button(text="Calculate", command= mileTokilo)
buttton.grid(column=6, row=4)

window.mainloop()
