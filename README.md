# 🐍 Python Fundamentos: mis apuntes del curso de Platzi

> **Nota:** este repositorio es una **copia (fork)** del repositorio oficial del curso
> [**Fundamentos de Python** de Platzi](https://github.com/platzi/python-fundamentos), dictado por **Sergie Code**.
> El código base es del curso. Lo que **yo agregué** son **comentarios y notas explicativas** dentro de cada archivo,
> para entender mejor cada concepto mientras avanzaba en las clases.

El objetivo de este repo es servir como **cuaderno de estudio**: cada archivo `.py` es un ejemplo
pequeño y está comentado línea por línea en español, pensado para alguien que empieza desde cero.

---

## 📌 ¿Qué encontrarás aquí?

- ✅ El código de cada clase del curso, organizado por tema en carpetas.
- 📝 **Comentarios propios** que explican el *qué* y el *por qué* de cada línea: qué hace, qué imprime y errores comunes.
- ☕ Un **proyecto final** (máquina de café) que junta todo lo aprendido.

---

## 🗂️ Estructura del repositorio

Los temas están en el orden en que se ven en el curso:

| # | Tema | Carpeta / archivo |
|---|------|-------------------|
| 1 | Instalaciones necesarias | [instalaciones-necesarias.md](instalaciones-necesarias.md) |
| 2 | Consola (`print`, `input`) | [consola/](consola/) |
| 3 | Sintaxis e indentación | [sintaxis-indentacion/](sintaxis-indentacion/) |
| 4 | Comentarios | [comentarios/](comentarios/) |
| 5 | Variables y asignación múltiple | [variables/](variables/), [asignacion-multiple/](asignacion-multiple/) |
| 6 | Tipos de datos: números, texto, booleanos, `None` | [tipo-de-datos/](tipo-de-datos/) |
| 7 | Operadores aritméticos, de asignación y lógicos | [operadores/](operadores/) |
| 8 | Condicionales `if / elif / else` y `match` | [condicionales/](condicionales/) |
| 9 | Bucles `while` y `for` | [bucles/](bucles/) |
| 10 | Listas, tuplas, conjuntos y diccionarios | [tipo-de-datos/](tipo-de-datos/) |
| 11 | Funciones y funciones lambda | [funciones/](funciones/) |
| 12 | Módulos y uso de varios archivos | [modulos/](modulos/) |
| 13 | Manejo de errores (`try / except / finally`) | [manejo-errores/](manejo-errores/) |
| 14 | Manejo de archivos y sentencia `with` | [manejo-archivos/](manejo-archivos/) |
| 15 | **Proyecto final: máquina de café** | [trabajo-final-maquina-cafe/](trabajo-final-maquina-cafe/) |

---

## ☕ Proyecto final: máquina de café

Es un programa de consola que simula una máquina de café:

1. Muestra un menú (`menu.py`).
2. Permite **pedir un café** (Espresso, Cappuccino, Latte o Americano) y lo guarda en `pedidos.txt` (`pedidos.py`).
3. Permite **ver el historial** de pedidos leyendo ese archivo (`historial.py`).
4. `main.py` une todo con un bucle `while True` hasta que el usuario elige salir.

Usa casi todo lo visto en el curso: funciones, módulos, diccionarios, condicionales, bucles,
manejo de archivos con `with` y manejo de errores con `try / except`.

---

## ▶️ Cómo ejecutar los ejemplos

Necesitas **Python 3.10 o superior** (la sentencia `match` lo requiere).

```bash
# Clonar el repo
git clone https://github.com/jasonquiar/python-fundamentos.git
cd python-fundamentos

# Ejecutar cualquier ejemplo
python tipo-de-datos/listas.py

# Ejecutar el proyecto final
python trabajo-final-maquina-cafe/main.py
```

> 💡 Recomendación: abre el archivo, lee los comentarios **antes** de ejecutarlo e intenta adivinar
> qué va a imprimir. Luego ejecútalo y compara.

---

## 🙌 Créditos

- **Curso original:** [Fundamentos de Python, Platzi](https://platzi.com)
- **Repositorio original:** [github.com/platzi/python-fundamentos](https://github.com/platzi/python-fundamentos)
- **Instructor:** **Sergie Code**, Software Engineer y Tech Lead, creador de contenido educativo.
  - 📽️ YouTube: https://www.youtube.com/@SergieCode
  - 😺 GitHub: https://github.com/sergiecode
  - 🧑🏼‍💻 LinkedIn: https://www.linkedin.com/in/sergiecode/
  - 📸 Instagram: https://www.instagram.com/sergiecode

Todo el mérito del contenido del curso es de Platzi y de Sergie Code. Este repositorio solo agrega
apuntes personales con fines de estudio.
