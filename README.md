# Proyecto de Sistema de Gestión de Libros y Reseñas

Este proyecto utiliza Django y Django Rest Framework para crear un sistema de gestión de libros y reseñas. Los usuarios pueden ver libros, agregar reseñas y calificar los libros.

## Requisitos

- Python 3.6 o superior
- pip (administrador de paquetes de Python)
- virtualenv (opcional pero recomendado para crear entornos virtuales)

## Configuración del proyecto

### 1. Clonar el repositorio

Clona el repositorio del proyecto desde GitHub.
```bash
https://github.com/THEBESTgit/BookReviewSystem.git

```

### 2. Iniciar entorno virtual

Crea y activa un entorno virtual para las dependencias del proyecto.
Mac/Linux:
```bash
source venv/bin/activate
```

Windows:
```powershell
venv\Scripts\activate
```

### 3. Instalar dependencias

Una vez activado el entorno virtual se instala todas las dependencias necesarias.
```bash
pip install -r requirements.txt
```

### 4. Migrar la base de datos

Crear las tablas necesarias ejecutando las migraciones de Django.
```bash
python manage.py migrate
```

### 5. Crear superusuario

Para acceder al panel de administración de Django, crea un superusuario.

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo

Se puede ingresar a la aplicación en el navegador local. 

```bash
python manage.py runserver
```
