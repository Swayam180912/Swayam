import tkinter as tk

import json
import os

root = tk.Tk()
root.geometry('2000x700')
root.title('Dynamicity')

def register_command():
    register_frame = tk.Frame()
    register_frame.pack(fill='both', expand=True)

    username_label = tk.Label(text='Username: ')
    username_label.place(x=50, y=50)
    username_entry = tk.Entry()
    username_entry.place(x=120, y=50)

    password_label = tk.Label(text='Password: ')
    password_label.place(x=50, y=80)
    password_entry = tk.Entry()
    password_entry.place(x=120 ,y=80)

    firstname_label = tk.Label(text='First Name: ')
    firstname_label.place(x=50, y=110)
    firstname_entry = tk.Entry()
    firstname_entry.place(x=120 ,y=110)

    lastname_label = tk.Label(text='Last Name: ')
    lastname_label.place(x=50, y=140)
    lastname_entry = tk.Entry()
    lastname_entry.place(x=120 ,y=140)

    email_label = tk.Label(text='email: ')
    email_label.place(x=50, y=170)
    email_entry = tk.Entry()
    email_entry.place(x=120 ,y=170)

    def signin_command():
        user_data = {
            "username": username_entry.get(),
            "password": password_entry.get(),
            "first_name": firstname_entry.get(),
            "last_name": lastname_entry.get(),
            "email": email_entry.get()
        }

        file_name = "users.json"

        # Check if file exists
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                try:
                    data = json.load(file)
                except:
                    data = []
        else:
            data = []

        # Add new user
        data.append(user_data)

        # Write back to file
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

        print("User registered successfully!")
        signin.config(state=tk.DISABLED)

        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        firstname_entry.delete(0, tk.END)
        lastname_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

    signin = tk.Button(text='sign in', command=signin_command)
    signin.place(x=200, y=200)

register = tk.Button(text='Register', width=13, command=register_command)
register.place(x=1080,y=30)

login = tk.Button(text='Login', width=13)
login.place(x=1200, y=30)

root.mainloop()