import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("Film Booking - Sign Up")
root.geometry("900x500")  # Fixed window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="white")  # Background color

# ---------------- Main Container Frame ----------------
container = tk.Frame(root, bg="#d92525")  # Red Background
container.place(relx=0.5, rely=0.5, anchor="center", width=700, height=350)

# ---------------- Left Side - Sign Up Form ----------------
left_frame = tk.Frame(container, bg="#d92525", width=350, height=350)
left_frame.pack(side="left", fill="both", padx=20, pady=20)

# Film Booking Title
tk.Label(left_frame, text="Film Booking", font=("Arial", 18, "bold"), fg="white", bg="#d92525").pack(anchor="w")
tk.Label(left_frame, text="Manage your movie bookings seamlessly.", 
         font=("Arial", 10), bg="#d92525", fg="white").pack(anchor="w", pady=5)

# Name Entry Fields (Side by Side)
name_frame = tk.Frame(left_frame, bg="#d92525")
name_frame.pack(fill="x", pady=(10, 0))

first_name_entry = tk.Entry(name_frame, font=("Arial", 11), bg="white", relief="solid", bd=1)
first_name_entry.insert(0, "Enter your First Name")
first_name_entry.pack(side="left", expand=True, padx=5, ipady=5)

last_name_entry = tk.Entry(name_frame, font=("Arial", 11), bg="white", relief="solid", bd=1)
last_name_entry.insert(0, "Enter your Last Name")
last_name_entry.pack(side="right", expand=True, padx=5, ipady=5)

# Email Entry
tk.Label(left_frame, text="Email", font=("Arial", 10, "bold"), bg="#d92525", fg="white").pack(anchor="w", pady=(10, 0))
email_entry = tk.Entry(left_frame, font=("Arial", 11), bg="white", relief="solid", bd=1)
email_entry.insert(0, "Enter your email")
email_entry.pack(fill="x", ipady=5, pady=2)

# Password Entry
tk.Label(left_frame, text="Password", font=("Arial", 10, "bold"), bg="#d92525", fg="white").pack(anchor="w", pady=(10, 0))
password_entry = tk.Entry(left_frame, show="*", font=("Arial", 11), bg="white", relief="solid", bd=1)
password_entry.insert(0, "Enter your password")
password_entry.pack(fill="x", ipady=5, pady=2)

# Sign Up Button
signup_btn = tk.Button(left_frame, text="Sign Up", font=("Arial", 11, "bold"), bg="black", fg="white",
                       relief="flat", cursor="hand2", height=2, activebackground="gray")
signup_btn.pack(fill="x", pady=(15, 5))

# Already Have an Account? Log In Link
bottom_frame = tk.Frame(left_frame, bg="#d92525")
bottom_frame.pack(fill="x")

login_label = tk.Label(bottom_frame, text="Already have an account? ", font=("Arial", 9), bg="#d92525", fg="white")
login_label.pack(side="left")

login_link = tk.Label(bottom_frame, text="Log In", font=("Arial", 9, "bold"), bg="#d92525", fg="white", cursor="hand2")
login_link.pack(side="left")

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
