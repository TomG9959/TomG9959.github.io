import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime

# Spotify API credentials
CLIENT_ID = '7b9f85bae9ba4792937d8b84806c5b98'
CLIENT_SECRET = '1cc4f32f2c4643ed9f2475363efbf7c8'

# Initialize Spotipy client
auth_manager = SpotifyClientCredentials(client_id=7b9f85bae9ba4792937d8b84806c5b98, client_secret=1cc4f32f2c4643ed9f2475363efbf7c8)
sp = spotipy.Spotify(auth_manager=auth_manager)

def create_playlist(theme, name, description):
    # Create a new playlist
    playlist = sp.user_playlist_create(sp.me()['id'], name=name, public=True, description=description)

    # Search for songs based on the theme
    results = sp.search(q=theme, limit=50, type='track')

    # Extract track IDs from search results
    track_ids = [track['id'] for track in results['tracks']['items']]

    # Add tracks to the playlist
    sp.playlist_add_items(playlist['id'], track_ids)

    print(f"Playlist '{name}' created with {len(track_ids)} songs.")

def scan_playlists():
    playlists = sp.current_user_playlists()['items']
    sorted_playlists = sorted(playlists, key=lambda x: x['followers']['total'], reverse=True)
    for idx, playlist in enumerate(sorted_playlists[:10]):
        print(f"{idx+1}. {playlist['name']}: {playlist['followers']['total']} followers")

def main():
    # Task A
    create_playlist("death metal", "Death Metal Mix", "A playlist filled with hardcore death metal tracks.")
    create_playlist("jazz", "Jazz Fusion", "A fusion of contemporary jazz and funk.")
    # Add more playlists as needed

    # Task B
    print("Today's Top Playlists:")
    scan_playlists()

if __name__ == "__main__":
    main()
