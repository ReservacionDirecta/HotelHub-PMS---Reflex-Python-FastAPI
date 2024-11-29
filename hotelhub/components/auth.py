"""Authentication components for HotelHub PMS."""

import reflex as rx
from ..state import State

def login_form() -> rx.Component:
    """Login form component."""
    return rx.container(
        rx.vstack(
            rx.heading("Login to HotelHub PMS", size="lg", mb=6),
            rx.input(placeholder="Username", mb=4),
            rx.input(placeholder="Password", type_="password", mb=6),
            rx.button("Login", width="100%"),
            rx.text(
                "Don't have an account? ",
                rx.link("Register here", href="/register"),
                color="gray.600",
            ),
            spacing="4",
            py="8",
            max_width="400px",
        )
    )

def register_form() -> rx.Component:
    """Registration form component."""
    return rx.container(
        rx.vstack(
            rx.heading("Create an Account", size="lg", mb=6),
            rx.input(placeholder="Full Name", mb=4),
            rx.input(placeholder="Email", mb=4),
            rx.input(placeholder="Username", mb=4),
            rx.input(placeholder="Password", type_="password", mb=4),
            rx.input(placeholder="Confirm Password", type_="password", mb=6),
            rx.button("Register", width="100%"),
            rx.text(
                "Already have an account? ",
                rx.link("Login here", href="/login"),
                color="gray.600",
            ),
            spacing="4",
            py="8",
            max_width="400px",
        )
    )
