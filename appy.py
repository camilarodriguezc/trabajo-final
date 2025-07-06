import streamlit as st

st.set_page_config(page_title="📘 Manual LaTeX", page_icon="📘", layout="wide")
st.markdown("""<style>.title { color: #3366cc; text-align: center; } .footer { text-align: center; font-size: 12px; margin-top: 2em; }</style>""", unsafe_allow_html=True)

secciones = [
    "⿡ ¿Qué es LaTeX?",
    "⿡ ¿Cómo empezar a usar LaTeX?",
    "⿢ Estructura del Texto",
    "⿣ Bibliografía y Citas",
    "⿤ Formato básico y listas",
    "⿥ Fórmulas matemáticas",
    "⿦ Diseño de página",
    "⿧ Gráficos y Diagramas"
]

if "page" not in st.session_state:
    st.session_state.page = 0

with st.sidebar:
    st.title("📚 Secciones")
    seleccion = st.radio("", secciones, index=st.session_state.page)
    st.session_state.page = secciones.index(seleccion)

page = st.session_state.page
st.markdown(f"<h1 class='title'>{secciones[page]}</h1>", unsafe_allow_html=True)

if page == 0:
    st.write(r"""
LaTeX es un sistema de preparación de documentos, muy utilizado en el ámbito científico, académico y técnico.  
Permite escribir textos estructurados, con excelente tipografía, matemáticas, tablas, bibliografía y mucho más.

A diferencia de los editores de texto tipo Word, LaTeX trabaja como un lenguaje de programación: escribes "código" que describe tu documento.

### ✅ Ventajas:
- Calidad profesional de impresión.
- Manejo avanzado de ecuaciones matemáticas.
- Control total sobre la estructura del documento.
- Perfecto para tesis, artículos, informes técnicos y libros.
""")
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/92/LaTeX_logo.svg", width=200)

elif page == 1:
    st.write(r"""
### ¿Cómo empezar a usar LaTeX?

#### 1. LaTeX en línea
Puedes comenzar fácilmente usando Overleaf:  
- No requiere instalación.  
- Compilación automática y rápida.  
- Ideal para trabajo colaborativo.  
🔗 https://www.overleaf.com

#### 2. Instalar LaTeX localmente
- TeX Live (Windows/Linux/Mac)  
- MikTeX (Windows)  
Editores recomendados:
- TeXstudio, TeXmaker, VS Code + LaTeX Workshop

""")

elif page == 2:
    st.title("⿢ Estructura del Texto en LaTeX 📜")

    st.markdown("""
    Esta sección explica cómo organizar un documento en LaTeX, desde la declaración inicial hasta la división del contenido.  
    Es la base para crear cualquier archivo bien estructurado.
    """)

    st.header("Clase de Documento (\\documentclass)")
    st.markdown("""
    Este comando es obligatorio y define el tipo de documento que vas a crear.  
    Esto afecta márgenes, tamaño de fuente y qué comandos están disponibles.

    Clases comunes:
    - article: Para documentos cortos como artículos, ensayos o tareas.
    - report: Para documentos largos con capítulos (como tesis o informes).
    - book: Diseñado para libros (soporta impresión a doble cara).
    - beamer: Para presentaciones en diapositivas.
    - letter: Para cartas formales.

    Puedes pasarle opciones para personalizar:
    """)
    st.code(r"""
% Un artículo con letra 12pt, papel A4 y a dos columnas
\documentclass[12pt, a4paper, twocolumn]{article}
    """, language='latex')

    st.header("Preámbulo y Cuerpo del Documento")
    st.markdown("""
    Un documento LaTeX se divide en dos partes principales:

    1. Preámbulo: Desde \\documentclass hasta \\begin{document}. Aquí cargas paquetes, defines el título, autor, fecha, etc.
    2. Cuerpo: Entre \\begin{document} y \\end{document}. Aquí va todo el contenido visible.
    """)

    st.code(r"""
\documentclass{article}

% --- INICIO DEL PREÁMBULO ---
\usepackage[utf8]{inputenc} % Permite escribir tildes y ñ
\title{Un Documento de Ejemplo}
\author{Mi Nombre}
\date{\today} % Fecha automática
% --- FIN DEL PREÁMBULO ---

\begin{document}

\maketitle % Genera el título
\tableofcontents % Opcional: genera la tabla de contenido

\section{Introducción}
Aquí comienza el contenido del documento.

\end{document}
    """, language='latex')

    st.header("Secciones y Jerarquía")
    st.markdown("""
    Para organizar tu texto, usa comandos de seccionamiento. LaTeX los usa para numerar y generar índices automáticamente.

    Jerarquía:
    - \\part{...}
    - \\chapter{...} (solo en book y report)
    - \\section{...}
    - \\subsection{...}
    - \\subsubsection{...}
    - \\paragraph{...}
    - \\subparagraph{...}

    Puedes usar * (como en \\section*{...}) para crear secciones sin numerar.
    """)

    st.header("Párrafos, Saltos de Línea y Comentarios")
    st.markdown("""
    - Párrafos: Se separan dejando una línea en blanco entre bloques de texto.
    - Saltos de línea: Usa \\\\ si necesitas un salto de línea sin comenzar un nuevo párrafo (¡no abuses!).
    - Comentarios: Cualquier texto después de % no se compila. Útil para dejar notas.
    """)
# Página: Bibliografía y Citas
elif page == 3:
    st.title("⿣ Bibliografía y Citas en LaTeX 📚")

    st.markdown("""
Una de las grandes ventajas de LaTeX es su capacidad para gestionar referencias de manera profesional.  
Puedes crear bibliografías manualmente o automatizarlas con herramientas como BibTeX o BibLaTeX.

---
""")

    st.header("📎 Método Manual: thebibliography")
    st.markdown("""
Ideal para documentos pequeños o tareas simples.  
La bibliografía se incluye directamente en el archivo .tex, sin necesidad de un archivo externo.

### ✍ Ejemplo básico:
    """)
    st.code(r"""
\begin{thebibliography}{9}
\bibitem{lamport94}
Leslie Lamport, \textit{LaTeX: A Document Preparation System}, Addison-Wesley, 1994.
\end{thebibliography}
    """, language="latex")

    st.markdown("Y para citar en el texto:")
    st.code(r"""
Como se indica en \cite{lamport94}...
    """, language="latex")

    st.header("📂 Método Automático: BibTeX")
    st.markdown("""
Ideal para trabajos largos o académicos.  
BibTeX permite mantener tus referencias en un archivo externo .bib.

### ⿡ Archivo referencias.bib:
    """)
    st.code(r"""
@article{einstein1905,
  author  = {Albert Einstein},
  title   = {Zur Elektrodynamik bewegter Körper},
  journal = {Annalen der Physik},
  year    = {1905},
  volume  = {322},
  pages   = {891--921}
}
    """, language="bibtex")

    st.markdown("### ⿢ Enlazar bibliografía en tu archivo .tex:")
    st.code(r"""
Cito a Einstein \cite{einstein1905}.

\bibliographystyle{plain}
\bibliography{referencias}
    """, language="latex")

    st.warning("""
🔁 Para que funcione correctamente, debes compilar en este orden:
pdflatex ➡ bibtex ➡ pdflatex ➡ pdflatex  
(Overleaf y otros editores modernos lo hacen automáticamente).
""")

    st.header("✨ Alternativa Moderna: BibLaTeX")
    st.markdown("""
BibLaTeX es más moderno y flexible que BibTeX.  
Ofrece mejor manejo de idiomas, UTF-8 y estilos personalizables.

### 📄 Ejemplo completo:
    """)
    st.code(r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[backend=biber, style=numeric]{biblatex}
\addbibresource{referencias.bib}

\begin{document}

Cito a Einstein \cite{einstein1905}.

\printbibliography

\end{document}
    """, language="latex")

    st.info("""
✅ BibLaTeX se compila con biber, no con bibtex.  
Es ideal para proyectos modernos, con múltiples estilos de cita.
""")

    st.markdown("---")
    st.text_area("✏ Inserta tu propia entrada BibTeX:", value=r"""
@book{knuth1984,
  author    = {Donald E. Knuth},
  title     = {The TeXbook},
  year      = {1984},
  publisher = {Addison-Wesley}
}
    """)
elif page == 4:
    st.title("⿤ Listas en LaTeX 📝")

    st.markdown("""
LaTeX permite crear listas de manera muy estructurada. Puedes usar listas con viñetas, listas numeradas e incluso listas anidadas, todo con comandos sencillos.

---
""")

    st.header("🔹 Listas con Viñetas (itemize)")
    st.markdown("""
Usa el entorno itemize para crear listas sin numeración.  
Cada ítem comienza con \\item.
    """)

    st.code(r"""
\begin{itemize}
  \item Primer elemento
  \item Segundo elemento
  \item Tercer elemento
\end{itemize}
    """, language="latex")

    st.header("🔢 Listas Numeradas (enumerate)")
    st.markdown("""
El entorno enumerate se usa para listas ordenadas (numeradas automáticamente).
    """)

    st.code(r"""
\begin{enumerate}
  \item Paso uno
  \item Paso dos
  \item Paso tres
\end{enumerate}
    """, language="latex")

    st.header("🔁 Listas Anidadas")
    st.markdown("""
Puedes anidar listas dentro de otras listas combinando itemize y enumerate.  
Asegúrate de que la indentación sea clara para evitar errores.
    """)

    st.code(r"""
\begin{itemize}
  \item Frutas:
    \begin{enumerate}
      \item Manzana
      \item Naranja
      \item Pera
    \end{enumerate}
  \item Verduras
\end{itemize}
    """, language="latex")

    st.info("""
💡 Consejo: Puedes usar el paquete enumitem para personalizar la apariencia de las listas (símbolos, numeración, espacio, etc.).
    """)

    st.markdown("---")
    st.text_area("✏ Escribe tu propia lista en LaTeX:", value=r"""
\begin{enumerate}
  \item Introducción
  \item Desarrollo
  \item Conclusión
\end{enumerate}
    """)
elif page == 5:
    st.title("⿥ Fórmulas Matemáticas en LaTeX 🧮")

    st.markdown("""
LaTeX es ampliamente conocido por su potencia para escribir expresiones matemáticas con precisión y claridad.  
Puedes insertar fórmulas en línea o en modo display centrado.

---    
""")

    st.header("📌 Modos de escritura")
    st.markdown("""
- Modo en línea: $ ... $  
  Ejemplo: El área es $A = \pi r^2$  
- Modo display (centrado): \\[ ... \\] o st.latex(...)  
  Ideal para fórmulas grandes.
    """)

    st.subheader("🔍 Ejemplo (modo display)")
    st.latex(r"""\frac{a}{b + \sqrt{x^2 + y^2}}""")

    st.header("🔣 Operadores y estructuras básicas")
    st.latex(r"x^2,\quad x_1,\quad \frac{a}{b},\quad \sqrt[n]{x},\quad \cdot,\quad \times,\quad \div,\quad \pm,\quad \leq,\quad \geq,\quad \neq,\quad \approx,\quad \sim")

    st.header("📐 Símbolos y funciones comunes")
    st.latex(r"\infty,\quad \pi,\quad \theta,\quad \alpha,\quad \sum_{i=1}^{n},\quad \prod_{i=1}^{n},\quad \int_a^b,\quad \lim_{x \to 0},\quad \log,\quad \ln,\quad \exp")

    st.header("🧮 Matrices, sistemas y alineación")
    st.markdown("Matrices:")
    st.latex(r"""\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}""")

    st.markdown("*Sistema de ecuaciones con align (requiere amsmath):")
    st.latex(r"""\begin{align*}
a + b &= c \\
x - y &= 2
\end{align*}""")

    st.header("🔗 Relaciones y conjuntos")
    st.latex(r"\in,\quad \notin,\quad \subset,\quad \supset,\quad \cup,\quad \cap,\quad \mathbb{R},\quad \forall,\quad \exists")

    st.header("💡 Otros útiles")
    st.latex(r"\text{Texto dentro de ecuación},\quad \overline{x},\quad \vec{v},\quad \dots,\quad \cdots")

    st.markdown("---")
    st.subheader("✏ Escribe tu propia fórmula LaTeX:")
    formula = st.text_area("Ingresa tu fórmula:", value=r"\int_0^1 x^2 \, dx")
    st.markdown("#### 👁 Vista previa:")
    st.latex(formula)
    st.divider()  # ✅ indentación corregida

    st.subheader("📋 Tabla de comandos comunes en LaTeX")

    st.markdown("""
| Comando | Resultado | Significado |
|---------|-----------|-------------|
| \\frac{a}{b} | $\\frac{a}{b}$ | Fracción |
| a^2 | $a^2$ | Potencia |
| x_1 | $x_1$ | Subíndice |
| \\sqrt{x} | $\\sqrt{x}$ | Raíz cuadrada |
| \\sqrt[3]{x} | $\\sqrt[3]{x}$ | Raíz cúbica |
| \\cdot | $\\cdot$ | Producto punto |
| \\times | $\\times$ | Multiplicación |
| \\div | $\\div$ | División |
| \\pm | $\\pm$ | Más/menos |
| \\leq | $\\leq$ | Menor o igual |
| \\geq | $\\geq$ | Mayor o igual |
| \\neq | $\\neq$ | Distinto |
| \\infty | $\\infty$ | Infinito |
| \\sum_{i=1}^n | $\\sum_{i=1}^n$ | Sumatoria |
| \\int_a^b | $\\int_a^b$ | Integral |
| \\lim_{x \\to 0} | $\\lim_{x \\to 0}$ | Límite |
| \\vec{v} | $\\vec{v}$ | Vector |
| \\overline{a} | $\\overline{a}$ | Línea superior |
| \\text{texto} | $\\text{texto}$ | Texto dentro de fórmula |
| \\mathbb{R} | $\\mathbb{R}$ | Conjunto ℝ |
| \\forall, \\exists | $\\forall$, $\\exists$ | Cuantificadores |
| \\cup, \\cap | $\\cup$, $\\cap$ | Unión e intersección |
""", unsafe_allow_html=True)
elif page == 6:
    st.title("Diseño de Página y Márgenes")

    st.write("""
    En LaTeX, el diseño de página y los márgenes se pueden personalizar fácilmente con el paquete geometry.
    Este paquete te permite definir el tamaño del papel y los márgenes superior, inferior, izquierdo y derecho.

    ### Personalizar márgenes con el paquete geometry

    latex
    \\usepackage[a4paper, left=2.5cm, right=3.5cm, top=45mm, bottom=20mm]{geometry}
    

    Explicación de los parámetros:
    - a4paper: define el tamaño del papel.
    - left=2.5cm: margen izquierdo de 2.5 cm.
    - right=3.5cm: margen derecho de 3.5 cm.
    - top=45mm: margen superior de 4.5 cm.
    - bottom=20mm: margen inferior de 2 cm.

    Puedes ajustar estos valores según el formato que exija tu universidad, revista o institución.

    ---

    ### Encabezados y pies de página con fancyhdr

    Para personalizar encabezados y pies de página, se utiliza el paquete fancyhdr. Este permite colocar textos diferentes en la parte izquierda, central y derecha de cada página, tanto en la parte superior como inferior.

    latex
    \\usepackage{fancyhdr}
    \\pagestyle{fancy}

    % Encabezado
    \\fancyhead[L]{Nombre del autor}
    \\fancyhead[C]{Título del documento}
    \\fancyhead[R]{\\thepage}  % Número de página

    % Pie de página (opcional)
    \\fancyfoot[L]{Facultad de Ciencias}
    \\fancyfoot[C]{}
    \\fancyfoot[R]{\\today}  % Fecha
    

    Consejos:
    - Puedes borrar los contenidos predeterminados con \\fancyhead{} o \\fancyfoot{} si deseas empezar desde cero.
    - Si quieres encabezados/pies diferentes entre páginas pares e impares (como en un libro), puedes usar la opción \\documentclass[twoside]{article} y configurar cada lado con \\fancyhead[LO]{...} y \\fancyhead[RE]{...}.

    ---

    Estas herramientas son muy útiles para dar un estilo profesional y organizado a tus documentos. ¡Personaliza el diseño como más te convenga!
    """)
elif page == 7:
    st.title("Gráficos y Diagramas en LaTeX")

    st.write("""
    En LaTeX, puedes crear gráficos vectoriales y diagramas directamente dentro del documento utilizando los paquetes TikZ y PGFPlots. Estos paquetes son muy potentes y permiten generar desde simples vectores hasta gráficos matemáticos avanzados.

    ---

    ### 🖊 TikZ — Dibujos vectoriales

    TikZ (que significa "TikZ ist kein Zeichenprogramm", en alemán: "TikZ no es un programa de dibujo") es un paquete para crear figuras geométricas, diagramas, flujos, vectores y más, directamente en LaTeX.

    #### Ejemplo básico:

    latex
    \\usepackage{tikz}

    \\begin{tikzpicture}
      \\draw[->] (0,0) -- (2,0);           % Eje X
      \\draw[->] (0,0) -- (0,2);           % Eje Y
      \\node at (2.2,0) {$x$};             % Etiqueta eje X
      \\node at (0,2.2) {$y$};             % Etiqueta eje Y
      \\draw[blue, thick] (0,0) -- (1,1);  % Vector en azul
    \\end{tikzpicture}
    

    ¿Qué hace este código?
    - Dibuja dos ejes con flechas.
    - Añade etiquetas $x$ y $y$ en sus extremos.
    - Traza un vector desde el origen hasta el punto (1,1) en color azul y línea gruesa.

    Puedes usar TikZ para diagramas de física, geometría, árboles, redes eléctricas, etc.

    ---

    ### 📊 PGFPlots — Gráficas científicas

    El paquete PGFPlots se construye sobre TikZ, y está pensado para crear gráficos de funciones matemáticas o datos experimentales. Es ideal para ciencias como física, matemáticas, economía y más.

    #### Ejemplo de gráfica:

    latex
    \\usepackage{pgfplots}

    \\begin{tikzpicture}
      \\begin{axis}[
          axis lines = left,
          xlabel = $x$,
          ylabel = {$f(x)$},
      ]
        \\addplot [
          domain=0:4,
          samples=100,
          color=red
        ]{x^2};
      \\end{axis}
    \\end{tikzpicture}
    

    ¿Qué hace este código?
    - Configura un sistema de ejes con etiquetas.
    - Grafica la función $f(x) = x^2$ en rojo entre 0 y 4, usando 100 muestras para mayor suavidad.

    ---

    ### ✅ Recomendaciones
    - Para usar estos paquetes en Overleaf, no necesitas instalar nada.
    - En editores locales, asegúrate de compilar con PDFLaTeX o LuaLaTeX (no con compilers simples como latex).
    - Puedes combinar TikZ con otros paquetes como circuitikz, tikz-cd o pgfplots para más funcionalidades.
    - PGFPlots también permite importar datos desde archivos .csv.

    Estas herramientas son poderosas para crear visualizaciones profesionales dentro de tus documentos LaTeX, sin depender de editores gráficos externos.
    """)
cols = st.columns([1, 2, 1])
with cols[0]:
    if st.button("⬅ Anterior") and st.session_state.page > 0:
        st.session_state.page -= 1
with cols[2]:
    if st.button("Siguiente ➡") and st.session_state.page < len(secciones) - 1:
        st.session_state.page += 1

st.markdown("""
<div class='footer'>
    Creado con ❤ por:<br>
    Gabriel Hurtado · Samuel Choles · Julián Salazar · Camila Rodríguez
</div>
""", unsafe_allow_html=True)