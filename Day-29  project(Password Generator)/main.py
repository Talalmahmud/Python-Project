from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    char = ['A', "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'R', 'S', 'T',
            'U', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    symbols = ['"', "'", '!', '~', '`', '@', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']',
               '|', '/', '?', '.', ',']
    password_list = []

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    for i in range(nr_letters):
        password_list.append(random.choice(char))
    for i in range(nr_numbers):
        password_list.append(random.choice(num))
    for i in range(nr_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    generate_password = ""
    for i in password_list:
        generate_password += i

    password_entry.insert(0, generate_password)
    pyperclip.copy(generate_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def data_save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.showinfo(title=website,
                                    message=f"There are the details entered:\n Email: {email} \n Password: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"\n{website} | {email} | {password}")
                website_entry.delete(0, END)
                email_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "talal@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

password_generator_button = Button(text="Generator", command=password_generator)
password_generator_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=data_save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()