from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # Sets password length as default. This could be updated to have a slider for password length in the tkinter window
    # which allows the user to choose how long to make it and randomly assigns nr_letters,nr_symbols, and nr_numbers
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = ([choice(letters) for char in range(nr_letters)] + [choice(symbols) for char in range(nr_symbols)] +
                     [choice(numbers) for char in range(nr_numbers)])
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    if len(password)<1 or len(user)<1 or len(website)<1:
        messagebox.showerror(title="Missing Information",message="You did not enter values in all fields")
    else:
        approved = messagebox.askokcancel(title="website", message=f"These are the details entered:  \nEmail: {user}"
                                                                   f"\nPassword: {password} \nIs this OK to save?")
        if approved:
            with open("passwords.txt","a") as password_list:
                password_list.write(f"{website} | {user} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manger")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200,highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(123,100,image=image)

canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1,sticky="W")

website_entry = Entry(width=51)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2,sticky="W")

user_label = Label(text="Email/Username:")
user_label.grid(column=0,row=2,sticky="W")

user_entry = Entry(width=51)
user_entry.insert(0,"email@email.com")
user_entry.grid(column=1,row=2,columnspan=2,sticky="W")

password_label = Label(text="Password:")
password_label.grid(column=0,row=3,sticky="W")

password_entry = Entry(width=32)
password_entry.grid(column=1,row=3,sticky="W")

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=2,row=3,sticky="W")

add_button = Button(text="Add", command=add_password,width=43)
add_button.grid(column=1,row=4,columnspan=2,sticky="W")

window.mainloop()

