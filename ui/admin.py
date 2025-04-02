import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
from PIL import Image, ImageTk
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Admin Dashboard")
root.geometry("1280x720")  # Adjusted window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = ctk.CTkFrame(root, fg_color="#d92525", width=300, corner_radius=0)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)  # Prevent the frame from shrinking

# Sidebar Title
ctk.CTkLabel(sidebar, text="Film Booking", font=("Arial", 28, "bold"), text_color="white").pack(pady=(40, 50), padx=20, anchor="w")

# Active indicator for admin dashboard (first option)
active_indicator = ctk.CTkFrame(sidebar, fg_color="white", width=5, height=40, corner_radius=0)
active_indicator.place(x=0, y=150)  # Position next to the Admin Dashboard button

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
admin_btn = create_sidebar_button(sidebar, "Admin Dashboard", "📊", 150, is_active=True)
bookings_btn = create_sidebar_button(sidebar, "Manage Bookings", "🎟️", 200)
users_btn = create_sidebar_button(sidebar, "Manage User", "👤", 250)
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
title_label = ctk.CTkLabel(
    content_container, 
    text="Admin Dashboard Overview", 
    font=("Arial", 28, "bold"), 
    text_color="white"
)
title_label.pack(anchor="w", pady=(0, 30))

# ---------------- Top Stats Cards ----------------
stats_frame = ctk.CTkFrame(content_container, fg_color="transparent")
stats_frame.pack(fill="x", pady=(0, 30))

# Function to create stat cards
def create_stat_card(parent, title, value, value_color, subtitle=None):
    card = ctk.CTkFrame(parent, fg_color="#2a2a2a", corner_radius=10, height=120)
    card.pack(side="left", fill="both", expand=True, padx=10)
    card.pack_propagate(False)  # Keep fixed height
    
    # Center the content vertically
    center_frame = ctk.CTkFrame(card, fg_color="transparent")
    center_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=1)
    
    # Title
    title_label = ctk.CTkLabel(
        center_frame, 
        text=title, 
        font=("Arial", 16), 
        text_color="white"
    )
    title_label.pack(anchor="center")
    
    # Value with color
    value_label = ctk.CTkLabel(
        center_frame, 
        text=value, 
        font=("Arial", 28, "bold"), 
        text_color=value_color
    )
    value_label.pack(anchor="center", pady=(5, 0))
    
    # Optional subtitle (like "Last 30 Days")
    if subtitle:
        subtitle_label = ctk.CTkLabel(
            center_frame, 
            text=subtitle, 
            font=("Arial", 12), 
            text_color="#aaaaaa"
        )
        subtitle_label.pack(anchor="center", pady=(5, 0))
    
    return card

# Create the three stat cards
tickets_card = create_stat_card(stats_frame, "Total Tickets Sold", "12,450", "#ff5252", "Last 30 Days")
movie_card = create_stat_card(stats_frame, "Best Rated Movie", "Interstellar (9.2/10)", "#ffd700")
revenue_card = create_stat_card(stats_frame, "Revenue Generated", "$125,800", "#4caf50", "Last 30 Days")

# ---------------- Charts Section ----------------
charts_frame = ctk.CTkFrame(content_container, fg_color="transparent")
charts_frame.pack(fill="both", expand=True, pady=(0, 0))

# Function to create chart cards
def create_chart_card(parent, title, width_ratio=0.5):
    card = ctk.CTkFrame(parent, fg_color="#2a2a2a", corner_radius=10)
    card.pack(side="left", fill="both", expand=True, padx=10)
    
    # Title
    title_label = ctk.CTkLabel(
        card, 
        text=title, 
        font=("Arial", 18, "bold"), 
        text_color="white"
    )
    title_label.pack(anchor="w", padx=20, pady=15)
    
    # Chart placeholder frame
    chart_frame = ctk.CTkFrame(card, fg_color="#222222", corner_radius=5)
    chart_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # Placeholder image for chart
    placeholder_label = ctk.CTkLabel(
        chart_frame,
        text="Chart Placeholder (400 x 200)",
        font=("Arial", 14),
        text_color="#aaaaaa"
    )
    placeholder_label.place(relx=0.5, rely=0.5, anchor="center")
    
    return card, chart_frame

# Create two chart cards
sales_card, sales_chart_frame = create_chart_card(charts_frame, "Ticket Sales Over Time")
genres_card, genres_chart_frame = create_chart_card(charts_frame, "Most Watched Genres")

# Function to create charts using matplotlib
def create_sales_chart(parent):
    # Sample data
    weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
    tickets = [1200, 1500, 1300, 1800]
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
    fig.patch.set_facecolor('#222222')
    ax.set_facecolor('#222222')
    
    # Create bar chart
    bars = ax.bar(weeks, tickets, color='#d92525', width=0.6)
    
    # Customize appearance
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#555555')
    ax.spines['left'].set_color('#555555')
    
    ax.tick_params(colors='white', which='both')
    ax.set_ylabel('Tickets Sold', color='white')
    
    # Add data labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 50,
                f'{height}', ha='center', va='bottom', color='white')
    
    # Remove the placeholder label
    for widget in parent.winfo_children():
        widget.destroy()
    
    # Add the chart to the frame
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    
    return canvas

def create_genres_chart(parent):
    # Sample data
    genres = ["Action", "Drama", "Comedy", "Sci-Fi"]
    views = [3400, 2900, 2500, 2700]
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
    fig.patch.set_facecolor('#222222')
    ax.set_facecolor('#222222')
    
    # Create bar chart with a different color
    bars = ax.bar(genres, views, color='#ffd700', width=0.6)
    
    # Customize appearance
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#555555')
    ax.spines['left'].set_color('#555555')
    
    ax.tick_params(colors='white', which='both')
    ax.set_ylabel('Total Views', color='white')
    
    # Add data labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 100,
                f'{height}', ha='center', va='bottom', color='white')
    
    # Remove the placeholder label
    for widget in parent.winfo_children():
        widget.destroy()
    
    # Add the chart to the frame
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    
    return canvas

# Create the actual charts
sales_canvas = create_sales_chart(sales_chart_frame)
genres_canvas = create_genres_chart(genres_chart_frame)

# Function to refresh data
def refresh_data():
    print("Refreshing dashboard data...")
    # Here you would update the data from your database
    # and then update the UI elements

# ---------------- Run Application ----------------
if __name__ == "__main__":
    root.mainloop()