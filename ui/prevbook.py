import customtkinter as ctk

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Previous Bookings")
root.geometry("1200x600")  # Fixed window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = ctk.CTkFrame(root, fg_color="#d92525", width=250, height=600)
sidebar.pack(side="left", fill="y")

# Sidebar Title
ctk.CTkLabel(sidebar, text="🎬 Film Booking", font=("Arial", 18, "bold"), text_color="white").pack(pady=20, padx=20, anchor="w")

# Sidebar Buttons
menu_items = [
    "🏠 Home",
    "📅 Previous Bookings",
    "👤 Profile",
    "ℹ️ About",
]

for item in menu_items:
    btn = ctk.CTkButton(sidebar, text=item, font=("Arial", 14),
                        fg_color="transparent", text_color="white",
                        anchor="w", corner_radius=0, hover_color="#b71c1c", height=40)
    btn.pack(fill="x", pady=3)

# Logout Button
logout_btn = ctk.CTkButton(sidebar, text="📤 Logout", font=("Arial", 14),
                           fg_color="transparent", text_color="white",
                           anchor="w", corner_radius=0, hover_color="#b71c1c", height=40)
logout_btn.pack(fill="x", pady=20, side="bottom")

# ---------------- Main Content ----------------
main_content = ctk.CTkFrame(root, fg_color="black")
main_content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Title
ctk.CTkLabel(main_content, text="🎟 Your Previous Bookings", font=("Arial", 20, "bold"), text_color="white").pack(anchor="w", pady=10)

# ---------------- Movie Booking Cards ----------------
bookings = [
    ("Avengers: Endgame", "IMAX Cinemas", "March 5, 2025", "7:30 PM", "A1, A2, A3"),
    ("The Batman", "Cinepolis", "February 20, 2025", "6:00 PM", "B5, B6"),
    ("Interstellar", "PVR Cinemas", "January 15, 2025", "8:45 PM", "C2, C3, C4, C5")
]

for movie, theater, date, time, seats in bookings:
    card_frame = ctk.CTkFrame(main_content, fg_color="#1a1a1a", corner_radius=10)
    card_frame.pack(fill="x", pady=10, padx=10)

    text_frame = ctk.CTkFrame(card_frame, fg_color="#1a1a1a")
    text_frame.pack(side="left", padx=15, pady=10, fill="both", expand=True)

    ctk.CTkLabel(text_frame, text=movie, font=("Arial", 14, "bold"), text_color="white").pack(anchor="w")
    ctk.CTkLabel(text_frame, text=f"Theater: {theater}", font=("Arial", 12), text_color="gray").pack(anchor="w")
    ctk.CTkLabel(text_frame, text=f"Date: {date}", font=("Arial", 12), text_color="gray").pack(anchor="w")
    ctk.CTkLabel(text_frame, text=f"Time: {time}", font=("Arial", 12), text_color="gray").pack(anchor="w")
    ctk.CTkLabel(text_frame, text=f"Seats: {seats}", font=("Arial", 12), text_color="gray").pack(anchor="w")

    view_btn = ctk.CTkButton(card_frame, text="🎫 View Ticket", font=("Arial", 12, "bold"),
                             fg_color="red", text_color="white",
                             hover_color="#b71c1c", corner_radius=5, width=120)
    view_btn.pack(side="right", padx=20, pady=15)

# ---------------- Run Application ----------------
root.mainloop()
