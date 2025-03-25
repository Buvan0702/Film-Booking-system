import customtkinter as ctk
from PIL import Image, ImageTk  # Required for images

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Homepage")
root.geometry("1400x700")  # Fixed window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = ctk.CTkFrame(root, fg_color="#d92525", width=250, height=700)
sidebar.pack(side="left", fill="y")

# Sidebar Title
ctk.CTkLabel(sidebar, text="Film Booking", font=("Arial", 20, "bold"), text_color="white").pack(pady=20, padx=20, anchor="w")

# Sidebar Buttons
menu_items = [
    ("🏠  Home", "home"),
    ("📅  Previous Bookings", "bookings"),
    ("👤  Profile", "profile"),
    ("ℹ️  About", "about"),
]
for item, cmd in menu_items:
    btn = ctk.CTkButton(sidebar, text=item, font=("Arial", 14),
                        fg_color="transparent", text_color="white",
                        anchor="w", corner_radius=0, hover_color="#b71c1c", height=40)
    btn.pack(fill="x", pady=3)

# Logout Button
logout_btn = ctk.CTkButton(sidebar, text="📤  Logout", font=("Arial", 14),
                           fg_color="transparent", text_color="white",
                           anchor="w", corner_radius=0, hover_color="#b71c1c", height=40)
logout_btn.pack(fill="x", pady=20, side="bottom")

# ---------------- Main Content ----------------
main_content = ctk.CTkFrame(root, fg_color="black")
main_content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Title
ctk.CTkLabel(main_content, text="Welcome to Film Booking", font=("Arial", 22, "bold"), text_color="white").pack(anchor="w", pady=5)

# Subtitle
ctk.CTkLabel(main_content, text="Browse and book your favorite movies", font=("Arial", 14), text_color="gray").pack(anchor="w")

# ---------------- Now Showing ----------------
ctk.CTkLabel(main_content, text="Now Showing", font=("Arial", 18, "bold"), text_color="white").pack(anchor="w", pady=10)

# Movie Poster Frame
movie_frame = ctk.CTkFrame(main_content, fg_color="black")
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
    label = ctk.CTkLabel(movie_frame, image=img, text="")
    label.pack(side="left", padx=10)

# ---------------- Featured Theaters ----------------
ctk.CTkLabel(main_content, text="Featured Theaters", font=("Arial", 18, "bold"), text_color="white").pack(anchor="w", pady=20)

# Theater Icons Frame
theater_frame = ctk.CTkFrame(main_content, fg_color="black")
theater_frame.pack(anchor="w", padx=10, pady=5)

theaters = [
    ("Theater 1", "City Center"),
    ("Theater 2", "Downtown"),
    ("Theater 3", "Mall"),
]

for name, location in theaters:
    icon = ctk.CTkLabel(theater_frame, text="🎬", font=("Arial", 40), text_color="white")
    icon.pack(side="left", padx=30)

    text = ctk.CTkLabel(theater_frame, text=f"{name}\nLocation: {location}", font=("Arial", 14, "bold"), text_color="white")
    text.pack(side="left")

# ---------------- Run Application ----------------
root.mainloop()
