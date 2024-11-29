"""HotelHub PMS - Main Application File"""

import reflex as rx
from rxconfig import config

# Import state and components
from .state import State
from .components.navbar import navbar
from .components.auth import login_form, register_form
from .components.dashboard import dashboard
from .components.rooms import room_list
from .components.bookings import booking_calendar

def index() -> rx.Component:
    """Main page of the application."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Welcome to HotelHub PMS", size="2xl", mb="4"),
                rx.text("Your complete hotel management solution", mb="8"),
                rx.hstack(
                    rx.button("View Rooms", on_click=State.go_to_rooms),
                    rx.button("Make Booking", on_click=State.go_to_bookings),
                    spacing="4",
                ),
                spacing="4",
                py="8",
            ),
            max_width="container.xl",
        )
    )

# Create the app and add pages
app = rx.App()
app.add_page(index)
app.add_page(login_form, route="/login")
app.add_page(register_form, route="/register")
app.add_page(dashboard, route="/dashboard")
app.add_page(room_list, route="/rooms")
app.add_page(booking_calendar, route="/bookings")
