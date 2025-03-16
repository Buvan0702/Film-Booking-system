import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("Film Booking - Movie Details")
root.geometry("1200x600")  # Fixed window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="black")  # Dark mode theme

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = tk.Frame(root, bg="#d92525", width=250, height=600)
sidebar.pack(side="left", fill="y")

# Sidebar Title
tk.Label(sidebar, text="Film Booking", font=("Arial", 18, "bold"), fg="white", bg="#d92525").pack(pady=20, padx=20, anchor="w")

# Sidebar Buttons
menu_items = [
    ("🏠  Home", "home"),
    ("📅  Previous Bookings", "bookings"),
    ("👤  Profile", "profile"),
    ("ℹ️  About", "about"),
]
for item, cmd in menu_items:
    btn = tk.Button(sidebar, text=item, font=("Arial", 12), fg="white", bg="#d92525",
                    relief="flat", anchor="w", padx=20, activebackground="#b71c1c", bd=0)
    btn.pack(fill="x", pady=3)

# Logout Button
logout_btn = tk.Button(sidebar, text="📤  Logout", font=("Arial", 12), fg="white", bg="#d92525",
                       relief="flat", anchor="w", padx=20, activebackground="#b71c1c", bd=0)
logout_btn.pack(fill="x", pady=20, side="bottom")

# ---------------- Main Content ----------------
main_content = tk.Frame(root, bg="black")
main_content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Layout Frame
movie_frame = tk.Frame(main_content, bg="black")
movie_frame.pack(fill="x")

# ---------------- Movie Poster Placeholder ----------------
poster_frame = tk.Frame(movie_frame, bg="black")
poster_frame.pack(side="left", padx=20)

# Load Placeholder Image (or replace with actual movie poster)
try:
    img = Image.open("placeholder.jpg")  # Replace with actual image file
    img = img.resize((250, 350), Image.Resampling.LANCZOS)
    movie_img = ImageTk.PhotoImage(img)
    img_label = tk.Label(poster_frame, image=movie_img, bg="black")
    img_label.image = movie_img
    img_label.pack()
except Exception as e:
    print(f"Error loading image: {e}")
    img_label = tk.Label(poster_frame, text="Movie Poster Here", font=("Arial", 14), fg="white", bg="gray")
    img_label.pack(padx=20, pady=20, ipadx=50, ipady=80)

# ---------------- Movie Details ----------------
details_frame = tk.Frame(movie_frame, bg="black")
details_frame.pack(side="right", fill="both", expand=True, padx=20)

tk.Label(details_frame, text="Movie Title", font=("Arial", 20, "bold"), fg="white", bg="black").pack(anchor="w")
tk.Label(details_frame, text="Subtitle | Genre | Duration | Rating", font=("Arial", 12), fg="gray", bg="black").pack(anchor="w", pady=5)

tk.Label(details_frame, text="This is a short description of the movie. It gives an overview of the plot and main themes.",
         font=("Arial", 12), fg="white", bg="black", wraplength=500, justify="left").pack(anchor="w", pady=10)

# ---------------- Show Timings ----------------
tk.Label(details_frame, text="Show Times:", font=("Arial", 12, "bold"), fg="white", bg="black").pack(anchor="w")

showtimes_frame = tk.Frame(details_frame, bg="black")
showtimes_frame.pack(anchor="w")

times = ["1:00 PM", "3:30 PM", "6:00 PM", "8:30 PM"]
for time in times:
    tk.Label(showtimes_frame, text=time, font=("Arial", 12), fg="white", bg="black").pack(anchor="w")

# ---------------- Book Ticket Button ----------------
book_btn = tk.Button(details_frame, text="Book Ticket", font=("Arial", 12, "bold"), fg="white", bg="red",
                     relief="flat", padx=20, pady=5, activebackground="#b71c1c")
book_btn.pack(pady=15, anchor="w")

# ---------------- Run Application ----------------
root.mainloop()
