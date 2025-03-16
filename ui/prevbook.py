import tkinter as tk
from tkinter import ttk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("Film Booking - Previous Bookings")
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

# Title
tk.Label(main_content, text="Your Previous Bookings", font=("Arial", 18, "bold"), fg="white", bg="black").pack(anchor="w", pady=10)

# ---------------- Movie Booking Cards ----------------
bookings = [
    ("Avengers: Endgame", "IMAX Cinemas", "March 5, 2025", "7:30 PM", "A1, A2, A3"),
    ("The Batman", "Cinepolis", "February 20, 2025", "6:00 PM", "B5, B6"),
    ("Interstellar", "PVR Cinemas", "January 15, 2025", "8:45 PM", "C2, C3, C4, C5")
]

for movie, theater, date, time, seats in bookings:
    card_frame = tk.Frame(main_content, bg="#1a1a1a", padx=10, pady=10)
    card_frame.pack(fill="x", pady=10)

    tk.Label(card_frame, text=movie, font=("Arial", 12, "bold"), fg="white", bg="#1a1a1a").pack(anchor="w")
    tk.Label(card_frame, text=f"Theater: {theater}", font=("Arial", 10), fg="gray", bg="#1a1a1a").pack(anchor="w")
    tk.Label(card_frame, text=f"Date: {date}", font=("Arial", 10), fg="gray", bg="#1a1a1a").pack(anchor="w")
    tk.Label(card_frame, text=f"Time: {time}", font=("Arial", 10), fg="gray", bg="#1a1a1a").pack(anchor="w")
    tk.Label(card_frame, text=f"Seats: {seats}", font=("Arial", 10), fg="gray", bg="#1a1a1a").pack(anchor="w")

    view_btn = tk.Button(card_frame, text="View Ticket", font=("Arial", 10, "bold"), fg="white", bg="red",
                         relief="flat", padx=10, pady=2, activebackground="#b71c1c")
    view_btn.pack(anchor="e", pady=5)

# ---------------- Run Application ----------------
root.mainloop()
