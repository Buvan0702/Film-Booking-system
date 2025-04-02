import customtkinter as ctk
from PIL import Image, ImageTk
import os
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Homepage")
root.geometry("1920x1080")  # Adjusted window size
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

# Title
ctk.CTkLabel(
    content_container, 
    text="Welcome to Film Booking", 
    font=("Arial", 32, "bold"), 
    text_color="white"
).pack(anchor="w", pady=(0, 10))

# Subtitle
ctk.CTkLabel(
    content_container, 
    text="Browse and book your favorite movies", 
    font=("Arial", 16), 
    text_color="#cccccc"
).pack(anchor="w", pady=(0, 40))

# ---------------- Now Showing ----------------
ctk.CTkLabel(
    content_container, 
    text="Now Showing", 
    font=("Arial", 24, "bold"), 
    text_color="white"
).pack(anchor="w", pady=(0, 20))

# Movie Poster Frame - use grid for better alignment
movie_frame = ctk.CTkFrame(content_container, fg_color="black")
movie_frame.pack(fill="x", pady=(0, 50))

# Movie data - title and image path
movies = [
    {"title": "John Wick", "path": "john_wick.jpg"},
    {"title": "Rocky", "path": "rocky.jpg"},
    {"title": "Blade Runner 2049", "path": "blade_runner.jpg"},
    {"title": "Rocky IV", "path": "rocky4.jpg"}
]

# Function to create clickable movie posters
def create_movie_poster(parent, title, image_path, index):
    frame = ctk.CTkFrame(parent, fg_color="black", corner_radius=10)
    frame.grid(row=0, column=index, padx=15)
    
    try:
        img = Image.open(image_path)
        img = img.resize((180, 250))  # Larger poster size
        photo = ImageTk.PhotoImage(img)
    except Exception as e:
        # Create placeholder with movie title if image not found
        photo = None
        print(f"Could not load image {image_path}: {e}")
    
    if photo:
        poster = ctk.CTkLabel(frame, image=photo, text="")
        poster.image = photo  # Keep a reference to prevent garbage collection
    else:
        # Create a placeholder with gradient background
        poster = ctk.CTkLabel(
            frame, 
            text=title,
            font=("Arial", 16, "bold"),
            width=180,
            height=250,
            corner_radius=10,
            fg_color="#333333",
            text_color="white"
        )
    
    poster.pack(padx=0, pady=0)
    
    # Make poster clickable
    poster.bind("<Button-1>", lambda e: print(f"Selected movie: {title}"))
    
    # Hover effect
    def on_enter(e):
        frame.configure(fg_color="#333333")
        poster.configure(fg_color="#444444")
    def on_leave(e):
        frame.configure(fg_color="black")
        if not photo:
            poster.configure(fg_color="#333333")
        else:
            poster.configure(fg_color="transparent")
    
    poster.bind("<Enter>", on_enter)
    poster.bind("<Leave>", on_leave)
    
    return frame

# Create movie posters
for i, movie in enumerate(movies):
    create_movie_poster(movie_frame, movie["title"], movie["path"], i)

# ---------------- Featured Theaters ----------------
ctk.CTkLabel(
    content_container, 
    text="Featured Theaters", 
    font=("Arial", 24, "bold"), 
    text_color="white"
).pack(anchor="w", pady=(0, 20))

# Theater container
theater_container = ctk.CTkFrame(content_container, fg_color="black")
theater_container.pack(fill="x")

# Theater data
theaters = [
    {"name": "Theater 1", "location": "Location: City Center"},
    {"name": "Theater 2", "location": "Location: Downtown"},
    {"name": "Theater 3", "location": "Location: Mall"}
]

# Function to create theater items
def create_theater_item(parent, name, location, index):
    # Create circular frame for film icon
    frame = ctk.CTkFrame(parent, fg_color="black")
    frame.grid(row=0, column=index, padx=30)
    
    # Circular background for icon
    circle = ctk.CTkFrame(frame, width=100, height=100, corner_radius=50, fg_color="#333333")
    circle.pack(pady=(0, 10))
    circle.pack_propagate(False)
    
    # Film icon in circle
    icon = ctk.CTkLabel(circle, text="🎬", font=("Arial", 40), text_color="white")
    icon.place(relx=0.5, rely=0.5, anchor="center")
    
    # Theater name
    name_label = ctk.CTkLabel(frame, text=name, font=("Arial", 18, "bold"), text_color="white")
    name_label.pack()
    
    # Location
    location_label = ctk.CTkLabel(frame, text=location, font=("Arial", 14), text_color="#cccccc")
    location_label.pack()
    
    # Make clickable
    def on_click(e):
        print(f"Selected theater: {name}")
    
    circle.bind("<Button-1>", on_click)
    icon.bind("<Button-1>", on_click)
    name_label.bind("<Button-1>", on_click)
    location_label.bind("<Button-1>", on_click)
    
    # Hover effect
    def on_enter(e):
        circle.configure(fg_color="#555555")
    def on_leave(e):
        circle.configure(fg_color="#333333")
    
    circle.bind("<Enter>", on_enter)
    circle.bind("<Leave>", on_leave)
    icon.bind("<Enter>", on_enter)
    icon.bind("<Leave>", on_leave)
    
    return frame

# Create theater items
for i, theater in enumerate(theaters):
    create_theater_item(theater_container, theater["name"], theater["location"], i)

# Function to handle navigation to other screens
def navigate_to(screen_name):
    print(f"Navigating to {screen_name} screen")
    # Here you can implement the actual navigation logic
    # For example, hide current screen and show the requested one

# ---------------- Run Application ----------------
if __name__ == "__main__":
    # Check if image directory exists, create it if not
    if not os.path.exists("images"):
        os.makedirs("images")
        print("Created 'images' directory. Please add movie poster images.")
    
    root.mainloop()