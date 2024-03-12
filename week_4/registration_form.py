from tkinter import *
master = Tk()

my_label = Label(master, text = "THIS IS A REGISTRATION FORM FOR STUDENTS WHO HAVE JUST COMPLETED FORM FOUR")



Label(master, text = "full names:").grid(row = 0)
Label(master, text = "what's your age:").grid(row = 1)
Label(master, text = "what's your grade:").grid(row = 2)

Label(master, text = "what's your course:").grid(row = 3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


mainloop()


