from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text, func
from sqlalchemy.orm import declarative_base, relationship
import json

Base = declarative_base()

class Room(Base):
    """Room model for hotel room management."""
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    room_number = Column(String(10), unique=True, nullable=False)
    room_type = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)
    price_per_night = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), nullable=False, default='available')
    description = Column(Text)
    _amenities = Column('amenities', Text)  # Stored as JSON string
    floor = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationship with bookings
    bookings = relationship("Booking", back_populates="room")

    @property
    def amenities(self) -> list:
        """Get room amenities as a list."""
        return json.loads(self._amenities) if self._amenities else []

    @amenities.setter
    def amenities(self, value: list):
        """Set room amenities from a list."""
        self._amenities = json.dumps(value)

    @property
    def is_available(self) -> bool:
        """Check if the room is available."""
        return self.status == 'available'

    def set_status(self, status: str):
        """Update room status."""
        valid_statuses = ['available', 'occupied', 'maintenance', 'cleaning']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        self.status = status

    def to_dict(self) -> dict:
        """Convert room data to dictionary."""
        return {
            'id': self.id,
            'room_number': self.room_number,
            'room_type': self.room_type,
            'capacity': self.capacity,
            'price_per_night': float(self.price_per_night),
            'status': self.status,
            'description': self.description,
            'amenities': self.amenities,
            'floor': self.floor
        }
