import tkinter as tk
from tkinter import ttk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("Film Booking - Select Your Seats")
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
tk.Label(main_content, text="Select Your Seats", font=("Arial", 18, "bold"), fg="white", bg="black").pack(anchor="n", pady=5)

# Sub-title (Show Timings)
tk.Label(main_content, text="Show Timings:", font=("Arial", 12, "bold"), fg="white", bg="black").pack(anchor="n")

# Show Timings Buttons
timing_frame = tk.Frame(main_content, bg="black")
timing_frame.pack(pady=5)

show_timings = ["1:00 PM", "3:30 PM", "6:00 PM", "8:30 PM"]
for time in show_timings:
    btn = tk.Button(timing_frame, text=time, font=("Arial", 10, "bold"), fg="white", bg="red",
                    relief="flat", padx=15, pady=5, activebackground="#b71c1c")
    btn.pack(side="left", padx=10)

# Screen Label
tk.Label(main_content, text="SCREEN", font=("Arial", 12, "bold"), fg="white", bg="red", width=50, pady=5).pack(pady=10)

# ---------------- Seats Layout ----------------
seat_frame = tk.Frame(main_content, bg="black")
seat_frame.pack()

seat_layout = [
    ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"],
    ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]
]

seat_colors = {
    "available": "#008000",  # Green
    "selected": "#FFD700",   # Yellow
    "unavailable": "#808080" # Gray
}

seat_status = {
    "A3": "unavailable", "A6": "unavailable", "A10": "unavailable",
    "B3": "selected", "B6": "unavailable", "B10": "unavailable"
}

for row in seat_layout:
    row_frame = tk.Frame(seat_frame, bg="black")
    row_frame.pack()
    for seat in row:
        color = seat_colors.get(seat_status.get(seat, "available"))  # Default to "available" (Green)
        btn = tk.Button(row_frame, text=seat, font=("Arial", 10, "bold"), fg="white", bg=color,
                        relief="flat", padx=10, pady=5, activebackground=color)
        btn.pack(side="left", padx=5, pady=5)

# ---------------- Proceed to Checkout Button ----------------
checkout_btn = tk.Button(main_content, text="Proceed to Checkout", font=("Arial", 12, "bold"), fg="white", bg="red",
                         relief="flat", padx=20, pady=8, activebackground="#b71c1c")
checkout_btn.pack(pady=20)

# ---------------- Run Application ----------------
root.mainloop()
