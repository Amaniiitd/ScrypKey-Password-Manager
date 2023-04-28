import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Manager")
        self.root.geometry("800x700")

        self.master_password = tk.StringVar()
        self.passwords = {}

        # create widgets for the first page
        self.label1 = tk.Label(self.root, text="Enter master password:")
        self.label1.pack(pady=20)

        self.entry1 = tk.Entry(self.root, show="*", textvariable=self.master_password)
        self.entry1.pack(pady=10)

        self.button1 = tk.Button(self.root, text="Submit", command=self.login)
        self.button1.pack(pady=10)

    def login(self):
        # check if the master password is correct
        if self.master_password.get() == "1234":
            self.destroy_all_widgets()
            self.options_page()
            
        else:
            messagebox.showerror("Error", "Invalid master password")
            
    def options_page(self):
        # create widgets for the second page
        self.label2 = tk.Label(self.root, text="Select an option:")
        self.label2.pack(pady=20)

        self.button2 = tk.Button(self.root, text="Add password", command=self.add_password)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self.root, text="Search password", command=self.search_password)
        self.button3.pack(pady=10)

        self.button4 = tk.Button(self.root, text="Modify password", command=self.modify_password)
        self.button4.pack(pady=10)

        self.button5 = tk.Button(self.root, text="Read all passwords", command=self.read_all_passwords)
        self.button5.pack(pady=10)

        self.button6 = tk.Button(self.root, text="Delete password", command=self.delete_password)
        self.button6.pack(pady=10)

        self.button7 = tk.Button(self.root, text="Generate password", command=self.generate_password)
        self.button7.pack(pady=10)

        self.button8 = tk.Button(self.root, text="Change master password", command=self.change_master_password)
        self.button8.pack(pady=10)

        self.button9 = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.button9.pack(pady=10)

    def destroy_all_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def add_password(self):
        self.destroy_all_widgets()
        
        # create widgets for the "add password" page
        pass

    def search_password(self):
        self.destroy_all_widgets()
        
        # create widgets for the "search password" page
        pass

    def modify_password(self):
        self.destroy_all_widgets()
        
        # create widgets for the "modify password" page
        pass

    def read_all_passwords(self):
        self.destroy_all_widgets()
        
        # create widgets for the "read all passwords" page
        pass

    def delete_password(self):
        self.destroy_all_widgets()
        
        # create widgets for the "delete password" page
        pass

    def generate_password(self):
        self.destroy_all_widgets()
        
        # create widgets for the "generate password" page
        pass

    def change_master_password(self):
        self.destroy_all_widgets()
        
        # create widgets for the "change master password" page
        pass

    def run(self):
        self.root.mainloop()

app = PasswordManager()
app.run()
