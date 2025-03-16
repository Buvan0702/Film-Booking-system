import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Required for images

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("Film Booking - Homepage")
root.geometry("1400x700")  # Fixed window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="black")  # Dark mode theme

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = tk.Frame(root, bg="#d92525", width=250, height=700)
sidebar.pack(side="left", fill="y")

# Sidebar Title
tk.Label(sidebar, text="Film Booking", font=("Arial", 20, "bold"), fg="white", bg="#d92525").pack(pady=20, padx=20, anchor="w")

# Sidebar Buttons
menu_items = [
    ("🏠  Home", "home"),
    ("📅  Previous Bookings", "bookings"),
    ("👤  Profile", "profile"),
    ("ℹ️  About", "about"),
]
for item, cmd in menu_items:
    btn = tk.Button(sidebar, text=item, font=("Arial", 14), fg="white", bg="#d92525",
                    relief="flat", anchor="w", padx=20, activebackground="#b71c1c", bd=0)
    btn.pack(fill="x", pady=3)

# Logout Button
logout_btn = tk.Button(sidebar, text="📤  Logout", font=("Arial", 14), fg="white", bg="#d92525",
                       relief="flat", anchor="w", padx=20, activebackground="#b71c1c", bd=0)
logout_btn.pack(fill="x", pady=20, side="bottom")

# ---------------- Main Content ----------------
main_content = tk.Frame(root, bg="black")
main_content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Title
tk.Label(main_content, text="Welcome to Film Booking", font=("Arial", 22, "bold"), fg="white", bg="black").pack(anchor="w", pady=5)

# Subtitle
tk.Label(main_content, text="Browse and book your favorite movies", font=("Arial", 14), fg="gray", bg="black").pack(anchor="w")

# ---------------- Now Showing ----------------
tk.Label(main_content, text="Now Showing", font=("Arial", 18, "bold"), fg="white", bg="black").pack(anchor="w", pady=10)

# Movie Poster Frame
movie_frame = tk.Frame(main_content, bg="black")
movie_frame.pack(anchor="w", padx=10, pady=5)

# Load Movie Posters (Replace 'placeholder.jpg' with actual image paths)
movie_paths = ["john_wick.jpg", "rocky.jpg", "blade_runner.jpg", "rocky4.jpg"]  # Replace with actual file paths
movie_images = []

for path in movie_paths:
    try:
        img = Image.open(path)
        img = img.resize((150, 200))  # Resize to fit UI
        img = ImageTk.PhotoImage(img)
        movie_images.append(img)
    except:
        img = Image.new("RGB", (150, 200), (50, 50, 50))  # Placeholder Gray Box
        img = ImageTk.PhotoImage(img)
        movie_images.append(img)

# Display Posters
for img in movie_images:
    label = tk.Label(movie_frame, image=img, bg="black")
    label.pack(side="left", padx=10)

# ---------------- Featured Theaters ----------------
tk.Label(main_content, text="Featured Theaters", font=("Arial", 18, "bold"), fg="white", bg="black").pack(anchor="w", pady=20)

# Theater Icons Frame
theater_frame = tk.Frame(main_content, bg="black")
theater_frame.pack(anchor="w", padx=10, pady=5)

theaters = [
    ("Theater 1", "City Center"),
    ("Theater 2", "Downtown"),
    ("Theater 3", "Mall"),
]

for name, location in theaters:
    icon = tk.Label(theater_frame, text="🎬", font=("Arial", 40), fg="white", bg="black")
    icon.pack(side="left", padx=30)

    text = tk.Label(theater_frame, text=f"{name}\nLocation: {location}", font=("Arial", 14, "bold"), fg="white", bg="black")
    text.pack(side="left")

# ---------------- Run Application ----------------
root.mainloop()
