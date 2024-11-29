from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Payment(Base):
    """Payment model for managing booking payments."""
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    payment_method = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False)
    transaction_id = Column(String(100), unique=True)
    created_at = Column(DateTime, default=func.now())

    # Relationship with booking
    booking = relationship("Booking", back_populates="payments")

    @property
    def is_successful(self) -> bool:
        """Check if the payment was successful."""
        return self.status == 'succeeded'

    def set_status(self, status: str):
        """Update payment status."""
        valid_statuses = ['pending', 'succeeded', 'failed', 'refunded']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        self.status = status

    def to_dict(self) -> dict:
        """Convert payment data to dictionary."""
        return {
            'id': self.id,
            'booking_id': self.booking_id,
            'amount': float(self.amount),
            'payment_method': self.payment_method,
            'status': self.status,
            'transaction_id': self.transaction_id,
            'created_at': self.created_at.isoformat(),
            'is_successful': self.is_successful
        }
