import streamlit as st
import base64
from pathlib import Path

# ─── Load logo as base64 ─────────────────────────────────────────────────────
def get_logo_b64():
    # Looks for the logo PNG next to app.py, falls back to the PDF in uploads
    for candidate in [
        Path(__file__).parent / "utils" / "pulpos_logo.png",
        Path(__file__).parent / "pulpos_logo.png",
        Path("/mnt/user-data/uploads/pulpos.pdf").parent / "pulpos_logo.png",
    ]:
        if candidate.exists():
            return base64.b64encode(candidate.read_bytes()).decode()
    # Last resort: convert the PDF on the fly if pdf2image is available
    try:
        from pdf2image import convert_from_path
        import numpy as np
        import io
        pdf_path = Path(__file__).parent / "utils" / "pulpos.ai"
        if not pdf_path.exists():
            pdf_path = Path(__file__).parent / "pulpos.pdf"
        pages = convert_from_path(str(pdf_path), dpi=300)
        img = pages[0]
        arr = np.array(img)
        mask = ~((arr[:,:,0] > 240) & (arr[:,:,1] > 240) & (arr[:,:,2] > 240))
        rows = np.any(mask, axis=1); cols = np.any(mask, axis=0)
        rmin, rmax = np.where(rows)[0][[0,-1]]; cmin, cmax = np.where(cols)[0][[0,-1]]
        pad = 20
        img = img.crop((max(0,cmin-pad), max(0,rmin-pad), min(img.width,cmax+pad), min(img.height,rmax+pad)))
        buf = io.BytesIO(); img.save(buf, "PNG"); buf.seek(0)
        return base64.b64encode(buf.read()).decode()
    except Exception:
        return None

LOGO_B64 = get_logo_b64()

def logo_html(size="clamp(200px,22vw,300px)", footer=False):
    if footer:
        if LOGO_B64:
            return '<img src="data:image/png;base64,' + LOGO_B64 + '" style="width:70px;filter:drop-shadow(0 0 12px rgba(79,200,79,0.5));opacity:0.7;" alt="Pulpos Logo">'
        return '<div style="font-size:2.5rem;opacity:0.6;">🐙</div>'
    if LOGO_B64:
        frame = (
            '<div style="'
            'width:' + size + ';aspect-ratio:1/1;border-radius:50%;'
            'background:radial-gradient(circle at 40% 35%, #0d2a0d 0%, #050e05 70%);'
            'box-shadow:0 0 0 3px #4fc84f,0 0 0 6px rgba(0,200,255,0.4),'
            '0 0 50px rgba(79,200,79,0.55),0 0 100px rgba(0,200,255,0.2),'
            'inset 0 0 30px rgba(0,0,0,0.6);'
            'display:flex;align-items:center;justify-content:center;'
            'animation:float 4s ease-in-out infinite;margin-bottom:24px;overflow:hidden;">'
            '<img src="data:image/png;base64,' + LOGO_B64 + '"'
            ' style="width:92%;height:92%;object-fit:contain;" alt="Pulpos Logo">'
            '</div>'
        )
        return frame
    return '<div style="font-size:clamp(5rem,12vw,9rem);filter:drop-shadow(0 0 40px rgba(79,200,79,0.5));animation:float 4s ease-in-out infinite;margin-bottom:10px;">🐙</div>'


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

html, body, [class*="css"] {
    font-family: 'Barlow', sans-serif;
    color: #e8f4e8;
}
.stApp {
    background: #060d06;
    background-image:
        radial-gradient(ellipse at 10% 0%, rgba(30,185,80,0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 100%, rgba(0,140,220,0.08) 0%, transparent 50%);
}
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
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 60% at 50% 0%, rgba(79,200,79,0.15) 0%, transparent 70%),
        radial-gradient(ellipse 60% 80% at 50% 100%, rgba(0,160,255,0.12) 0%, transparent 70%);
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
}
.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(5rem, 15vw, 14rem);
    line-height: 0.9;
    background: linear-gradient(160deg, #a8f07a 0%, #4fc84f 40%, #00c8ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    filter: drop-shadow(0 0 60px rgba(79,200,79,0.35));
}
.hero-subtitle {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(1.8rem, 5vw, 4rem);
    letter-spacing: 0.08em;
    color: #00c8ff;
    margin: 8px 0 30px;
}
.hero-dates {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 20px;
}
.date-pill {
    background: rgba(79,200,79,0.12);
    border: 1px solid rgba(79,200,79,0.4);
    border-radius: 100px;
    padding: 10px 28px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    color: #a8f07a;
}
.scroll-arrow {
    position: absolute;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2rem;
    color: rgba(79,200,79,0.5);
    animation: bounce 2s infinite;
}
@keyframes bounce {
    0%,100%{transform:translateX(-50%) translateY(0);}
    50%{transform:translateX(-50%) translateY(10px);}
}
@keyframes float {
    0%,100%{transform:translateY(0px);}
    50%{transform:translateY(-14px);}
}

/* ── DIVIDER ── */
.divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #4fc84f, #00c8ff, #4fc84f, transparent);
    margin: 0;
    opacity: 0.35;
}

/* ── SECTION HEADERS ── */
.sec-wrap { padding: 50px 5vw 0; max-width: 1200px; margin: 0 auto; }
.section-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    color: #4fc84f;
    margin-bottom: 4px;
}
.section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    line-height: 1;
    letter-spacing: 0.04em;
    color: #fff;
    margin-bottom: 24px;
}
.section-title span { color: #4fc84f; }

/* ── STAT STRIP ── */
.stat-strip {
    display: flex;
    border-top: 1px solid rgba(79,200,79,0.15);
    border-bottom: 1px solid rgba(79,200,79,0.15);
    background: rgba(79,200,79,0.04);
}
.stat-item {
    flex: 1;
    padding: 24px 10px;
    text-align: center;
    border-right: 1px solid rgba(79,200,79,0.1);
}
.stat-item:last-child { border-right: none; }
.stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    line-height: 1;
    color: #4fc84f;
}
.stat-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(200,232,200,0.45);
    margin-top: 4px;
}

/* ── OBJETIVO ── */
.objetivo-box {
    background: linear-gradient(135deg, rgba(79,200,79,0.07) 0%, rgba(0,200,255,0.05) 100%);
    border: 1px solid rgba(79,200,79,0.2);
    border-left: 4px solid #4fc84f;
    border-radius: 12px;
    padding: 32px 36px;
    font-size: 1.1rem;
    line-height: 1.85;
    color: #c8e8c8;
}
.objetivo-box p { margin: 0 0 16px; }
.objetivo-box p:last-child { margin-bottom: 0; }

/* ── CARD ── */
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 28px;
    height: 100%;
    transition: border-color 0.3s;
}
.card:hover { border-color: rgba(79,200,79,0.35); }
.card-icon { font-size: 2.2rem; margin-bottom: 14px; }
.card-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #a8f07a;
    margin-bottom: 10px;
}
.card-body { font-size: 0.95rem; line-height: 1.7; color: #9eb89e; }
.card-body strong { color: #c8e8c8; }

/* ── CHIP ── */
.chip {
    display: inline-block;
    background: rgba(79,200,79,0.12);
    border: 1px solid rgba(79,200,79,0.3);
    border-radius: 100px;
    padding: 3px 12px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #7bdd7b;
    margin: 2px;
}
.link-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(0,200,255,0.08);
    border: 1px solid rgba(0,200,255,0.3);
    border-radius: 8px;
    padding: 8px 16px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    color: #00c8ff;
    text-decoration: none;
    margin-top: 10px;
}

/* ── TIMELINE ── */
.timeline { position: relative; padding-left: 28px; }
.timeline::before {
    content: '';
    position: absolute;
    left: 7px; top: 0; bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, #4fc84f, #00c8ff, #4fc84f);
    opacity: 0.35;
}
.day-header {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    letter-spacing: 0.08em;
    color: #4fc84f;
    margin: 0 0 14px;
    position: relative;
}
.day-header::before {
    content: 'o';
    position: absolute;
    left: -28px;
    color: #4fc84f;
    font-size: 0.75rem;
    top: 50%;
    transform: translateY(-50%);
}
.event-row {
    display: flex;
    gap: 14px;
    align-items: flex-start;
    padding: 11px 14px;
    border-radius: 10px;
    margin-bottom: 7px;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
}
.event-time {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    font-size: 0.82rem;
    color: #00c8ff;
    letter-spacing: 0.04em;
    white-space: nowrap;
    min-width: 78px;
    padding-top: 2px;
}
.event-desc { font-size: 0.92rem; color: #b0c8b0; line-height: 1.5; }

/* ── STAFF CARD ── */
.staff-card {
    background: rgba(0,200,255,0.06);
    border: 1px solid rgba(0,200,255,0.2);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    margin-bottom: 4px;
}
.staff-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #00c8ff;
    letter-spacing: 0.06em;
}

/* ── COMIDAS TABLE ── */
.comidas-table {
    width: 100%;
    border-collapse: collapse;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(79,200,79,0.2);
}
.comidas-table th {
    background: rgba(79,200,79,0.18);
    padding: 14px 16px;
    text-align: center;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #a8f07a;
    border: 1px solid rgba(79,200,79,0.15);
}
.comidas-table td {
    padding: 13px 16px;
    text-align: center;
    font-size: 0.9rem;
    color: #9eb89e;
    border: 1px solid rgba(255,255,255,0.05);
}
.comidas-table td.row-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    font-size: 0.88rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #00c8ff;
    background: rgba(0,200,255,0.05);
    text-align: left;
}
.comidas-table td.ok { color: #4fc84f; }
.comidas-table td.na { color: rgba(255,255,255,0.25); }
.comidas-table tr:nth-child(even) td:not(.row-label) { background: rgba(255,255,255,0.015); }

/* ── CUOTAS ── */
.cuota-wrap {
    background: rgba(79,200,79,0.07);
    border: 1px solid rgba(79,200,79,0.2);
    border-radius: 12px;
    padding: 16px 10px;
    text-align: center;
}
.cuota-wrap.last {
    border-color: rgba(0,200,255,0.3);
    background: rgba(0,200,255,0.07);
}
.cuota-mes {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4fc84f;
    margin-bottom: 6px;
}
.cuota-wrap.last .cuota-mes { color: #00c8ff; }
.cuota-monto {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.5rem;
    color: #fff;
}

/* ── LLEVAR ── */
.llevar-box {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 26px;
}
.llevar-box.no-llevar {
    border-color: rgba(255,80,80,0.2);
    background: rgba(255,80,80,0.03);
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
    padding: 8px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    font-size: 0.92rem;
    color: #9eb89e;
    line-height: 1.4;
}
.llevar-item:last-child { border-bottom: none; }

/* ── DOCS ── */
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
    margin-bottom: 10px;
}
.doc-icon { font-size: 1.4rem; }

/* ── WARN ── */
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
    margin-top: 16px;
}
.warn-icon { font-size: 1.5rem; flex-shrink: 0; }

/* ── FOOTER ── */
.footer {
    background: rgba(0,0,0,0.5);
    border-top: 1px solid rgba(79,200,79,0.15);
    padding: 40px 5vw;
    text-align: center;
    color: rgba(200,232,200,0.35);
    font-size: 0.85rem;
    letter-spacing: 0.05em;
    margin-top: 60px;
}
.footer strong { color: rgba(79,200,79,0.6); }

/* Remove extra streamlit column padding */
[data-testid="column"] { padding: 4px 6px !important; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="hero">
    {logo_html()}
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

# ══════════════════════════════════════════════════════════════════════════════
# STAT STRIP
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="stat-strip">
    <div class="stat-item"><div class="stat-num">34</div><div class="stat-label">Jugadores</div></div>
    <div class="stat-item"><div class="stat-num">8</div><div class="stat-label">Staff</div></div>
    <div class="stat-item"><div class="stat-num">3</div><div class="stat-label">Días</div></div>
    <div class="stat-item"><div class="stat-num">7</div><div class="stat-label">Cuotas</div></div>
    <div class="stat-item"><div class="stat-num">4</div><div class="stat-label">Equipos</div></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# OBJETIVO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="sec-wrap">
    <div class="section-title">Nuestro <span>Objetivo</span></div>
    <div class="objetivo-box">
        <p>🏉 Fortalecer la amistad, el compañerismo y el espíritu de equipo a través del juego, la convivencia y el respeto.</p>
        <p>🌊 Vivir juntos una experiencia inolvidable dentro y fuera de la cancha, aprendiendo a compartir, cuidar al otro y disfrutar en grupo, con alegría y compromiso.</p>
    </div>
</div>
<div style="height:50px;"></div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# INTEGRANTES  —  st.columns para las 2 cards grandes
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap"><div class="section-title"><span>Integrantes</span></div></div>', unsafe_allow_html=True)

_, inner, _ = st.columns([1, 10, 1])
with inner:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="card">
            <div class="card-icon">🐙</div>
            <div class="card-title">Jugadores</div>
            <div class="card-body">
                <span style="font-family:'Bebas Neue',sans-serif;font-size:3rem;color:#4fc84f;">34</span><br>
                Jugadores del Liceo Naval M10
            </div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card">
            <div class="card-icon">🎽</div>
            <div class="card-title">Staff Técnico</div>
            <div class="card-body">
                <span style="font-family:'Bebas Neue',sans-serif;font-size:3rem;color:#00c8ff;">8</span><br>
                Entrenadores y Managers
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="padding:16px 5vw 0;"><div class="section-label">Staff</div></div>', unsafe_allow_html=True)
staff = ["Ote", "Ale", "Mati", "Fran", "Marian", "Tucu", "Cris", "Ema"]
_, inner2, _ = st.columns([1, 10, 1])
with inner2:
    cols = st.columns(8)
    for col, name in zip(cols, staff):
        with col:
            st.markdown(f'<div class="staff-card"><div class="staff-name">🧑‍💼 {name}</div></div>', unsafe_allow_html=True)

st.markdown('<div style="height:50px;"></div><div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CLUB & ALOJAMIENTO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap"><div class="section-title">Club &amp; <span>Alojamiento</span></div></div>', unsafe_allow_html=True)

_, inner3, _ = st.columns([1, 10, 1])
with inner3:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="card">
            <div class="card-icon">🏉</div>
            <div class="card-title">Club Visitante</div>
            <div class="card-body">
                <strong>Camarones · Pinamar</strong><br><br>
                El rival que nos espera con el campo listo y el tercer tiempo preparado.
            </div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card">
            <div class="card-icon">🏨</div>
            <div class="card-title">Espacio Arena Hotel</div>
            <div class="card-body">
                <span class="chip">A/A</span><span class="chip">WiFi</span><span class="chip">TV Satelital</span>
                <span class="chip">Frigobar</span><span class="chip">Ropa de cama</span><span class="chip">Toallas</span>
                <span class="chip">Pileta</span><span class="chip">Quinchos</span><span class="chip">Asadores</span>
                <span class="chip">Cancha Fútbol</span><span class="chip">Cancha Tenis</span>
                <span class="chip">Estacionamiento techado</span><br><br>
                <a class="link-btn" href="https://share.google/sHaJsoc6ak4D2hrFk" target="_blank">🗺️ Ver en Maps</a>
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="height:50px;"></div><div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# FECHAS & LOGÍSTICA
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap"><div class="section-title">Fechas &amp; <span>Logística</span></div></div>', unsafe_allow_html=True)

_, inner4, _ = st.columns([1, 10, 1])
with inner4:
    c1, c2, c3, c4 = st.columns(4)
    cards_data = [
        (c1, "🛫", "Partida", "<strong>Viernes 13 de Noviembre</strong><br>Encuentro en el Liceo: <strong>7:00 am</strong><br>Salida: <strong>8:00 hs</strong>"),
        (c2, "🏠", "Regreso", "<strong>Domingo 15 de Noviembre</strong><br>Salida Pinamar: <strong>15:00 hs</strong><br>Llegada aprox.: <strong>20:00 hs</strong>"),
        (c3, "🚌", "Transporte", "<strong>Serrano Turismo</strong><br><br>Control alcoholemia obligatorio.<br>Estacionamiento en Liceo el viernes y domingo."),
        (c4, "🏥", "Seguro Médico", "<strong>Assist Travel</strong><br><br>Asistencia médica completa durante toda la gira."),
    ]
    for col, icon, title, body in cards_data:
        with col:
            st.markdown(f"""<div class="card">
                <div class="card-icon">{icon}</div>
                <div class="card-title">{title}</div>
                <div class="card-body">{body}</div>
            </div>""", unsafe_allow_html=True)

st.markdown('<div style="height:50px;"></div><div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CRONOGRAMA  —  3 columnas con timeline HTML interno
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap"><div class="section-title"><span>Cronograma</span></div></div>', unsafe_allow_html=True)

def make_timeline(day_name, events):
    rows = "".join(
        f'<div class="event-row"><div class="event-time">{t}</div><div class="event-desc">{d}</div></div>'
        for t, d in events
    )
    return f'<div class="timeline"><div class="day-header">{day_name}</div>{rows}</div>'

viernes = [("07:00 am","🏫 Encuentro en el Liceo"),("08:00 hs","🚌 Salida hacia Pinamar"),
           ("15:00 hs","🏨 Arribo al hotel · Almuerzo"),("Tarde","🌊 Día de playa"),("Noche","🍽️ Cena en el hotel")]
sabado  = [("Mañana","☕ Desayuno en hotel"),("10:00 hs","🏉 Partido vs Camarones"),
           ("Post-partido","🍻 Tercer tiempo"),("Tarde","🏄 Playa + Sandboard + Inflables"),("Noche","🍽️ Cena en Hotel")]
domingo = [("Mañana","☕ Desayuno en Hotel"),("Mañana","🌿 Kalo Eco Parque · Cariló"),
           ("Almuerzo","🍽️ Almuerzo en Hotel"),("15:00 hs","🚌 Salida hacia el Liceo"),
           ("Camino","🥐 Merienda en el Bondi"),("~20:00 hs","🏁 Llegada al Liceo")]

_, inner5, _ = st.columns([1, 10, 1])
with inner5:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(make_timeline("Viernes 13", viernes), unsafe_allow_html=True)
    with c2:
        st.markdown(make_timeline("Sábado 14", sabado), unsafe_allow_html=True)
    with c3:
        st.markdown(make_timeline("Domingo 15", domingo), unsafe_allow_html=True)

st.markdown('<div style="height:50px;"></div><div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# COMIDAS  —  <table> real, no CSS grid
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap"><div class="section-title"><span>Comidas</span></div></div>', unsafe_allow_html=True)
st.markdown("""
<div style="padding:0 5vw 50px;max-width:1200px;margin:0 auto;">
<table class="comidas-table">
  <thead>
    <tr>
      <th>Comida</th><th>Viernes</th><th>Sábado</th><th>Domingo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="row-label">🌅 Desayuno</td>
      <td class="na">— No incluido</td>
      <td class="ok">✅ Hotel</td>
      <td class="ok">✅ Hotel</td>
    </tr>
    <tr>
      <td class="row-label">☀️ Almuerzo</td>
      <td class="ok">✅ Hotel</td>
      <td class="ok">✅ Camarones</td>
      <td class="ok">✅ Hotel</td>
    </tr>
    <tr>
      <td class="row-label">🌤️ Merienda</td>
      <td class="ok">✅ Playa</td>
      <td class="ok">✅ Playa</td>
      <td class="ok">✅ Bondi</td>
    </tr>
    <tr>
      <td class="row-label">🌙 Cena</td>
      <td class="ok">✅ Hotel</td>
      <td class="ok">✅ Hotel</td>
      <td class="na">—</td>
    </tr>
  </tbody>
</table>
</div>
""", unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# COSTO & CUOTAS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap"><div class="section-title">Costo &amp; <span>Cuotas</span></div></div>', unsafe_allow_html=True)

_, inner6, _ = st.columns([1, 10, 1])
with inner6:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="card">
            <div class="card-icon">💰</div>
            <div class="card-title">Costo total por jugador</div>
            <div class="card-body">
                <span style="font-family:'Bebas Neue',sans-serif;font-size:3rem;color:#a8f07a;">$635.500</span><br>
                <em style="font-size:0.85rem;color:#7a9a7a;">Si viajan menos de 30 jugadores, la diferencia se distribuye entre todos los pasajeros.</em>
            </div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card">
            <div class="card-icon">🗓️</div>
            <div class="card-title">Modalidad de Pago</div>
            <div class="card-body">
                <strong>7 cuotas</strong><br>
                6 cuotas de $100.000 + 1 cuota final de $35.500
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)

cuotas = [("Abril","$100K",False),("Mayo","$100K",False),("Junio","$100K",False),
          ("Julio","$100K",False),("Agosto","$100K",False),("Septiembre","$100K",False),
          ("Octubre","$35,5K",True)]

_, inner7, _ = st.columns([1, 10, 1])
with inner7:
    cols = st.columns(7)
    for col, (mes, monto, last) in zip(cols, cuotas):
        cls = "cuota-wrap last" if last else "cuota-wrap"
        with col:
            st.markdown(f'<div class="{cls}"><div class="cuota-mes">{mes}</div><div class="cuota-monto">{monto}</div></div>', unsafe_allow_html=True)

st.markdown('<div style="height:50px;"></div><div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# QUÉ LLEVAR
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap"><div class="section-title">¿Qué <span>Llevar</span>?</div></div>', unsafe_allow_html=True)

llevar = ["Peluche","Pijama","Artículos de aseo personal","Gorra","Traje de baño",
          "Campera","Ojotas / Crocs","Ropa interior x2","Bolsa para ropa mojada",
          "2 mudas de ropa adicional","Short + camiseta","Botines + medias del Liceo","🦷 Protector bucal"]
no_llevar = ["Toallón (incluido en la cabaña)","Dinero","Caramelos, chicles, chupetines",
             "Tecnología (cel, tablet, etc.)","Protector solar (compra comunitaria)",
             "Off repelente (compra comunitaria)","Papas fritas, chizitos, doritos, etc."]

si_rows = "".join(f'<div class="llevar-item">✅&nbsp; {i}</div>' for i in llevar)
no_rows = "".join(f'<div class="llevar-item">❌&nbsp; {i}</div>' for i in no_llevar)

_, inner8, _ = st.columns([1, 10, 1])
with inner8:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="llevar-box"><div class="llevar-title si">✅ Llevar en Bolso</div>{si_rows}</div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="llevar-box no-llevar"><div class="llevar-title no">❌ NO Llevar</div>{no_rows}</div>', unsafe_allow_html=True)

st.markdown("""
<div style="padding:0 5vw;max-width:1200px;margin:0 auto;">
<div class="warn-box">
    <span class="warn-icon">🧴</span>
    <div><strong style="color:#f0c060;">OFF y Protector Solar — Compra Comunitaria</strong><br>
    Se hace una compra en conjunto para todos. Responsable: <strong>¡Guada, una genia!</strong> 🌟</div>
</div>
</div>
""", unsafe_allow_html=True)
st.markdown('<div style="height:50px;"></div><div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENTACIÓN
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap"><div class="section-title"><span>Documentación</span></div></div>', unsafe_allow_html=True)
st.markdown("""
<div style="padding:0 5vw 50px;max-width:1200px;margin:0 auto;">
    <div class="doc-row"><span class="doc-icon">📝</span> Autorización firmada por Padre / Madre (físico o impresión digital)</div>
    <div class="doc-row"><span class="doc-icon">🪪</span> DNI original vigente (verificar que no esté vencido)</div>
    <div class="doc-row"><span class="doc-icon">🏥</span> Ficha médica firmada para concurrir a la gira</div>
    <div class="doc-row"><span class="doc-icon">💳</span> Carnet de obra social (físico o impresión digital)</div>
    <div class="doc-row"><span class="doc-icon">✅</span> Cuota social al día (no hace falta presentar comprobante)</div>
</div>
""", unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# REGLAS & DETALLES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap"><div class="section-title">Reglas &amp; <span>Detalles</span></div></div>', unsafe_allow_html=True)

_, inner9, _ = st.columns([1, 10, 1])
with inner9:
    c1, c2, c3, c4 = st.columns(4)
    extras = [
        (c1,"👨‍👩‍👦","Padres Acompañantes","<strong>No pueden viajar</strong> con los chicos.<br><br>✅ Pueden ir a verlos el <strong>sábado a la mañana</strong> al club donde se juega."),
        (c2,"📵","Tecnología","<strong>No está permitida.</strong><br><br>Sin celulares, tablets ni dispositivos electrónicos. ¡Tiempo de desconectarse!"),
        (c3,"🅿️","Estacionamiento","Los padres pueden estacionar en el <strong>Liceo Naval</strong> el viernes de salida y el domingo de regreso."),
        (c4,"🎁","Regalos de Gira","Habrá sorpresas especiales para los jugadores. <strong>¡Más info próximamente!</strong>"),
    ]
    for col, icon, title, body in extras:
        with col:
            st.markdown(f"""<div class="card">
                <div class="card-icon">{icon}</div>
                <div class="card-title">{title}</div>
                <div class="card-body">{body}</div>
            </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="footer">
    {logo_html(footer=True)}
    <div style="font-family:'Bebas Neue',sans-serif;font-size:1.8rem;color:rgba(79,200,79,0.5);letter-spacing:0.12em;">PULPOS · LICEO NAVAL</div>
    <div style="margin-top:8px;">División M10 · <strong>Gira Pinamar 2024</strong> · 13 al 15 de Noviembre</div>
    <div style="margin-top:16px;font-size:0.75rem;opacity:0.5;">Con alegría, compromiso y espíritu de equipo. ¡Vamos Pulpos! 💚</div>
</div>
""", unsafe_allow_html=True)
