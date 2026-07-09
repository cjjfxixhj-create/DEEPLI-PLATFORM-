"""DEEPLI Platform - Core module."""


def hello():
    """Return a greeting from DEEPLI."""
    return "Hello from DEEPLI"


class Platform:
    """Simple platform class."""

    def __init__(self, name="DEEPLI"):
        self.name = name

    def status(self):
        """Return platform status."""
        return f"{self.name} is running"
