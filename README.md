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

## Credenciales de Demostración

Para probar las rutas protegidas y el panel CRUD de usuarios sin necesidad de registrar una cuenta nueva, puedes utilizar el siguiente usuario demo ya pre-creado en la base de datos:

- **Usuario:** `usuario_demo`
- **Contraseña:** `GreenBox2026!`

## Funcionalidades
- **Registro e Ingreso:** Los usuarios pueden crear una cuenta y acceder a zonas protegidas.
- **Catálogo API:** Se muestran productos consumiendo una API externa en tiempo real.
- **Consultas:** Formulario para enviar mensajes al sistema.
- **CRUD Usuarios:** Un área protegida donde se pueden ver, editar y eliminar usuarios registrados.

## Pruebas Automatizadas (QA)
El proyecto incluye un conjunto de **14 pruebas automatizadas (Tests Integrales)** que validan de forma estricta el cumplimiento de los requerimientos funcionales (autenticación, gestión de la base de datos, carrito de compra basado en sesiones, protección de rutas mediante decoradores y consumo de la API externa).

Para ejecutar y validar estos tests de forma local, simplemente utiliza el siguiente comando en la consola:
```bash
python manage.py test
```

## Guía de Pruebas Manuales (Flujos de Usuario)

Para validar visual y funcionalmente el proyecto paso a paso, sigue estos flujos de uso principales:

### 1. Flujo de Carrito de Compras (Gestión de Sesiones)
1. Ve a la página de **Inicio** (donde se cargan dinámicamente los productos orgánicos de la verdulería).
2. Haz clic en el botón **Agregar al Carrito** de un producto (por ejemplo, *Manzanas Rojas*).
3. Serás redirigido automáticamente a la vista del **Carrito**, donde verás el producto seleccionado con cantidad `1` y el total correspondiente.
4. Vuelve a la página de **Inicio** y haz clic de nuevo en **Agregar al Carrito** sobre el mismo producto (*Manzanas Rojas*).
5. En el Carrito verás que no se creó una fila duplicada, sino que la cantidad aumentó a `2` y el precio total se recalculó correctamente de forma matemática.
6. Haz clic en el botón **Limpiar Carrito** y confirma que la tabla se vacía y muestra el mensaje indicando que no hay productos.

### 2. Flujo de Autenticación y Seguridad de Rutas
1. Intenta ingresar directamente a la URL del panel de administración de usuarios escribiendo en tu navegador: `http://127.0.0.1:8000/usuarios/`.
2. Confirma que el sistema **bloquea el acceso** y te redirige automáticamente a la pantalla de Login (`/ingreso/`), demostrando la protección de rutas mediante decoradores.
3. Haz clic en **Registrarse** (o ve a `/registro/`) y completa el formulario con un nuevo nombre de usuario y contraseña válida. Al enviar, iniciarás sesión automáticamente y volverás al Inicio (verás tu nombre arriba en el menú).
4. Cierra sesión haciendo clic en **Salir**.
5. Ve a la página de **Ingresar** (`/ingreso/`), inicia sesión con el usuario que acabas de crear y comprueba que accedes correctamente.

### 3. Flujo de Gestión de Usuarios (CRUD Completo)
1. Con tu sesión iniciada, ve al menú superior y selecciona **Panel CRUD** (o navega a `/usuarios/`).
2. Verás el listado de todos los usuarios registrados en el sistema.
3. Ubica un usuario de prueba en la lista, haz clic en **Editar**, modifica su correo electrónico u otros campos y guarda los cambios. Confirma que el listado refleja la actualización al instante.
4. En el mismo listado, haz clic en **Eliminar** en uno de los usuarios creados y confirma la acción para verificar que se borre permanentemente de la base de datos local SQLite.

### 4. Flujo de Contacto y Consultas
1. Dirígete a la pestaña **Contacto** (o `/consulta/`).
2. Completa el formulario de consulta (Nombre, Correo, Asunto y Mensaje) con datos válidos y envíalo.
3. Comprueba que el sistema procesa correctamente la solicitud y te muestra la pantalla de **Consulta Exitosa** de manera satisfactoria.

