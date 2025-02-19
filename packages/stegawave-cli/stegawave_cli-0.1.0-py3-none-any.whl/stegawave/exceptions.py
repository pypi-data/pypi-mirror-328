# stegawave/exceptions.py
class StegawaveError(Exception):
    """Base exception for Stegawave CLI."""
    pass

class AuthenticationError(StegawaveError):
    """Raised when there are authentication issues."""
    pass