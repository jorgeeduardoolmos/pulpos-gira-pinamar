import streamlit as st
import base64
from pathlib import Path

# ─── Authorization page embedded ────────────────────────────────────────────
from datetime import date as _date, datetime as _datetime

def render_autorizacion():
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
        import gspread
        from google.oauth2.service_account import Credentials
        try:
            creds = Credentials.from_service_account_info(
                st.secrets["gcp_service_account"],
                scopes=[
                    "https://spreadsheets.google.com/feeds",
                    "https://www.googleapis.com/auth/drive",
                ],
            )
            client = gspread.authorize(creds)
            sheet = client.open_by_key(st.secrets["SHEET_ID"])
            ws = sheet.sheet1

            # Append data row directly — headers should already be in row 1
            fila = [
                _datetime.now().strftime("%d/%m/%Y %H:%M"),
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
            ]
            # Debug info
            sheet_id_usado = st.secrets["SHEET_ID"]
            todas_las_filas = ws.get_all_values()
            st.info(f"🔍 Debug: Sheet ID={sheet_id_usado} | Filas actuales={len(todas_las_filas)} | Solapa={ws.title}")
            
            ws.append_row(fila, value_input_option="USER_ENTERED")
            
            # Verify it was written
            todas_despues = ws.get_all_values()
            st.info(f"✅ Debug: Filas después={len(todas_despues)}")
            return True
        except Exception as e:
            st.error(f"❌ Error al guardar: {e}")
            import traceback
            st.error(traceback.format_exc())
            return False
    
    # ── Header ─────────────────────────────────────────────────────────────────────
    
    st.markdown("""
    <div class="page-header">
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
            _date.today().strftime("%d de %B de %Y")
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
            st.session_state.submitted = False  # reset before trying
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
    

# ─── Page routing via query params ───────────────────────────────────────────
if st.query_params.get("page") == "autorizacion":
    render_autorizacion()
    st.stop()

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
            'background:radial-gradient(circle at 40% 35%, #051830 0%, #020810 70%);'
            'box-shadow:0 0 0 3px #1a6bbf,0 0 0 6px rgba(112,200,240,0.4),'
            '0 0 50px rgba(26,107,191,0.6),0 0 100px rgba(112,200,240,0.2),'
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
    background: #040810;
    background-image:
        radial-gradient(ellipse at 10% 0%, rgba(0,100,200,0.1) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 100%, rgba(100,180,255,0.07) 0%, transparent 50%);
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
        radial-gradient(ellipse 80% 60% at 50% 0%, rgba(100,180,255,0.15) 0%, transparent 70%),
        radial-gradient(ellipse 60% 80% at 50% 100%, rgba(255,255,255,0.06) 0%, transparent 70%);
    pointer-events: none;
}
.hero-eyebrow {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: #70c8f0;
    margin-bottom: 12px;
}
.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(5rem, 15vw, 14rem);
    line-height: 0.9;
    background: linear-gradient(160deg, #ffffff 0%, #70c8f0 40%, #1a6bbf 100%);
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
    color: #a8d8f0;
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
    background: rgba(100,180,255,0.12);
    border: 1px solid rgba(100,180,255,0.4);
    border-radius: 100px;
    padding: 10px 28px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    color: #a8d8f0;
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
    background: linear-gradient(90deg, transparent, #1a6bbf, #70c8f0, #ffffff, #70c8f0, #1a6bbf, transparent);
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
    color: #70c8f0;
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
.section-title span { color: #70c8f0; }

/* ── STAT STRIP ── */
.stat-strip {
    display: flex;
    border-top: 1px solid rgba(100,180,255,0.15);
    border-bottom: 1px solid rgba(100,180,255,0.15);
    background: rgba(100,180,255,0.04);
}
.stat-item {
    flex: 1;
    padding: 24px 10px;
    text-align: center;
    border-right: 1px solid rgba(100,180,255,0.1);
}
.stat-item:last-child { border-right: none; }
.stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    line-height: 1;
    color: #70c8f0;
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
    background: linear-gradient(135deg, rgba(26,107,191,0.1) 0%, rgba(112,200,240,0.05) 100%);
    border: 1px solid rgba(100,180,255,0.2);
    border-left: 4px solid #70c8f0;
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
    min-height: 220px;
    display: flex;
    flex-direction: column;
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
    color: #a8d8f0;
    margin-bottom: 10px;
}
.card-body { font-size: 0.95rem; line-height: 1.7; color: #9eb89e; }
.card-body strong { color: #c8e8c8; }

/* ── CHIP ── */
.chip {
    display: inline-block;
    background: rgba(100,180,255,0.12);
    border: 1px solid rgba(100,180,255,0.3);
    border-radius: 100px;
    padding: 3px 12px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #a8d8f0;
    margin: 2px;
}
.link-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(100,180,255,0.08);
    border: 1px solid rgba(100,180,255,0.3);
    border-radius: 8px;
    padding: 8px 16px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    color: #70c8f0;
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
    background: linear-gradient(180deg, #1a6bbf, #70c8f0, #ffffff);
    opacity: 0.35;
}
.day-header {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    letter-spacing: 0.08em;
    color: #70c8f0;
    margin: 0 0 14px;
    position: relative;
}
.day-header::before {
    content: 'o';
    position: absolute;
    left: -28px;
    color: #70c8f0;
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
    color: #a8d8f0;
    letter-spacing: 0.04em;
    white-space: nowrap;
    min-width: 78px;
    padding-top: 2px;
}
.event-desc { font-size: 0.92rem; color: #b0c8b0; line-height: 1.5; }

/* ── STAFF CARD ── */
.staff-card {
    background: rgba(26,107,191,0.12);
    border: 1px solid rgba(100,180,255,0.25);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    margin-bottom: 4px;
}
.staff-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #a8d8f0;
    letter-spacing: 0.06em;
}

/* ── COMIDAS TABLE ── */
.comidas-table {
    width: 100%;
    border-collapse: collapse;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(100,180,255,0.2);
}
.comidas-table th {
    background: rgba(26,107,191,0.3);
    padding: 14px 16px;
    text-align: center;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #ffffff;
    border: 1px solid rgba(100,180,255,0.2);
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
    color: #a8d8f0;
    background: rgba(26,107,191,0.08);
    text-align: left;
}
.comidas-table td.ok { color: #70c8f0; }
.comidas-table td.na { color: rgba(255,255,255,0.25); }
.comidas-table tr:nth-child(even) td:not(.row-label) { background: rgba(255,255,255,0.015); }

/* ── CUOTAS ── */
.cuota-wrap {
    background: rgba(26,107,191,0.1);
    border: 1px solid rgba(100,180,255,0.2);
    border-radius: 12px;
    padding: 16px 10px;
    text-align: center;
}
.cuota-wrap.last {
    border-color: rgba(255,255,255,0.3);
    background: rgba(255,255,255,0.06);
}
.cuota-mes {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #70c8f0;
    margin-bottom: 6px;
}
.cuota-wrap.last .cuota-mes { color: #ffffff; }
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
.llevar-title.si { color: #70c8f0; }
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
    border-top: 1px solid rgba(100,180,255,0.15);
    padding: 40px 5vw;
    text-align: center;
    color: rgba(200,232,200,0.35);
    font-size: 0.85rem;
    letter-spacing: 0.05em;
    margin-top: 60px;
}
.footer strong { color: rgba(100,180,255,0.6); }

/* Remove extra streamlit column padding */
[data-testid="column"] { padding: 4px 6px !important; }

/* Equal height columns — makes all cards in the same row stretch equally */
[data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
}
[data-testid="stHorizontalBlock"] > [data-testid="column"] {
    display: flex !important;
    flex-direction: column !important;
}
[data-testid="stHorizontalBlock"] > [data-testid="column"] > div {
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
}
[data-testid="stHorizontalBlock"] > [data-testid="column"] > div > div {
    flex: 1 !important;
}
[data-testid="stHorizontalBlock"] .card {
    flex: 1 !important;
}
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
staff = [
    ("👑", "Ote"),
    ("🎖️", "Ale"),
    ("🧠", "Mati"),
    ("🏉", "Tucu"),
    ("🏉", "Fran"),
    ("🆕", "Cris"),
    ("📋", "Marian"),
    ("📋", "Ema"),
]
_, inner2, _ = st.columns([1, 10, 1])
with inner2:
    cols = st.columns(8)
    for col, (icon, name) in zip(cols, staff):
        with col:
            st.markdown(f'<div class="staff-card"><div class="staff-name">{icon} {name}</div></div>', unsafe_allow_html=True)

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
        (c1, "🟢", "Partida", "<strong>Viernes 13 de Noviembre</strong><br>Encuentro en el Liceo: <strong>7:00 am</strong><br>Salida: <strong>8:00 hs</strong>"),
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
domingo = [("Mañana","☕ Desayuno en Hotel"),("Mañana","🌿 Kalo Eco Parque · Cariló &nbsp;<a href='https://share.google/RXsnm8bbZVZyqlAeI' target='_blank' style='color:#00c8ff;font-family:Barlow Condensed,sans-serif;font-size:0.8rem;border:1px solid rgba(0,200,255,0.3);border-radius:6px;padding:2px 8px;text-decoration:none;'>🗺️ Maps</a>"),
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
                <span style="font-family:'Bebas Neue',sans-serif;font-size:3rem;color:#a8f07a;">$650.000</span><br>
                <em style="font-size:0.85rem;color:#7a9a7a;">Si viajan menos de 30 jugadores, la diferencia se distribuye entre todos los pasajeros.</em>
            </div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card">
            <div class="card-icon">🗓️</div>
            <div class="card-title">Modalidad de Pago</div>
            <div class="card-body">
                <strong>7 cuotas</strong><br>
                6 cuotas de $100.000 + 1 cuota final de $50.000
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)

cuotas = [("Mayo","$100K",False),("Junio","$100K",False),("Julio","$100K",False),
          ("Agosto","$100K",False),("Septiembre","$100K",False),("Octubre","$100K",False),
          ("Noviembre","$50K",True)]

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


# CTA AUTORIZACION
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Box content
st.markdown('''
<div style="padding:60px 5vw 24px;max-width:860px;margin:0 auto;text-align:center;">
    <div style="background:linear-gradient(135deg,rgba(26,107,191,0.15),rgba(112,200,240,0.08));
                border:1px solid rgba(112,200,240,0.3);border-radius:20px;padding:50px 40px 36px;">
        <div style="font-size:3.5rem;margin-bottom:16px;">&#x1F4CB;</div>
        <div style="font-family:Bebas Neue,sans-serif;font-size:clamp(2rem,5vw,3.2rem);
                    letter-spacing:0.06em;color:#fff;margin-bottom:12px;">
            Firm&#225; la Autorizaci&#243;n <span style="color:#70c8f0;">Online</span>
        </div>
        <div style="font-size:1rem;color:rgba(168,216,240,0.7);max-width:520px;
                    margin:0 auto 32px;line-height:1.75;">
            Complet&#225; los datos del jugador y de los padres, revis&#225; el documento
            y firm&#225; digitalmente en segundos. Sin papeles, sin vueltas.
        </div>
''', unsafe_allow_html=True)

# Button — st.button + st.switch_page is the only reliable navigation in Streamlit Cloud
_, btn_col, _ = st.columns([2, 3, 2])
with btn_col:
    st.markdown('''<style>
    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #1a6bbf, #70c8f0) !important;
        color: #fff !important;
        font-family: "Bebas Neue", sans-serif !important;
        font-size: 1.4rem !important;
        letter-spacing: 0.12em !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 18px 48px !important;
        box-shadow: 0 6px 28px rgba(26,107,191,0.45) !important;
        width: 100% !important;
    }
    div[data-testid="stButton"] button:hover { opacity: 0.88 !important; }
    </style>''', unsafe_allow_html=True)
    if st.button("\u270d\ufe0f  FIRMAR AUTORIZACI\u00d3N  \u2192", use_container_width=True, key="cta_auth"):
        st.query_params["page"] = "autorizacion"
        st.rerun()

# Close the box div
st.markdown('''    </div>
</div>''', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="footer">
    {logo_html(footer=True)}
    <div style="font-family:'Bebas Neue',sans-serif;font-size:1.8rem;color:rgba(100,180,255,0.6);letter-spacing:0.12em;">PULPOS · LICEO NAVAL</div>
    <div style="margin-top:8px;">División M10 · <strong>Gira Pinamar 2024</strong> · 13 al 15 de Noviembre</div>
    <div style="margin-top:16px;font-size:0.75rem;opacity:0.5;">Con alegría, compromiso y espíritu de equipo. ¡Vamos Pulpos! 💚</div>
    <div style="margin-top:28px;font-size:0.7rem;opacity:0.2;letter-spacing:0.15em;font-family:'Barlow Condensed',sans-serif;">Gestión Lopez 2020–2030</div>
</div>
""", unsafe_allow_html=True)
