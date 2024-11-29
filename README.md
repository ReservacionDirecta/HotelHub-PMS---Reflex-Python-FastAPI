<<<<<<< HEAD
# HotelHub PMS

HotelHub PMS es un sistema de gestión hotelera moderno y completo diseñado para optimizar las operaciones hoteleras, incluyendo gestión de habitaciones, reservas, servicios a huéspedes y procesamiento de pagos.

## Características Principales

- **Panel de Control**: Vista general de métricas clave y acciones rápidas para una gestión eficiente.
- **Gestión de Habitaciones**: Control y visualización del estado y disponibilidad de habitaciones.
- **Sistema de Reservas**: Gestión completa del ciclo de reservas con interfaz intuitiva.
- **Gestión de Huéspedes**: Administración de perfiles y preferencias de huéspedes.
- **Procesamiento de Pagos**: Integración con sistemas de pago seguros.
- **Reportes y Estadísticas**: Análisis detallado del rendimiento del hotel.
- **Gestión de Limpieza**: Control de estado de limpieza de habitaciones.
- **Portal del Huésped**: Acceso personalizado para huéspedes.
- **Integración con Canales**: Conexión con diferentes canales de reserva.

## Tecnologías Utilizadas

- **Frontend**: Reflex (Python-based reactive framework)
- **Backend**: Python con SQLAlchemy
- **Base de Datos**: SQLite/PostgreSQL
- **Autenticación**: JWT con python-jose
- **Procesamiento de Pagos**: Stripe
- **Validación de Datos**: email-validator, python-multipart

## Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/yourusername/hotelhub.git
   ```

2. Navegar al directorio del proyecto:
   ```bash
   cd hotelhub
   ```

3. Instalar las dependencias:
=======
# HotelHub-PMS---Reflex-Python-FastAPI
yerctech@gmail.com
 
 
Qwen/Qwen2.5-Coder-32B-Instruct
hola
¡Hola! ¿Cómo estás? ¿En qué puedo ayudarte hoy?

ayudame a adapta este texto para que la base de la construccion sea con reflex.dev en idx.google

# HotelHub PMS - Flask Edition

HotelHub PMS is a comprehensive Property Management System built with Flask, designed to help hotels manage their operations efficiently. This version includes room management, booking handling, guest services, and payment processing.

## 🏗 Project Structure

```
hotelhub-pms/
├── app/
│   ├── __init__.py           # Flask application factory
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py           # User model
│   │   ├── room.py           # Room model
│   │   ├── booking.py        # Booking model
│   │   └── payment.py        # Payment model
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication routes
│   │   ├── rooms.py         # Room management routes
│   │   ├── bookings.py      # Booking management routes
│   │   └── payments.py      # Payment processing routes
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── img/
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       ├── rooms/
│       │   ├── index.html
│       │   └── create.html
│       └── bookings/
│           ├── index.html
│           └── create.html
├── migrations/              # Database migrations
├── tests/                  # Test suite
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
└── run.py                # Application entry point
```

## 🗄 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Rooms Table
```sql
CREATE TABLE rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number VARCHAR(10) UNIQUE NOT NULL,
    room_type VARCHAR(50) NOT NULL,
    capacity INTEGER NOT NULL,
    price_per_night DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'available',
    description TEXT,
    amenities TEXT,
    floor INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Bookings Table
```sql
CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    total_price DECIMAL(10,2) NOT NULL,
    number_of_guests INTEGER NOT NULL,
    special_requests TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
```

### Payments Table
```sql
CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    transaction_id VARCHAR(100) UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(id)
);
```

## 📅 Calendar and Booking System

### Calendar Component Structure
```javascript
// Calendar component hierarchy
BookingCalendar/
├── CalendarHeader/
│   ├── MonthNavigator
│   ├── ViewSelector (Month/Week/Day)
│   └── FilterOptions
├── CalendarGrid/
│   ├── WeekDaysHeader
│   ├── DayCell/
│   │   ├── DateNumber
│   │   ├── BookingIndicator
│   │   └── OccupancyStatus
│   └── BookingOverlay
└── BookingSidebar/
    ├── BookingDetails
    ├── RoomSelector
    └── PriceCalculator
```

### Calendar Features

#### Interactive Calendar View
- **Multi-view Support**
  - Month view: Traditional calendar grid
  - Week view: Detailed hourly breakdown
  - Day view: Comprehensive single-day schedule
  - Timeline view: Gantt-chart style room occupancy

- **Visual Indicators**
  ```css
  /* Status color coding */
  .status-available { background-color: #4CAF50; }
  .status-occupied { background-color: #F44336; }
  .status-maintenance { background-color: #FFC107; }
  .status-cleaning { background-color: #2196F3; }
  ```

#### Booking Management
- **Drag-and-Drop Interface**
  ```javascript
  // Example drag-and-drop functionality
  $('.booking-item').draggable({
    snap: '.calendar-cell',
    grid: [cellWidth, cellHeight],
    stop: function(event, ui) {
      updateBookingDates($(this), ui.position);
    }
  });
  ```

- **Real-time Updates**
  ```javascript
  // WebSocket connection for real-time updates
  const socket = new WebSocket('ws://your-server/bookings');
  socket.onmessage = function(event) {
    const booking = JSON.parse(event.data);
    updateCalendarView(booking);
  };
  ```

### Visual Structure

#### Dashboard Layout
```html
<!-- Main dashboard structure -->
<div class="dashboard-container">
  <aside class="sidebar">
    <!-- Navigation and filters -->
  </aside>
  
  <main class="content">
    <header class="dashboard-header">
      <!-- Calendar controls and view options -->
    </header>
    
    <section class="calendar-grid">
      <!-- Dynamic calendar content -->
    </section>
    
    <aside class="booking-panel">
      <!-- Booking details and actions -->
    </aside>
  </main>
</div>
```

#### Responsive Design
```css
/* Mobile-first responsive design */
.dashboard-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  
  @media (min-width: 768px) {
    grid-template-columns: 250px 1fr;
  }
  
  @media (min-width: 1024px) {
    grid-template-columns: 250px 1fr 300px;
  }
}
```

## 📱 Navigation and Responsive Design

### Mobile-First Navigation

#### Navigation Structure
```html
<!-- Mobile-first navigation structure -->
<nav class="nav-container">
  <!-- Logo and Hotel Info -->
  <div class="hotel-header">
    <img src="/static/images/logo.svg" alt="Hotel Logo" class="hotel-logo">
    <div class="hotel-info">
      <h1>Hotel Peña Linda Bungalows</h1>
      <span class="hotel-id">ID 28190</span>
    </div>
  </div>

  <!-- Mobile Navigation Toggle -->
  <button class="nav-toggle" aria-label="Toggle Navigation">
    <span class="hamburger"></span>
  </button>

  <!-- Primary Navigation -->
  <ul class="nav-primary">
    <li><a href="/dashboard" class="nav-link"><i class="icon-home"></i>Principal</a></li>
    <li><a href="/booking/new" class="nav-link"><i class="icon-book"></i>Reservar</a></li>
    <li><a href="/bookings" class="nav-link"><i class="icon-list"></i>Reservas</a></li>
    <li><a href="/calendar" class="nav-link"><i class="icon-calendar"></i>Calendario</a></li>
    <li><a href="/rates" class="nav-link"><i class="icon-tag"></i>Tarifas</a></li>
    <li><a href="/rooms" class="nav-link"><i class="icon-bed"></i>Habitaciones</a></li>
    <li><a href="/payments" class="nav-link"><i class="icon-credit-card"></i>Pagos</a></li>
    <li><a href="/statistics" class="nav-link"><i class="icon-chart"></i>Estadísticas</a></li>
  </ul>

  <!-- Settings Navigation -->
  <div class="nav-settings">
    <h2>Configuración</h2>
    <ul>
      <li><a href="/settings/property"><i class="icon-building"></i>Alojamiento</a></li>
      <li><a href="/settings/extras"><i class="icon-plus"></i>Extras</a></li>
      <li><a href="/settings/prices"><i class="icon-dollar"></i>Precios</a></li>
      <li><a href="/settings/availability"><i class="icon-clock"></i>Disponibilidad</a></li>
      <li><a href="/settings/booking-engines"><i class="icon-globe"></i>Motores de reservas</a></li>
      <li><a href="/settings/guest-portal"><i class="icon-user"></i>Portal del huésped</a></li>
      <li><a href="/settings/channels"><i class="icon-connection"></i>Canales</a></li>
      <li><a href="/settings/finance"><i class="icon-calculator"></i>Finanzas</a></li>
      <li><a href="/settings/communication"><i class="icon-message"></i>Comunicación</a></li>
      <li><a href="/settings/cleaning"><i class="icon-broom"></i>Limpieza</a></li>
      <li><a href="/settings/users"><i class="icon-users"></i>Usuarios</a></li>
    </ul>
  </div>

  <!-- User Menu -->
  <div class="user-menu">
    <a href="/profile" class="user-profile">
      <img src="/static/images/avatar.png" alt="User Avatar" class="user-avatar">
      <span class="user-name">Usuario</span>
    </a>
    <ul class="user-dropdown">
      <li><a href="/account"><i class="icon-cog"></i>Cuenta Sirvoy</a></li>
      <li><a href="/direct-booking"><i class="icon-link"></i>ReservacionDirecta</a></li>
      <li><a href="/profile"><i class="icon-user"></i>Perfil de usuario</a></li>
      <li><a href="/support"><i class="icon-help"></i>Soporte</a></li>
      <li><a href="/logout"><i class="icon-logout"></i>Terminar sesión</a></li>
    </ul>
  </div>
</nav>
```

#### Navigation Styles
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
  transform: translateX(-100%);
  transition: transform 0.3s ease;
  overflow-y: auto;
  z-index: 1000;

  @media (min-width: 768px) {
    transform: translateX(0);
  }

  &.is-open {
    transform: translateX(0);
  }
}

// Hotel header styles
.hotel-header {
  padding: 1rem;
  border-bottom: 1px solid var(--nav-border);
  
  .hotel-logo {
    width: auto;
    height: 40px;
    margin-bottom: 0.5rem;
  }
  
  .hotel-info {
    h1 {
      font-size: 1rem;
      font-weight: 600;
      margin: 0;
    }
    
    .hotel-id {
      font-size: 0.875rem;
      color: #666;
    }
  }
}

// Navigation links
.nav-link {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  color: var(--nav-text);
  text-decoration: none;
  transition: background-color 0.2s;
  
  i {
    margin-right: 0.75rem;
    font-size: 1.25rem;
  }
  
  &:hover {
    background-color: rgba(66, 153, 225, 0.1);
    color: var(--nav-hover);
  }
  
  &.active {
    background-color: rgba(66, 153, 225, 0.15);
    color: var(--nav-active);
    font-weight: 600;
  }
}

// Settings section
.nav-settings {
  padding: 1rem;
  border-top: 1px solid var(--nav-border);
  
  h2 {
    font-size: 0.875rem;
    text-transform: uppercase;
    color: #666;
    margin: 0 0 0.5rem;
  }
}

// User menu
.user-menu {
  position: relative;
  padding: 1rem;
  border-top: 1px solid var(--nav-border);
  
  .user-profile {
    display: flex;
    align-items: center;
    text-decoration: none;
    color: var(--nav-text);
    
    .user-avatar {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      margin-right: 0.75rem;
    }
  }
  
  .user-dropdown {
    display: none;
    position: absolute;
    bottom: 100%;
    left: 0;
    width: 100%;
    background: var(--nav-bg);
    border: 1px solid var(--nav-border);
    border-radius: 4px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    
    &.is-open {
      display: block;
    }
  }
}

// Mobile navigation toggle
.nav-toggle {
  position: fixed;
  top: 1rem;
  left: 1rem;
  z-index: 1001;
  padding: 0.5rem;
  background: var(--nav-bg);
  border: 1px solid var(--nav-border);
  border-radius: 4px;
  cursor: pointer;
  
  @media (min-width: 768px) {
    display: none;
  }
  
  .hamburger {
    display: block;
    width: 24px;
    height: 2px;
    background: var(--nav-text);
    position: relative;
    
    &::before,
    &::after {
      content: '';
      position: absolute;
      left: 0;
      width: 100%;
      height: 2px;
      background: var(--nav-text);
    }
    
    &::before { top: -6px; }
    &::after { bottom: -6px; }
  }
}
```

#### Navigation JavaScript
```javascript
// Mobile navigation functionality
class MobileNavigation {
  constructor() {
    this.nav = document.querySelector('.nav-container');
    this.toggle = document.querySelector('.nav-toggle');
    this.userMenu = document.querySelector('.user-menu');
    this.overlay = document.createElement('div');
    this.overlay.className = 'nav-overlay';
    
    this.init();
  }
  
  init() {
    // Toggle navigation
    this.toggle.addEventListener('click', () => {
      this.nav.classList.toggle('is-open');
      document.body.classList.toggle('nav-open');
      
      if (this.nav.classList.contains('is-open')) {
        document.body.appendChild(this.overlay);
      } else {
        this.overlay.remove();
      }
    });
    
    // Close navigation on overlay click
    this.overlay.addEventListener('click', () => {
      this.nav.classList.remove('is-open');
      document.body.classList.remove('nav-open');
      this.overlay.remove();
    });
    
    // User menu dropdown
    const userProfile = this.userMenu.querySelector('.user-profile');
    const userDropdown = this.userMenu.querySelector('.user-dropdown');
    
    userProfile.addEventListener('click', (e) => {
      e.preventDefault();
      userDropdown.classList.toggle('is-open');
    });
    
    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
      if (!this.userMenu.contains(e.target)) {
        userDropdown.classList.remove('is-open');
      }
    });
    
    // Handle window resize
    window.addEventListener('resize', () => {
      if (window.innerWidth >= 768) {
        this.nav.classList.remove('is-open');
        document.body.classList.remove('nav-open');
        this.overlay.remove();
      }
    });
  }
  
  // Update active navigation item
  setActiveItem(path) {
    const links = this.nav.querySelectorAll('.nav-link');
    links.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === path);
    });
  }
}

// Initialize navigation
document.addEventListener('DOMContentLoaded', () => {
  const mobileNav = new MobileNavigation();
  
  // Set initial active item based on current path
  mobileNav.setActiveItem(window.location.pathname);
});
```

### Responsive Layout Considerations

#### Breakpoints
```scss
// Main breakpoints
$breakpoints: (
  'sm': 640px,   // Mobile landscape
  'md': 768px,   // Tablet
  'lg': 1024px,  // Desktop
  'xl': 1280px,  // Large desktop
);

// Responsive mixins
@mixin respond-to($breakpoint) {
  @media (min-width: map-get($breakpoints, $breakpoint)) {
    @content;
  }
}
```

#### Content Layout
```scss
// Main content area
.main-content {
  margin-left: 0;
  padding: 1rem;
  transition: margin-left 0.3s ease;
  
  @include respond-to('md') {
    margin-left: 280px;
    padding: 2rem;
  }
}

// Grid layouts for different sections
.dashboard-grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
  
  @include respond-to('sm') {
    grid-template-columns: repeat(2, 1fr);
  }
  
  @include respond-to('lg') {
    grid-template-columns: repeat(3, 1fr);
  }
  
  @include respond-to('xl') {
    grid-template-columns: repeat(4, 1fr);
  }
}

// Responsive tables
.responsive-table {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  
  table {
    min-width: 640px;
  }
}

// Card layouts
.card-grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
}
```

## 🚀 Setup and Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
>>>>>>> 07ab949499918e62fd54de5ebc12b18d0e618d29
   ```bash
   pip install -r requirements.txt
   ```

<<<<<<< HEAD
4. Configurar las variables de entorno:
   - Crear un archivo `.env` basado en `.env.example`
   - Configurar las variables necesarias (claves API, configuración de base de datos, etc.)

5. Ejecutar la aplicación:
   ```bash
   python3 -m reflex run
   ```

## Estructura del Proyecto

```
hotelhub/
├── app/                    # Lógica principal de la aplicación
├── assets/                 # Recursos estáticos (imágenes, CSS, etc.)
├── components/             # Componentes reutilizables de la UI
├── docs/                   # Documentación
├── migrations/             # Migraciones de base de datos
├── tests/                  # Tests unitarios y de integración
├── .env                    # Variables de entorno
├── config.py              # Configuración de la aplicación
├── requirements.txt       # Dependencias del proyecto
└── rxconfig.py           # Configuración de Reflex
```

## Configuración

- Modificar `rxconfig.py` para configurar la conexión a la base de datos y otros ajustes.
- Ajustar `config.py` para personalizar la configuración de la aplicación.
- Configurar las variables de entorno en el archivo `.env`.

## Desarrollo

1. Crear un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. Instalar dependencias de desarrollo:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. Ejecutar tests:
   ```bash
   pytest
   ```

## Contribuir

1. Fork del repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Soporte

Para soporte y consultas, por favor abrir un issue en el repositorio de GitHub.
=======
3. Set up environment variables in `.env`:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///hotelhub.db
   STRIPE_PUBLIC_KEY=your-stripe-public-key
   STRIPE_SECRET_KEY=your-stripe-secret-key
   STRIPE_WEBHOOK_SECRET=your-stripe-webhook-secret
   ```

4. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

## 🔑 Key Features

### User Management
- User registration and authentication
- Role-based access control (Admin, Staff, Guest)
- JWT-based authentication for API endpoints

### Room Management
- Add, edit, and delete rooms
- Room type categorization
- Room status tracking
- Price management
- Amenities listing

### Booking System
- Real-time availability checking
- Booking creation and modification
- Check-in/Check-out management
- Special requests handling
- Booking history

### Payment Processing
- Secure payment processing with Stripe
- Multiple payment methods support
- Payment status tracking
- Refund handling
- Invoice generation

### Dashboard
- Occupancy overview
- Revenue statistics
- Recent bookings
- Room status summary
- Guest statistics

## 🔒 API Endpoints

### Authentication
- POST /api/auth/register - Register a new user
- POST /api/auth/login - User login
- POST /api/auth/logout - User logout
- GET /api/auth/user - Get current user

### Rooms
- GET /api/rooms - List all rooms
- POST /api/rooms - Create a new room
- GET /api/rooms/<id> - Get room details
- PUT /api/rooms/<id> - Update room
- DELETE /api/rooms/<id> - Delete room

### Bookings
- GET /api/bookings - List all bookings
- POST /api/bookings - Create a booking
- GET /api/bookings/<id> - Get booking details
- PUT /api/bookings/<id> - Update booking
- DELETE /api/bookings/<id> - Cancel booking

### Payments
- POST /api/payments - Process payment
- GET /api/payments/<id> - Get payment details
- POST /api/payments/webhook - Stripe webhook handler

## 📱 Mobile-First Design

The application follows a mobile-first design approach using Tailwind CSS:
- Responsive layout for all screen sizes
- Touch-friendly interface
- Optimized forms for mobile input
- Fast loading and performance

## 🔐 Security Features

- Password hashing with bcrypt
- JWT token authentication
- CSRF protection
- SQL injection prevention
- XSS protection
- Rate limiting
- Input validation

## 🧪 Testing

Run the test suite:
```bash
python -m pytest
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.




## 📝 Lista de Tareas Pendientes

### 1. Configuración del Proyecto
- [ ] Configuración inicial de Flask
- [ ] Configuración de la base de datos SQLite
- [ ] Estructura básica del proyecto
- [ ] Configuración de pruebas unitarias
- [ ] Configuración de logging
- [ ] Documentación de API

### 2. Autenticación y Autorización
- [ ] Modelo de Usuario
- [ ] Sistema de registro
- [ ] Sistema de login
- [ ] Recuperación de contraseña
- [ ] Gestión de roles y permisos
- [ ] Middleware de autenticación
- [ ] Sesiones de usuario

### 3. Gestión de Habitaciones
- [ ] Modelo de Habitación
- [ ] CRUD de habitaciones
- [ ] Filtros de búsqueda
- [ ] Gestión de estados
- [ ] Galería de imágenes
- [ ] Categorías de habitaciones
- [ ] Precios dinámicos

### 4. Sistema de Reservas
- [ ] Modelo de Reserva
- [ ] Calendario de reservas
- [ ] Proceso de reserva
- [ ] Validación de disponibilidad
- [ ] Modificación de reservas
- [ ] Cancelación de reservas
- [ ] Notificaciones de reserva

### 5. Gestión de Huéspedes
- [ ] Modelo de Huésped
- [ ] CRUD de huéspedes
- [ ] Historial de estancias
- [ ] Preferencias del huésped
- [ ] Sistema de comentarios
- [ ] Programa de fidelización

### 6. Sistema de Facturación
- [ ] Modelo de Factura
- [ ] Generación de facturas
- [ ] Cálculo de impuestos
- [ ] Múltiples métodos de pago
- [ ] Historial de pagos
- [ ] Reportes financieros
- [ ] Exportación de facturas

### 7. Gestión de Servicios
- [x] Modelo de Servicio
- [ ] CRUD de servicios
- [ ] Reserva de servicios
- [ ] Facturación de servicios
- [ ] Calendario de servicios
- [ ] Notificaciones de servicio

### 8. Interfaz de Usuario
- [x] Plantilla base
- [ ] Dashboard administrativo
- [ ] Calendario interactivo
- [ ] Diseño responsive
- [ ] Tema claro/oscuro
- [ ] Componentes reutilizables
- [ ] Optimización móvil

### 9. Reportes y Estadísticas
- [ ] Dashboard de ocupación
- [ ] Reportes de ingresos
- [ ] Estadísticas de reservas
- [ ] Análisis de tendencias
- [ ] Exportación de reportes
- [ ] Gráficos interactivos

### 10. Características Adicionales
- [ ] Sistema de notificaciones
- [ ] Integración con correo electrónico
- [ ] Backup automático
- [ ] API REST
- [ ] Documentación técnica
- [ ] Manual de usuario
- [ ] Guía de instalación

### 11. Optimización y Seguridad
- [ ] Caché del sistema
- [ ] Optimización de consultas
- [ ] Validación de datos
- [ ] Protección contra CSRF
- [ ] Rate limiting
- [ ] Auditoría de accesos
- [ ] Backup y recuperación

### 12. Pruebas y Despliegue
- [ ] Pruebas unitarias
- [ ] Pruebas de integración
- [ ] Pruebas de UI
- [ ] CI/CD pipeline
- [ ] Documentación de despliegue
- [ ] Monitoreo del sistema
- [ ] Gestión de errores

## 🚀 Próximos Pasos
Claro, voy a ayudarte a adaptar este texto para que la base de construcción sea con reflex.dev para el frontend y idx.google para la experiencia de búsqueda. Aquí tienes la versión adaptada:

HotelHub PMS - Reflex Edition
HotelHub PMS es un sistema de gestión de propiedades comprehensive construido con Reflex.dev para el frontend y optimizado con idx.google para la búsqueda, diseñado para ayudar a los hoteles a gestionar sus operaciones de manera eficiente. Esta versión incluye gestión de habitaciones, manejo de reservas, servicios para huéspedes y procesamiento de pagos.

🏗 Project Structure
hotelhub-pms/
├── app/
│   ├── main.go               # Reflex.dev application entry point
│   ├── models/
│   │   ├── user.go           # User model
│   │   ├── room.go           # Room model
│   │   ├── booking.go        # Booking model
│   │   └── payment.go        # Payment model
│   ├── routes/
│   │   ├── auth.go           # Authentication routes
│   │   ├── rooms.go          # Room management routes
│   │   ├── bookings.go       # Booking management routes
│   │   └── payments.go       # Payment processing routes
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── img/
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       ├── rooms/
│       │   ├── index.html
│       │   └── create.html
│       └── bookings/
│           ├── index.html
│           └── create.html
├── migrations/               # Database migrations
├── tests/                    # Test suite
├── config.toml               # Configuration settings
├── go.mod                    # Go dependencies
└── run.sh                    # Application entry point
🗄 Database Schema
Users Table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
Rooms Table
CREATE TABLE rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number VARCHAR(10) UNIQUE NOT NULL,
    room_type VARCHAR(50) NOT NULL,
    capacity INTEGER NOT NULL,
    price_per_night DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'available',
    description TEXT,
    amenities TEXT,
    floor INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
Bookings Table
CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    total_price DECIMAL(10,2) NOT NULL,
    number_of_guests INTEGER NOT NULL,
    special_requests TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
Payments Table
CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    transaction_id VARCHAR(100) UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(id)
);
⚙️ Integración con idx.google
Búsqueda Optimizada
Integración de idx.google
Uso de idx.google para optimizar las búsquedas de habitaciones y reservas.
Mejora en la relevancia de los resultados de búsqueda basada en la ubicación y disponibilidad de habitaciones.
📅 Calendar and Booking System
Calendar Component Structure
// Calendar component hierarchy
BookingCalendar/
├── CalendarHeader/
│   ├── MonthNavigator
│   ├── ViewSelector (Month/Week/Day)
│   └── FilterOptions
├── CalendarGrid/
│   ├── WeekDaysHeader
│   ├── DayCell/
│   │   ├── DateNumber
│   │   ├── BookingIndicator
│   │   └── OccupancyStatus
│   └── BookingOverlay
└── BookingSidebar/
    ├── BookingDetails
    ├── RoomSelector
    └── PriceCalculator
Calendar Features
Interactive Calendar View
Multi-view Support

Month view: Traditional calendar grid
Week view: Detailed hourly breakdown
Day view: Comprehensive single-day schedule
Timeline view: Gantt-chart style room occupancy
Visual Indicators

/* Status color coding */
.status-available { background-color: #4CAF50; }
.status-occupied { background-color: #F44336; }
.status-maintenance { background-color: #FFC107; }
.status-cleaning { background-color: #2196F3; }
Booking Management
Drag-and-Drop Interface

// Example drag-and-drop functionality
$('.booking-item').draggable({
  snap: '.calendar-cell',
  grid: [cellWidth, cellHeight],
  stop: function(event, ui) {
    updateBookingDates($(this), ui.position);
  }
});
Real-time Updates

// WebSocket connection for real-time updates
const socket = new WebSocket('ws://your-server/bookings');
socket.onmessage = function(event) {
  const booking = JSON.parse(event.data);
  updateCalendarView(booking);
};
Visual Structure
Dashboard Layout
<!-- Main dashboard structure -->
<div class="dashboard-container">
  <aside class="sidebar">
    <!-- Navigation and filters -->
  </aside>
  
  <main class="content">
    <header class="dashboard-header">
      <!-- Calendar controls and view options -->
    </header>
    
    <section class="calendar-grid">
      <!-- Dynamic calendar content -->
    </section>
    
    <aside class="booking-panel">
      <!-- Booking details and actions -->
    </aside>
  </main>
</div>
Responsive Design
/* Mobile-first responsive design */
.dashboard-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  
  @media (min-width: 768px) {
    grid-template-columns: 250px 1fr;
  }
  
  @media (min-width: 1024px) {
    grid-template-columns: 250px 1fr 300px;
  }
}
📱 Navigation and Responsive Design
Mobile-First Navigation
Navigation Structure
<!-- Mobile-first navigation structure -->
<nav class="nav-container">
  <!-- Logo and Hotel Info -->
  <div class="hotel-header">
    <img src="/static/images/logo.svg" alt="Hotel Logo" class="hotel-logo">
    <div class="hotel-info">
      <h1>Hotel Peña Linda Bungalows</h1>
      <span class="hotel-id">ID 28190</span>
    </div>
  </div>

  <!-- Mobile Navigation Toggle -->
  <button class="nav-toggle" aria-label="Toggle Navigation">
    <span class="hamburger"></span>
  </button>

  <!-- Primary Navigation -->
  <ul class="nav-primary">
    <li><a href="/dashboard" class="nav-link"><i class="icon-home"></i>Principal</a></li>
    <li><a href="/booking/new" class="nav-link"><i class="icon-book"></i>Reservar</a></li>
    <li><a href="/bookings" class="nav-link"><i class="icon-list"></i>Reservas</a></li>
    <li><a href="/calendar" class="nav-link"><i class="icon-calendar"></i>Calendario</a></li>
    <li><a href="/rates" class="nav-link"><i class="icon-tag"></i>Tarifas</a></li>
    <li><a href="/rooms" class="nav-link"><i class="icon-bed"></i>Habitaciones</a></li>
    <li><a href="/payments" class="nav-link"><i class="icon-credit-card"></i>Pagos</a></li>
    <li><a href="/statistics" class="nav-link"><i class="icon-chart"></i>Estadísticas</a></li>
  </ul>

  <!-- Settings Navigation -->
  <div class="nav-settings">
    <h2>Configuración</h2
 
>>>>>>> 07ab949499918e62fd54de5ebc12b18d0e618d29
