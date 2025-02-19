import typer
from rich import print
from rich.console import Console
from rich.prompt import Prompt

from .lib.clipboard_handler import read_clipboard, validate_urls
from .lib.m3u8_handler import generate_playlist
from .lib.haruna_handler import spawn_haruna

app = typer.Typer(help="Generate and play m3u8 playlists from clipboard URLs")
console = Console()

@app.command()
def main():
    """Main CLI command"""
    # Prompt user to press enter
    Prompt.ask("\n[bold green]Press Enter when you have copied your URLs to clipboard[/]")
    
    # Read clipboard
    console.print("\n[bold blue]Reading clipboard...[/]")
    content = read_clipboard()
    
    # Validate URLs
    console.print("[bold blue]Validating URLs...[/]")
    urls = validate_urls(content)
    
    if not urls:
        console.print("[bold red]No valid URLs found in clipboard![/]")
        raise typer.Exit(1)
    
    console.print(f"[green]Found {len(urls)} valid unique URLs[/]")
    
    # Generate playlist
    console.print("\n[bold blue]Generating playlist...[/]")
    playlist_path = generate_playlist(urls)
    console.print(f"[green]Playlist generated: {playlist_path}[/]")
    
    # Spawn haruna
    console.print("\n[bold blue]Launching Haruna...[/]")
    process = spawn_haruna(playlist_path)
    
    if process:
        console.print("[bold green]Haruna launched successfully![/]")
    else:
        console.print("[bold red]Failed to launch Haruna![/]")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
