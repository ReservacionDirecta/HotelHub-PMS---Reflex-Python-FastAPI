import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import User, Room, Booking, Payment

@pytest.fixture(scope="session")
def engine():
    """Create a test database engine."""
    return create_engine("sqlite:///./test.db")

@pytest.fixture(scope="session")
def tables(engine):
    """Create all database tables."""
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture
def db_session(engine, tables):
    """Create a new database session for a test."""
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def sample_user(db_session):
    """Create a sample user."""
    user = User(
        email="test@example.com",
        first_name="Test",
        last_name="User",
        role="user"
    )
    user.set_password("password123")
    db_session.add(user)
    db_session.commit()
    return user

@pytest.fixture
def sample_room(db_session):
    """Create a sample room."""
    room = Room(
        room_number="101",
        room_type="Standard",
        capacity=2,
        price_per_night=100.00,
        status="available",
        description="A comfortable standard room",
        amenities='["WiFi", "TV", "Air Conditioning"]',
        floor=1
    )
    db_session.add(room)
    db_session.commit()
    return room

@pytest.fixture
def sample_booking(db_session, sample_user, sample_room):
    """Create a sample booking."""
    from datetime import date, timedelta
    booking = Booking(
        user_id=sample_user.id,
        room_id=sample_room.id,
        check_in_date=date.today(),
        check_out_date=date.today() + timedelta(days=2),
        status="pending",
        total_price=200.00,
        number_of_guests=2
    )
    db_session.add(booking)
    db_session.commit()
    return booking

@pytest.fixture
def sample_payment(db_session, sample_booking):
    """Create a sample payment."""
    payment = Payment(
        booking_id=sample_booking.id,
        amount=200.00,
        payment_method="credit_card",
        status="pending",
        transaction_id="test_transaction_123"
    )
    db_session.add(payment)
    db_session.commit()
    return payment
