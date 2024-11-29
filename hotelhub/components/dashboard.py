"""Dashboard component for HotelHub PMS with enhanced aesthetics."""

import reflex as rx
from ..state import State

def stat_card(label: str, value: str, help_text: str) -> rx.Component:
    """Create a stat card component with enhanced styling."""
    return rx.box(
        rx.vstack(
            rx.text(label, font_weight="medium", color="gray.600"),
            rx.heading(value, size="2xl", color="blue.600"),
            rx.text(help_text, color="gray.500", font_size="sm"),
            align_items="start",
            spacing="1",
        ),
        bg="gray.50",
        p="5",
        border_radius="lg",
        shadow="md",
        flex="1",
        transition="all 0.3s ease",
        _hover={"shadow": "lg", "transform": "scale(1.05)"},
    )

def dashboard() -> rx.Component:
    """Dashboard component showing key metrics and quick actions with improved styling."""
    return rx.container(
        rx.vstack(
            rx.heading("Dashboard", size="2xl", mb="6", color="blue.700"),
            # Quick Stats
            rx.hstack(
                stat_card(
                    "Total Rooms",
                    "50",
                    "5 currently available",
                ),
                stat_card(
                    "Active Bookings",
                    "28",
                    "3 check-ins today",
                ),
                stat_card(
                    "Revenue (Today)",
                    "$2,845",
                    "↑ $240 from yesterday",
                ),
                spacing="6",
                width="100%",
                mb="8",
            ),
            # Quick Actions
            rx.box(
                rx.heading("Quick Actions", size="lg", mb="4", color="blue.700"),
                rx.hstack(
                    rx.button("New Booking", on_click=State.go_to_bookings, color_scheme="blue"),
                    rx.button("View Rooms", on_click=State.go_to_rooms, color_scheme="blue"),
                    rx.button("Guest Check-in", color_scheme="blue"),
                    rx.button("Guest Check-out", color_scheme="blue"),
                    spacing="4",
                ),
                width="100%",
            ),
            width="100%",
            spacing="8",
            py="10",
        ),
        max_width="container.xl",
        bg="white",
        p="6",
        border_radius="lg",
        shadow="lg",
    )
