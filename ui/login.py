import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("Film Booking - Login")
root.geometry("900x500")  # Fixed window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="white")  # Background color

# ---------------- Main Container Frame ----------------
container = tk.Frame(root, bg="#d92525")  # Red Background
container.place(relx=0.5, rely=0.5, anchor="center", width=700, height=350)

# ---------------- Left Side - Login Form ----------------
left_frame = tk.Frame(container, bg="#d92525", width=350, height=350)
left_frame.pack(side="left", fill="both", padx=20, pady=20)

# Film Booking Title
tk.Label(left_frame, text="Film Booking", font=("Arial", 18, "bold"), fg="white", bg="#d92525").pack(anchor="w")
tk.Label(left_frame, text="Manage your movie bookings seamlessly.", 
         font=("Arial", 10), bg="#d92525", fg="white").pack(anchor="w", pady=5)

# Entry Field Styling
entry_style = {"font": ("Arial", 11), "bg": "white", "relief": "solid", "bd": 1}

# --- Email Entry ---
tk.Label(left_frame, text="Email", font=("Arial", 10, "bold"), bg="#d92525", fg="white").pack(anchor="w", pady=(15, 0))
email_entry = tk.Entry(left_frame, **entry_style)
email_entry.insert(0, "Enter your email")
email_entry.pack(fill="x", ipady=7, pady=2)

# --- Password Entry ---
tk.Label(left_frame, text="Password", font=("Arial", 10, "bold"), bg="#d92525", fg="white").pack(anchor="w", pady=(10, 0))
password_entry = tk.Entry(left_frame, show="*", **entry_style)
password_entry.insert(0, "Enter your password")
password_entry.pack(fill="x", ipady=7, pady=2)

# --- Login Button ---
login_btn = tk.Button(left_frame, text="Login", font=("Arial", 11, "bold"), bg="black", fg="white",
                       relief="flat", cursor="hand2", height=2, activebackground="gray")
login_btn.pack(fill="x", pady=(15, 5))

# --- Sign Up & Forgot Password Links ---
bottom_frame = tk.Frame(left_frame, bg="#d92525")
bottom_frame.pack(fill="x")

signup_label = tk.Label(bottom_frame, text="Don't have an account?", font=("Arial", 9), bg="#d92525", fg="white")
signup_label.pack(side="left")

signup_link = tk.Label(bottom_frame, text="Sign Up", font=("Arial", 9, "bold"), bg="#d92525", fg="white", cursor="hand2")
signup_link.pack(side="left")

forgot_password = tk.Label(left_frame, text="Forgot Password?", font=("Arial", 9), bg="#d92525", fg="white", cursor="hand2")
forgot_password.pack(anchor="center", pady=(5, 0))

# ---------------- Right Side - Image ----------------
right_frame = tk.Frame(container, bg="#d92525", width=350, height=350)
right_frame.pack(side="right", fill="both")

# Load and Display Image (Replace 'cinema.png' with your actual image file)
try:
    image = Image.open("cinema.png")  # Load your movie booking image
    image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize image
    movie_img = ImageTk.PhotoImage(image)
    img_label = tk.Label(right_frame, image=movie_img, bg="#d92525")
    img_label.place(relx=0.5, rely=0.5, anchor="center")
except Exception as e:
    print("Image not found. Please add 'cinema.png' to the project folder.")

# ---------------- Run Application ----------------
root.mainloop()
