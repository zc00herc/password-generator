import tkinter
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    length = int(spinbox.get())
    nr_letters = randint(0, length-2)
    length -= nr_letters
    nr_symbols = randint(0, length-1)
    length -= nr_symbols
    nr_numbers = length

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
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }
    if len(password)<1 or len(user)<1 or len(website)<1:
        messagebox.showerror(title="Missing Information",message="You did not enter values in all fields")
    else:
        try:
            with open("passwords.json","r") as password_list:
                # Read old data and save as "data"
                data = json.load(password_list)
                # update old data with newly added data
                data.update(new_data)
        except FileNotFoundError:
            with open("passwords.json", "w") as password_list:
                # rewrite file with new, bigger data set
                json.dump(new_data, password_list, indent=4)
        else:
            with open("passwords.json","w") as password_list:
                # rewrite file with new, bigger data set
                json.dump(data,password_list, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- SEARCH WEBSITES ------------------------------- #
def search_websites():
    website = website_entry.get()
    try:
        with open("passwords.json",'r') as password_list:
            data = json.load(password_list)
    except FileNotFoundError:
        messagebox.showinfo(title="Details",
                            message="No Password Details Exist")
    else:
        if website in data:
            messagebox.showinfo(title="Details",
                                message=f"Username: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Details",
                                message=f"No data is saved for this {website}")
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

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1,row=1,sticky="W")

search_button = Button(text="Search", command=search_websites,width=14)
search_button.grid(column=2,row=1,sticky="W")

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

var=tkinter.DoubleVar(value=5)
spinbox = Spinbox(from_=0, to=100, width=5,textvariable=var)
spinbox.grid(column=3,row=3)

add_button = Button(text="Add", command=add_password,width=43)
add_button.grid(column=1,row=4,columnspan=2,sticky="W")

window.mainloop()

