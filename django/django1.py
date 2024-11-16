import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    
    if not name or not email or not password or not confirm_password:
        messagebox.showerror("Input Error", "All fields are required")
        return

    if password != confirm_password:
        messagebox.showerror("Password Error", "Passwords do not match")
        return

    # Display a success message
    messagebox.showinfo("Success", "Registration successful!")
    # Optionally, here you could add code to save the registration details to a file or database

    # Clear the form fields after submission
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_confirm_password.delete(0, tk.END)

# Set up the main application window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x300")

# Title Label
label_title = tk.Label(root, text="Register Here", font=("Helvetica", 16, "bold"))
label_title.pack(pady=10)

# Name
label_name = tk.Label(root, text="Full Name:")
label_name.pack(anchor="w", padx=20)
entry_name = tk.Entry(root, width=30)
entry_name.pack(padx=20, pady=5)

# Email
label_email = tk.Label(root, text="Email:")
label_email.pack(anchor="w", padx=20)
entry_email = tk.Entry(root, width=30)
entry_email.pack(padx=20, pady=5)

# Password
label_password = tk.Label(root, text="Password:")
label_password.pack(anchor="w", padx=20)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(padx=20, pady=5)

# Confirm Password
label_confirm_password = tk.Label(root, text="Confirm Password:")
label_confirm_password.pack(anchor="w", padx=20)
entry_confirm_password = tk.Entry(root, show="*", width=30)
entry_confirm_password.pack(padx=20, pady=5)

# Submit Button
button_submit = tk.Button(root, text="Submit", command=submit_form)
button_submit.pack(pady=20)

# Start the main application loop
root.mainloop()
