import streamlit as st
from datetime import date, datetime

st.set_page_config(
    page_title="Autorización Gira Pinamar · Pulpos",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow+Condensed:wght@400;600;700&family=Barlow:wght@400;500&family=Dancing+Script:wght@600&display=swap');

html, body, [class*="css"] { font-family: 'Barlow', sans-serif; color: #e8f0f8; }

.stApp {
    background: #040810;
    background-image:
        radial-gradient(ellipse at 10% 0%, rgba(0,100,200,0.1) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 100%, rgba(100,180,255,0.07) 0%, transparent 50%);
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 860px !important; padding: 40px 20px 60px !important; margin: 0 auto; }

.page-header {
    text-align: center;
    padding: 40px 0 30px;
    border-bottom: 2px solid rgba(100,180,255,0.15);
    margin-bottom: 36px;
}
.page-header h1 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(2.5rem, 6vw, 4rem);
    letter-spacing: 0.06em;
    color: #fff;
    margin: 0;
}
.page-header h1 span { color: #70c8f0; }
.page-header p {
    color: rgba(168,216,240,0.6);
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-top: 6px;
}

.form-section {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: #70c8f0;
    margin: 32px 0 12px;
    padding-bottom: 6px;
    border-bottom: 1px solid rgba(100,180,255,0.15);
}

[data-testid="stTextInput"] label,
[data-testid="stNumberInput"] label {
    font-family: 'Barlow Condensed', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: rgba(168,216,240,0.7) !important;
}
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(100,180,255,0.4) !important;
    border-radius: 8px !important;
    color: #ffffff !important;
    font-family: 'Barlow', sans-serif !important;
    caret-color: #70c8f0 !important;
    font-size: 1rem !important;
}
[data-testid="stTextInput"] input::placeholder,
[data-testid="stNumberInput"] input::placeholder { color: rgba(168,216,240,0.3) !important; }
div[data-baseweb="input"] { background: rgba(255,255,255,0.06) !important; }
div[data-baseweb="base-input"] { background: transparent !important; }
div[data-baseweb="input"] input,
div[data-baseweb="base-input"] input { color: #ffffff !important; font-size: 1rem !important; }
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus {
    border-color: rgba(112,200,240,0.6) !important;
    box-shadow: 0 0 0 2px rgba(112,200,240,0.15) !important;
}

.auth-field {
    border-bottom: 1px solid #999;
    display: inline-block;
    min-width: 280px;
    color: #1a3a6e;
    font-weight: 600;
}
.auth-field.empty {
    color: #aaa;
    font-weight: 400;
    font-style: italic;
}

[data-testid="stCheckbox"] label {
    font-family: 'Barlow Condensed', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em !important;
    color: #e8f0f8 !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #1a6bbf 0%, #70c8f0 100%) !important;
    color: #ffffff !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.4rem !important;
    letter-spacing: 0.12em !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 16px !important;
    margin-top: 12px;
}
.stButton > button:hover { opacity: 0.88 !important; }
.stButton > button:disabled {
    background: rgba(100,180,255,0.15) !important;
    color: rgba(255,255,255,0.3) !important;
}

.success-box {
    background: linear-gradient(135deg, rgba(26,107,191,0.2), rgba(112,200,240,0.1));
    border: 1px solid rgba(112,200,240,0.4);
    border-radius: 14px;
    padding: 36px;
    text-align: center;
    margin-top: 24px;
}
.success-box h2 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.5rem;
    color: #70c8f0;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
}
.success-box p { color: #a8d8f0; font-size: 1rem; line-height: 1.7; }

.req-note {
    font-size: 0.8rem;
    color: rgba(168,216,240,0.4);
    font-family: 'Barlow Condensed', sans-serif;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
}
.back-link-wrap a {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: rgba(168,216,240,0.45);
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.88rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    text-decoration: none;
    padding: 8px 0;
    transition: color 0.2s;
}
.back-link-wrap a:hover { color: #70c8f0; }
</style>
""", unsafe_allow_html=True)

# ── Google Sheets helper ───────────────────────────────────────────────────────
def guardar_en_sheets(datos: dict) -> bool:
    try:
        import gspread
        from google.oauth2.service_account import Credentials

        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=[
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive",
            ],
        )
        client = gspread.authorize(creds)
        sheet = client.open_by_key(st.secrets["SHEET_ID"])
        ws = sheet.sheet1  # usa siempre la primera solapa

        # Si la hoja está vacía agregamos los headers
        if ws.row_count == 0 or ws.cell(1, 1).value is None:
            ws.append_row([
                "Timestamp", "Jugador Nombre", "Jugador Apellido", "Jugador DNI",
                "Domicilio", "Localidad", "Teléfono",
                "Padre Nombre", "Padre Apellido", "Padre DNI",
                "Madre Nombre", "Madre Apellido", "Madre DNI",
            ])

        ws.append_row([
            datetime.now().strftime("%d/%m/%Y %H:%M"),
            datos["jugador_nombre"],
            datos["jugador_apellido"],
            datos["jugador_dni"],
            datos["jugador_domicilio"],
            datos["jugador_localidad"],
            datos["jugador_tel"],
            datos["padre_nombre"],
            datos["padre_apellido"],
            datos["padre_dni"],
            datos["madre_nombre"],
            datos["madre_apellido"],
            datos["madre_dni"],
        ])
        return True
    except Exception as e:
        st.error(f"❌ Error al guardar en Google Sheets: {e}")
        return False

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div style="margin-bottom:16px;">
        <a href="https://pulpos-gira-pinamar.streamlit.app" 
           style="color:rgba(168,216,240,0.5);font-family:'Barlow Condensed',sans-serif;
                  font-size:0.9rem;font-weight:600;letter-spacing:0.12em;text-decoration:none;
                  border:1px solid rgba(100,180,255,0.2);border-radius:8px;padding:6px 16px;
                  text-transform:uppercase;transition:color 0.2s;">
            ← Volver a la Gira
        </a>
    </div>
    <h1>🐙 Autorización <span>Gira Pinamar</span></h1>
    <p>División M10 · Liceo Naval · Noviembre 2026</p>
</div>
""", unsafe_allow_html=True)

st.markdown('''
<style>
div[data-testid="stButton"]:has(button[kind="secondary"]) button {
    background: transparent !important;
    border: 1px solid rgba(100,180,255,0.3) !important;
    color: rgba(168,216,240,0.6) !important;
    font-family: "Barlow Condensed", sans-serif !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.1em !important;
    width: auto !important;
    padding: 6px 20px !important;
    margin-bottom: 8px;
}
</style>
''', unsafe_allow_html=True)
if st.button("← VOLVER A LA GIRA", key="back_top", type="secondary"):
    st.switch_page("app.py")

# ── Session state ──────────────────────────────────────────────────────────────
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ══════════════════════════════════════════════════════════════════════════════
# FORMULARIO
# ══════════════════════════════════════════════════════════════════════════════
if not st.session_state.submitted:

    st.markdown('<div class="req-note">* Todos los campos son obligatorios</div>', unsafe_allow_html=True)

    # ── JUGADOR ───────────────────────────────────────────────────────────────
    st.markdown('<div class="form-section">Datos del Jugador</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2, 2, 1.2])
    with c1:
        jugador_nombre = st.text_input("Nombre *", placeholder="Nombre del jugador", key="jnombre")
    with c2:
        jugador_apellido = st.text_input("Apellido *", placeholder="Apellido del jugador", key="japellido")
    with c3:
        jugador_dni = st.text_input("DNI *", placeholder="12.345.678", key="jdni")

    c4, c5 = st.columns([2, 2])
    with c4:
        jugador_domicilio = st.text_input("Domicilio *", placeholder="Calle y número", key="jdomicilio")
    with c5:
        jugador_localidad = st.text_input("Localidad *", placeholder="Ciudad / Barrio", key="jlocalidad")

    jugador_tel = st.text_input("Teléfono de contacto *", placeholder="11 1234-5678", key="jtel")

    # ── PADRE ─────────────────────────────────────────────────────────────────
    st.markdown('<div class="form-section">Datos del Padre</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2, 2, 1.2])
    with c1:
        padre_nombre = st.text_input("Nombre *", placeholder="Nombre del padre", key="pnombre")
    with c2:
        padre_apellido = st.text_input("Apellido *", placeholder="Apellido del padre", key="papellido")
    with c3:
        padre_dni = st.text_input("DNI *", placeholder="12.345.678", key="pdni")

    # ── MADRE ─────────────────────────────────────────────────────────────────
    st.markdown('<div class="form-section">Datos de la Madre</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2, 2, 1.2])
    with c1:
        madre_nombre = st.text_input("Nombre *", placeholder="Nombre de la madre", key="mnombre")
    with c2:
        madre_apellido = st.text_input("Apellido *", placeholder="Apellido de la madre", key="mapellido")
    with c3:
        madre_dni = st.text_input("DNI *", placeholder="12.345.678", key="mdni")

    # ── PREVIEW DEL DOCUMENTO ─────────────────────────────────────────────────
    st.markdown('<div class="form-section">Vista previa de la autorización</div>', unsafe_allow_html=True)

    def field(val, placeholder, width="280px"):
        if val.strip():
            return f'<span class="auth-field" style="min-width:{width};">{val.strip()}</span>'
        return f'<span class="auth-field empty" style="min-width:{width};">{placeholder}</span>'

    nombre_completo_jugador = f"{jugador_nombre.strip()} {jugador_apellido.strip()}".strip()
    fecha_hoy = (
        date.today().strftime("%d de %B de %Y")
        .replace("January","enero").replace("February","febrero")
        .replace("March","marzo").replace("April","abril")
        .replace("May","mayo").replace("June","junio")
        .replace("July","julio").replace("August","agosto")
        .replace("September","septiembre").replace("October","octubre")
        .replace("November","noviembre").replace("December","diciembre")
    )

    madre_display = f"{madre_nombre.strip()} {madre_apellido.strip()}".strip() or "Madre / Tutora"
    padre_display = f"{padre_nombre.strip()} {padre_apellido.strip()}".strip() or "Padre / Tutor"
    madre_dni_display = madre_dni.strip() or "\u2014\u2014\u2014\u2014\u2014\u2014"
    padre_dni_display = padre_dni.strip() or "\u2014\u2014\u2014\u2014\u2014\u2014"

    doc_html = " ".join([
        '<div style="background:rgba(255,255,255,0.97);border-radius:12px;padding:44px 52px;',
        'color:#1a1a2e;font-family:Georgia,serif;font-size:0.95rem;line-height:1.9;',
        'box-shadow:0 8px 40px rgba(0,0,0,0.5);margin:32px 0;border-top:6px solid #1a6bbf;">',
        '<div style="text-align:center;font-size:1.15rem;font-weight:700;text-transform:uppercase;margin-bottom:6px;">GIRA PINAMAR 2026</div>',
        '<div style="text-align:center;font-size:1rem;font-weight:600;margin-bottom:24px;color:#1a3a6e;">Autorización para concurrir</div>',
    ])
    doc_html += "<p>Por medio de la presente autorizo a mi hijo/a " + field(nombre_completo_jugador, "Nombre y Apellido del jugador", "320px") + "</p>"
    doc_html += "<p>DNI N° " + field(jugador_dni, "DNI del jugador", "200px") + "</p>"
    doc_html += "<p>domiciliado en la calle " + field(jugador_domicilio, "Domicilio", "260px") + "</p>"
    doc_html += "<p>de la localidad de " + field(jugador_localidad, "Localidad", "220px") + "</p>"
    doc_html += "<p>Teléfono " + field(jugador_tel, "Teléfono", "200px") + "</p>"
    doc_html += (
        "<p style='margin-top:16px;'>que concurre al <strong>Centro De Graduados Del Liceo Naval Militar"
        " Almirante Guillermo Brown</strong> de la Ciudad Autónoma de Buenos Aires"
        " a participar de la Salida denominada <strong>Pinamar 2026</strong>"
        " a realizarse en la localidad de Pinamar, Provincia de Buenos Aires"
        " desde el <strong>13 de Noviembre de 2026</strong>"
        " hasta el <strong>15 de noviembre de 2026</strong>.</p>"
        "<p>Dejo constancia que he sido informado de las características particulares de dicha salida,"
        " las actividades a desarrollar, medios de transporte a utilizar y lugares donde se realizarán dichas actividades.</p>"
        "<p>Autorizo a los responsables de la salida a disponer cambios con relación a la planificación"
        " de las actividades en aspectos acotados, que resulten necesarios, a su solo criterio y sin aviso previo,"
        " sobre lo cual me deberán informar y fundamentar al regreso.</p>"
        "<p>Autorizo, en caso de necesidad y urgencia, a hacer atender a mi hijo por profesionales médicos"
        " y a que se adopten las prescripciones que ellos indiquen, sobre lo cual requiero inmediato aviso.</p>"
        "<p>Los entrenadores y personal a cargo del cuidado y vigilancia activa de los menores no serán"
        " responsables de los objetos u otros elementos de valor que los mismos puedan llevar.</p>"
    )
    doc_html += (
        f"<div style='margin-top:28px;display:flex;gap:30px;flex-wrap:wrap;'>"
        f"<p><strong>Lugar:</strong> Ciudad Autónoma de Buenos Aires</p>"
        f"<p><strong>Fecha:</strong> {fecha_hoy}</p></div>"
    )
    doc_html += (
        "<div style='display:flex;gap:48px;margin-top:48px;'>"
        # Madre — izquierda
        f"<div style='flex:1;text-align:center;'>"
        f"<div style='font-family:Dancing Script,cursive;font-size:1.6rem;color:#1a3a6e;margin-bottom:4px;min-height:2.2rem;'>{madre_display}</div>"
        f"<div style='border-top:1px solid #aaa;padding-top:8px;font-size:0.82rem;color:#555;'>"
        f"<strong>{madre_display}</strong> &nbsp;·&nbsp; DNI: {madre_dni_display}<br>"
        "Firma de la Madre / Tutora</div></div>"
        # Padre — derecha
        f"<div style='flex:1;text-align:center;'>"
        f"<div style='font-family:Dancing Script,cursive;font-size:1.6rem;color:#1a3a6e;margin-bottom:4px;min-height:2.2rem;'>{padre_display}</div>"
        f"<div style='border-top:1px solid #aaa;padding-top:8px;font-size:0.82rem;color:#555;'>"
        f"<strong>{padre_display}</strong> &nbsp;·&nbsp; DNI: {padre_dni_display}<br>"
        "Firma del Padre / Tutor</div></div>"
        "</div></div>"
    )
    st.markdown(doc_html, unsafe_allow_html=True)

    # ── CHECKBOX ──────────────────────────────────────────────────────────────
    st.markdown('<div class="form-section">Confirmación</div>', unsafe_allow_html=True)
    autorizo = st.checkbox("Leí la autorización, los datos son correctos y **AUTORIZO** la participación de mi hijo/a en la Gira Pinamar 2026.")

    # ── VALIDACIÓN ────────────────────────────────────────────────────────────
    campos_obligatorios = [
        jugador_nombre, jugador_apellido, jugador_dni,
        jugador_domicilio, jugador_localidad, jugador_tel,
        padre_nombre, padre_apellido, padre_dni,
        madre_nombre, madre_apellido, madre_dni,
    ]
    todo_completo = all(c.strip() for c in campos_obligatorios) and autorizo

    if not todo_completo and any(c.strip() for c in campos_obligatorios):
        faltantes = []
        if not jugador_nombre.strip() or not jugador_apellido.strip() or not jugador_dni.strip():
            faltantes.append("datos del jugador")
        if not jugador_domicilio.strip() or not jugador_localidad.strip() or not jugador_tel.strip():
            faltantes.append("domicilio / teléfono")
        if not padre_nombre.strip() or not padre_apellido.strip() or not padre_dni.strip():
            faltantes.append("datos del padre")
        if not madre_nombre.strip() or not madre_apellido.strip() or not madre_dni.strip():
            faltantes.append("datos de la madre")
        if not autorizo:
            faltantes.append("casilla de autorización")
        if faltantes:
            st.warning(f"⚠️ Falta completar: {', '.join(faltantes)}.")

    # ── BOTÓN ENVIAR ──────────────────────────────────────────────────────────
    enviar = st.button(
        "ENVIAR AUTORIZACIÓN →",
        disabled=not todo_completo,
        use_container_width=True,
    )

    if enviar and todo_completo:
        with st.spinner("Guardando autorización..."):
            ok = guardar_en_sheets({
                "jugador_nombre":   jugador_nombre.strip(),
                "jugador_apellido": jugador_apellido.strip(),
                "jugador_dni":      jugador_dni.strip(),
                "jugador_domicilio":jugador_domicilio.strip(),
                "jugador_localidad":jugador_localidad.strip(),
                "jugador_tel":      jugador_tel.strip(),
                "padre_nombre":     padre_nombre.strip(),
                "padre_apellido":   padre_apellido.strip(),
                "padre_dni":        padre_dni.strip(),
                "madre_nombre":     madre_nombre.strip(),
                "madre_apellido":   madre_apellido.strip(),
                "madre_dni":        madre_dni.strip(),
            })
        if ok:
            st.session_state.submitted = True
            st.session_state.jugador = f"{jugador_nombre.strip()} {jugador_apellido.strip()}"
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# PANTALLA DE ÉXITO
# ══════════════════════════════════════════════════════════════════════════════
else:
    jugador = st.session_state.get("jugador", "el jugador")
    st.markdown(f"""
    <div class="success-box">
        <div style="font-size:3.5rem;margin-bottom:12px;">✅</div>
        <h2>¡Autorización enviada!</h2>
        <p>
            La autorización de <strong style="color:#ffffff;">{jugador}</strong> fue registrada correctamente
            en la planilla del equipo.<br><br>
            El staff de los Pulpos ya puede verla. ¡Nos vemos en Pinamar! 🐙🏉
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;margin-top:24px;">
        <a href="https://pulpos-gira-pinamar.streamlit.app"
           style="display:inline-block;background:linear-gradient(135deg,#1a6bbf,#70c8f0);
                  color:#fff;font-family:'Bebas Neue',sans-serif;font-size:1.3rem;
                  letter-spacing:0.12em;text-decoration:none;border-radius:12px;
                  padding:14px 36px;box-shadow:0 4px 20px rgba(26,107,191,0.4);">
            ← VOLVER A LA GIRA
        </a>
    </div>
    """, unsafe_allow_html=True)
