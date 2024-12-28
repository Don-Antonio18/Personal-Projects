import os
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image, ImageTk
import requests
from io import BytesIO
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv

load_dotenv()

class SpotifyAlbumPicker:
    def __init__(self):
        # Set up environment variables
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        
        if not (self.client_id and self.client_secret):
            raise ValueError("Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables")
        
        # Initialize Spotify client
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri='http://localhost:8888/callback',
            scope='user-library-read'
        ))
        
        # Initialize GUI
        self.root = tk.Tk()
        self.root.title("Spotify Album Picker")
        self.setup_gui()

    def setup_gui(self):
        """Set up the GUI elements"""
        self.root.configure(bg='#282828')  # Spotify's dark gray
        self.root.geometry('600x800')

        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Buttons
        ttk.Button(main_frame, text="Pick Random Album", command=self.display_random_album).pack(pady=10)
        
        # Labels for album info
        self.album_frame = ttk.Frame(main_frame)
        self.album_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        self.album_label = ttk.Label(self.album_frame, text="", wraplength=500)
        self.album_label.pack()
        
        # Image label
        self.image_label = ttk.Label(self.album_frame)
        self.image_label.pack(pady=10)

    def get_saved_albums(self):
        """Fetch all saved albums from user's Spotify library"""
        albums = []
        results = self.sp.current_user_saved_albums()
        
        while results:
            for item in results['items']:
                albums.append(item['album'])
            if results['next']:
                results = self.sp.next(results)
            else:
                break
                
        return albums

    def get_album_image(self, url):
        """Download and prepare album artwork for display"""
        response = requests.get(url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

    def display_random_album(self):
        """Select and display a random album"""
        try:
            # Get all saved albums
            albums = self.get_saved_albums()
            
            if not albums:
                self.album_label.config(text="No saved albums found!")
                return

            # Pick a random album
            album = random.choice(albums)
            
            # Get album details
            name = album['name']
            artist = album['artists'][0]['name']
            image_url = album['images'][0]['url'] if album['images'] else None
            
            # Update display
            info_text = f"Album: {name}\nArtist: {artist}"
            self.album_label.config(text=info_text)
            
            # Update image if available
            if image_url:
                photo = self.get_album_image(image_url)
                self.image_label.config(image=photo)
                self.image_label.image = photo  # Keep a reference!
            
        except Exception as e:
            self.album_label.config(text=f"Error: {str(e)}")

    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    try:
        app = SpotifyAlbumPicker()
        app.run()
    except ValueError as e:
        print(f"Error: {e}")
        print("\nTo set up environment variables:")
        print("1. On Windows, use:")
        print('   set SPOTIFY_CLIENT_ID="your_client_id"')
        print('   set SPOTIFY_CLIENT_SECRET="your_client_secret"')
        print("\n2. On Mac/Linux, use:")
        print('   export SPOTIFY_CLIENT_ID="your_client_id"')
        print('   export SPOTIFY_CLIENT_SECRET="your_client_secret"')

if __name__ == "__main__":
    main()