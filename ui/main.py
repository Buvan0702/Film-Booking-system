import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector
import hashlib
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
            root.destroy()  # Close the login window upon successful login
            open_home_page()  # Open the home page after login
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
        subprocess.Popen(["python", "signup.py"])  # Make sure 'signup.py' is in the same folder
        root.destroy()  # Close the current login window
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open signup page: {e}")

# ------------------- Open Home Page -------------------
def open_home_page():
    try:
        subprocess.Popen(["python", "home.py"])  # Open home.py when login is successful
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open home page: {e}")

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("light")  # Set light mode
root = ctk.CTk()
root.title("Film Booking - Login")
root.geometry("900x500")  # Fixed window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Main Container Frame ----------------
container = ctk.CTkFrame(root, fg_color="#d92525")  # Red Background
container.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- Left Side - Login Form ----------------
left_frame = ctk.CTkFrame(container, fg_color="#d92525")
left_frame.pack(side="left", fill="both", padx=20, pady=20)

# Film Booking Title
ctk.CTkLabel(left_frame, text="Film Booking", font=("Arial", 18, "bold"), text_color="white").pack(anchor="w")
ctk.CTkLabel(left_frame, text="Manage your movie bookings seamlessly.",
             font=("Arial", 10), text_color="white").pack(anchor="w", pady=5)

# --- Email Entry ---
ctk.CTkLabel(left_frame, text="Email", font=("Arial", 10, "bold"), text_color="white").pack(anchor="w", pady=(15, 0))
email_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter your email", height=35)
email_entry.pack(fill="x", pady=2)

# --- Password Entry ---
ctk.CTkLabel(left_frame, text="Password", font=("Arial", 10, "bold"), text_color="white").pack(anchor="w", pady=(10, 0))
password_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter your password", show="*", height=35)
password_entry.pack(fill="x", pady=2)

# --- Login Button ---
login_btn = ctk.CTkButton(left_frame, text="Login", font=("Arial", 11, "bold"), fg_color="black",
                           text_color="white", height=40, hover_color="gray", command=login_user)
login_btn.pack(fill="x", pady=(15, 5))

# --- Sign Up & Forgot Password Links ---
bottom_frame = ctk.CTkFrame(left_frame, fg_color="#d92525")
bottom_frame.pack(fill="x")

ctk.CTkLabel(bottom_frame, text="Don't have an account?", font=("Arial", 9), text_color="white").pack(side="left")

signup_link = ctk.CTkLabel(bottom_frame, text="Sign Up", font=("Arial", 9, "bold"), text_color="white", cursor="hand2")
signup_link.pack(side="left")
signup_link.bind("<Button-1>", lambda e: open_signup())  # Opens signup page when clicked

forgot_password = ctk.CTkLabel(left_frame, text="Forgot Password?", font=("Arial", 9), text_color="white", cursor="hand2")
forgot_password.pack(anchor="center", pady=(5, 0))

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
