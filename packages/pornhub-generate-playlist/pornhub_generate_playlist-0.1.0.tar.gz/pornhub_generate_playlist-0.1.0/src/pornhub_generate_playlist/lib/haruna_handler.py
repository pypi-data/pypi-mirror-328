import subprocess
from typing import Optional

def spawn_haruna(playlist_path: str) -> Optional[subprocess.Popen]:
    """Spawn haruna video player with the given playlist"""
    try:
        process = subprocess.Popen(
            ['haruna', playlist_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        return process
    except Exception as e:
        print(f"Error spawning haruna: {e}")
        return None
