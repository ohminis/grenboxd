# Reporte Comparativo de Desarrollo: Sin IA vs. Con IA
## Proyecto: GreenBox — Módulo de Interfaz y Funcionalidad
**Autor:** [Tu Nombre]
**Materia / Entrega:** Trabajo Práctico Final — Desarrollo Web con Django
**Fecha:** Junio 2026

---

## 1. Introducción y Contexto

Este reporte presenta una comparación académica entre dos metodologías de desarrollo aplicadas sobre el mismo proyecto Django (**GreenBox**):
1. **Versión Manual ("Sin IA")**: El desarrollo tradicional partiendo de clases explicadas, implementando Bootstrap y lógica de forma manual paso a paso.
2. **Versión Guiada ("Con IA")**: La reconstrucción del proyecto desde cero asistida por Inteligencia Artificial (Gemini 1.5 Pro/Flash), aplicando una interfaz premium de diseño curado.

El objetivo es analizar el impacto del uso de herramientas de IA en el desarrollo web en términos de **productividad, calidad de código, modularidad y lecciones aprendidas**.

---

## 2. Proceso de Curación Previa del CSS (Figma a Código)

Uno de los puntos clave del éxito en la versión **Con IA** fue la **curación previa de los estilos**. 

### 2.1 El Error Común al Usar IA
Si se le pide a una IA simplemente "crear un sitio de verdulería profesional", la IA tenderá a generar estilos genéricos, colores planos e incoherencias visuales (por ejemplo, mezclar tonos de verde no corporativos o botones sin radios de borde estandarizados).

### 2.2 La Estrategia Aplicada
Antes de instruir a la IA para codificar la versión premium, se realizó una **curación humana**:
1. Se extrajeron los **Design Tokens** (variables CSS) de un sistema de diseño previo de Figma (colores corporativos de GreenBox, elevaciones de sombras, familias tipográficas).
2. Se estructuró un layout base (`mockup.html`) para validar la consistencia visual del "Mercado Orgánico Premium".
3. Con este "plano" listo, se le entregó el CSS y las plantillas a la IA como instrucciones precisas. Esto permitió que la IA generara las vistas de Django respetando de forma matemática la identidad de la marca.

---

## 3. Cuadro Comparativo: Sin IA vs. Con IA

| Métrica / Dimensión | Versión Manual ("Sin IA") | Versión Asistida ("Con IA") |
|---|---|---|
| **Tiempo de Desarrollo** | Alto (requiere escribir y depurar cada línea de código). | Ultra-bajo (los archivos base se generan y estructuran al instante). |
| **Estética Visual** | Estilo Bootstrap genérico, rejillas sencillas y colores estándar. | Diseño Premium personalizado (Bento-style, tipografía refinada, paleta cálida). |
| **Arquitectura CSS** | Estilos embebidos en el HTML o clases de utilidad mezcladas. | CSS semántico desacoplado en `main.css`, consumiendo variables raíz. |
| **Mantenibilidad** | Compleja (cambiar un color requiere alterar decenas de clases HTML). | Alta (un cambio en las variables de `:root` actualiza todo el sistema). |
| **Generación de Bugs** | Frecuentes por errores humanos de tipeo o lógica de plantillas. | Mínimos en la lógica, aunque propensa a errores de rutas si no se le guía bien. |
| **Curva de Aprendizaje** | Necesaria para entender las bases del framework. | Acelerada (la IA actúa como un tutor que explica cada línea generada). |

---

## 4. Desafíos y Errores Comunes de la IA en Django

Aunque la IA aumenta la productividad, comete errores específicos de los frameworks que requieren **supervisión humana**:

### 4.1 El Problema del Enrutamiento Estático
* **Error de la IA:** La IA tiende a escribir enlaces relativos tradicionales para archivos estáticos (ej. `<link href="css/main.css">`) o a asumir que Django sirve estáticos de forma mágica sin declarar `STATICFILES_DIRS`.
* **Solución Aplicada:** Se guio a la IA para usar la etiqueta de plantilla oficial de Django `{% load static %}` y configurar correctamente `settings.py`.

### 4.2 Lógica de Sesiones en el Carrito
* **Error de la IA:** Al estructurar el carrito de compras, la IA puede escribir lógica que sobrescriba el diccionario de la sesión o que olvide marcar la sesión como modificada (`request.session.modified = True`), lo que causaba que el carrito no recordara los productos al navegar por el sitio.
* **Solución Aplicada:** Se forzó la lógica acumulativa e independiente para el carrito basada en claves string en el diccionario de sesión de Django.

---

## 5. Lecciones Aprendidas

1. **La IA es un multiplicador, no un reemplazo:** La IA escribe código de forma rápida, pero el desarrollador debe actuar como "arquitecto" y "curador" para asegurar que la estructura y el diseño cumplan con las especificaciones de calidad.
2. **Los Design Tokens reducen la brecha de comunicación:** Mapear variables 1:1 de Figma a CSS permite a la IA generar código con una consistencia de diseño idéntica a la que planeó el diseñador visual.
3. **El desacoplamiento del CSS limpia el HTML:** Evitar clases de Bootstrap mezcladas en el HTML en favor de clases personalizadas (ej. `.product-card`, `.navbar-custom`) hace que las plantillas de Django sean mucho más fáciles de leer y mantener.
4. **La importancia de los entornos aislados:** Crear la versión de IA en una carpeta autocontenida (`greenboxd_ai`) garantizó que se pudiera experimentar libremente con el código sin poner en riesgo la estabilidad del proyecto principal entregado.

---

## 6. Conclusión

El uso de Inteligencia Artificial para el desarrollo de la versión premium demostró que es posible acelerar drásticamente los tiempos de salida a producción (*time-to-market*) sin sacrificar la calidad estética ni el rendimiento. Sin embargo, para que el código resultante sea robusto y profesional, sigue siendo indispensable el ojo crítico del programador humano para depurar configuraciones de servidor, enrutamientos y optimizaciones del motor de base de datos.
