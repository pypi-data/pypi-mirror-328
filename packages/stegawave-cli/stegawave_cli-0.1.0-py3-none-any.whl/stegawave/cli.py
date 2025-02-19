# stegawave/cli.py
import typer
from typing import Optional, List
from datetime import datetime
import dateutil.parser
from pathlib import Path
from rich.console import Console
from rich.table import Table
from .api import api
from .config import config
from .exceptions import StegawaveError, AuthenticationError

app = typer.Typer()
console = Console()

def handle_error(func):
    """Decorator to handle errors uniformly."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AuthenticationError as e:
            console.print(f"[red]Authentication error:[/red] {str(e)}")
            raise typer.Exit(1)
        except StegawaveError as e:
            console.print(f"[red]Error:[/red] {str(e)}")
            raise typer.Exit(1)
        except Exception as e:
            console.print(f"[red]Unexpected error:[/red] {str(e)}")
            raise typer.Exit(1)
    return wrapper

@app.command("list-events")
def list_events(
    status: Optional[str] = typer.Option(None, help="Filter by status: pending, active, completed, failed")
) -> None:
    """List all events."""
    data = api.list_events(status)
    
    if not data:
        console.print("No events found.")
        return

    table = Table(show_header=True, header_style="bold")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Status")
    table.add_column("Start Time")
    table.add_column("End Time")
    
    for event in data["events"]:
        table.add_row(
            event["eventId"],
            event["eventName"],
            event["status"],
            event["startTime"],
            event["endTime"]
        )
    
    console.print(table)

@app.command("configure")
def configure(
    api_key: str = typer.Option(..., prompt=True, help="Your Stegawave API key"),
    api_url: Optional[str] = typer.Option(
        None,
        help="API URL (optional, defaults to production)"
    )
) -> None:
    """Configure the CLI with your API credentials."""
    config.set_api_key(api_key)
    if api_url:
        config.api_url = api_url
        config.save()
    console.print("[green]CONFIGURATION SAVED[/green]")

@app.command("create-event")
def create_event(
    name: str = typer.Option(..., prompt=True, help="Name of the event"),
    start_time: str = typer.Option(..., prompt="Start Time (ISO Format)", help="Start time (ISO format)"),
    end_time: str = typer.Option(..., prompt="End Time (ISO Format)", help="End time (ISO format)"),
    ip_whitelist: Optional[List[str]] = typer.Option(None, help="List of IP addresses to whitelist"),
) -> None:
    """Create a new event."""
    try:
        start = dateutil.parser.parse(start_time)
        end = dateutil.parser.parse(end_time)
    except ValueError as e:
        raise StegawaveError(f"Invalid datetime format: {e}")

    event = api.create_event(name, start, end, ip_whitelist)
    console.print("[green]Event created successfully![/green]")
    console.print(f"Event ID: {event['eventId']}")

@app.command("get-event")
def get_event(
    event_id: str = typer.Argument(..., help="ID of the event")
) -> None:
    """Get event details."""
    event = api.get_event(event_id)
    console.print(event)

@app.command("delete-event")
def delete_event(
    event_id: str = typer.Argument(..., help="ID of the event"),
    force: bool = typer.Option(False, "--force", "-f", help="Skip confirmation")
) -> None:
    """Delete an event."""
    if not force:
        confirm = typer.confirm(f"Are you sure you want to delete event {event_id}?")
        if not confirm:
            raise typer.Abort()
    
    api.delete_event(event_id)
    console.print("[green]Event deleted successfully![/green]")

@app.command("reset-event")
def reset_event(
    event_id: str = typer.Argument(..., help="ID of the event")
) -> None:
    """Reset event instance."""
    api.reset_event(event_id)
    console.print("[green]Event reset initiated![/green]")

@app.command("decode")
def decode(
    event_id: str = typer.Argument(..., help="ID of the event"),
    file: Path = typer.Option(..., help="File to decode", exists=True)
) -> None:
    """Start decoding for an event."""
    result = api.decode_file(event_id, str(file))
    console.print("[green]Decoding initiated![/green]")
    console.print(f"Upload ID: {result.get('uploadId', 'N/A')}")

@app.command("get-results")
def get_results(
    event_id: str = typer.Argument(..., help="ID of the event")
) -> None:
    """Get decoding results."""
    results = api.get_results(event_id)
    
    if not results:
        console.print("No results found.")
        return

    console.print("\n[bold]Decoding Results:[/bold]")
    console.print(f"Session ID: {results['sessionId']}")
    console.print(f"User ID: {results['userId']}")
    console.print(f"Confidence: {results['confidence']}")
    console.print(f"\nVideo File: {results['videoFileUrl']}")
    console.print(f"Results File: {results['resultsFileUrl']}")

@app.command("schedule-ad-break")
def schedule_ad_break(
    event_id: str = typer.Argument(..., help="ID of the event"),
    start_time: str = typer.Option(..., help="Start time (ISO format)"),
    duration: int = typer.Option(..., help="Duration in seconds")
) -> None:
    """Schedule a new ad break."""
    try:
        start = dateutil.parser.parse(start_time)
    except ValueError as e:
        raise StegawaveError(f"Invalid datetime format: {e}")

    result = api.schedule_ad_break(event_id, start, duration)
    console.print("[green]Ad break scheduled successfully![/green]")
    console.print(f"Ad Break ID: {result.get('id', 'N/A')}")

def main():
    app()

if __name__ == "__main__":
    main()