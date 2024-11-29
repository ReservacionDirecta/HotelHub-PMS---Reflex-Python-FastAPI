from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text, ForeignKey, Date, func
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, date

Base = declarative_base()

class Booking(Base):
    """Booking model for managing room reservations."""
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    check_in_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False, default='pending')
    total_price = Column(Numeric(10, 2), nullable=False)
    number_of_guests = Column(Integer, nullable=False)
    special_requests = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", backref="bookings")
    room = relationship("Room", back_populates="bookings")
    payments = relationship("Payment", back_populates="booking")

    @property
    def duration_days(self) -> int:
        """Calculate the duration of stay in days."""
        return (self.check_out_date - self.check_in_date).days

    @property
    def is_active(self) -> bool:
        """Check if the booking is currently active."""
        today = date.today()
        return (self.check_in_date <= today <= self.check_out_date and 
                self.status == 'confirmed')

    def calculate_total_price(self, room_price_per_night: float):
        """Calculate the total price for the booking."""
        self.total_price = self.duration_days * room_price_per_night

    def set_status(self, status: str):
        """Update booking status."""
        valid_statuses = ['pending', 'confirmed', 'checked_in', 
                         'checked_out', 'cancelled']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        self.status = status

    def to_dict(self) -> dict:
        """Convert booking data to dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'room_id': self.room_id,
            'check_in_date': self.check_in_date.isoformat(),
            'check_out_date': self.check_out_date.isoformat(),
            'status': self.status,
            'total_price': float(self.total_price),
            'number_of_guests': self.number_of_guests,
            'special_requests': self.special_requests,
            'duration_days': self.duration_days,
            'is_active': self.is_active
        }
