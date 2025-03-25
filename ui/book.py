import customtkinter as ctk
from PIL import Image, ImageTk

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Movie Details")
root.geometry("1200x600")  # Fixed window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = ctk.CTkFrame(root, fg_color="#d92525", width=250, height=600)
sidebar.pack(side="left", fill="y")

# Sidebar Title
ctk.CTkLabel(sidebar, text="Film Booking", font=("Arial", 18, "bold"), text_color="white").pack(pady=20, padx=20, anchor="w")

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

# Layout Frame
movie_frame = ctk.CTkFrame(main_content, fg_color="black")
movie_frame.pack(fill="x")

# ---------------- Movie Poster Placeholder ----------------
poster_frame = ctk.CTkFrame(movie_frame, fg_color="black")
poster_frame.pack(side="left", padx=20)

# Load Movie Poster (Replace with actual movie image)
try:
    img = Image.open("placeholder.jpg")  # Replace with actual image file
    img = img.resize((250, 350), Image.Resampling.LANCZOS)
    movie_img = ImageTk.PhotoImage(img)
    img_label = ctk.CTkLabel(poster_frame, image=movie_img, text="")
    img_label.pack()
except Exception as e:
    print(f"Error loading image: {e}")
    img_label = ctk.CTkLabel(poster_frame, text="Movie Poster Here", font=("Arial", 14), text_color="white", fg_color="gray", width=250, height=350)
    img_label.pack(padx=20, pady=20)

# ---------------- Movie Details ----------------
details_frame = ctk.CTkFrame(movie_frame, fg_color="black")
details_frame.pack(side="right", fill="both", expand=True, padx=20)

ctk.CTkLabel(details_frame, text="Movie Title", font=("Arial", 22, "bold"), text_color="white").pack(anchor="w")
ctk.CTkLabel(details_frame, text="Subtitle | Genre | Duration | Rating", font=("Arial", 14), text_color="gray").pack(anchor="w", pady=5)

ctk.CTkLabel(details_frame, text="This is a short description of the movie. It gives an overview of the plot and main themes.",
             font=("Arial", 14), text_color="white", wraplength=500, justify="left").pack(anchor="w", pady=10)

# ---------------- Show Timings ----------------
ctk.CTkLabel(details_frame, text="Show Times:", font=("Arial", 14, "bold"), text_color="white").pack(anchor="w")

showtimes_frame = ctk.CTkFrame(details_frame, fg_color="black")
showtimes_frame.pack(anchor="w")

times = ["1:00 PM", "3:30 PM", "6:00 PM", "8:30 PM"]
for time in times:
    ctk.CTkLabel(showtimes_frame, text=time, font=("Arial", 14), text_color="white").pack(anchor="w")

# ---------------- Book Ticket Button ----------------
book_btn = ctk.CTkButton(details_frame, text="🎟️ Book Ticket", font=("Arial", 14, "bold"),
                         fg_color="red", text_color="white", hover_color="#b71c1c", corner_radius=10, height=40)
book_btn.pack(pady=15, anchor="w")

# ---------------- Run Application ----------------
root.mainloop()
