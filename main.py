from tkinter import *
from tkinter import messagebox  # messagebox is not a class so using the wildcard * won't work
import random
import pyperclip
import json
# ---------------------------- SEARCH FUNCTION ---------------------------------- #
def find_password():
    website = site_input.get()
    try:
        with open("Day29-PasswordManager/data.json", mode="r") as file:
            data = json.load(file)
            print(data[website]["email"])
    except FileNotFoundError:
        messagebox.showerror(title="Lul, oops", message="No data file found.")
    except KeyError:
        messagebox.showerror(title="Lul, nope", message="No details for the website exists")
    else:
        messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [random.choice(letters) for i in range(random.randint(8, 10))]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    symbol_list = [random.choice(symbols) for i in range(random.randint(2, 4))]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    number_list = [random.choice(numbers) for i in range(random.randint(2, 4)
    )]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)   # putting all the strings inside a list together not separated with a space " " or an underscore "_", but rather ""
    pass_input.insert(0, password)
    pyperclip.copy(password)    # automatically copies the password, so you can just already paste it to the website you're signing up in instead of manually copying AND THEN PASTING IT, so it skips the step of manually copying
# print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = site_input.get()
    user = user_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }

    if website == "" or user == "" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {user}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            try:
                with open("Day29-PasswordManager/data.json", mode="r") as file2:
                    data = json.load(file2)
            except FileNotFoundError:
                with open("Day29-PasswordManager/data.json", mode="w") as file2:
                    json.dump(new_data, file2, indent=4)
            else:
                data.update(new_data)
                with open("Day29-PasswordManager/data.json", mode="w") as file3:    
                    json.dump(data, file3, indent=4)
            finally:
                site_input.delete(0, 'end')
                pass_input.delete(0, 'end')
    # print(data)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

site_label = Label(text="Website:", font=("Arial", 12))
site_label.grid(column=0, row=1)
site_input = Entry(width=32)
site_input.grid(sticky="W", column=1, row=1)
site_input.focus()      # allows the cursor to already be there, so it's ready for the user to type the website

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

user_label = Label(text="Email/Username:", font=("Arial", 12))
user_label.grid(column=0, row=2)
user_input = Entry(width=32)
user_input.grid(sticky="W", column=1, row=2)
user_input.insert(0, "test@email.com")     # placeholder email starting at index 0 or if you want to append at the end, then use END rather than 0

pass_label = Label(text="Password:", font=("Arial", 12))
pass_label.grid(column=0, row=3)
pass_input = Entry(width=32)
pass_input.grid(sticky="W", column=1, row=3)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=3)

add_pass = Button(text="Add", width=36, command=save)
add_pass.grid(column=1, row=4, columnspan=2)    # columnspan allows the button to stretch to the next column


canvas = Canvas(width=200, height=200)
p_image = PhotoImage(file="Day29-PasswordManager/logo.png")
canvas.create_image(100, 100, image=p_image)
canvas.grid(column=1, row=0)


window.mainloop()
