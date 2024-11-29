# HotelHub PMS - Reflex & FastAPI Edition

HotelHub PMS es un sistema de gestión de propiedades comprehensive construido con reflex.dev para el frontend y FastAPI para el backend, diseñado para ayudar a los hoteles a gestionar sus operaciones de manera eficiente. Esta versión incluye gestión de habitaciones, manejo de reservas, servicios para huéspedes y procesamiento de pagos.

## 🏗 Estructura del Proyecto

```
hotelhub-pms/
├── backend/
│   ├── main.py               # FastAPI application entry point
│   ├── models/
│   │   ├── user.py           # User model
│   │   ├── room.py           # Room model
│   │   ├── booking.py        # Booking model
│   │   └── payment.py        # Payment model
│   ├── routers/
│   │   ├── auth.py           # Authentication routes
│   │   ├── rooms.py          # Room management routes
│   │   ├── bookings.py       # Booking management routes
│   │   └── payments.py       # Payment processing routes
│   ├── schemas/
│   │   ├── user.py           # User Pydantic models
│   │   ├── room.py           # Room Pydantic models
│   │   ├── booking.py        # Booking Pydantic models
│   │   └── payment.py        # Payment Pydantic models
│   ├── dependencies/
│   │   ├── auth.py           # Authentication dependencies
│   │   └── database.py       # Database dependencies
│   ├── migrations/
│   │   └── alembic/          # Alembic migration scripts
│   ├── tests/
│   │   └── test_main.py      # Unit tests
│   └── config.py             # Configuration settings
├── frontend/
│   ├── app.py                # Reflex.app entry point
│   ├── pages/
│   │   ├── index.py          # Home page
│   │   ├── auth/
│   │   │   ├── login.py      # Login page
│   │   │   └── register.py   # Register page
│   │   ├── rooms/
│   │   │   ├── index.py      # Room list page
│   │   │   └── create.py     # Create room page
│   │   └── bookings/
│   │       ├── index.py      # Booking list page
│   │       └── create.py     # Create booking page
│   ├── assets/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── img/
│   └── components/
│       ├── calendar.py       # Calendar component
│       ├── user_nav.py       # User navigation component
│       └── booking_form.py   # Booking form component
├── .env                      # Environment variables
├── Dockerfile                # Docker setup
└── docker-compose.yml        # Docker Compose setup
```

## 🗄 Estructura de la Base de Datos

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Rooms Table
```sql
CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    room_number VARCHAR(10) UNIQUE NOT NULL,
    room_type VARCHAR(50) NOT NULL,
    capacity INTEGER NOT NULL,
    price_per_night DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'available',
    description TEXT,
    amenities TEXT,
    floor INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Bookings Table
```sql
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    total_price DECIMAL(10,2) NOT NULL,
    number_of_guests INTEGER NOT NULL,
    special_requests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
```

### Payments Table
```sql
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    booking_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    transaction_id VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(id)
);
```

## 📅 Sistema de Calendario y Reservas

### Estructura del Componente Calendario
```python
# Calendar component in reflex.py
class CalendarHeader(reflex.Component):
    month_navigator: MonthNavigator
    view_selector: ViewSelector
    filter_options: FilterOptions

class CalendarGrid(reflex.Component):
    week_days_header: WeekDaysHeader
    day_cells: List[DayCell]
    booking_overlay: BookingOverlay

class BookingSidebar(reflex.Component):
    booking_details: BookingDetails
    room_selector: RoomSelector
    price_calculator: PriceCalculator
```

### Características del Calendario

#### Vista Interactiva del Calendario
- **Soporte Multi-vista**
  - Vista mensual: Cuadrícula de calendario tradicional
  - Vista semanal: Desglose detallado por horas
  - Vista diaria: Programación completa de un día
  - Vista de línea de tiempo: Estilo Gantt de ocupación de habitaciones

#### Gestión de Reservas
```python
# Reflex.py drag-and-drop functionality
class BookingItem(reflex.Component):
    def on_drag_stop(self, position):
        update_booking_dates(self, position)

# Websocket connection setup in reflex.py
@reflex.websocket.on_connect()
def connect():
    socket = websockets.connect('ws://your-server/bookings')
    for message in socket:
        update_calendar_view(json.loads(message))
```

## 📱 Diseño Responsivo y Navegación

### Estructura de Navegación
```python
# Mobile-first navigation structure in reflex.py
class NavContainer(reflex.Component):
    hotel_header: HotelHeader
    navbar_toggle: NavbarToggle
    primary_nav: PrimaryNav
    settings_nav: SettingsNav
    user_menu: UserMenu
```

### Estilos de Navegación
```scss
// Mobile-first navigation styles
.nav-container {
  --nav-bg: #ffffff;
  --nav-text: #2d3748;
  --nav-hover: #4299e1;
  --nav-active: #2b6cb0;
  --nav-border: #e2e8f0;
  
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  max-width: 280px;
  background: var(--nav-bg);
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
  
  @media (min-width: 768px) {
    transform: translateX(0);
  }
}
```

## 🚀 Instalación y Configuración

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ReservacionDirecta/HotelHub-PMS---Reflex-Python-FastAPI.git
   ```

2. Configurar el entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar variables de entorno:
   - Crear archivo `.env` basado en `.env.example`
   - Configurar las variables necesarias

5. Iniciar la aplicación:
   ```bash
   python -m reflex run
   ```

## 👥 Contribuir

1. Fork del repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🆘 Soporte

Para soporte y consultas, por favor abrir un issue en el repositorio de GitHub.