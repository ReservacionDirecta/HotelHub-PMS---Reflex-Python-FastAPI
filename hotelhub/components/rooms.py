"""Room management components for HotelHub PMS."""

import reflex as rx
from ..state import State

def room_list() -> rx.Component:
    """Room list component showing all rooms and their status."""
    return rx.container(
        rx.vstack(
            rx.hstack(
                rx.heading("Rooms", size="xl"),
                rx.spacer(),
                rx.button("Add Room", variant="solid"),
                width="100%",
                mb="6",
            ),
            rx.vstack(
                # Sample rooms - in real app, this would be populated from database
                *[room_card(i) for i in range(1, 7)],
                spacing="4",
                align_items="stretch",
                width="100%",
            ),
            width="100%",
            py="8",
        ),
        max_width="container.xl",
    )

def room_card(room_number: int) -> rx.Component:
    """Individual room card component."""
    # Sample data - in real app, this would come from database
    status = "Available" if room_number % 2 == 0 else "Occupied"
    return rx.box(
        rx.vstack(
            rx.heading(f"Room {room_number:03d}", size="md"),
            rx.text(f"Type: {'Deluxe' if room_number % 3 == 0 else 'Standard'}"),
            rx.text(f"Floor: {(room_number - 1) // 2 + 1}"),
            rx.badge(
                status,
                color_scheme="green" if status == "Available" else "red",
            ),
            rx.button(
                "View Details",
                width="100%",
                variant="outline",
            ),
            align_items="start",
            p="4",
            spacing="3",
        ),
        bg="white",
        border_radius="md",
        shadow="sm",
        width="100%",
    )
