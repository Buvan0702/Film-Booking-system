import customtkinter as ctk
import os
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Select Your Seats")
root.geometry("1280x720")  # Adjusted window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = ctk.CTkFrame(root, fg_color="#d92525", width=300, corner_radius=0)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)  # Prevent the frame from shrinking

# Sidebar Title
ctk.CTkLabel(sidebar, text="Film Booking", font=("Arial", 28, "bold"), text_color="white").pack(pady=(40, 50), padx=20, anchor="w")

# Active indicator for home button
active_indicator = ctk.CTkFrame(sidebar, fg_color="white", width=5, height=40, corner_radius=0)
active_indicator.place(x=0, y=150)  # Position next to the Home button

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
home_btn = create_sidebar_button(sidebar, "Home", "🏠", 150, is_active=True)
bookings_btn = create_sidebar_button(sidebar, "Previous Bookings", "📅", 200)
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

# Center the content vertically and horizontally
content_container = ctk.CTkFrame(main_content, fg_color="black")
content_container.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = ctk.CTkLabel(
    content_container, 
    text="Select Your Seats", 
    font=("Arial", 28, "bold"), 
    text_color="white"
)
title_label.pack(pady=(0, 20))

# Show Timings Section
timing_container = ctk.CTkFrame(content_container, fg_color="black")
timing_container.pack(pady=(0, 30))

timing_label = ctk.CTkLabel(
    timing_container, 
    text="Show Timings:", 
    font=("Arial", 18, "bold"), 
    text_color="white"
)
timing_label.pack(pady=(0, 15))

# Time buttons container
time_buttons_frame = ctk.CTkFrame(timing_container, fg_color="black")
time_buttons_frame.pack()

# Selected time tracker
selected_time = ctk.StringVar(value="3:30 PM")  # Default selected time

# Function to handle time selection
def select_time(time):
    selected_time.set(time)
    
    # Update button appearances
    for t, btn in time_buttons.items():
        if t == time:
            btn.configure(fg_color="#b71c1c")  # Darker red for selected
        else:
            btn.configure(fg_color="#d92525")  # Normal red for unselected

# Create time buttons
show_timings = ["1:00 PM", "3:30 PM", "6:00 PM", "8:30 PM"]
time_buttons = {}

for time in show_timings:
    is_selected = time == selected_time.get()
    btn = ctk.CTkButton(
        time_buttons_frame, 
        text=time, 
        font=("Arial", 14, "bold"),
        fg_color="#b71c1c" if is_selected else "#d92525",  # Selected time is darker
        text_color="white", 
        hover_color="#951616",
        width=100, 
        height=40,
        corner_radius=5,
        command=lambda t=time: select_time(t)
    )
    btn.pack(side="left", padx=10)
    time_buttons[time] = btn

# Screen display
screen_label = ctk.CTkLabel(
    content_container, 
    text="SCREEN", 
    font=("Arial", 16, "bold"), 
    text_color="white",
    fg_color="#d92525",  # Red background
    width=700,  # Wider screen
    height=40,
    corner_radius=0
)
screen_label.pack(pady=(0, 40))

# Seat grid container
seat_grid = ctk.CTkFrame(content_container, fg_color="black")
seat_grid.pack(pady=(0, 30))

# Seat statuses and colors
seat_colors = {
    "available": "#008000",   # Green
    "selected": "#FFD700",    # Yellow
    "unavailable": "#808080"  # Gray
}

# Define seat statuses based on the image
seat_status = {
    "A3": "unavailable", "A6": "unavailable", "A10": "unavailable",
    "B3": "selected", "B6": "unavailable", "B10": "unavailable"
}

# Track selected seats
selected_seats = {"B3"}  # B3 is pre-selected as shown in the image

# Function to toggle seat selection
def toggle_seat(seat, button):
    if seat_status.get(seat, "available") == "unavailable":
        return  # Ignore clicks on unavailable seats
    
    current_status = "selected" if seat in selected_seats else "available"
    
    if current_status == "selected":
        selected_seats.remove(seat)
        button.configure(fg_color=seat_colors["available"])
    else:
        selected_seats.add(seat)
        button.configure(fg_color=seat_colors["selected"])
    
    # Update the "Proceed to Checkout" button based on selection
    if selected_seats:
        checkout_btn.configure(state="normal", fg_color="#d92525", hover_color="#b71c1c")
    else:
        checkout_btn.configure(state="disabled", fg_color="#999999", hover_color="#999999")
    
    # Print selected seats for debugging
    print(f"Selected seats: {selected_seats}")

# Create the seat grid
rows = ["A", "B"]
columns = list(range(1, 11))

# Create a dictionary to store seat buttons
seat_buttons = {}

# Create each row of seats
for i, row in enumerate(rows):
    row_frame = ctk.CTkFrame(seat_grid, fg_color="black")
    row_frame.pack(pady=5)
    
    for col in columns:
        seat_id = f"{row}{col}"
        status = seat_status.get(seat_id, "available")
        
        # Determine seat color based on status
        if status == "unavailable":
            color = seat_colors["unavailable"]
        elif status == "selected":
            color = seat_colors["selected"]
        else:
            color = seat_colors["available"]
        
        # Create the seat button
        seat_btn = ctk.CTkButton(
            row_frame,
            text=seat_id,
            font=("Arial", 14, "bold"),
            fg_color=color,
            text_color="white",
            hover_color=color if status == "unavailable" else "#005000" if status == "available" else "#DAA520",
            width=50,
            height=50,
            corner_radius=5
        )
        seat_btn.pack(side="left", padx=5)
        
        # Store button reference and add command if seat is available
        seat_buttons[seat_id] = seat_btn
        
        if status != "unavailable":
            seat_btn.configure(command=lambda s=seat_id, b=seat_btn: toggle_seat(s, b))

# Create the "Proceed to Checkout" button
checkout_btn = ctk.CTkButton(
    content_container,
    text="Proceed to Checkout",
    font=("Arial", 16, "bold"),
    fg_color="#d92525",  # Red background
    text_color="white",
    hover_color="#b71c1c",
    corner_radius=5,
    height=45,
    width=200
)
checkout_btn.pack(pady=20)

# Enable checkout button only if seats are selected
if not selected_seats:
    checkout_btn.configure(state="disabled", fg_color="#999999", hover_color="#999999")

# Function to handle checkout process
def proceed_to_checkout():
    print(f"Proceeding to checkout with seats: {selected_seats}")
    # Add checkout functionality here

checkout_btn.configure(command=proceed_to_checkout)

# Start the application
if __name__ == "__main__":
    root.mainloop()