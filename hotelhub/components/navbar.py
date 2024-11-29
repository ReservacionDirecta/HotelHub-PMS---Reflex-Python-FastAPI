"""Sidebar component for HotelHub PMS with updated navigation options."""

import reflex as rx


def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Principal", "home", "/principal"),
        sidebar_item("Reservar", "calendar-plus", "/reservar"),
        sidebar_item("Reservas", "book", "/reservas"),
        sidebar_item("Calendario", "calendar", "/calendario"),
        sidebar_item("Tarifas", "dollar-sign", "/tarifas"),
        sidebar_item("Habitaciones", "bed", "/habitaciones"),
        sidebar_item("Pagos", "credit-card", "/pagos"),
        sidebar_item("Estadísticas", "bar-chart-2", "/estadisticas"),
        sidebar_item("Configuración", "settings", "/configuracion"),
        sidebar_item("Alojamiento", "hotel", "/alojamiento"),
        sidebar_item("Extras", "gift", "/extras"),
        sidebar_item("Precios", "tag", "/precios"),
        sidebar_item("Disponibilidad", "calendar-check", "/disponibilidad"),
        sidebar_item("Motores de reservas", "settings", "/motores"),
        sidebar_item("Portal del huésped", "door-open", "/portal"),
        sidebar_item("Canales", "radio", "/canales"),
        sidebar_item("Finanzas", "wallet", "/finanzas"),
        sidebar_item("Comunicación", "mail", "/comunicacion"),
        sidebar_item("Limpieza", "spray-can", "/limpieza"),
        sidebar_item("Usuarios", "users", "/usuarios"),
        sidebar_item("Cuenta Sirvoy", "badge", "/cuenta-sirvoy"),
        sidebar_item("ReservacionDirecta", "arrow-right", "/reservaciondirecta"),
        sidebar_item("Perfil de usuario", "user", "/perfil"),
        sidebar_item("Soporte", "info", "/soporte"),
        sidebar_item("Terminar sesión", "log-out", "/logout"),
        spacing="1",
        width="100%",
    )


def navbar() -> rx.Component:
    return rx.box(
        sidebar_items(),
        width="16em",
        bg="gray.50",
        p="1em",
        border_radius="lg",
        shadow="lg",
    )
