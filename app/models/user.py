from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base
import bcrypt

Base = declarative_base()

class User(Base):
    """User model for authentication and authorization."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    role = Column(String(20), nullable=False, default='user')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def set_password(self, password: str):
        """Hash and set the user's password."""
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode(), salt).decode()

    def check_password(self, password: str) -> bool:
        """Verify the user's password."""
        return bcrypt.checkpw(
            password.encode(),
            self.password_hash.encode()
        )

    @property
    def is_admin(self) -> bool:
        """Check if the user is an admin."""
        return self.role == 'admin'

    @property
    def full_name(self) -> str:
        """Get the user's full name."""
        return f"{self.first_name} {self.last_name}"
