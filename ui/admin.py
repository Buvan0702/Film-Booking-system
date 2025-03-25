import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("dark")  # Dark Mode
root = ctk.CTk()
root.title("Film Booking - Admin Dashboard")
root.geometry("1100x600")  # Fixed window size
root.resizable(False, False)  # Prevent resizing

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = ctk.CTkFrame(root, fg_color="#d92525", width=250, height=600)
sidebar.pack(side="left", fill="y")

# Sidebar Title
ctk.CTkLabel(sidebar, text="🎬 Film Booking", font=("Arial", 18, "bold"), text_color="white").pack(pady=20, padx=20, anchor="w")

# Sidebar Buttons
menu_items = [
    "📅 Admin Dashboard",
    "🎟 Manage Bookings",
    "👤 Manage Users",
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

# Header Title
ctk.CTkLabel(main_content, text="📊 Admin Dashboard Overview", font=("Arial", 22, "bold"), text_color="white").pack(anchor="w", pady=5)

# ---------------- Top Analytics Cards ----------------
analytics_frame = ctk.CTkFrame(main_content, fg_color="black")
analytics_frame.pack(fill="x", pady=10)

cards = [
    ("Total Tickets Sold", "12,450", "red", "Last 30 Days"),
    ("Best Rated Movie", "Interstellar (9.2/10)", "yellow", ""),
    ("Revenue Generated", "$125,800", "green", "Last 30 Days"),
]

for title, value, color, subtitle in cards:
    card = ctk.CTkFrame(analytics_frame, fg_color="gray15", corner_radius=10, height=100)
    card.pack(side="left", expand=True, padx=10, fill="both")

    ctk.CTkLabel(card, text=title, font=("Arial", 12, "bold"), text_color="white").pack(anchor="w", padx=10, pady=5)
    ctk.CTkLabel(card, text=value, font=("Arial", 16, "bold"), text_color=color).pack(anchor="w", padx=10)
    if subtitle:
        ctk.CTkLabel(card, text=subtitle, font=("Arial", 10), text_color="gray").pack(anchor="w", padx=10)

# ---------------- Graphs Section ----------------
graph_frame = ctk.CTkFrame(main_content, fg_color="black")
graph_frame.pack(fill="both", pady=20)

# Matplotlib Graphs
def create_chart(frame, title, x_data, y_data, color):
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.bar(x_data, y_data, color=color)
    ax.set_title(title, fontsize=10, color="white")
    ax.tick_params(colors="white")
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()

# Sales Chart
sales_frame = ctk.CTkFrame(graph_frame, fg_color="gray15", corner_radius=10, height=200)
sales_frame.pack(side="left", expand=True, padx=10, fill="both")
create_chart(sales_frame, "🎟 Ticket Sales Over Time", ["Week 1", "Week 2", "Week 3", "Week 4"], [1200, 1500, 1300, 1800], "red")

# Genre Popularity Chart
genre_frame = ctk.CTkFrame(graph_frame, fg_color="gray15", corner_radius=10, height=200)
genre_frame.pack(side="left", expand=True, padx=10, fill="both")
create_chart(genre_frame, "🎬 Most Watched Genres", ["Action", "Drama", "Comedy", "Sci-Fi"], [3400, 2900, 2500, 2700], "yellow")

# ---------------- Run Application ----------------
root.mainloop()
