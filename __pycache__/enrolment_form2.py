import tkinter as tk
from tkinter import messagebox

def enroll():
    # You may want to add functionality to handle the enrollment process
    messagebox.showinfo("Enrollment", "Form submitted successfully!")

# Create the main window
root = tk.Tk()
root.title("Enrollment Agreement Form")
root.geometry("400x500")
root.configure(bg='beige')

# Create and place labels and entry fields using grid
tk.Label(root, text="Enrollment Agreement Form", bg='beige', font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Student's Name:", bg='beige').grid(row=1, column=0, sticky='w')
first_name = tk.Entry(root)
first_name.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Last Name:", bg='beige').grid(row=2, column=0, sticky='w')
last_name = tk.Entry(root)
last_name.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Date of Birth:", bg='beige').grid(row=3, column=0, sticky='w')
dob = tk.Entry(root)
dob.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Age:", bg='beige').grid(row=4, column=0, sticky='w')
age = tk.Entry(root)
age.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Email:", bg='beige').grid(row=5, column=0, sticky='w')
email = tk.Entry(root)
email.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Phone Number:", bg='beige').grid(row=6, column=0, sticky='w')
phone_number = tk.Entry(root)
phone_number.grid(row=6, column=1, padx=5, pady=5)

tk.Label(root, text="Signature of Parent/Guardian:", bg='beige').grid(row=7, column=0, sticky='w', pady=10)
signature = tk.Entry(root)
signature.grid(row=7, column=1, padx=5, pady=5)

tk.Label(root, text="Date Signed:", bg='beige').grid(row=8, column=0, sticky='w')
date_signed = tk.Entry(root)
date_signed.grid(row=8, column=1, padx=5, pady=5)

# Enroll button
enroll_button = tk.Button(root, text="Enroll", command=enroll)
enroll_button.grid(row=9, column=0, columnspan=2, pady=20)

# Start the application
root.mainloop()