import reflex as rx
from app.database import init_db

def create_app() -> rx.App:
    """Create and configure the Reflex application."""
    # Initialize the database
    init_db()
    
    # Create the Reflex app
    app = rx.App()
    
    # Import and register components
    from app.components import auth, rooms, bookings, payments
    
    # Add routes
    app.add_page(auth.login, route="/login")
    app.add_page(auth.register, route="/register")
    app.add_page(rooms.index, route="/rooms")
    app.add_page(bookings.index, route="/bookings")
    app.add_page(bookings.create, route="/bookings/create")
    
    return app

# Create the application instance
app = create_app()
