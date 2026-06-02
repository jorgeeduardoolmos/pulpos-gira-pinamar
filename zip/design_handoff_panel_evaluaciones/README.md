# Handoff: Panel de Evaluaciones M10 · Liceo Naval

## Overview
Panel web interno del **cuerpo técnico de rugby (división M10, Liceo Naval)** para analizar dos
encuestas trimestrales:

1. **Encuesta al Staff** — el cuerpo técnico evalúa el progreso del equipo en 17 indicadores
   (escala 1–4) agrupados en 4 dimensiones, + 3 preguntas abiertas.
2. **Evaluación Individual** — cada jugador es evaluado en 5 métricas con un semáforo
   Rojo / Amarillo / Verde (escala 1–3) por varios evaluadores.

El objetivo del panel es que las **fortalezas y debilidades del equipo, el desempeño del staff y
los jugadores que necesitan atención** se entiendan **de un vistazo**, con insights calculados
automáticamente (no tablas planas como en la versión anterior).

> ⚠️ **REQUISITO CLAVE — ANONIMATO.** Las respuestas deben ser **anónimas**: la identidad de quien
> evalúa/responde NUNCA debe mostrarse ni viajar al cliente. Los evaluadores se muestran como
> "Evaluador 1…N" (con orden mezclado, no alfabético) y las respuestas abiertas no llevan autor.
> Los **jugadores SÍ** se identifican con nombre (son el sujeto evaluado; uso interno del staff).

## About the Design Files
Los archivos de este bundle son **referencias de diseño hechas en HTML/React (con Babel en el
navegador)** — un prototipo funcional que muestra el look & feel y el comportamiento deseado, **no
código de producción para copiar tal cual**. La tarea es **recrear este diseño en el entorno del
codebase destino** (lo ideal: React + Vite/Next, TypeScript, y una librería de gráficos como
Recharts o visualizaciones propias), usando sus patrones establecidos. Si no existe codebase aún,
elegir el stack más apropiado (sugerido: **React + TypeScript + Vite**, datos desde XLSX/CSV o API).

El prototipo lee los datos desde `panel/data.js` (un `window.RUGBY = {...}`). En producción esos
datos deben venir de la **planilla Excel original** (`M10 - Evaluaciones.xlsx`, 2 solapas:
`Eval_Individual` y `Encuesta_Staff`) o de un backend, parseados y **anonimizados antes** de llegar
al front.

## Fidelity
**Alta fidelidad (hi-fi).** Colores, tipografía, espaciado, semáforo e interacciones son finales.
Recrear la UI con fidelidad de píxel usando las librerías del codebase.

---

## Modelo de datos

### Solapa `Eval_Individual` (una fila = un evaluador califica a un jugador)
Columnas: `Trimestre, Fecha, Evaluador, Jugador, Pase, Tacle, Percepción, Frustración, Foco`.
- Cada métrica toma un valor categórico **`Rojo` | `Amarillo` | `Verde`** que mapea a
  **Rojo=1, Amarillo=2, Verde=3**.
- Hay **35 jugadores × 6 evaluadores = 210 filas** (T1).
- **Frustración**: más alto = mejor (igual dirección que las demás; NO invertir).
- Pueden existir celdas con valores inválidos (p.ej. un `"14"` por error de carga) → tratar como
  **nulo/ausente**, no romper.

**Cálculos:**
- Promedio por jugador y métrica = media de los votos válidos de los evaluadores.
- Promedio del jugador = media de sus 5 promedios de métrica.
- KPI de la división por métrica = media de **todos** los votos de esa métrica.
- Distribución por métrica = conteo de Rojo / Amarillo / Verde.
- "Votos en rojo" de un jugador = cantidad de votos crudos `Rojo` que recibió.

### Solapa `Encuesta_Staff` (una fila = un evaluador)
Columnas: `Trimestre, Fecha, Evaluador,` + **17 preguntas (1–4)** + 3 abiertas
(`Aprendizajes y avances técnicos/tácticos`, `Oportunidades de mejora del staff`, `Suma libre`).
- **7 evaluadores** (T1). Alguna fila puede no tener las abiertas → manejar vacío.

**Agrupación de las 17 preguntas en 4 dimensiones (KPIs):**
- **Técnica**: Progreso técnico general · Calidad y seguridad del tackle · Relación del equipo con el contacto · Calidad del pase y recepción en movimiento · Continuidad post-contacto
- **Táctica**: Comprensión de la ubicación en cancha · Organización del ataque · Organización de la defensa · Lectura del espacio y toma de decisiones · Disciplina táctica
- **Emocional**: Actitud frente al contacto · Resiliencia frente al error · Conexión entre jugadores
- **Staff**: Claridad de roles · Coordinación en entrenamientos · Coordinación en partidos · Comunicación interna

**Cálculos:**
- Promedio por pregunta = media de los 7 votos válidos.
- **Dispersión** por pregunta = desviación estándar poblacional de los votos (mide consenso del staff).
- KPI por dimensión = media de todos los votos de las preguntas de esa dimensión.
- Promedio global = media de los 17 promedios de pregunta.

### Anonimización (hacer en el parseo, antes del front)
- Recolectar evaluadores distintos por solapa → asignar `"Evaluador 1..N"` con un **shuffle
  determinístico** (semilla fija) para que el orden NO sea alfabético/adivinable.
- En la tabla del staff, ordenar columnas por el ID anónimo.
- Las respuestas abiertas se muestran SIN autor (etiqueta "Respuesta anónima").
- Nota: el texto libre puede mencionar nombres propios escritos por el respondente; el prototipo NO
  los edita (es contenido del autor). Si se requiere anonimato estricto, scrub manual/automático aparte.

---

## Design Tokens

### Color (CSS custom properties, ver `<style>` en el HTML)
```
/* Superficies (dark) */
--bg:           #080A0F   /* fondo app */
--panel:        #0F141E   /* base de cards (con gradiente a --panel-2) */
--panel-2:      #141A26
--panel-3:      #1A2231   /* hover / chips */
--line:         rgba(255,255,255,.07)
--line-2:       rgba(255,255,255,.12)
--line-strong:  rgba(255,255,255,.18)

/* Texto */
--text:   #ECEFF6    --text-2: #9AA5B6    --text-3: #626D80    --text-4: #454F60

/* Acento (azul "naval / performance") */
--accent:      #3F9BF5
--accent-soft: rgba(63,155,245,.14)
--accent-line: rgba(63,155,245,.4)

/* Semáforo (datos) */
--rojo:  #F0544F   (rgb 240,84,79)
--ambar: #F2B23E   (rgb 242,178,62)
--verde: #3FBF7F   (rgb 63,191,127)
--verde-profundo (heatmap tope): rgb 46,168,108
*-soft: misma color a 14% alpha
```

### Tipografía (Google Fonts)
- **Display** (`--display`): **Saira Condensed** — pesos 500/600/700. Uso: títulos, labels de
  sección (UPPERCASE, letter-spacing .14–.18em), números de KPI, encabezados de tabla.
- **Texto/datos** (`--sans`): **Saira** — pesos 400/450/500/600/700. Números con
  `font-variant-numeric: tabular-nums`.
- Escala aprox: KPI value 42px/700; título topbar 25px/700; sección 14px/600 tracked;
  body 15px; tabla 13.5px; labels 10–11px tracked.

### Forma / espaciado
- Radios: cards `14px`, sub-elementos `9px`, chips `6px`, pills `999px`.
- Sidebar `248px` fijo. Content `max-width:1480px`, padding `28px 32px`.
- Gap entre secciones `30px`; grid interno `16px`.
- Cards: `background: linear-gradient(180deg,var(--panel-2),var(--panel))`, `border:1px solid var(--line)`.
- Hover de KPI: `translateY(-2px)` + borde `--line-2`, transición `.15s`.
- Animación de entrada de vista: fade + translateY(6px), `.4s ease` (no esencial; el contenido
  debe ser visible aunque la animación no corra).

### Semáforo — zonas y cortes (DECIDIDOS, ajustables)
Función `zoneOf(valor, escala)` con cortes por escala:
- **Individual (1–3)** cortes `[1.67, 2.33, 2.67]`
- **Staff (1–4)** cortes `[1.8, 2.7, 3.5]`

Zonas: `< cut0` = **En riesgo** (rojo) · `< cut1` = **En desarrollo** (ámbar) ·
`< cut2` = **Sólido** (verde) · `≥ cut2` = **Destacado** (verde intenso).

**Color continuo del heatmap/barras** (`scoreColor`): interpola rojo→ámbar→verde anclado a los
cortes (los valores bajos quedan rojos, el medio ámbar, los altos verdes), no una rampa lineal cruda.
Ver implementación exacta en `panel/ui.jsx`.

---

## Screens / Views

Layout general: **sidebar fija (248px)** a la izquierda + **main** con **topbar sticky** (eyebrow +
título + selector de Trimestre segmentado, T2–T4 deshabilitados si no hay datos) + **content**.

### Sidebar
- Brand: cuadro/crest 42px con "M10" (Saira Condensed, color acento) + "LICEO NAVAL" /
  "RUGBY · INFANTILES".
- Nav (label "EVALUACIONES"): items **Encuesta al Staff** y **Evaluación Individual**. Item activo:
  fondo `--accent-soft`, borde `--accent-line`, texto `#cfe5ff`. Hover: fondo `--panel-2`.
- Pie: "Evaluación de desempeño · Cuerpo técnico · Uso interno" + badge con candado
  **"Respuestas anónimas"**.

### Vista 1 — Encuesta al Staff
1. **Promedio por dimensión** — 4 `KpiCard` (Técnica, Táctica, Emocional, Staff): label + descriptor
   chico + valor grande coloreado por zona + `/4` + badge de zona + meter. **Clickeables**: filtran el
   "Detalle por pregunta". Badge "Global X.X" a la derecha del encabezado.
2. **Lectura rápida** — 3 `insight` cards:
   - **Fortalezas**: top 4 preguntas por promedio (rank, nombre, dimensión, valor).
   - **A trabajar**: bottom 4 preguntas.
   - **Consenso del staff**: "Mayor acuerdo" (3 preguntas con menor dispersión, ±sd en verde) y
     "Más dividido" (3 con mayor dispersión, ±sd en ámbar).
3. **Detalle por pregunta** — barras horizontales agrupadas por dimensión (encabezado de dimensión
   con dot + "prom X.X"), cada barra coloreada por `scoreColor`, ordenadas desc. Filtrable por la KPI
   clickeada. Leyenda 1–4 al pie.
4. **Tabla completa** — orden por columnas (Dimensión, Indicador, **E1…E7** voto anónimo como chip
   de color, Disp. ±, Prom. como pill de zona). Sticky header.
5. **Respuestas abiertas** — 2 columnas (Aprendizajes [verde], Oportunidades de mejora [ámbar]) +
   "Suma libre" (2-up). Cada respuesta es una `quote` (borde izquierdo de color) con pie
   "Respuesta anónima".

### Vista 2 — Evaluación Individual
1. **Promedio de la división** — 5 KPIs (Pase, Tacle, Percepción, Frustración, Foco): valor `/3` +
   **mini barra de distribución** Rojo/Amarillo/Verde + conteos. Badge "Global X.X" +
   **select de evaluador** ("Todos los evaluadores" / "Mirada · Evaluador N" → recalcula todo con los
   votos de ese evaluador).
2. **Lectura rápida** — 3 insight cards:
   - **Jugadores en foco**: 5 jugadores con menor promedio (rank, nombre corto, "N votos en rojo", valor).
   - **Referentes**: top 5 jugadores.
   - **Fortaleza y déficit del equipo**: mejor y peor dimensión + línea resumen (# en riesgo / # destacados).
3. **Mapa de calor por jugador** — filas = jugadores (default orden por promedio ascendente, peor
   arriba), columnas = 5 métricas + **Prom.** Celdas con fondo `scoreColor` y valor. **Click en
   columna ordena** por ella. **Buscador** de jugador. **Hover** resalta fila+columna. Scroll-x si no
   entra. Nombres en formato corto "Nombre Apellido".
4. **Detalle por jugador** — tabla ordenable: Jugador · 5 métricas (pill de zona) · Rojos · Promedio
   (pill sólida).

---

## Interactions & Behavior
- **Navegación**: sidebar cambia la vista (estado `view`). No recarga.
- **Trimestre**: segmented control; sólo T1 activo (resto disabled con tooltip "Sin datos cargados").
  Al haber más trimestres en los datos, se habilitan solos (lista `meta.trimestres`).
- **KPIs de dimensión (Staff)**: toggle de filtro del detalle por pregunta.
- **Ordenamiento**: click en headers de tabla y de heatmap; alterna asc/desc; flecha indicadora en acento.
- **Buscador (Individual)**: filtra heatmap y tabla por nombre (case-insensitive).
- **Hover heatmap**: resalta fila (label) + columna (header) + outline blanco en celda.
- **Select de evaluador (Individual)**: recalcula KPIs/insights/heatmap/tabla con un solo evaluador.
- Transiciones `.15s` en hover; barras animan width `.6s`.
- Responsive: < 880px la sidebar se oculta (margen 0) — se puede mejorar con un drawer en producción.

## State Management
- `view`: `'staff' | 'individual'`.
- `trimestre`: string (default `'T1'`), validado contra `meta.trimestres`.
- Staff: `catFilter` (dimensión|null), `sort` ({key,dir}).
- Individual: `evaluador` (`'__all'`|id), `sort` ({key,dir}), `q` (búsqueda), `hover` ({r,c}).
- Todos los agregados se derivan con `useMemo` a partir de los datos crudos + filtros (no se
  precalculan promedios fuera; recalcular permite el filtro por evaluador y por trimestre).

## Assets
- **Sin imágenes ni íconos externos.** Íconos = SVG inline minimalistas (ver `ICONS` en `ui.jsx`).
- Crest = texto "M10". Si el club provee escudo oficial, reemplazar el contenido del `.crest`.
- Fuentes: Google Fonts (Saira, Saira Condensed).

## Files (en este bundle)
- `Panel M10 - Liceo Naval.html` — shell, todos los design tokens en `<style>`, carga de scripts.
- `panel/data.js` — `window.RUGBY` con datos **ya anonimizados** (referencia del modelo + fixture).
- `panel/ui.jsx` — helpers (`mean`, `stdev`, `zoneOf`, `scoreColor`, escalas) + primitivas
  (`KpiCard`, `BarRow`, `DistBar`, `InsightItem`, `Th`, badges, íconos).
- `panel/staff.jsx` — vista Encuesta Staff + `useStaffStats`.
- `panel/individual.jsx` — vista Evaluación Individual + `useIndStats`.
- `panel/app.jsx` — shell/navegación/filtros y render.

## Cómo correr el prototipo
Servir la carpeta con cualquier static server (los `.jsx` se transpilan con Babel en el navegador) y
abrir `Panel M10 - Liceo Naval.html`. Para producción, precompilar y mover los datos a un parser de
XLSX/CSV o API, **anonimizando en el servidor/parseo**.
