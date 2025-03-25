import customtkinter as ctk

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Select Your Seats")
root.geometry("1200x600")  # Fixed window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = ctk.CTkFrame(root, fg_color="#d92525", width=250, height=600)
sidebar.pack(side="left", fill="y")

# Sidebar Title
ctk.CTkLabel(sidebar, text="Film Booking", font=("Arial", 18, "bold"), text_color="white").pack(pady=20, padx=20, anchor="w")

# Sidebar Buttons
menu_items = [
    "🏠  Home",
    "📅  Previous Bookings",
    "👤  Profile",
    "ℹ️  About",
]
for item in menu_items:
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
ctk.CTkLabel(main_content, text="Select Your Seats", font=("Arial", 22, "bold"), text_color="white").pack(anchor="n", pady=5)

# Sub-title (Show Timings)
ctk.CTkLabel(main_content, text="Show Timings:", font=("Arial", 14, "bold"), text_color="white").pack(anchor="n")

# Show Timings Buttons
timing_frame = ctk.CTkFrame(main_content, fg_color="black")
timing_frame.pack(pady=5)

show_timings = ["1:00 PM", "3:30 PM", "6:00 PM", "8:30 PM"]
selected_time = ctk.StringVar(value=show_timings[0])

for time in show_timings:
    btn = ctk.CTkButton(timing_frame, text=time, font=("Arial", 12, "bold"),
                        fg_color="red", text_color="white", hover_color="#b71c1c",
                        width=80, height=30,
                        command=lambda t=time: selected_time.set(t))
    btn.pack(side="left", padx=10)

# Screen Label
ctk.CTkLabel(main_content, text="SCREEN", font=("Arial", 14, "bold"), text_color="white",
             fg_color="red", width=450, height=30, corner_radius=10).pack(pady=10)

# ---------------- Seats Layout ----------------
seat_frame = ctk.CTkFrame(main_content, fg_color="black")
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

selected_seats = set()

# Function to handle seat selection
def toggle_seat(seat, button):
    if seat_status.get(seat, "available") == "unavailable":
        return  # Ignore clicks on unavailable seats
    
    if seat in selected_seats:
        selected_seats.remove(seat)
        button.configure(fg_color=seat_colors["available"])  # Reset to Green
    else:
        selected_seats.add(seat)
        button.configure(fg_color=seat_colors["selected"])  # Change to Yellow

for row in seat_layout:
    row_frame = ctk.CTkFrame(seat_frame, fg_color="black")
    row_frame.pack()
    for seat in row:
        color = seat_colors.get(seat_status.get(seat, "available"))  # Default to "available" (Green)
        btn = ctk.CTkButton(row_frame, text=seat, font=("Arial", 12, "bold"),
                            fg_color=color, text_color="white", hover_color=color,
                            width=50, height=40,
                            command=lambda s=seat, b=None: toggle_seat(s, b))
        btn.pack(side="left", padx=5, pady=5)
        btn.command = lambda s=seat, b=btn: toggle_seat(s, b)  # Fix command issue

# ---------------- Proceed to Checkout Button ----------------
checkout_btn = ctk.CTkButton(main_content, text="🎟️ Proceed to Checkout", font=("Arial", 14, "bold"),
                             fg_color="red", text_color="white", hover_color="#b71c1c",
                             corner_radius=10, height=40)
checkout_btn.pack(pady=20)

# ---------------- Run Application ----------------
root.mainloop()
