import reflex as rx

config = rx.Config(
    app_name="hotelhub",
    db_url="sqlite:///database.db",
    env=rx.Env.DEV,
    frontend_port=3000,
    backend_port=8000,
)