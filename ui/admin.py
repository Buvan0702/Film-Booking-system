import tkinter as tk
from tkinter import ttk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("Film Booking - Admin Dashboard")
root.geometry("1100x600")  # Fixed window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="black")  # Dark mode theme

# ---------------- Sidebar (Red Navigation Panel) ----------------
sidebar = tk.Frame(root, bg="#d92525", width=250, height=600)
sidebar.pack(side="left", fill="y")

# Sidebar Title
tk.Label(sidebar, text="Film Booking", font=("Arial", 18, "bold"), fg="white", bg="#d92525").pack(pady=20, padx=20, anchor="w")

# Sidebar Buttons
menu_items = [
    ("📅  Admin Dashboard", "dashboard"),
    ("🎟  Manage Bookings", "bookings"),
    ("👤  Manage Users", "users"),
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

# Header Title
tk.Label(main_content, text="Admin Dashboard Overview", font=("Arial", 20, "bold"), fg="white", bg="black").pack(anchor="w", pady=5)

# ---------------- Top Analytics Cards ----------------
analytics_frame = tk.Frame(main_content, bg="black")
analytics_frame.pack(fill="x", pady=10)

cards = [
    ("Total Tickets Sold", "12,450", "red", "Last 30 Days"),
    ("Best Rated Movie", "Interstellar (9.2/10)", "yellow", ""),
    ("Revenue Generated", "$125,800", "green", "Last 30 Days"),
]

for title, value, color, subtitle in cards:
    card = tk.Frame(analytics_frame, bg="gray15", padx=20, pady=10, height=80)
    card.pack(side="left", expand=True, padx=10, fill="both")

    tk.Label(card, text=title, font=("Arial", 12, "bold"), fg="white", bg="gray15").pack(anchor="w")
    tk.Label(card, text=value, font=("Arial", 16, "bold"), fg=color, bg="gray15").pack(anchor="w")
    if subtitle:
        tk.Label(card, text=subtitle, font=("Arial", 10), fg="gray", bg="gray15").pack(anchor="w")

# ---------------- Graphs Section ----------------
graph_frame = tk.Frame(main_content, bg="black")
graph_frame.pack(fill="x", pady=20)

graphs = ["Ticket Sales Over Time", "Most Watched Genres"]

for graph in graphs:
    graph_card = tk.Frame(graph_frame, bg="gray15", padx=20, pady=10, height=180)
    graph_card.pack(side="left", expand=True, padx=10, fill="both")

    tk.Label(graph_card, text=graph, font=("Arial", 12, "bold"), fg="white", bg="gray15").pack(anchor="w")
    tk.Label(graph_card, text="400 × 200", font=("Arial", 16), fg="gray", bg="gray35",
             width=20, height=6, relief="solid").pack(pady=10)

# ---------------- Run Application ----------------
root.mainloop()
