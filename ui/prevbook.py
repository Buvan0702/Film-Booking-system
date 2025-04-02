import customtkinter as ctk
import os
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Previous Bookings")
root.geometry("1920x1080")  # Adjusted window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = ctk.CTkFrame(root, fg_color="#d92525", width=300, corner_radius=0)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)  # Prevent the frame from shrinking

# Sidebar Title
ctk.CTkLabel(sidebar, text="Film Booking", font=("Arial", 28, "bold"), text_color="white").pack(pady=(40, 50), padx=20, anchor="w")

# Active indicator for previous bookings button (second option)
active_indicator = ctk.CTkFrame(sidebar, fg_color="white", width=5, height=40, corner_radius=0)
active_indicator.place(x=0, y=200)  # Position next to the Previous Bookings button

# Sidebar Buttons with proper styling and positioning
def create_sidebar_button(parent, text, icon, y_position, is_active=False):
    button_frame = ctk.CTkFrame(parent, fg_color="transparent", height=40)
    button_frame.pack(fill="x", pady=3)
    button_frame.pack_propagate(False)  # Maintain the height
    
    # Icon and text in the button
    icon_label = ctk.CTkLabel(button_frame, text=icon, font=("Arial", 16), text_color="white", width=30)
    icon_label.pack(side="left", padx=(20, 10))
    
    text_label = ctk.CTkLabel(button_frame, text=text, font=("Arial", 16), text_color="white", anchor="w")
    text_label.pack(side="left", fill="x", expand=True)
    
    # Make the whole frame clickable
    button_frame.bind("<Button-1>", lambda e: print(f"Clicked on {text}"))
    icon_label.bind("<Button-1>", lambda e: print(f"Clicked on {text}"))
    text_label.bind("<Button-1>", lambda e: print(f"Clicked on {text}"))
    
    # Hover effect
    def on_enter(e):
        button_frame.configure(fg_color="#b71c1c")
    def on_leave(e):
        button_frame.configure(fg_color="transparent" if not is_active else "#b71c1c")
    
    button_frame.bind("<Enter>", on_enter)
    button_frame.bind("<Leave>", on_leave)
    icon_label.bind("<Enter>", on_enter)
    icon_label.bind("<Leave>", on_leave)
    text_label.bind("<Enter>", on_enter)
    text_label.bind("<Leave>", on_leave)
    
    # Set active state
    if is_active:
        button_frame.configure(fg_color="#b71c1c")
    
    return button_frame

# Create menu buttons
home_btn = create_sidebar_button(sidebar, "Home", "🏠", 150)
bookings_btn = create_sidebar_button(sidebar, "Previous Bookings", "📅", 200, is_active=True)
profile_btn = create_sidebar_button(sidebar, "Profile", "👤", 250)
about_btn = create_sidebar_button(sidebar, "About", "ℹ️", 300)

# Logout button at bottom
logout_frame = ctk.CTkFrame(sidebar, fg_color="transparent", height=40)
logout_frame.pack(side="bottom", fill="x", pady=(0, 30))
logout_frame.pack_propagate(False)

logout_icon = ctk.CTkLabel(logout_frame, text="📤", font=("Arial", 16), text_color="white", width=30)
logout_icon.pack(side="left", padx=(20, 10))

logout_text = ctk.CTkLabel(logout_frame, text="Logout", font=("Arial", 16), text_color="white", anchor="w")
logout_text.pack(side="left")

# Hover effect for logout
def on_enter_logout(e):
    logout_frame.configure(fg_color="#b71c1c")
def on_leave_logout(e):
    logout_frame.configure(fg_color="transparent")

logout_frame.bind("<Enter>", on_enter_logout)
logout_frame.bind("<Leave>", on_leave_logout)
logout_icon.bind("<Enter>", on_enter_logout)
logout_icon.bind("<Leave>", on_leave_logout)
logout_text.bind("<Enter>", on_enter_logout)
logout_text.bind("<Leave>", on_leave_logout)

# ---------------- Main Content ----------------
main_content = ctk.CTkFrame(root, fg_color="black", corner_radius=0)
main_content.pack(side="right", fill="both", expand=True)

# Content container with padding
content_container = ctk.CTkFrame(main_content, fg_color="black")
content_container.pack(fill="both", expand=True, padx=40, pady=40)

# Main Title
title_label = ctk.CTkLabel(
    content_container,
    text="Your Previous Bookings",
    font=("Arial", 32, "bold"),
    text_color="white"
)
title_label.pack(anchor="w", pady=(0, 30))

# Function to create booking cards
def create_booking_card(parent, movie, theater, date, time, seats):
    # Main card frame with dark gray background
    card = ctk.CTkFrame(
        parent,
        fg_color="#222222",
        corner_radius=10,
        height=120
    )
    card.pack(fill="x", pady=10)
    card.pack_propagate(False)  # Maintain consistent height
    
    # Content frame for movie details
    content = ctk.CTkFrame(card, fg_color="transparent")
    content.pack(side="left", fill="both", expand=True, padx=20, pady=15)
    
    # Movie title
    movie_title = ctk.CTkLabel(
        content,
        text=movie,
        font=("Arial", 20, "bold"),
        text_color="white",
        anchor="w"
    )
    movie_title.pack(anchor="w")
    
    # Movie details (theater, date, time, seats)
    details_frame = ctk.CTkFrame(content, fg_color="transparent")
    details_frame.pack(fill="x", pady=(5, 0))
    
    # Theater info
    theater_label = ctk.CTkLabel(
        details_frame,
        text=f"Theater: {theater}",
        font=("Arial", 14),
        text_color="#aaaaaa",
        anchor="w"
    )
    theater_label.pack(anchor="w")
    
    # Date info
    date_label = ctk.CTkLabel(
        details_frame,
        text=f"Date: {date}",
        font=("Arial", 14),
        text_color="#aaaaaa",
        anchor="w"
    )
    date_label.pack(anchor="w")
    
    # Time info
    time_label = ctk.CTkLabel(
        details_frame,
        text=f"Time: {time}",
        font=("Arial", 14),
        text_color="#aaaaaa",
        anchor="w"
    )
    time_label.pack(anchor="w")
    
    # Seats info
    seats_label = ctk.CTkLabel(
        details_frame,
        text=f"Seats: {seats}",
        font=("Arial", 14),
        text_color="#aaaaaa",
        anchor="w"
    )
    seats_label.pack(anchor="w")
    
    # View ticket button
    view_btn = ctk.CTkButton(
        card,
        text="View Ticket",
        font=("Arial", 14, "bold"),
        fg_color="#d92525",
        text_color="white",
        hover_color="#b71c1c",
        corner_radius=5,
        width=120,
        height=40,
        command=lambda m=movie: view_ticket(m)
    )
    view_btn.pack(side="right", padx=20)
    
    return card

# Function to handle viewing ticket
def view_ticket(movie):
    print(f"Viewing ticket for {movie}")
    # Add functionality to display ticket

# Sample booking data
bookings = [
    {
        "movie": "Avengers: Endgame",
        "theater": "IMAX Cinemas",
        "date": "March 5, 2025",
        "time": "7:30 PM",
        "seats": "A1, A2, A3"
    },
    {
        "movie": "The Batman",
        "theater": "Cinepolis",
        "date": "February 20, 2025",
        "time": "6:00 PM",
        "seats": "B5, B6"
    },
    {
        "movie": "Interstellar",
        "theater": "PVR Cinemas",
        "date": "January 15, 2025",
        "time": "8:45 PM",
        "seats": "C2, C3, C4, C5"
    }
]

# Create booking cards for each booking
for booking in bookings:
    create_booking_card(
        content_container,
        booking["movie"],
        booking["theater"],
        booking["date"],
        booking["time"],
        booking["seats"]
    )

# Start the application
if __name__ == "__main__":
    root.mainloop()