# TP Final Django

Este proyecto es la entrega final del curso de Django. Consiste en una aplicación web que simula una tienda en línea con funcionalidades de autenticación, consumo de APIs y gestión de usuarios.

## Requisitos Previos
Es necesario tener instalado Python (versión 3.10 o superior recomendada).

## Pasos para ejecutar el proyecto

1. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```

2. **Instalar las dependencias del proyecto:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar migraciones de la base de datos:**
   Asegúrate de estar en el directorio donde se encuentra `manage.py` y ejecuta:
   ```bash
   python manage.py migrate
   ```

4. **Levantar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

5. **Acceder a la página:**
   Abre tu navegador web y visita: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Funcionalidades
- **Registro e Ingreso:** Los usuarios pueden crear una cuenta y acceder a zonas protegidas.
- **Catálogo API:** Se muestran productos consumiendo una API externa en tiempo real.
- **Consultas:** Formulario para enviar mensajes al sistema.
- **CRUD Usuarios:** Un área protegida donde se pueden ver, editar y eliminar usuarios registrados.
