import streamlit as st
import base64
from pathlib import Path

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Gira Pinamar 2024 · Pulpos Liceo Naval",
    page_icon="🐙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow+Condensed:wght@400;600;700&family=Barlow:wght@400;500&display=swap');

/* ── Base Reset ── */
html, body, [class*="css"] {
    font-family: 'Barlow', sans-serif;
    color: #e8f4e8;
}

.stApp {
    background: #060d06;
    background-image:
        radial-gradient(ellipse at 10% 0%, rgba(30, 185, 80, 0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 100%, rgba(0, 140, 220, 0.08) 0%, transparent 50%);
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── HERO ── */
.hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 60px 20px;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 60% at 50% 0%, rgba(79, 200, 79, 0.15) 0%, transparent 70%),
        radial-gradient(ellipse 60% 80% at 50% 100%, rgba(0, 160, 255, 0.12) 0%, transparent 70%);
    pointer-events: none;
}

.hero-eyebrow {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: #7bdd7b;
    margin-bottom: 12px;
    opacity: 0.9;
}

.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(5rem, 15vw, 14rem);
    line-height: 0.9;
    letter-spacing: 0.02em;
    background: linear-gradient(160deg, #a8f07a 0%, #4fc84f 40%, #00c8ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    text-shadow: none;
    filter: drop-shadow(0 0 60px rgba(79, 200, 79, 0.35));
}

.hero-subtitle {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(1.8rem, 5vw, 4rem);
    letter-spacing: 0.08em;
    color: #00c8ff;
    margin: 8px 0 30px;
    opacity: 0.9;
}

.hero-logo {
    width: clamp(180px, 22vw, 320px);
    filter: drop-shadow(0 0 40px rgba(79, 200, 79, 0.5));
    margin-bottom: 30px;
    animation: float 4s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-14px); }
}

.hero-dates {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 20px;
}

.date-pill {
    background: rgba(79, 200, 79, 0.12);
    border: 1px solid rgba(79, 200, 79, 0.4);
    border-radius: 100px;
    padding: 10px 28px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    color: #a8f07a;
}

/* ── SCROLL ARROW ── */
.scroll-arrow {
    position: absolute;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2rem;
    color: rgba(79, 200, 79, 0.5);
    animation: bounce 2s infinite;
}
@keyframes bounce {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50% { transform: translateX(-50%) translateY(10px); }
}

/* ── DIVIDER ── */
.divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #4fc84f, #00c8ff, #4fc84f, transparent);
    margin: 0;
    opacity: 0.4;
}

/* ── SECTION ── */
.section {
    padding: 70px 5vw;
    max-width: 1200px;
    margin: 0 auto;
}

.section-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    color: #4fc84f;
    margin-bottom: 6px;
}

.section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(2.5rem, 6vw, 5rem);
    line-height: 1;
    letter-spacing: 0.04em;
    color: #ffffff;
    margin-bottom: 30px;
}

.section-title span {
    color: #4fc84f;
}

/* ── OBJETIVO ── */
.objetivo-box {
    background: linear-gradient(135deg, rgba(79, 200, 79, 0.07) 0%, rgba(0, 200, 255, 0.05) 100%);
    border: 1px solid rgba(79, 200, 79, 0.2);
    border-left: 4px solid #4fc84f;
    border-radius: 12px;
    padding: 36px 40px;
    font-size: 1.15rem;
    line-height: 1.85;
    color: #c8e8c8;
}

/* ── GRID CARDS ── */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-top: 10px;
}

.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 28px;
    transition: border-color 0.3s, transform 0.3s;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(79,200,79,0.05), transparent);
    opacity: 0;
    transition: opacity 0.3s;
}
.card:hover::before { opacity: 1; }
.card:hover {
    border-color: rgba(79, 200, 79, 0.35);
    transform: translateY(-4px);
}

.card-icon { font-size: 2.2rem; margin-bottom: 14px; }
.card-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #a8f07a;
    margin-bottom: 10px;
}
.card-body {
    font-size: 0.95rem;
    line-height: 1.7;
    color: #9eb89e;
}
.card-body strong { color: #c8e8c8; }

/* ── CRONOGRAMA ── */
.timeline {
    position: relative;
    padding-left: 30px;
}
.timeline::before {
    content: '';
    position: absolute;
    left: 8px; top: 0; bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, #4fc84f, #00c8ff, #4fc84f);
    opacity: 0.4;
}

.day-block { margin-bottom: 40px; }
.day-header {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    letter-spacing: 0.08em;
    color: #4fc84f;
    margin-bottom: 16px;
    position: relative;
}
.day-header::before {
    content: '●';
    position: absolute;
    left: -30px;
    color: #4fc84f;
    font-size: 0.8rem;
    top: 50%;
    transform: translateY(-50%);
}

.event-row {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding: 12px 16px;
    border-radius: 10px;
    margin-bottom: 8px;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
}
.event-time {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    font-size: 0.85rem;
    color: #00c8ff;
    letter-spacing: 0.05em;
    white-space: nowrap;
    min-width: 80px;
    padding-top: 2px;
}
.event-desc {
    font-size: 0.95rem;
    color: #b0c8b0;
    line-height: 1.5;
}

/* ── COMIDAS TABLE ── */
.comidas-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(79,200,79,0.2);
}
.comidas-header {
    background: rgba(79, 200, 79, 0.2);
    padding: 14px 10px;
    text-align: center;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #a8f07a;
    border-right: 1px solid rgba(79,200,79,0.15);
}
.comidas-header:last-child { border-right: none; }

.comidas-cell {
    padding: 14px 10px;
    text-align: center;
    font-size: 0.88rem;
    color: #9eb89e;
    border-right: 1px solid rgba(255,255,255,0.05);
    border-top: 1px solid rgba(255,255,255,0.05);
    line-height: 1.4;
}
.comidas-cell:last-child { border-right: none; }
.comidas-cell.row-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    color: #00c8ff;
    letter-spacing: 0.05em;
    font-size: 0.85rem;
    text-transform: uppercase;
    background: rgba(0,200,255,0.05);
}
.comidas-cell.incluido { color: #4fc84f; }
.comidas-cell.no-incluido { color: rgba(255,255,255,0.3); }

/* ── CUOTAS ── */
.cuotas-row {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 10px;
    margin-top: 10px;
}
.cuota-card {
    background: rgba(79,200,79,0.07);
    border: 1px solid rgba(79,200,79,0.2);
    border-radius: 12px;
    padding: 16px 10px;
    text-align: center;
}
.cuota-mes {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4fc84f;
    margin-bottom: 8px;
}
.cuota-monto {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.4rem;
    color: #ffffff;
    letter-spacing: 0.03em;
}
.cuota-card.last {
    border-color: rgba(0,200,255,0.3);
    background: rgba(0,200,255,0.07);
}
.cuota-card.last .cuota-mes { color: #00c8ff; }

/* ── LLEVAR ── */
.llevar-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}
.llevar-box {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 26px;
}
.llevar-box.no-llevar {
    border-color: rgba(255, 80, 80, 0.2);
    background: rgba(255, 80, 80, 0.03);
}
.llevar-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 14px;
}
.llevar-title.si { color: #4fc84f; }
.llevar-title.no { color: #ff6060; }
.llevar-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 7px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    font-size: 0.92rem;
    color: #9eb89e;
    line-height: 1.4;
}
.llevar-item:last-child { border-bottom: none; }
.llevar-item .dot { flex-shrink: 0; font-size: 0.6rem; margin-top: 5px; }
.dot.si { color: #4fc84f; }
.dot.no { color: #ff6060; }

/* ── DOCS ── */
.docs-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.doc-row {
    display: flex;
    align-items: center;
    gap: 14px;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 14px 20px;
    font-size: 0.95rem;
    color: #b0c8b0;
}
.doc-row .doc-icon { font-size: 1.4rem; }

/* ── STAFF ── */
.staff-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 14px;
    margin-top: 10px;
}
.staff-card {
    background: rgba(0,200,255,0.06);
    border: 1px solid rgba(0,200,255,0.2);
    border-radius: 12px;
    padding: 18px 14px;
    text-align: center;
}
.staff-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #00c8ff;
    letter-spacing: 0.06em;
}

/* ── FOOTER ── */
.footer {
    background: rgba(0,0,0,0.5);
    border-top: 1px solid rgba(79,200,79,0.15);
    padding: 40px 5vw;
    text-align: center;
    color: rgba(200,232,200,0.35);
    font-size: 0.85rem;
    letter-spacing: 0.05em;
}
.footer strong { color: rgba(79,200,79,0.6); }

/* ── STAT STRIP ── */
.stat-strip {
    display: flex;
    gap: 0;
    border-top: 1px solid rgba(79,200,79,0.15);
    border-bottom: 1px solid rgba(79,200,79,0.15);
    background: rgba(79,200,79,0.04);
    overflow: hidden;
}
.stat-item {
    flex: 1;
    padding: 24px 20px;
    text-align: center;
    border-right: 1px solid rgba(79,200,79,0.1);
}
.stat-item:last-child { border-right: none; }
.stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    line-height: 1;
    color: #4fc84f;
    letter-spacing: 0.04em;
}
.stat-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(200,232,200,0.45);
    margin-top: 4px;
}

/* ── HIGHLIGHT CHIP ── */
.chip {
    display: inline-block;
    background: rgba(79,200,79,0.12);
    border: 1px solid rgba(79,200,79,0.3);
    border-radius: 100px;
    padding: 4px 14px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7bdd7b;
    margin: 3px 3px;
}

/* ── LINK BUTTON ── */
.link-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(0,200,255,0.08);
    border: 1px solid rgba(0,200,255,0.3);
    border-radius: 8px;
    padding: 10px 18px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    color: #00c8ff;
    text-decoration: none;
    transition: background 0.2s;
}
.link-btn:hover { background: rgba(0,200,255,0.15); }

/* ── WARNING BOX ── */
.warn-box {
    background: rgba(255,180,0,0.07);
    border: 1px solid rgba(255,180,0,0.25);
    border-radius: 12px;
    padding: 20px 24px;
    display: flex;
    gap: 14px;
    align-items: flex-start;
    font-size: 0.95rem;
    color: #d4b060;
    line-height: 1.65;
}
.warn-icon { font-size: 1.6rem; flex-shrink: 0; }

/* ── RESPONSIVE ── */
@media (max-width: 700px) {
    .cuotas-row { grid-template-columns: repeat(4, 1fr); }
    .llevar-grid { grid-template-columns: 1fr; }
    .comidas-grid { grid-template-columns: 1fr; }
    .comidas-header:not(:first-child) { display: none; }
}
</style>
""", unsafe_allow_html=True)

# ─── Load logo from PDF (display as uploaded) ────────────────────────────────
logo_path = Path("pulpos.pdf")

# Try to use a base64 embedded logo; fallback to emoji if file not present
def get_logo_html():
    try:
        with open("pulpos.pdf", "rb") as f:
            pass
        # We can't embed PDF directly in <img>, so we use the emoji fallback
        # with a big octopus-style display
        return '<div style="font-size:8rem;filter:drop-shadow(0 0 40px rgba(79,200,79,0.5));animation:float 4s ease-in-out infinite;margin-bottom:20px;">🐙</div>'
    except:
        return '<div style="font-size:8rem;margin-bottom:20px;">🐙</div>'

# ─── HERO ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
    {get_logo_html()}
    <div class="hero-eyebrow">División M10 · Liceo Naval</div>
    <h1 class="hero-title">PULPOS</h1>
    <div class="hero-subtitle">Gira Pinamar 2024</div>
    <div class="hero-dates">
        <div class="date-pill">📅 13 · 14 · 15 Noviembre</div>
        <div class="date-pill">📍 Pinamar · Buenos Aires</div>
        <div class="date-pill">🏉 vs Camarones</div>
    </div>
    <div class="scroll-arrow">↓</div>
</div>
""", unsafe_allow_html=True)

# ─── STAT STRIP ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-strip">
    <div class="stat-item">
        <div class="stat-num">34</div>
        <div class="stat-label">Jugadores</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">8</div>
        <div class="stat-label">Staff</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">3</div>
        <div class="stat-label">Días</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">7</div>
        <div class="stat-label">Cuotas</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">1</div>
        <div class="stat-label">Partido</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── OBJETIVO ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">01</div>
    <div class="section-title">Nuestro <span>Objetivo</span></div>
    <div class="objetivo-box">
        <p>🏉 Fortalecer la amistad, el compañerismo y el espíritu de equipo a través del juego, la convivencia y el respeto.</p>
        <p>🌊 Vivir juntos una experiencia inolvidable dentro y fuera de la cancha, aprendiendo a compartir, cuidar al otro y disfrutar en grupo, con alegría y compromiso.</p>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── INTEGRANTES ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">02</div>
    <div class="section-title"><span>Integrantes</span></div>
    <div class="cards-grid">
        <div class="card">
            <div class="card-icon">🐙</div>
            <div class="card-title">Jugadores</div>
            <div class="card-body"><strong style="font-size:2.5rem;font-family:'Bebas Neue',sans-serif;color:#4fc84f;">34</strong><br>Guerreros del mar</div>
        </div>
        <div class="card">
            <div class="card-icon">🎽</div>
            <div class="card-title">Staff Técnico</div>
            <div class="card-body"><strong style="font-size:2.5rem;font-family:'Bebas Neue',sans-serif;color:#00c8ff;">8</strong><br>Profes & acompañantes</div>
        </div>
    </div>
    <div style="margin-top:24px;">
        <div class="section-label">Staff</div>
        <div class="staff-grid">
            <div class="staff-card"><div class="staff-name">🧑‍💼 Ote</div></div>
            <div class="staff-card"><div class="staff-name">🧑‍💼 Ale</div></div>
            <div class="staff-card"><div class="staff-name">🧑‍💼 Mati</div></div>
            <div class="staff-card"><div class="staff-name">🧑‍💼 Fran</div></div>
            <div class="staff-card"><div class="staff-name">🧑‍💼 Marian</div></div>
            <div class="staff-card"><div class="staff-name">🧑‍💼 Tucu</div></div>
            <div class="staff-card"><div class="staff-name">🧑‍💼 Cris</div></div>
            <div class="staff-card"><div class="staff-name">🧑‍💼 Ema</div></div>
        </div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── CLUB Y COMPLEJO ──────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">03 — 04</div>
    <div class="section-title">Club & <span>Alojamiento</span></div>
    <div class="cards-grid">
        <div class="card">
            <div class="card-icon">🏉</div>
            <div class="card-title">Club Visitante</div>
            <div class="card-body">
                <strong>Camarones · Pinamar</strong><br><br>
                El rival que nos espera con el campo listo y el tercer tiempo preparado.
            </div>
        </div>
        <div class="card">
            <div class="card-icon">🏨</div>
            <div class="card-title">Espacio Arena Hotel</div>
            <div class="card-body">
                <span class="chip">A/A</span>
                <span class="chip">WiFi</span>
                <span class="chip">TV Satelital</span>
                <span class="chip">Frigobar</span>
                <span class="chip">Ropa de cama</span>
                <span class="chip">Toallas</span>
                <span class="chip">Pileta</span>
                <span class="chip">Quinchos</span>
                <span class="chip">Asadores</span>
                <span class="chip">Cancha Fútbol</span>
                <span class="chip">Cancha Tenis</span>
                <span class="chip">Estacionamiento techado</span>
                <br><br>
                <a class="link-btn" href="https://share.google/sHaJsoc6ak4D2hrFk" target="_blank">🗺️ Ver en Maps</a>
            </div>
        </div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── FECHAS Y TRANSPORTE ──────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">05 — 07</div>
    <div class="section-title">Fechas & <span>Logística</span></div>
    <div class="cards-grid">
        <div class="card">
            <div class="card-icon">🛫</div>
            <div class="card-title">Partida</div>
            <div class="card-body">
                <strong>Viernes 13 de Noviembre</strong><br>
                Encuentro en el Liceo: <strong>7:00 am</strong><br>
                Salida: <strong>8:00 hs</strong>
            </div>
        </div>
        <div class="card">
            <div class="card-icon">🏠</div>
            <div class="card-title">Regreso</div>
            <div class="card-body">
                <strong>Domingo 15 de Noviembre</strong><br>
                Salida Pinamar: <strong>15:00 hs</strong><br>
                Llegada aprox.: <strong>20:00 hs</strong>
            </div>
        </div>
        <div class="card">
            <div class="card-icon">🚌</div>
            <div class="card-title">Transporte</div>
            <div class="card-body">
                <strong>Serrano Turismo</strong><br><br>
                Control alcoholemia obligatorio.<br>
                Estacionamiento en Liceo el viernes y el domingo para padres.
            </div>
        </div>
        <div class="card">
            <div class="card-icon">🏥</div>
            <div class="card-title">Seguro Médico</div>
            <div class="card-body">
                <strong>Assist Travel</strong><br><br>
                Asistencia médica completa durante toda la gira.
            </div>
        </div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── CRONOGRAMA ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">09</div>
    <div class="section-title"><span>Cronograma</span></div>
    <div class="timeline">
        <div class="day-block">
            <div class="day-header">Viernes 13</div>
            <div class="event-row"><div class="event-time">07:00 am</div><div class="event-desc">🏫 Encuentro en el Liceo</div></div>
            <div class="event-row"><div class="event-time">08:00 hs</div><div class="event-desc">🚌 Salida hacia Pinamar</div></div>
            <div class="event-row"><div class="event-time">15:00 hs</div><div class="event-desc">🏨 Arribo al hotel · Almuerzo</div></div>
            <div class="event-row"><div class="event-time">Tarde</div><div class="event-desc">🌊 Día de playa</div></div>
            <div class="event-row"><div class="event-time">Noche</div><div class="event-desc">🍽️ Cena en el hotel</div></div>
        </div>
        <div class="day-block">
            <div class="day-header">Sábado 14</div>
            <div class="event-row"><div class="event-time">Mañana</div><div class="event-desc">☕ Desayuno en hotel</div></div>
            <div class="event-row"><div class="event-time">10:00 hs</div><div class="event-desc">🏉 Partido vs Camarones</div></div>
            <div class="event-row"><div class="event-time">Post-partido</div><div class="event-desc">🍻 Tercer tiempo en Camarones</div></div>
            <div class="event-row"><div class="event-time">Tarde</div><div class="event-desc">🏄 Playa + Sandboard + Inflables</div></div>
            <div class="event-row"><div class="event-time">Noche</div><div class="event-desc">🍽️ Cena en Hotel</div></div>
        </div>
        <div class="day-block">
            <div class="day-header">Domingo 15</div>
            <div class="event-row"><div class="event-time">Mañana</div><div class="event-desc">☕ Desayuno en Hotel</div></div>
            <div class="event-row"><div class="event-time">Mañana</div><div class="event-desc">🌿 Kalo Eco Parque · Cariló <a class="link-btn" style="padding:4px 12px;font-size:0.8rem;" href="https://share.google/RXsnm8bbZVZyqlAeI" target="_blank">🗺️ Maps</a></div></div>
            <div class="event-row"><div class="event-time">Almuerzo</div><div class="event-desc">🍽️ Almuerzo en Hotel</div></div>
            <div class="event-row"><div class="event-time">15:00 hs</div><div class="event-desc">🚌 Salida hacia el Liceo</div></div>
            <div class="event-row"><div class="event-time">Camino</div><div class="event-desc">🥐 Merienda en el Bondi</div></div>
            <div class="event-row"><div class="event-time">~20:00 hs</div><div class="event-desc">🏁 Llegada al Liceo</div></div>
        </div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── COMIDAS ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">11</div>
    <div class="section-title"><span>Comidas</span></div>
    <div class="comidas-grid">
        <div class="comidas-header">Comida</div>
        <div class="comidas-header">Viernes</div>
        <div class="comidas-header">Sábado</div>
        <div class="comidas-header">Domingo</div>

        <div class="comidas-cell row-label">🌅 Desayuno</div>
        <div class="comidas-cell no-incluido">— No incluido</div>
        <div class="comidas-cell incluido">✅ Hotel</div>
        <div class="comidas-cell incluido">✅ Hotel</div>

        <div class="comidas-cell row-label">☀️ Almuerzo</div>
        <div class="comidas-cell incluido">✅ Hotel</div>
        <div class="comidas-cell incluido">✅ Camarones</div>
        <div class="comidas-cell incluido">✅ Hotel</div>

        <div class="comidas-cell row-label">🌤️ Merienda</div>
        <div class="comidas-cell incluido">✅ Playa</div>
        <div class="comidas-cell incluido">✅ Playa</div>
        <div class="comidas-cell incluido">✅ Bondi</div>

        <div class="comidas-cell row-label">🌙 Cena</div>
        <div class="comidas-cell incluido">✅ Hotel</div>
        <div class="comidas-cell incluido">✅ Hotel</div>
        <div class="comidas-cell no-incluido">—</div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── COSTO Y CUOTAS ───────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">06</div>
    <div class="section-title">Costo & <span>Cuotas</span></div>
    <div class="cards-grid" style="margin-bottom:30px;">
        <div class="card">
            <div class="card-icon">💰</div>
            <div class="card-title">Costo total por jugador</div>
            <div class="card-body">
                <span style="font-family:'Bebas Neue',sans-serif;font-size:2.8rem;color:#a8f07a;">$635.500</span><br>
                <em style="font-size:0.85rem;color:#7a9a7a;">Si viajan menos de 30 jugadores, la diferencia se distribuye entre todos los pasajeros.</em>
            </div>
        </div>
        <div class="card">
            <div class="card-icon">🗓️</div>
            <div class="card-title">Modalidad de Pago</div>
            <div class="card-body"><strong>7 cuotas</strong><br>6 cuotas de $100.000 + 1 cuota final de $35.500</div>
        </div>
    </div>
    <div class="cuotas-row">
        <div class="cuota-card"><div class="cuota-mes">Abril</div><div class="cuota-monto">$100K</div></div>
        <div class="cuota-card"><div class="cuota-mes">Mayo</div><div class="cuota-monto">$100K</div></div>
        <div class="cuota-card"><div class="cuota-mes">Junio</div><div class="cuota-monto">$100K</div></div>
        <div class="cuota-card"><div class="cuota-mes">Julio</div><div class="cuota-monto">$100K</div></div>
        <div class="cuota-card"><div class="cuota-mes">Agosto</div><div class="cuota-monto">$100K</div></div>
        <div class="cuota-card"><div class="cuota-mes">Septiembre</div><div class="cuota-monto">$100K</div></div>
        <div class="cuota-card last"><div class="cuota-mes">Octubre</div><div class="cuota-monto">$35,5K</div></div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── QUÉ LLEVAR ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">14</div>
    <div class="section-title">¿Qué <span>Llevar</span>?</div>
    <div class="llevar-grid">
        <div class="llevar-box">
            <div class="llevar-title si">✅ Llevar en Bolso</div>
            <div class="llevar-item"><span class="dot si">●</span>Peluche</div>
            <div class="llevar-item"><span class="dot si">●</span>Pijama</div>
            <div class="llevar-item"><span class="dot si">●</span>Artículos de aseo personal</div>
            <div class="llevar-item"><span class="dot si">●</span>Gorra</div>
            <div class="llevar-item"><span class="dot si">●</span>Traje de baño</div>
            <div class="llevar-item"><span class="dot si">●</span>Campera</div>
            <div class="llevar-item"><span class="dot si">●</span>Ojotas / Crocs</div>
            <div class="llevar-item"><span class="dot si">●</span>Ropa interior x2</div>
            <div class="llevar-item"><span class="dot si">●</span>Bolsa para ropa mojada</div>
            <div class="llevar-item"><span class="dot si">●</span>2 mudas de ropa adicional</div>
            <div class="llevar-item"><span class="dot si">●</span>Short + camiseta</div>
            <div class="llevar-item"><span class="dot si">●</span>Botines + medias del Liceo</div>
            <div class="llevar-item"><span class="dot si">●</span>🦷 Protector bucal</div>
        </div>
        <div class="llevar-box no-llevar">
            <div class="llevar-title no">❌ NO Llevar</div>
            <div class="llevar-item"><span class="dot no">●</span>Toallón (incluido en la cabaña)</div>
            <div class="llevar-item"><span class="dot no">●</span>Dinero</div>
            <div class="llevar-item"><span class="dot no">●</span>Caramelos, chicles, chupetines</div>
            <div class="llevar-item"><span class="dot no">●</span>Tecnología (cel, tablet, etc.)</div>
            <div class="llevar-item"><span class="dot no">●</span>Protector solar (compra comunitaria)</div>
            <div class="llevar-item"><span class="dot no">●</span>Off repelente (compra comunitaria)</div>
            <div class="llevar-item"><span class="dot no">●</span>Papas fritas, chizitos, doritos, etc.</div>
        </div>
    </div>
    <div style="margin-top:20px;" class="warn-box">
        <span class="warn-icon">🧴</span>
        <div>
            <strong style="color:#f0c060;">OFF y Protector Solar — Compra Comunitaria</strong><br>
            Se hace una compra en conjunto. Responsable: <strong>¡Guada, una genia!</strong> 🌟
        </div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── DOCUMENTACIÓN ────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">16</div>
    <div class="section-title"><span>Documentación</span></div>
    <div class="docs-list">
        <div class="doc-row"><span class="doc-icon">📝</span> Autorización firmada por Padre / Madre (físico o impresión digital)</div>
        <div class="doc-row"><span class="doc-icon">🪪</span> DNI original vigente (verificar que no esté vencido)</div>
        <div class="doc-row"><span class="doc-icon">🏥</span> Ficha médica firmada para concurrir a la gira</div>
        <div class="doc-row"><span class="doc-icon">💳</span> Carnet de obra social (físico o impresión digital)</div>
        <div class="doc-row"><span class="doc-icon">✅</span> Cuota social al día (no hace falta presentar comprobante)</div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── REGLAS ADICIONALES ───────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">Extra</div>
    <div class="section-title">Reglas & <span>Detalles</span></div>
    <div class="cards-grid">
        <div class="card">
            <div class="card-icon">👨‍👩‍👦</div>
            <div class="card-title">Padres Acompañantes</div>
            <div class="card-body">
                <strong>No pueden viajar</strong> con los chicos.<br><br>
                ✅ Pueden ir a verlos el <strong>sábado a la mañana</strong> al club donde se juega.
            </div>
        </div>
        <div class="card">
            <div class="card-icon">📵</div>
            <div class="card-title">Tecnología</div>
            <div class="card-body">
                <strong>No está permitida.</strong><br><br>
                Sin celulares, tablets ni dispositivos electrónicos. ¡Tiempo de desconectarse y vivir la gira!
            </div>
        </div>
        <div class="card">
            <div class="card-icon">🅿️</div>
            <div class="card-title">Estacionamiento</div>
            <div class="card-body">
                Los padres pueden estacionar en el <strong>Liceo Naval</strong> el viernes de salida y el domingo de regreso.
            </div>
        </div>
        <div class="card">
            <div class="card-icon">🎁</div>
            <div class="card-title">Regalos de Gira</div>
            <div class="card-body">
                Habrá sorpresas especiales para los jugadores. <strong>¡Más info próximamente!</strong>
            </div>
        </div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div style="font-size:3rem;margin-bottom:8px;">🐙</div>
    <div style="font-family:'Bebas Neue',sans-serif;font-size:1.8rem;color:rgba(79,200,79,0.5);letter-spacing:0.12em;">PULPOS · LICEO NAVAL</div>
    <div style="margin-top:8px;">División M10 · <strong>Gira Pinamar 2024</strong> · 13 al 15 de Noviembre</div>
    <div style="margin-top:16px;font-size:0.75rem;opacity:0.5;">Con alegría, compromiso y espíritu de equipo. ¡Vamos Pulpos! 💚</div>
</div>
""", unsafe_allow_html=True)
