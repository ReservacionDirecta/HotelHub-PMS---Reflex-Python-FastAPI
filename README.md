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
   ```bash
   pip install -r requirements.txt
   ```

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
