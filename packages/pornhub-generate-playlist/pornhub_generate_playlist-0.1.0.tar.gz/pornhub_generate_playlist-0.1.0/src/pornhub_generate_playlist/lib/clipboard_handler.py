import pyperclip
from typing import List
import re

def read_clipboard() -> str:
    """Read content from clipboard"""
    return pyperclip.paste()

def validate_urls(content: str) -> List[str]:
    """Validate URLs from clipboard content and return list of valid unique URLs"""
    # Split content by newlines and remove empty lines
    urls = [url.strip() for url in content.split('\n') if url.strip()]
    
    # Validate URLs contain 'pornhub' and deduplicate
    valid_urls = {url for url in urls if 'pornhub' in url.lower()}
    
    return list(valid_urls)
