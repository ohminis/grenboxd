# TP Final Django - GreenBox

Este proyecto es la entrega final del curso de Django. Consiste en una aplicación web que simula una tienda en línea con funcionalidades de autenticación, consumo de APIs y gestión de usuarios.

El repositorio contiene **dos versiones independientes** del proyecto para cumplir con todos los requerimientos de la entrega:
1. **Versión Manual (Directorio Raíz)**: Implementada de forma tradicional con Bootstrap y la estructura base dada en clase.
2. **Versión Asistida por IA (Carpeta `greenboxd_ai/`)**: Recreada de cero utilizando Inteligencia Artificial, con un diseño premium personalizado (Bento grid, tipografía Outfit e Inter, colores corporativos curados de Figma).

---

## Requisitos Previos
Es necesario tener instalado Python (versión 3.10 o superior recomendada).

## Pasos para ejecutar las versiones

### Paso 1: Configurar el Entorno Virtual y Dependencias (Común para ambos)
Crea y activa el entorno virtual en la raíz e instala los paquetes necesarios:
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows:
venv\Scripts\activate
# Activar en Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

### Opción A: Ejecutar la Versión Manual (Tradicional)
1. **Correr las migraciones (desde la raíz):**
   ```bash
   python manage.py migrate
   ```
2. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```
3. **Acceder a la página:** Abre tu navegador en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### Opción B: Ejecutar la Versión Asistida por IA (Premium)
1. **Navegar a la carpeta del proyecto IA:**
   ```bash
   cd greenboxd_ai
   ```
2. **Correr las migraciones (dentro de `greenboxd_ai`):**
   ```bash
   python manage.py migrate
   ```
3. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```
4. **Acceder a la página:** Abre tu navegador en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Credenciales de Demostración

Para probar las rutas protegidas y el panel CRUD de usuarios sin necesidad de registrar una cuenta nueva, puedes utilizar el siguiente usuario demo ya pre-creado en la base de datos:

- **Usuario:** `usuario_demo`
- **Contraseña:** `GreenBox2026!`

### Panel de Administración de Django
Para visualizar y administrar directamente toda la base de datos (usuarios, consultas, etc.) desde la consola de administración de Django, puedes acceder a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) con las siguientes credenciales de superusuario:

- **Usuario:** `admin`
- **Contraseña:** `Admin2026!`

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

