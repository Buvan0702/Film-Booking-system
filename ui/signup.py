import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector
import hashlib
import sys
from tkinter import messagebox
import subprocess  # To open another Python script
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

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
        subprocess.Popen([sys.executable, "login.py"])  # Ensure 'login.py' is in the same folder
        root.destroy()  # Close the current signup window
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open login page: {e}")

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("light")  # Set light mode
root = ctk.CTk()
root.title("Film Booking - Sign Up")
root.geometry("1000x700")  # Adjusted window size
root.resizable(False, False)  # Prevent resizing

# Set the background to red (#d92525)
root.configure(fg_color="#d92525")

# ---------------- Left Side - Sign Up Form ----------------
left_frame = ctk.CTkFrame(root, fg_color="#d92525", corner_radius=0)
left_frame.pack(side="left", fill="both", expand=True, padx=(50, 20), pady=50)

# Film Booking Title
ctk.CTkLabel(left_frame, text="Film Booking", font=("Arial", 32, "bold"), text_color="white").pack(anchor="w", pady=(0, 5))
ctk.CTkLabel(left_frame, text="Manage your movie bookings seamlessly.",
             font=("Arial", 14), text_color="white").pack(anchor="w", pady=(0, 30))

# First Name Label and Entry
ctk.CTkLabel(left_frame, text="First Name", font=("Arial", 12), text_color="white").pack(anchor="w", pady=(0, 5))
first_name_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter your First Name", 
                               height=40, fg_color="white", text_color="black",
                               border_width=0, corner_radius=5)
first_name_entry.pack(fill="x", pady=(0, 15))

# Last Name Label and Entry
ctk.CTkLabel(left_frame, text="Last Name", font=("Arial", 12), text_color="white").pack(anchor="w", pady=(0, 5))
last_name_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter your Last Name", 
                              height=40, fg_color="white", text_color="black",
                              border_width=0, corner_radius=5)
last_name_entry.pack(fill="x", pady=(0, 15))

# Email Label and Entry
ctk.CTkLabel(left_frame, text="Email", font=("Arial", 12), text_color="white").pack(anchor="w", pady=(0, 5))
email_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter your email", 
                          height=40, fg_color="white", text_color="black",
                          border_width=0, corner_radius=5)
email_entry.pack(fill="x", pady=(0, 15))

# Password Label and Entry
ctk.CTkLabel(left_frame, text="Password", font=("Arial", 12), text_color="white").pack(anchor="w", pady=(0, 5))
password_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter your password", show="*", 
                             height=40, fg_color="white", text_color="black",
                             border_width=0, corner_radius=5)
password_entry.pack(fill="x", pady=(0, 25))

# Sign Up Button - Black with white text
signup_btn = ctk.CTkButton(left_frame, text="Sign Up", font=("Arial", 14, "bold"),
                          fg_color="black", text_color="white", height=40, 
                          hover_color="#333333", corner_radius=5, command=register_user)
signup_btn.pack(fill="x", pady=(5, 15))

# Already Have an Account? Log In Link
login_frame = ctk.CTkFrame(left_frame, fg_color="#d92525")
login_frame.pack(fill="x")

ctk.CTkLabel(login_frame, text="Already have an account?  ", font=("Arial", 12), text_color="white").pack(side="left")
login_link = ctk.CTkLabel(login_frame, text="Log In", font=("Arial", 12, "bold"), text_color="white", cursor="hand2")
login_link.pack(side="left")
login_link.bind("<Button-1>", lambda e: open_login())

# ---------------- Right Side - Image ----------------
right_frame = ctk.CTkFrame(root, fg_color="#d92525", corner_radius=0)
right_frame.pack(side="right", fill="both", expand=True, padx=30, pady=50)

# Load the image of a person watching a movie
try:
    # Replace this with the path to your movie viewer image
    image = Image.open("movie_viewer.png")  
    # Resize to fit the frame
    image = image.resize((300, 300), Image.LANCZOS)
    movie_img = ImageTk.PhotoImage(image)
    img_label = ctk.CTkLabel(right_frame, image=movie_img, text="")
    img_label.place(relx=0.5, rely=0.5, anchor="center")
except Exception as e:
    # If image not found, display a placeholder
    placeholder = ctk.CTkLabel(right_frame, text="Movie Viewer Image\n(Place movie_viewer.png in the same folder)", 
                              font=("Arial", 14), text_color="white")
    placeholder.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- Run Application ----------------
root.mainloop()