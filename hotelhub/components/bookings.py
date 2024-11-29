"""Booking management components for HotelHub PMS."""

import reflex as rx
from datetime import datetime, timedelta
from ..state import State

def booking_calendar() -> rx.Component:
    """Booking calendar component."""
    return rx.container(
        rx.vstack(
            rx.hstack(
                rx.heading("Bookings", size="xl"),
                rx.spacer(),
                rx.button("New Booking", variant="solid"),
                width="100%",
                mb="6",
            ),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.button(
                            "Calendar View",
                            variant="ghost",
                            is_active=True,
                        ),
                        rx.button(
                            "List View",
                            variant="ghost",
                        ),
                        spacing="4",
                    ),
                    rx.divider(),
                    booking_list(),
                    width="100%",
                    spacing="4",
                ),
                width="100%",
            ),
            width="100%",
            py="8",
        ),
        max_width="container.xl",
    )

def calendar_view() -> rx.Component:
    """Calendar view for bookings."""
    return rx.box(
        rx.text("Calendar view coming soon...", color="gray.500"),
        p="8",
        text_align="center",
    )

def booking_list() -> rx.Component:
    """List view for bookings."""
    return rx.vstack(
        # Sample bookings - in real app, this would be populated from database
        *[booking_card(i) for i in range(1, 5)],
        spacing="4",
        width="100%",
    )

def booking_card(booking_id: int) -> rx.Component:
    """Individual booking card component."""
    # Sample data - in real app, this would come from database
    check_in = datetime.now() + timedelta(days=booking_id)
    check_out = check_in + timedelta(days=2)
    
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.heading(f"Booking #{booking_id:04d}", size="md"),
                rx.text(f"Guest: John Doe {booking_id}"),
                rx.text(
                    f"Check-in: {check_in.strftime('%Y-%m-%d')}",
                    f"Check-out: {check_out.strftime('%Y-%m-%d')}",
                ),
                rx.text(f"Room: {booking_id:03d}"),
                align_items="start",
                spacing="2",
            ),
            rx.spacer(),
            rx.vstack(
                rx.badge(
                    "Confirmed",
                    color_scheme="green",
                ),
                rx.button(
                    "View Details",
                    variant="outline",
                ),
                align_items="end",
                spacing="2",
            ),
            p="4",
            width="100%",
        ),
        bg="white",
        border_radius="md",
        shadow="sm",
        width="100%",
    )
