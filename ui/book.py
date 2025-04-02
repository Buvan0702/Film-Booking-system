import customtkinter as ctk
from PIL import Image, ImageTk
import os
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Movie Details")
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

# Content container with padding
content_container = ctk.CTkFrame(main_content, fg_color="black")
content_container.pack(fill="both", expand=True, padx=40, pady=40)

# Movie content layout using grid
movie_content = ctk.CTkFrame(content_container, fg_color="black")
movie_content.pack(fill="both", expand=True)

# ---------------- Movie Poster ----------------
poster_frame = ctk.CTkFrame(movie_content, fg_color="black", width=300, height=450)
poster_frame.grid(row=0, column=0, padx=(0, 30), sticky="nw")
poster_frame.grid_propagate(False)  # Maintain size

# Load and display John Wick movie poster
try:
    img = Image.open("john_wick.jpg")
    img = img.resize((300, 450), Image.LANCZOS)
    movie_img = ImageTk.PhotoImage(img)
    img_label = ctk.CTkLabel(poster_frame, image=movie_img, text="")
    img_label.image = movie_img  # Keep a reference
    img_label.place(relx=0.5, rely=0.5, anchor="center")
except Exception as e:
    print(f"Error loading image: {e}")
    # Create a styled placeholder if image not found
    placeholder = ctk.CTkFrame(poster_frame, fg_color="#333333", corner_radius=10, width=300, height=450)
    placeholder.place(relx=0.5, rely=0.5, anchor="center")
    
    # Add placeholder text
    ctk.CTkLabel(
        placeholder, 
        text="John Wick", 
        font=("Arial", 20, "bold"), 
        text_color="white"
    ).place(relx=0.5, rely=0.5, anchor="center")

# ---------------- Movie Details ----------------
details_frame = ctk.CTkFrame(movie_content, fg_color="black")
details_frame.grid(row=0, column=1, sticky="nw")

# Movie title with large bold font
title_label = ctk.CTkLabel(
    details_frame, 
    text="Movie Title", 
    font=("Arial", 32, "bold"), 
    text_color="white"
)
title_label.pack(anchor="w", pady=(0, 10))

# Movie metadata (subtitle, genre, etc.)
metadata_label = ctk.CTkLabel(
    details_frame, 
    text="Subtitle | Genre | Duration | Rating", 
    font=("Arial", 16), 
    text_color="#aaaaaa"
)
metadata_label.pack(anchor="w", pady=(0, 20))

# Movie description
description_text = "This is a short description of the movie. It gives an overview of the plot and main themes."
description_label = ctk.CTkLabel(
    details_frame, 
    text=description_text, 
    font=("Arial", 16), 
    text_color="white",
    wraplength=600,
    justify="left"
)
description_label.pack(anchor="w", pady=(0, 30))

# Show times section
showtimes_label = ctk.CTkLabel(
    details_frame, 
    text="Show Times:", 
    font=("Arial", 18, "bold"), 
    text_color="white"
)
showtimes_label.pack(anchor="w", pady=(0, 15))

# Show times
times = ["1:00 PM", "3:30 PM", "6:00 PM", "8:30 PM"]
for time in times:
    time_label = ctk.CTkLabel(
        details_frame, 
        text=time, 
        font=("Arial", 16), 
        text_color="white"
    )
    time_label.pack(anchor="w", pady=(0, 8))

# Book ticket button with proper styling
book_btn = ctk.CTkButton(
    details_frame, 
    text="Book Ticket", 
    font=("Arial", 16, "bold"),
    fg_color="#d92525", 
    text_color="white", 
    hover_color="#b71c1c", 
    corner_radius=5, 
    height=40,
    width=150
)
book_btn.pack(anchor="w", pady=(20, 0))

# Function to handle booking
def book_ticket():
    print("Booking ticket")
    # Implement booking functionality here

book_btn.configure(command=book_ticket)

# ---------------- Run Application ----------------
if __name__ == "__main__":
    # Create image directory if it doesn't exist
    if not os.path.exists("images"):
        os.makedirs("images")
        print("Created 'images' directory for movie posters")
    
    root.mainloop()