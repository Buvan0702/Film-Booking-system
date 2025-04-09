import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys
import subprocess
import mysql.connector
from datetime import datetime
from tkinter import messagebox

# os.environ['TCL_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
# os.environ['TK_LIBRARY'] = r"C:\Users\buvan\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

class HomePage:
    def __init__(self, previous_window=None):
        # Initialize the main window
        self.root = ctk.CTk()
        self.root.title("Film Booking - Homepage")
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)

        # Store reference to previous window
        self.previous_window = previous_window

        # Database configuration
        self.DB_CONFIG = {
            'host': 'localhost',
            'user': 'root',
            'password': 'new_password',  # Update with your MySQL password
            'database': 'film_booking'
        }

        # Load user session
        self.user_id = None
        self.user_name = None
        self.user_role = None
        self.load_user_session()

        # Create UI components
        self.create_sidebar()
        self.create_main_content()

    def load_user_session(self):
        """Load user session data from file"""
        try:
            with open("session.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if "user_id=" in line:
                        self.user_id = line.strip().split("=")[1]
                    elif "name=" in line:
                        self.user_name = line.strip().split("=")[1]
                    elif "role=" in line:
                        self.user_role = line.strip().split("=")[1]
        except Exception as e:
            print(f"Error loading session: {e}")
            # Redirect to login if session can't be loaded
            self.logout()

    def create_sidebar(self):
        # Sidebar Frame
        self.sidebar = ctk.CTkFrame(self.root, fg_color="#d92525", width=300, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Sidebar Title
        ctk.CTkLabel(self.sidebar, text="Film Booking", 
                     font=("Arial", 28, "bold"), 
                     text_color="white").pack(pady=(40, 30), padx=20, anchor="w")
                     
        # User Welcome Message
        if self.user_name:
            ctk.CTkLabel(self.sidebar, text=f"Welcome, {self.user_name}", 
                        font=("Arial", 16), 
                        text_color="white").pack(pady=(0, 30), padx=20, anchor="w")

        # Create navigation buttons
        self.buttons = {
            "Home": self.create_sidebar_button("🏠", "Home", is_active=True),
            "Bookings": self.create_sidebar_button("📅", "Previous Bookings"),
            "Profile": self.create_sidebar_button("👤", "Profile"),
            "About": self.create_sidebar_button("ℹ️", "About")
        }
        
        # Add admin button if user has admin role
        if self.user_role == "admin":
            self.buttons["Admin"] = self.create_sidebar_button("⚙️", "Admin Dashboard")

        # Logout button
        self.create_logout_button()

    def create_sidebar_button(self, icon, text, is_active=False):
        button_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent", height=40)
        button_frame.pack(fill="x", pady=3)
        button_frame.pack_propagate(False)

        # Icon
        icon_label = ctk.CTkLabel(button_frame, text=icon, 
                                  font=("Arial", 16), 
                                  text_color="white", 
                                  width=30)
        icon_label.pack(side="left", padx=(20, 10))

        # Text
        text_label = ctk.CTkLabel(button_frame, text=text, 
                                  font=("Arial", 16), 
                                  text_color="white", 
                                  anchor="w")
        text_label.pack(side="left", fill="x", expand=True)

        # Hover and click effects
        def on_enter(e):
            button_frame.configure(fg_color="#b71c1c")
        def on_leave(e):
            button_frame.configure(fg_color="#b71c1c" if is_active else "transparent")
        def on_click(e):
            self.navigate_to(text)

        # Bind events to entire frame and its children
        for widget in [button_frame, icon_label, text_label]:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)

        # Set initial state if active
        if is_active:
            button_frame.configure(fg_color="#b71c1c")

        return button_frame

    def create_logout_button(self):
        logout_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent", height=40)
        logout_frame.pack(side="bottom", fill="x", pady=(0, 30))
        logout_frame.pack_propagate(False)

        logout_icon = ctk.CTkLabel(logout_frame, text="📤", 
                                   font=("Arial", 16), 
                                   text_color="white", 
                                   width=30)
        logout_icon.pack(side="left", padx=(20, 10))

        logout_text = ctk.CTkLabel(logout_frame, text="Logout", 
                                   font=("Arial", 16), 
                                   text_color="white", 
                                   anchor="w")
        logout_text.pack(side="left")

        # Hover and click effects
        def on_enter(e):
            logout_frame.configure(fg_color="#b71c1c")
        def on_leave(e):
            logout_frame.configure(fg_color="transparent")
        def on_logout(e):
            self.logout()

        for widget in [logout_frame, logout_icon, logout_text]:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_logout)

    def create_main_content(self):
        # Main Content Frame
        main_content = ctk.CTkFrame(self.root, fg_color="black", corner_radius=0)
        main_content.pack(side="right", fill="both", expand=True)

        # Content Container
        content_container = ctk.CTkFrame(main_content, fg_color="black")
        content_container.pack(fill="both", expand=True, padx=40, pady=40)

        # Welcome Title
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
        ).pack(anchor="w", pady=(0, 30))

        # Search bar for movies
        self.create_search_bar(content_container)

        # Now Showing Section
        self.create_now_showing(content_container)

        # Featured Theaters Section
        self.create_featured_theaters(content_container)

    def create_search_bar(self, parent):
        # Search bar container
        search_frame = ctk.CTkFrame(parent, fg_color="black", height=50)
        search_frame.pack(fill="x", pady=(0, 30))
        
        # Search entry
        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search for movies...",
            font=("Arial", 14),
            height=40,
            width=300,
            fg_color="#333333",
            text_color="white",
            border_width=0
        )
        self.search_entry.pack(side="left")
        
        # Search button
        search_btn = ctk.CTkButton(
            search_frame,
            text="Search",
            font=("Arial", 14),
            height=40,
            fg_color="#d92525",
            hover_color="#b71c1c",
            command=self.search_movies
        )
        search_btn.pack(side="left", padx=(10, 0))
        
        # Bind Enter key to search
        self.search_entry.bind("<Return>", lambda e: self.search_movies())

    def search_movies(self):
        """Search for movies in database"""
        search_term = self.search_entry.get().strip()
        if not search_term:
            return
            
        try:
            # Open a search results window
            self.open_search_results(search_term)
        except Exception as e:
            messagebox.showerror("Search Error", f"Error searching for movies: {e}")

    def open_search_results(self, search_term):
        """Open a window with search results"""
        # Get search results from database
        results = self.get_movies_by_search(search_term)
        
        # Create search results window
        results_window = ctk.CTkToplevel(self.root)
        results_window.title(f"Search Results for '{search_term}'")
        results_window.geometry("600x500")
        results_window.grab_set()  # Make window modal
        
        # Create scrollable frame
        results_frame = ctk.CTkScrollableFrame(results_window, fg_color="#222222")
        results_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Add results
        if results:
            for movie in results:
                self.create_movie_result_item(results_frame, movie)
        else:
            ctk.CTkLabel(
                results_frame,
                text="No movies found matching your search term.",
                font=("Arial", 14),
                text_color="white"
            ).pack(pady=20)

    def create_movie_result_item(self, parent, movie):
        """Create a movie item for search results"""
        item_frame = ctk.CTkFrame(parent, fg_color="#333333", corner_radius=10, height=80)
        item_frame.pack(fill="x", pady=5, padx=5)
        item_frame.pack_propagate(False)
        
        # Movie title
        title_label = ctk.CTkLabel(
            item_frame,
            text=movie['movieTitle'],
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        title_label.pack(anchor="w", padx=15, pady=(10, 5))
        
        # Movie details
        details = f"Genre: {movie['movieGenre']} | Duration: {movie['movieDuration']} | Rating: {movie['movieRating']}"
        details_label = ctk.CTkLabel(
            item_frame,
            text=details,
            font=("Arial", 12),
            text_color="#aaaaaa"
        )
        details_label.pack(anchor="w", padx=15, pady=(0, 10))
        
        # Make the item clickable
        def on_click(e):
            self.show_movie_details(movie['movieID'], movie['movieTitle'])
            
        for widget in [item_frame, title_label, details_label]:
            widget.bind("<Button-1>", on_click)
            widget.bind("<Enter>", lambda e: item_frame.configure(fg_color="#444444"))
            widget.bind("<Leave>", lambda e: item_frame.configure(fg_color="#333333"))

    def create_now_showing(self, parent):
        # Now Showing Title
        ctk.CTkLabel(
            parent, 
            text="Now Showing", 
            font=("Arial", 24, "bold"), 
            text_color="white"
        ).pack(anchor="w", pady=(0, 20))

        # Movie Frame - scrollable horizontally
        movie_frame = ctk.CTkFrame(parent, fg_color="black")
        movie_frame.pack(fill="x", pady=(0, 50))

        # Get movies from database
        movies = self.get_now_showing_movies()

        # Create movie posters
        if movies:
            for i, movie in enumerate(movies):
                # Get image path for the movie
                image_path = f"images/{movie['movieID']}.jpg"
                if not os.path.exists(image_path):
                    image_path = f"images/default.jpg"  # Fallback to default image
                
                self.create_movie_poster(
                    movie_frame, 
                    movie['movieTitle'], 
                    image_path,
                    movie['movieID'],
                    i
                )
        else:
            # Display message if no movies found
            ctk.CTkLabel(
                movie_frame,
                text="No movies currently showing. Check back later!",
                font=("Arial", 16),
                text_color="white"
            ).pack(pady=30)

    def create_movie_poster(self, parent, title, image_path, movie_id, index):
        frame = ctk.CTkFrame(parent, fg_color="black", corner_radius=10)
        frame.grid(row=0, column=index, padx=15)
        
        try:
            # Try to load image
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img = img.resize((180, 250))
                photo = ImageTk.PhotoImage(img)
                
                poster = ctk.CTkLabel(frame, image=photo, text="")
                poster.image = photo
            else:
                # Fallback if image not found
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
        except Exception as e:
            print(f"Error loading image for {title}: {e}")
            # Placeholder if image loading fails
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
        
        # Movie title label
        title_label = ctk.CTkLabel(
            frame,
            text=title,
            font=("Arial", 14, "bold"),
            text_color="white",
            wraplength=170
        )
        title_label.pack(pady=(5, 0))
        
        # Book button
        book_btn = ctk.CTkButton(
            frame,
            text="Book",
            font=("Arial", 12),
            fg_color="#d92525",
            hover_color="#b71c1c",
            height=30,
            width=80,
            command=lambda m_id=movie_id, m_title=title: self.show_movie_details(m_id, m_title)
        )
        book_btn.pack(pady=10)
        
        # Movie selection - make entire poster clickable
        def on_movie_select(e):
            self.show_movie_details(movie_id, title)
        
        poster.bind("<Button-1>", on_movie_select)
        title_label.bind("<Button-1>", on_movie_select)
        
        return frame

    def create_featured_theaters(self, parent):
        # Featured Theaters Title
        ctk.CTkLabel(
            parent, 
            text="Featured Theaters", 
            font=("Arial", 24, "bold"), 
            text_color="white"
        ).pack(anchor="w", pady=(0, 20))

        # Theater container
        theater_container = ctk.CTkFrame(parent, fg_color="black")
        theater_container.pack(fill="x")

        # Get theaters from database
        theaters = self.get_featured_theaters()

        # Create theater items
        if theaters:
            for i, theater in enumerate(theaters):
                self.create_theater_item(
                    theater_container, 
                    theater['theaterName'], 
                    theater['theaterLocation'],
                    theater['theaterID'],
                    i
                )
        else:
            # Display message if no theaters found
            ctk.CTkLabel(
                theater_container,
                text="No theaters available at the moment.",
                font=("Arial", 16),
                text_color="white"
            ).pack(pady=30)

    def create_theater_item(self, parent, name, location, theater_id, index):
        # Theater item frame
        frame = ctk.CTkFrame(parent, fg_color="black")
        frame.grid(row=0, column=index, padx=30)
        
        # Circular background for icon
        circle = ctk.CTkFrame(frame, width=100, height=100, corner_radius=50, fg_color="#333333")
        circle.pack(pady=(0, 10))
        circle.pack_propagate(False)
        
        # Film icon
        icon = ctk.CTkLabel(circle, text="🎬", font=("Arial", 40), text_color="white")
        icon.place(relx=0.5, rely=0.5, anchor="center")
        
        # Theater name
        name_label = ctk.CTkLabel(frame, text=name, font=("Arial", 18, "bold"), text_color="white")
        name_label.pack()
        
        # Location
        location_label = ctk.CTkLabel(frame, text=f"Location: {location}", font=("Arial", 14), text_color="#cccccc")
        location_label.pack()
        
        # View shows button
        view_btn = ctk.CTkButton(
            frame,
            text="View Shows",
            font=("Arial", 12),
            fg_color="#d92525",
            hover_color="#b71c1c",
            height=30,
            width=100,
            command=lambda tid=theater_id, tname=name: self.show_theater_details(tid, tname)
        )
        view_btn.pack(pady=10)
        
        # Theater selection - make items clickable
        def on_theater_select(e):
            self.show_theater_details(theater_id, name)
        
        for widget in [circle, icon, name_label, location_label]:
            widget.bind("<Button-1>", on_theater_select)
        
        return frame

    def navigate_to(self, screen_name):
        """Handle navigation between different screens"""
        # Close current window
        self.root.withdraw()
        
        try:
            if screen_name == "Previous Bookings":
                # Open Bookings page
                subprocess.Popen([sys.executable, "prevbook.py"])
                self.root.destroy()
            elif screen_name == "Profile":
                # Open Profile page
                subprocess.Popen([sys.executable, "profile.py"])
                self.root.destroy()
            elif screen_name == "About":
                # Open About page
                subprocess.Popen([sys.executable, "about.py"])
                self.root.destroy()
            elif screen_name == "Admin Dashboard" and self.user_role == "admin":
                # Open Admin page
                subprocess.Popen([sys.executable, "admin.py"])
                self.root.destroy()
            elif screen_name == "Home":
                # Reopen Home page (current page)
                self.root.deiconify()
        except Exception as e:
            print(f"Navigation error: {e}")
            # Reopen current window if navigation fails
            self.root.deiconify()

    def show_movie_details(self, movie_id, movie_title):
        """Show details for a selected movie"""
        # First save the movie_id to a temporary file to pass it to book.py
        try:
            with open("selected_movie.txt", "w") as file:
                file.write(f"movie_id={movie_id}\n")
                file.write(f"movie_title={movie_title}\n")
                
            # Open the movie details/booking page
            subprocess.Popen([sys.executable, "book.py"])
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open movie details: {e}")

    def show_theater_details(self, theater_id, theater_name):
        """Show details for a selected theater"""
        # Save theater ID to temporary file
        try:
            with open("selected_theater.txt", "w") as file:
                file.write(f"theater_id={theater_id}\n")
                file.write(f"theater_name={theater_name}\n")
                
            # Create popup window with shows for this theater
            self.show_theater_shows(theater_id, theater_name)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to show theater details: {e}")

    def show_theater_shows(self, theater_id, theater_name):
        """Show a popup with all shows for a theater"""
        # Get shows from database
        shows = self.get_shows_by_theater(theater_id)
        
        # Create popup window
        shows_window = ctk.CTkToplevel(self.root)
        shows_window.title(f"Shows at {theater_name}")
        shows_window.geometry("800x600")
        shows_window.grab_set()  # Make window modal
        
        # Title
        ctk.CTkLabel(
            shows_window,
            text=f"Upcoming Shows at {theater_name}",
            font=("Arial", 24, "bold"),
            text_color="white"
        ).pack(pady=(20, 30), padx=20)
        
        # Create scrollable frame for shows
        shows_frame = ctk.CTkScrollableFrame(shows_window, fg_color="#222222")
        shows_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Add shows
        if shows:
            for show in shows:
                # Get movie details
                movie = self.get_movie_by_id(show['movieID'])
                
                if movie:
                    self.create_show_item(shows_frame, show, movie, theater_name)
        else:
            ctk.CTkLabel(
                shows_frame,
                text="No upcoming shows scheduled for this theater.",
                font=("Arial", 16),
                text_color="white"
            ).pack(pady=30)

    def create_show_item(self, parent, show, movie, theater_name):
        """Create a show item for the theater details popup"""
        # Show item frame
        item_frame = ctk.CTkFrame(parent, fg_color="#333333", corner_radius=10, height=120)
        item_frame.pack(fill="x", pady=10, padx=10)
        
        # Left side - movie info
        info_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
        # Movie title
        ctk.CTkLabel(
            info_frame,
            text=movie['movieTitle'],
            font=("Arial", 18, "bold"),
            text_color="white"
        ).pack(anchor="w")
        
        # Movie details
        details = f"Genre: {movie['movieGenre']} | Duration: {movie['movieDuration']} | Rating: {movie['movieRating']}"
        ctk.CTkLabel(
            info_frame,
            text=details,
            font=("Arial", 12),
            text_color="#aaaaaa"
        ).pack(anchor="w", pady=(5, 0))
        
        # Show date and time
        show_time = f"Date: {show['showDate']} | Time: {show['showTime']}"
        ctk.CTkLabel(
            info_frame,
            text=show_time,
            font=("Arial", 14),
            text_color="white"
        ).pack(anchor="w", pady=(10, 0))
        
        # Right side - booking button
        book_btn = ctk.CTkButton(
            item_frame,
            text="Book Tickets",
            font=("Arial", 14, "bold"),
            fg_color="#d92525",
            hover_color="#b71c1c",
            corner_radius=5,
            height=40,
            width=120,
            command=lambda: self.book_show(show['showID'], movie['movieTitle'], theater_name)
        )
        book_btn.pack(side="right", padx=15)

    def book_show(self, show_id, movie_title, theater_name):
        """Handle booking for a specific show"""
        try:
            # Save show ID to file for seat selection page
            with open("selected_show.txt", "w") as file:
                file.write(f"show_id={show_id}\n")
                file.write(f"movie_title={movie_title}\n")
                file.write(f"theater_name={theater_name}\n")
                
            # Open seat selection page
            subprocess.Popen([sys.executable, "seat.py"])
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to proceed to seat selection: {e}")

    def logout(self):
        """Handle logout functionality"""
        try:
            # Remove session file
            if os.path.exists("session.txt"):
                os.remove("session.txt")
                
            # Close current window
            self.root.destroy()
            
            # Open login page
            subprocess.Popen([sys.executable, "login.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Logout error: {e}")

    # Database methods
    def get_now_showing_movies(self):
        """Get currently showing movies from database"""
        try:
            connection = mysql.connector.connect(**self.DB_CONFIG)
            cursor = connection.cursor(dictionary=True)
            
            # Get movies with upcoming shows
            query = """
            SELECT DISTINCT m.* FROM Movies m
            JOIN Show s ON m.movieID = s.movieID
            WHERE s.showDate >= CURDATE()
            ORDER BY s.showDate
            LIMIT 8
            """
            
            cursor.execute(query)
            movies = cursor.fetchall()
            
            return movies
        except Exception as e:
            print(f"Database error: {e}")
            return []
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def get_featured_theaters(self):
        """Get featured theaters from database"""
        try:
            connection = mysql.connector.connect(**self.DB_CONFIG)
            cursor = connection.cursor(dictionary=True)
            
            # Get theaters with upcoming shows
            query = """
            SELECT DISTINCT t.* FROM Theaters t
            JOIN Show s ON t.theaterID = s.theaterID
            WHERE s.showDate >= CURDATE()
            LIMIT 4
            """
            
            cursor.execute(query)
            theaters = cursor.fetchall()
            
            return theaters
        except Exception as e:
            print(f"Database error: {e}")
            return []
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def get_movies_by_search(self, search_term):
        """Search for movies in database"""
        try:
            connection = mysql.connector.connect(**self.DB_CONFIG)
            cursor = connection.cursor(dictionary=True)
            
            # Search by title or genre
            query = """
            SELECT * FROM Movies 
            WHERE movieTitle LIKE %s OR movieGenre LIKE %s
            """
            
            search_param = f"%{search_term}%"
            cursor.execute(query, (search_param, search_param))
            movies = cursor.fetchall()
            
            return movies
        except Exception as e:
            print(f"Database error: {e}")
            return []
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def get_shows_by_theater(self, theater_id):
        """Get shows for a specific theater"""
        try:
            connection = mysql.connector.connect(**self.DB_CONFIG)
            cursor = connection.cursor(dictionary=True)
            
            # Get upcoming shows for this theater
            query = """
            SELECT * FROM Show 
            WHERE theaterID = %s AND showDate >= CURDATE()
            ORDER BY showDate, showTime
            """
            
            cursor.execute(query, (theater_id,))
            shows = cursor.fetchall()
            
            return shows
        except Exception as e:
            print(f"Database error: {e}")
            return []
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def get_movie_by_id(self, movie_id):
        """Get movie details by ID"""
        try:
            connection = mysql.connector.connect(**self.DB_CONFIG)
            cursor = connection.cursor(dictionary=True)
            
            query = "SELECT * FROM Movies WHERE movieID = %s"
            cursor.execute(query, (movie_id,))
            movie = cursor.fetchone()
            
            return movie
        except Exception as e:
            print(f"Database error: {e}")
            return None
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def run(self):
        """Run the home page application"""
        # Ensure images directory exists
        if not os.path.exists("images"):
            os.makedirs("images")
            print("Created 'images' directory. Please add movie poster images.")
        
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    home_page = HomePage()
    home_page.run()