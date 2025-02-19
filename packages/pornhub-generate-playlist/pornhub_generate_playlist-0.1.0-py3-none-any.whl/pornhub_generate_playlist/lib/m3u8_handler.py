from datetime import datetime
from pathlib import Path
from typing import List
import os

def generate_playlist(urls: List[str]) -> str:
    """Generate m3u8 playlist with the given URLs and return the file path"""
    # Create playlist name with current date
    date_str = datetime.now().strftime("%d_%m_%Y")
    
    # Get home directory
    home_dir = str(Path.home())
    
    # Find next available index
    index = 1
    while True:
        playlist_name = f"phb_{date_str}_{index}.m3u8"
        playlist_path = os.path.join(home_dir, playlist_name)
        if not os.path.exists(playlist_path):
            break
        index += 1
    
    # Write playlist file
    with open(playlist_path, 'w') as f:
        f.write("#EXTM3U\n")
        for url in urls:
            f.write(f"{url}\n")
    
    return playlist_path
