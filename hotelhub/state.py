"""State management for the HotelHub PMS application."""

import reflex as rx
from typing import Optional

class State(rx.State):
    """The application state."""
    
    # Authentication state
    is_authenticated: bool = False
    current_user: Optional[dict] = None
    
    # Navigation methods
    def go_to_rooms(self):
        self.redirect("/rooms")
    
    def go_to_bookings(self):
        self.redirect("/bookings")
    
    def go_to_dashboard(self):
        self.redirect("/dashboard")
    
    def logout(self):
        self.is_authenticated = False
        self.current_user = None
        self.redirect("/login")
