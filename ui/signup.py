import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector
import hashlib
import sys
from tkinter import messagebox
import subprocess  # To open another Python script

# ------------------- Database Connection -------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="new_password",  # Replace with your MySQL password
        database="film_booking"
    )

# ------------------- Password Hashing -------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------- Register User Function -------------------
def register_user():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not first_name or not last_name or not email or not password:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    hashed_password = hash_password(password)

    try:
        connection = connect_db()
        cursor = connection.cursor()
        
        cursor.execute(
            "INSERT INTO Users (first_name, last_name, email, password, role) VALUES (%s, %s, %s, %s, %s)",
            (first_name, last_name, email, hashed_password, "user")
        )
        
        connection.commit()
        messagebox.showinfo("Success", "User registered successfully!")
        
        # Clear the input fields
        first_name_entry.delete(0, ctk.END)
        last_name_entry.delete(0, ctk.END)
        email_entry.delete(0, ctk.END)
        password_entry.delete(0, ctk.END)
        
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# ------------------- Open Login Page -------------------
def open_login():
    try:
        subprocess.Popen([sys.executable, "login.py"])
  # Ensure 'login.py' is in the same folder
        root.destroy()  # Close the current signup window
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open login page: {e}")

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("light")  # Set light mode
root = ctk.CTk()
root.title("Film Booking - Sign Up")
root.geometry("900x500")  # Fixed window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Main Container Frame ----------------
container = ctk.CTkFrame(root, fg_color="#d92525")  # Red Background
container.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- Left Side - Sign Up Form ----------------
left_frame = ctk.CTkFrame(container, fg_color="#d92525")
left_frame.pack(side="left", fill="both", padx=20, pady=20)

# Film Booking Title
ctk.CTkLabel(left_frame, text="Film Booking", font=("Arial", 18, "bold"), text_color="white").pack(anchor="w")
ctk.CTkLabel(left_frame, text="Manage your movie bookings seamlessly.",
             font=("Arial", 10), text_color="white").pack(anchor="w", pady=5)

# Name Entry Fields (Side by Side)
name_frame = ctk.CTkFrame(left_frame, fg_color="#d92525")
name_frame.pack(fill="x", pady=(10, 0))

first_name_entry = ctk.CTkEntry(name_frame, placeholder_text="First Name", height=35)
first_name_entry.pack(side="left", expand=True, padx=5, pady=2)

last_name_entry = ctk.CTkEntry(name_frame, placeholder_text="Last Name", height=35)
last_name_entry.pack(side="right", expand=True, padx=5, pady=2)

# Email Entry
ctk.CTkLabel(left_frame, text="Email", font=("Arial", 10, "bold"), text_color="white").pack(anchor="w", pady=(10, 0))
email_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter your email", height=35)
email_entry.pack(fill="x", pady=2)

# Password Entry
ctk.CTkLabel(left_frame, text="Password", font=("Arial", 10, "bold"), text_color="white").pack(anchor="w", pady=(10, 0))
password_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter your password", show="*", height=35)
password_entry.pack(fill="x", pady=2)

# Sign Up Button
signup_btn = ctk.CTkButton(left_frame, text="Sign Up", font=("Arial", 11, "bold"),
                           fg_color="black", text_color="white", height=40, hover_color="gray", command=register_user)
signup_btn.pack(fill="x", pady=(15, 5))

# Already Have an Account? Log In Link
bottom_frame = ctk.CTkFrame(left_frame, fg_color="#d92525")
bottom_frame.pack(fill="x")

ctk.CTkLabel(bottom_frame, text="Already have an account?", font=("Arial", 9), text_color="white").pack(side="left")

login_link = ctk.CTkLabel(bottom_frame, text="Log In", font=("Arial", 9, "bold"), text_color="white", cursor="hand2")
login_link.pack(side="left")
login_link.bind("<Button-1>", lambda e: open_login())  # Opens login page when clicked

# ---------------- Right Side - Image ----------------
right_frame = ctk.CTkFrame(container, fg_color="#d92525", width=350, height=350)
right_frame.pack(side="right", fill="both")

# Load and Display Image (Replace 'cinema.png' with your actual image file)
try:
    image = Image.open("cinema.png")  # Load your movie booking image
    image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize image
    movie_img = ImageTk.PhotoImage(image)
    img_label = ctk.CTkLabel(right_frame, image=movie_img, text="")
    img_label.place(relx=0.5, rely=0.5, anchor="center")
except Exception as e:
    print("Image not found. Please add 'cinema.png' to the project folder.")

# ---------------- Run Application ----------------
root.mainloop()
