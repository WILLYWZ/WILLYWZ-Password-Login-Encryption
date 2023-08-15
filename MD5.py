import hashlib
import tkinter as tk
from tkinter import ttk

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    password_hash = hashlib.md5(password.encode()).hexdigest()

    
    if username == '' or password == '':
            result_label.config(text="Username or Password Cannot Be Empty!", fg="red")
            reset_form()
    
    else:
        with open("passwords.txt", "r") as f:
            for line in f:
                if line.startswith(username):
                    result_label.config(text="Username Already Exists!", fg="red")
                    reset_form()
                    return
                
    with open("passwords.txt", "a") as f:
        f.write(f"{username} {password_hash}\n")

    result_label.config(text="User Registered Successfully!", fg="green")
    reset_form()

def verify_user():

    username = username_entry.get()
    password = password_entry.get()
    password_hash = hashlib.md5(password.encode()).hexdigest()

    try:
        file = "passwords.txt"
        with open(file, "r") as f:
            for line in f.readlines():
                if line.startswith(username):
                    stored_password = line.split(" ")[1].strip()
                    if password_hash == stored_password:
                        result_label.config(text = "Login Successful!", fg = "green")
                        reset_form()
                        return
                    else:
                        result_label.config(text = "User Not Found or Incorrect Password!", fg = "red")
                        reset_form()
                        return
            result_label.config(text = "User Not Found!\n Do you Want To Register?", fg = "red")
            reset_form()

    except FileNotFoundError:
        open(file, "w").close()
        result_label.config(text="System Error! Data file Not Found.", fg = "red")
        reset_form()


def reset_form():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


root = tk.Tk()
root.geometry("400x350")
root.title("Password Authentication System")

input_frame = ttk.Frame(root)
input_frame.pack(pady=20)

username_label = tk.Label(input_frame, text="Username")
username_label.pack()

username_entry = tk.Entry(input_frame, font=("Arial", 14), width=20)
username_entry.pack(pady=5)

password_label = tk.Label(input_frame, text="Password")
password_label.pack()

password_entry = tk.Entry(input_frame, font=("Arial", 14), width=20)
password_entry.pack(pady=5)

register_button = tk.Button(root, text="Register", command=register_user, width=20, height=2)
register_button.pack(pady=10)

login_button = tk.Button(root, text="Login", command=verify_user, width=20, height=2)
login_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(side="top")

root.mainloop()
