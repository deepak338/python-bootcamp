from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list=password_letters+password_symbols+password_numbers
    shuffle(password_list)

    passwords="".join(password_list)
    password_entry.insert(0,passwords)
    pyperclip.copy(passwords)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    Website = website_entry.get()
    Email = email_entry.get()
    Password = password_entry.get()

    if len(Website) == 0 or len(Password) == 0:
        messagebox.showinfo(title='oops', message='invalid entry')
    else:
        is_ok = messagebox.askokcancel(title=Website, message='are you sure')
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'\n{Website}  | {Email} | {Password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('password manager')
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website = Label(text='Website')
website.grid(row=1, column=0)
email = Label(text='Email/Username')
email.grid(row=2, column=0)
password = Label(text='Password')
password.grid(row=3, column=0)

# buttons
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
gen_password = Button(text='Generate password',command=generate_password)
gen_password.grid(row=3, column=2)

# entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'deepakthedev@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

window.mainloop()
