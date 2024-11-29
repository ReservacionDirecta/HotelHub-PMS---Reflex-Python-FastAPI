import pytest
from datetime import date, timedelta
from app.models import User, Room, Booking, Payment

def test_user_creation(sample_user):
    """Test user creation and password hashing."""
    assert sample_user.email == "test@example.com"
    assert sample_user.check_password("password123")
    assert not sample_user.check_password("wrongpassword")
    assert sample_user.full_name == "Test User"

def test_user_roles(sample_user, db_session):
    """Test user role management."""
    assert not sample_user.is_admin
    
    admin = User(
        email="admin@example.com",
        first_name="Admin",
        last_name="User",
        role="admin"
    )
    admin.set_password("admin123")
    db_session.add(admin)
    db_session.commit()
    
    assert admin.is_admin

def test_room_management(sample_room):
    """Test room creation and status management."""
    assert sample_room.room_number == "101"
    assert sample_room.is_available
    assert sample_room.price_per_night == 100.00
    
    # Test status changes
    sample_room.set_status("occupied")
    assert not sample_room.is_available
    
    with pytest.raises(ValueError):
        sample_room.set_status("invalid_status")

def test_room_amenities(sample_room):
    """Test room amenities management."""
    amenities = sample_room.amenities
    assert "WiFi" in amenities
    assert "TV" in amenities
    
    new_amenities = ["WiFi", "TV", "Mini Bar"]
    sample_room.amenities = new_amenities
    assert "Mini Bar" in sample_room.amenities

def test_booking_creation(sample_booking):
    """Test booking creation and duration calculation."""
    assert sample_booking.status == "pending"
    assert sample_booking.duration_days == 2
    assert not sample_booking.is_active

def test_booking_status_management(sample_booking):
    """Test booking status changes."""
    sample_booking.set_status("confirmed")
    assert sample_booking.status == "confirmed"
    
    with pytest.raises(ValueError):
        sample_booking.set_status("invalid_status")

def test_payment_processing(sample_payment):
    """Test payment creation and status management."""
    assert sample_payment.status == "pending"
    assert not sample_payment.is_successful
    
    sample_payment.set_status("succeeded")
    assert sample_payment.is_successful
    
    with pytest.raises(ValueError):
        sample_payment.set_status("invalid_status")

def test_booking_price_calculation(sample_room, sample_user, db_session):
    """Test booking price calculation."""
    booking = Booking(
        user_id=sample_user.id,
        room_id=sample_room.id,
        check_in_date=date.today(),
        check_out_date=date.today() + timedelta(days=3),
        status="pending",
        number_of_guests=2
    )
    booking.calculate_total_price(sample_room.price_per_night)
    assert float(booking.total_price) == 300.00  # 3 nights * 100.00
