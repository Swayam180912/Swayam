import tkinter as tk

import json
import os

root = tk.Tk()
root.geometry('2000x700')
root.title('Dynamicity')

def open_dashboard(user_data):
    # Clear window
    for widget in root.winfo_children():
        widget.destroy()

    dashboard_frame = tk.Frame(root)
    dashboard_frame.pack(fill='both', expand=True)

    # Top bar
    profile_btn = tk.Button(dashboard_frame, text="Profile")
    profile_btn.pack(anchor='ne', padx=20, pady=10)

    # Title
    title = tk.Label(dashboard_frame, text=f"{user_data['username']}'s Watchlist", font=("Arial", 20))
    title.pack(pady=20)

    # Watchlist display
    watchlist_box = tk.Listbox(dashboard_frame, width=50, height=15)
    watchlist_box.pack(pady=10)

    # Load existing watchlist (if exists)
    if "watchlist" in user_data:
        for word in user_data["watchlist"]:
            watchlist_box.insert(tk.END, word)

    # Entry to add word
    word_entry = tk.Entry(dashboard_frame)
    word_entry.pack(pady=5)

    # Add word function
    def add_word():
        word = word_entry.get()
        if word:
            watchlist_box.insert(tk.END, word)
            word_entry.delete(0, tk.END)

            # Update JSON
            update_watchlist(user_data["username"], word)

    add_btn = tk.Button(dashboard_frame, text="Add Word", command=add_word)
    add_btn.pack(pady=10)

def update_watchlist(username, new_word):
    file_name = "users.json"

    with open(file_name, "r") as file:
        data = json.load(file)

    for user in data:
        if user["username"] == username:
            if "watchlist" not in user:
                user["watchlist"] = []
            user["watchlist"].append(new_word)

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

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

        open_dashboard(user_data)

    signin = tk.Button(text='sign in', command=signin_command)
    signin.place(x=200, y=200)


def login_command():
    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    login_frame = tk.Frame(root)
    login_frame.pack(fill='both', expand=True)

    username_label = tk.Label(login_frame, text='Username:')
    username_label.place(x=50, y=50)
    username_entry = tk.Entry(login_frame)
    username_entry.place(x=120, y=50)

    password_label = tk.Label(login_frame, text='Password:')
    password_label.place(x=50, y=80)
    password_entry = tk.Entry(login_frame, show="*")
    password_entry.place(x=120, y=80)

    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        file_name = "users.json"

        if not os.path.exists(file_name):
            print("No user found")
            return

        with open(file_name, "r") as file:
            data = json.load(file)

        for user in data:
            if user["username"] == username and user["password"] == password:
                print("Login successful!")
                open_dashboard(user)
                return

        print("Invalid username or password")

    login_btn = tk.Button(login_frame, text="Login", command=check_login)
    login_btn.place(x=120, y=120)



register = tk.Button(text='Register', width=13, command=register_command)
register.place(x=1080,y=30)

login = tk.Button(text='Login', width=13, command=login_command)
login.place(x=1200, y=30)

root.mainloop()