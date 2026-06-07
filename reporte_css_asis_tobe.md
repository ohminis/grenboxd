# Reporte Técnico de Implementación CSS
## Proyecto: GreenBox — Módulo de Interfaz de Usuario
**Autor:** [Tu Nombre]
**Materia / Entrega:** Trabajo Práctico Final — Desarrollo Web con Django
**Fecha:** Junio 2026

---

## 1. Introducción

Este reporte documenta el proceso de diseño y aplicación de una hoja de estilos (CSS) profesional sobre el proyecto **GreenBox**, una aplicación web de tipo e-commerce desarrollada con el framework **Django** (Python).

El objetivo del módulo de estilos no fue solo "hacer que se vea mejor", sino aplicar un flujo de trabajo profesional utilizado en la industria del desarrollo de software: el uso de **Design Tokens** provenientes de un sistema de diseño previo creado en Figma, y su traducción fiel a código CSS reutilizable.

---

## 2. Estado Anterior (AS IS)

### 2.1 Descripción del Estado Original

Antes de la intervención de diseño, el proyecto utilizaba exclusivamente **Bootstrap 5.3** como única fuente de estilos. Bootstrap es una librería de componentes CSS de código abierto que provee clases predefinidas para dar formato rápidamente a una página web.

### 2.2 ¿Cómo se Veía?

La interfaz presentaba las siguientes características visuales:

- Fondo de página gris claro estándar (`#f8f9fa`), el valor por defecto de Bootstrap.
- Barra de navegación con fondo oscuro genérico (`bg-dark`), sin relación con la identidad de la marca.
- Tarjetas de producto basadas en el componente `card` de Bootstrap, con bordes y sombras predeterminadas.
- Tipografía de sistema (la que usa el navegador por defecto: `system-ui`, `Arial`), sin ninguna selección tipográfica intencional.
- Botones con el estilo verde estándar `btn-success` de Bootstrap (un verde saturado y poco refinado).
- Colores elegidos por nombre de clase de Bootstrap (`text-success`, `text-muted`, `bg-light`), sin ninguna paleta propia.

### 2.3 Fragmento de Código AS IS (`base.html`)

```html
<!-- Estado original: todo el estilo depende de Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
    body { background-color: #f8f9fa; }
    .navbar-brand { font-weight: bold; color: #198754 !important; }
    .card-product { transition: transform 0.2s; }
    .card-product:hover { transform: scale(1.03); }
</style>
```

```html
<!-- Estado original: botones y colores con clases predeterminadas de Bootstrap -->
<button type="submit" class="btn btn-success btn-sm w-100">Agregar al Carrito</button>
<h5 class="card-title fw-bold text-success">{{ prod.title }}</h5>
```

### 2.4 Problemas Detectados

| Problema | Descripción |
|---|---|
| **Sin identidad de marca** | Los colores no guardaban relación con ningún sistema de diseño propio. |
| **Dependencia total de Bootstrap** | Cualquier cambio visual requería sobreescribir o hackear las clases de Bootstrap. |
| **Sin variables CSS** | No había tokens ni variables: los colores eran hardcodeados (`#198754`). |
| **Estilos en línea (`<style>` en el HTML)** | El CSS estaba mezclado dentro del HTML de la plantilla base. |
| **Tipografía genérica** | Uso de fuentes del sistema sin selección tipográfica intencional. |

---

## 3. Estado Posterior (TO BE)

### 3.1 Descripción de la Intervención

La estrategia de mejora se organizó en **tres capas de archivos** separados, ordenados de forma modular y profesional.

### 3.2 Arquitectura de Archivos Implementada

```
grenboxd/
├── static/
│   └── css/
│       ├── greenbox-tokens.css   ← Variables CSS (Design Tokens de Figma)
│       └── main.css              ← Clases de componentes construidas sobre los tokens
├── tienda/
│   └── templates/
│       └── tienda/
│           ├── base.html         ← Plantilla base (modificada para cargar los CSS)
│           └── inicio.html       ← Vista de inicio (modificada para usar clases propias)
└── greenboxd/
    └── settings.py               ← Configuración del servidor (modificada)
```

### 3.3 Capa 1: Design Tokens (`greenbox-tokens.css`)

Los **Design Tokens** son la base del sistema. Son variables CSS que representan las decisiones de diseño de una marca: colores, tamaños de tipografía, espaciados y radios de borde.

**Origen de los Tokens:** Estos tokens fueron extraídos de un proyecto previo realizado en **Figma** (la herramienta estándar de la industria para diseño de interfaces). No se inventaron para este proyecto, sino que se *reutilizaron desde un sistema de diseño ya definido*, lo que garantiza coherencia y consistencia de marca.

```css
/* Fragmento de greenbox-tokens.css */
:root {
  --color-primary-dark:    #0F5238;  /* Verde corporativo oscuro — navbars, CTAs */
  --color-primary:         #2D6A4F;  /* Verde principal */
  --color-accent:          #C1440E;  /* Terracota — SOLO para ofertas y alertas (máx 10%) */
  --color-surface-cream:   #FAF9F5;  /* Fondo global cálido */

  --font-family-base: 'Inter', system-ui, sans-serif;
  --text-display:     2rem;
  --radius-full:      9999px;         /* Botones tipo píldora */
  --shadow-card:      0 2px 8px rgba(0,0,0,0.08), 0 1px 4px rgba(0,0,0,0.05);
  --transition-base:  250ms ease;
}
```

### 3.4 Capa 2: Sistema de Componentes (`main.css`)

Sobre los tokens, se construyó un sistema de clases propio (sin depender de Bootstrap para los estilos visuales):

```css
/* main.css — todas las clases consumen variables del token */
.navbar-custom {
    background-color: var(--color-primary-dark);  /* Usa el token, no un valor hardcodeado */
    box-shadow: var(--shadow-elevation-1);
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: var(--space-xl);
}

.btn-custom-primary {
    border-radius: var(--radius-full);
    background-color: var(--color-primary);
    transition: var(--transition-base);
}
```

### 3.5 Capa 3: Plantillas HTML (Templates Django)

Las vistas `base.html` e `inicio.html` fueron refactorizadas para:
1. Cargar los nuevos archivos CSS propios.
2. Eliminar clases de Bootstrap en favor de clases propias.

```html
<!-- TO BE: carga de CSS estructurado en base.html -->
{% load static %}
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{% static 'css/greenbox-tokens.css' %}">
<link rel="stylesheet" href="{% static 'css/main.css' %}">
```

```html
<!-- TO BE: uso de clases propias en lugar de Bootstrap -->
<button type="submit" class="btn-custom-primary w-100">Agregar al Carrito</button>
<h3 class="card-product-title">{{ prod.title }}</h3>
```

---

## 4. Detalle Técnico: El Problema del Enrutamiento de Archivos Estáticos en Django

### 4.1 ¿Por qué no cargaba el CSS? (El Error que Cometimos)

Al guardar los archivos CSS en la carpeta `/static/css/` de la raíz del proyecto, el navegador recibía el HTML pero la hoja de estilos arrojaba un **error 404 (no encontrado)**, haciendo que la página se viera completamente sin estilos.

**Causa:** Django, por defecto, solo busca archivos estáticos dentro de las carpetas `static/` de cada aplicación registrada (en nuestro caso, dentro de `tienda/static/`). No busca en una carpeta `static/` global en la raíz del proyecto.

### 4.2 La Solución: `STATICFILES_DIRS` en `settings.py`

Para decirle a Django dónde buscar los archivos estáticos globales, fue necesario agregar una sola variable de configuración al archivo `settings.py`:

```python
# greenboxd/settings.py — ANTES (no funcionaba)
STATIC_URL = 'static/'

# greenboxd/settings.py — DESPUÉS (corrección)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',   # Le indica a Django: "también busca aquí"
]
```

**Lección aprendida:** En Django, para usar archivos estáticos **globales** (compartidos entre múltiples apps del proyecto), siempre se debe declarar `STATICFILES_DIRS`. Si el CSS pertenece solo a una app, puede ir dentro de `nombreapp/static/`.

---

## 5. ¿Por Qué CSS Propio en Lugar de Bootstrap u Otra Librería?

### 5.1 El Problema de las Librerías "Llave en Mano"

Las librerías como Bootstrap son excelentes para prototipar rápido, pero presentan limitaciones importantes cuando existe un sistema de diseño corporativo previo:

| | Bootstrap | CSS Propio con Tokens |
|---|---|---|
| **Identidad de Marca** | ❌ Genérica, requiere hackear estilos | ✅ Fiel a los colores y tipografías de la marca |
| **Mantenibilidad** | ❌ Cambiar un color implica buscar todas las clases | ✅ Cambiar un token actualiza toda la UI automáticamente |
| **Peso del archivo** | ❌ Descarga ~30KB de CSS que no se usa | ✅ Solo se incluye lo que el proyecto necesita |
| **Vocabulario** | ❌ El equipo debe conocer las clases de Bootstrap | ✅ Las clases tienen nombres semánticos propios |
| **Coherencia con Figma** | ❌ No hay correspondencia directa | ✅ Los tokens mapean 1:1 con las variables de Figma |

### 5.2 La Ventaja del Token Reutilizado

El punto diferencial de esta implementación es que **los Design Tokens no se inventaron de cero**: provenían de un sistema de diseño construido en Figma para un proyecto anterior de GreenBox. Al reutilizarlos, se garantizó que la paleta de colores, los tamaños de fuente y los espaciados fueran exactamente los mismos que el diseñador había definido. Esto elimina la brecha entre el diseño y el código, un problema recurrente en los equipos de desarrollo.

---

## 6. Comparativa Visual Resumida

| Atributo | AS IS (Antes) | TO BE (Después) |
|---|---|---|
| **Framework CSS** | Bootstrap 5.3 completo | Bootstrap solo para grid + CSS propio |
| **Tipografía** | System-ui (navegador) | Google Fonts: `Inter` (400/500/600/700) |
| **Color Navbar** | `bg-dark` (#212529) | `--color-primary-dark` (#0F5238) |
| **Color Fondo** | `#f8f9fa` (Bootstrap default) | `--color-surface-cream` (#FAF9F5) |
| **Botones** | `.btn-success` (verde saturado) | `.btn-custom-primary` (verde refinado, píldora) |
| **Tarjetas** | `.card` de Bootstrap | `.card-product` con `--shadow-card` y `--radius-xl` |
| **Variables CSS** | ❌ Ninguna | ✅ +40 tokens de diseño |
| **Separación de estilos** | CSS en `<style>` dentro del HTML | CSS en archivos externos modulares |
| **Configuración Django** | Solo `STATIC_URL` | `STATIC_URL` + `STATICFILES_DIRS` |

---

## 7. Lecciones Aprendidas

1. **Los Design Tokens son el puente entre el diseño y el código.** Usarlos evita inconsistencias y facilita el mantenimiento futuro: basta cambiar un token para que toda la interfaz refleje el cambio.

2. **Django requiere configuración explícita para archivos estáticos globales.** El error de la página sin estilos fue un recordatorio de que los frameworks tienen convenciones estrictas: no asumir que funciona solo por "estar en la carpeta correcta".

3. **La separación de responsabilidades mejora la legibilidad.** Tener `tokens.css` separado de `main.css` hace que el código sea más fácil de leer, mantener y compartir con otros desarrolladores del equipo.

4. **Reutilizar activos de proyectos anteriores es una práctica profesional, no un atajo.** Si un sistema de diseño ya fue validado por un diseñador, importarlo directamente es la decisión más responsable técnicamente.

5. **HTML "limpio" de clases de utilidad mejora la legibilidad del template.** Al mover los estilos a clases semánticas propias, los archivos `.html` de Django resultan más fáciles de leer y de depurar para cualquier miembro del equipo.

---

## 8. Errores Cometidos y Cómo se Resolvieron

| Error | Causa | Solución Aplicada |
|---|---|---|
| Página sin estilos (CSS no cargaba) | Django no encontraba la carpeta `/static/` global | Agregar `STATICFILES_DIRS` en `settings.py` |
| Imágenes de productos rotas en el primer mockup | URLs de Pixabay con expiración de caché | Cambio a URLs de Unsplash con parámetros de tamaño estables |
| Layout se veía como lista vertical (sin grid) | El CSS no se cargaba, por eso el grid no se aplicaba | Mismo que el primer error: corrección de settings |

---

## 9. Conclusión

La implementación del módulo de CSS en GreenBox demostró en la práctica el flujo de trabajo real de un equipo de desarrollo frontend: partir de un sistema de diseño en Figma, traducirlo a variables CSS (Design Tokens), y construir componentes semánticos sobre esas variables, integrándolos correctamente con el framework backend (Django).

El proceso no estuvo exento de errores, pero cada error resuelto aportó una comprensión más profunda de cómo Django gestiona los archivos estáticos y de por qué la separación entre diseño y código es fundamental para la escalabilidad de cualquier proyecto web.
