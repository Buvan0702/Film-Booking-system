import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector
import hashlib
from tkinter import messagebox
import sys
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

# ------------------- Login Function -------------------
def login_user():
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showwarning("Input Error", "Please enter both email and password.")
        return

    hashed_password = hash_password(password)

    try:
        connection = connect_db()
        cursor = connection.cursor()
        
        cursor.execute(
            "SELECT first_name, last_name FROM Users WHERE email = %s AND password = %s",
            (email, hashed_password)
        )
        
        user = cursor.fetchone()
        
        if user:
            first_name, last_name = user
            messagebox.showinfo("Success", f"Welcome {first_name} {last_name}!")
            
            root.destroy()  # Close the login window
            
            # Open home.py after successful login
            subprocess.Popen([sys.executable, "home.py"])
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")
    
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# ------------------- Open Sign Up Page -------------------
def open_signup():
    try:
        subprocess.Popen([sys.executable, "signup.py"])
        root.destroy()  # Close the current login window
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open signup page: {e}")

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("light")  # Set light mode
root = ctk.CTk()
root.title("Film Booking - Login")
root.geometry("900x500")  # Fixed window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Main Container Frame ----------------
# Matching the bright red color from the image
container = ctk.CTkFrame(root, fg_color="#d92525")
container.pack(fill="both", expand=True)

# ---------------- Login Form ----------------
form_frame = ctk.CTkFrame(container, fg_color="#d92525", width=450)
form_frame.pack(side="left", fill="both", padx=40, pady=40)

# Film Booking Title - Larger and white as shown in image
ctk.CTkLabel(form_frame, text="Film Booking", font=("Arial", 28, "bold"), text_color="white").pack(anchor="w")
ctk.CTkLabel(form_frame, text="Manage your movie bookings seamlessly.",
             font=("Arial", 14), text_color="white").pack(anchor="w", pady=(2, 25))

# --- Email Entry ---
ctk.CTkLabel(form_frame, text="Email", font=("Arial", 14), text_color="white").pack(anchor="w", pady=(10, 5))
email_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter your email", height=40, 
                          fg_color="white", text_color="black", corner_radius=5)
email_entry.pack(fill="x", pady=2)

# --- Password Entry ---
ctk.CTkLabel(form_frame, text="Password", font=("Arial", 14), text_color="white").pack(anchor="w", pady=(15, 5))
password_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter your password", show="*", height=40,
                             fg_color="white", text_color="black", corner_radius=5)
password_entry.pack(fill="x", pady=2)

# --- Login Button --- (Black button with white text as in the image)
login_btn = ctk.CTkButton(form_frame, text="Login", font=("Arial", 14, "bold"), 
                         fg_color="black", text_color="white", height=40, 
                         hover_color="#333333", corner_radius=5,
                         command=login_user)
login_btn.pack(fill="x", pady=(25, 10))

# --- Sign Up & Forgot Password Links ---
signup_frame = ctk.CTkFrame(form_frame, fg_color="#d92525")
signup_frame.pack(fill="x")

ctk.CTkLabel(signup_frame, text="Don't have an account? ", font=("Arial", 12), text_color="white").pack(side="left")
signup_link = ctk.CTkLabel(signup_frame, text="Sign Up", font=("Arial", 12, "bold"), text_color="white", cursor="hand2")
signup_link.pack(side="left")
signup_link.bind("<Button-1>", lambda e: open_signup())

# Forgot Password - Center aligned as in the image
forgot_password = ctk.CTkLabel(form_frame, text="Forgot Password?", font=("Arial", 12), text_color="white", cursor="hand2")
forgot_password.pack(anchor="center", pady=(10, 0))

# ---------------- Right Side - Image ----------------
image_frame = ctk.CTkFrame(container, fg_color="#d92525")
image_frame.pack(side="right", fill="both", expand=True)

# Try to load the viewer image, otherwise use a placeholder
try:
    # Load the image of person sitting on couch watching movie
    image = Image.open("cinema_viewer.png")  # Use the filename of your image with person on couch
    photo = ImageTk.PhotoImage(image)
    image_label = ctk.CTkLabel(image_frame, image=photo, text="")
    image_label.image = photo  # Keep a reference to prevent garbage collection
    image_label.place(relx=0.5, rely=0.5, anchor="center")
except Exception as e:
    print(f"Image not found: {e}")
    # Create a placeholder text label if image is not found
    placeholder = ctk.CTkLabel(image_frame, text="[Viewer Image]", font=("Arial", 20), text_color="white")
    placeholder.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- Run Application ----------------
root.mainloop()