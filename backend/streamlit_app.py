"""
RASTRO — Radar Agéntico de Integridad en Compras Públicas
Media Party Buenos Aires 2026
Metodología: Giovanny Flores (México) & Ricardo Gabriel Diaz (Argentina)
Alimentado por datos públicos oficiales vía OpenARG MCP
"""

import time

import pandas as pd
import plotly.express as px
import streamlit as st

from openarg_client import client  # noqa: F401  (conexión OpenARG para la siguiente fase)

st.set_page_config(
    page_title="Rastro — Radar de Integridad en Compras Públicas",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# ESTILO: RADAR DE INTELIGENCIA
# ==============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');
:root{--bg:#0B132B;--panel:#111C38;--panel2:#16234A;--line:#24335F;--text:#E2E8F0;--muted:#94A3B8;
      --amber:#F58220;--amber-soft:rgba(245,130,32,.14);--emerald:#10B981;--emerald-soft:rgba(16,185,129,.14);
      --slate-soft:rgba(148,163,184,.14);--mono:'JetBrains Mono',ui-monospace,Menlo,monospace}
html,body,[class*="css"],.stApp{font-family:'Inter',-apple-system,sans-serif}
.stApp{background:radial-gradient(1200px 600px at 85% -10%,rgba(245,130,32,.08),transparent 60%),var(--bg)}
[data-testid="stSidebar"]{background:#0A1024;border-right:1px solid var(--line)}
[data-testid="stHeader"]{background:transparent}
.block-container{padding-top:2.2rem;max-width:1280px}
.mono{font-family:var(--mono)}
.hero-title{font-size:2.6rem;font-weight:800;letter-spacing:-.02em;color:#fff;line-height:1.05;margin:0}
.hero-title span{color:var(--amber)}
.hero-sub{color:var(--muted);font-size:1.05rem;margin:.4rem 0 1rem}
.statusline{font-family:var(--mono);font-size:.78rem;color:var(--muted);display:flex;gap:18px;flex-wrap:wrap;
            border:1px solid var(--line);background:var(--panel);padding:8px 14px;border-radius:8px;margin-bottom:1.2rem}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--emerald);margin-right:6px;box-shadow:0 0 0 0 rgba(16,185,129,.6);animation:pulse 2s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(16,185,129,.55)}70%{box-shadow:0 0 0 8px rgba(16,185,129,0)}100%{box-shadow:0 0 0 0 rgba(16,185,129,0)}}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:.4rem 0 1.4rem}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px 18px}
.kpi .lbl{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.kpi .val{font-family:var(--mono);font-size:2rem;font-weight:700;color:#fff;margin-top:6px}
.kpi.amber .val{color:var(--amber)} .kpi.green .val{color:var(--emerald)}
.ficha{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-left:4px solid var(--amber);
       border-radius:14px;padding:20px 22px;margin-top:6px}
.ficha.ok{border-left-color:var(--emerald)} .ficha.off{border-left-color:#64748B;opacity:.75}
.ficha-top{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.fid{font-family:var(--mono);font-size:.78rem;color:var(--muted);letter-spacing:.05em}
.ficha h4{color:#fff;font-size:1.35rem;margin:.35rem 0 .5rem;font-weight:700}
.tag{display:inline-block;font-family:var(--mono);font-size:.74rem;padding:3px 9px;border-radius:6px;margin:0 6px 6px 0;
     background:rgba(99,102,241,.14);color:#C7D2FE;border:1px solid rgba(99,102,241,.3)}
.badge{font-family:var(--mono);font-size:.74rem;font-weight:700;padding:5px 11px;border-radius:999px;letter-spacing:.04em}
.badge.pend{background:var(--amber-soft);color:#FDBA74;border:1px solid rgba(245,130,32,.4)}
.badge.ok{background:var(--emerald-soft);color:#6EE7B7;border:1px solid rgba(16,185,129,.45)}
.badge.off{background:var(--slate-soft);color:#CBD5E1;border:1px solid rgba(148,163,184,.35)}
.patron{color:var(--text);font-size:1rem;line-height:1.55;margin:.4rem 0 .9rem}
.meter{margin:.2rem 0 1rem}
.meter .row{display:flex;justify-content:space-between;font-size:.75rem;color:var(--muted);font-family:var(--mono);margin-bottom:5px}
.meter .track{height:8px;background:#0A1024;border-radius:99px;overflow:hidden;border:1px solid var(--line)}
.meter .fill{height:100%;background:linear-gradient(90deg,#FDBA74,var(--amber),#FF6B35)}
.grid3{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:12px}
.cell{background:#0C1530;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.cell .k{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.cell .v{font-size:.88rem;color:var(--text);margin-top:4px;line-height:1.4}
.cell .v.mono{font-family:var(--mono);font-size:.78rem;color:#FDBA74;word-break:break-all}
.gate-title{font-family:var(--mono);font-size:.78rem;letter-spacing:.12em;color:var(--muted);margin:14px 0 6px;text-transform:uppercase}
div[class*="st-key-ok_"] button{background:#065F46!important;border:1px solid var(--emerald)!important;color:#ECFDF5!important;font-weight:700!important;padding:.7rem 0!important}
div[class*="st-key-ok_"] button:hover{background:#047857!important}
div[class*="st-key-no_"] button{background:#1F2937!important;border:1px solid #475569!important;color:#E2E8F0!important;font-weight:700!important;padding:.7rem 0!important}
div[class*="st-key-pe_"] button{background:#3B2410!important;border:1px solid var(--amber)!important;color:#FED7AA!important;font-weight:700!important;padding:.7rem 0!important}
.terminal{background:#05080F;border:1px solid #1E293B;border-radius:12px;font-family:var(--mono);font-size:.85rem;color:#CBD5E1;overflow:hidden}
.terminal .bar{background:#0F172A;padding:8px 12px;border-bottom:1px solid #1E293B;color:var(--muted);font-size:.75rem}
.terminal .bar b{color:#EF4444}.terminal .bar i{color:#F59E0B;font-style:normal}.terminal .bar u{color:#10B981;text-decoration:none}
.terminal .body{padding:14px 16px;line-height:1.75;white-space:pre-wrap}
.t-ok{color:#34D399}.t-warn{color:#FBBF24}.t-err{color:#F87171}.t-dim{color:#64748B}.t-acc{color:#FDBA74}
.story{background:#F8FAFC;color:#0F172A;border-radius:16px;padding:20px 22px;border-top:6px solid var(--amber);height:100%}
.story .where{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:#64748B;font-weight:700}
.story h5{font-size:1.2rem;margin:.35rem 0 .6rem;color:#0F172A;font-weight:800}
.story .money{font-family:var(--mono);font-size:1.6rem;font-weight:700;color:#C2410C}
.story p{font-size:.95rem;line-height:1.5;color:#334155;margin:.5rem 0 0}
.story .who{margin-top:.8rem;font-size:.85rem;color:#475569}
.story .chip{display:inline-block;margin-top:.8rem;font-size:.75rem;padding:4px 10px;border-radius:999px;background:#ECFDF5;color:#065F46;font-weight:700}
.story .chip.p{background:#FFF7ED;color:#9A3412}
.section-k{font-family:var(--mono);font-size:.78rem;letter-spacing:.14em;color:var(--amber);text-transform:uppercase;margin-bottom:.2rem}
.stTabs [data-baseweb="tab-list"]{gap:6px;border-bottom:1px solid var(--line)}
.stTabs [data-baseweb="tab"]{background:var(--panel);border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;padding:10px 16px;color:var(--muted)}
.stTabs [aria-selected="true"]{background:var(--panel2)!important;color:#fff!important;border-color:var(--amber)!important}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# CASOS DE LA DEMO (ilustrativos, anonimizados)
# ==============================================================================
CASOS = [
    {
        "id": "A",
        "codigo": "RST-CABA-A-001",
        "nombre": "Proveedor A — sector salud",
        "tags": ["#CompetenciaRecurrente", "#MismaTerna", "#Salud"],
        "patron": "En la mayoría de sus concursos compite contra la misma terna de distribuidoras, que pierden por márgenes mínimos.",
        "organismo": "Ministerio de Salud CABA / Hospitales Públicos",
        "fuente": "raw.caba__buenos_aires_compras__d09720af__v2",
        "regla": "Competencia recurrente: mismo grupo de oferentes en 3 o más procedimientos.",
        "senal": 78,
    },
    {
        "id": "B",
        "codigo": "RST-CABA-B-002",
        "nombre": "Proveedor B — servicios urbanos",
        "tags": ["#Plazo48hs", "#OferenteÚnico", "#EspacioPúblico"],
        "patron": "Varios expedientes con menos de 48 horas hábiles entre la publicación y la apertura de sobres, con un solo oferente.",
        "organismo": "Ministerio de Espacio Público CABA",
        "fuente": "raw.caba__buenos_aires_compras__d09720af__v2",
        "regla": "Plazo corto: menos de 3 días hábiles entre convocatoria y apertura.",
        "senal": 64,
    },
    {
        "id": "C",
        "codigo": "RST-CABA-C-003",
        "nombre": "Proveedores C y D — obra vial",
        "tags": ["#VínculoRegistral", "#TeléfonoCompartido", "#ObraVial"],
        "patron": "Dos empresas que compiten entre sí en licitaciones de pavimentación comparten teléfono comercial en el registro de proveedores.",
        "organismo": "Dirección General de Obras Viales",
        "fuente": "Registro de Proveedores BAC",
        "regla": "Vínculo registral: oferentes del mismo procedimiento con domicilio, teléfono o apoderado en común.",
        "senal": 52,
    },
]
ESTADOS = ["Pendiente", "Aprobado por periodista", "Descartado"]
if "decisiones" not in st.session_state:
    st.session_state.decisiones = {c['id']: {"estado": "Pendiente", "nota": ""} for c in CASOS}


def estado_de(caso_id):
    return st.session_state.decisiones[caso_id]["estado"]


def badge(estado):
    if estado == ESTADOS[1]:
        return '<span class="badge ok">✔ VERIFICADO POR PERIODISTA</span>'
    if estado == ESTADOS[2]:
        return '<span class="badge off">✕ DESCARTADO</span>'
    return '<span class="badge pend">● PENDIENTE DE VERIFICACIÓN</span>'


def decidir(caso_id, estado):
    nota = st.session_state.get(f"nota_{caso_id}", "")
    st.session_state.decisiones[caso_id] = {"estado": estado, "nota": nota}
    st.toast(f"Caso {caso_id}: {estado}", icon="✅" if estado == ESTADOS[1] else "📝")


# ==============================================================================
# SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown("### 🛰️ RASTRO")
    st.caption("Radar agéntico de integridad en compras públicas")
    st.divider()
    nivel = st.selectbox(
        "Ámbito de auditoría",
        [
            "🏛️ CABA — Buenos Aires Compras (BAC)",
            "🇦🇷 Nacional — Presupuesto & Obra Pública",
            "🇲🇽 México — Compranet / PNT (Demo Regional)",
        ],
    )
    tipo_alerta = st.multiselect(
        "Reglas activas",
        ["Concentración de Contratos", "Competencia recurrente", "Plazos cortos (< 72h)", "Vínculos registrales"],
        default=["Concentración de Contratos", "Competencia recurrente"],
    )
    st.divider()
    st.markdown("**Metodología:** Giovanny Flores (México)")
    st.markdown("**Desarrollo & OpenARG:** Ricardo Gabriel Diaz (Argentina)")
    st.caption("Media Party Buenos Aires 2026")

# ==============================================================================
# HEADER
# ==============================================================================
aprobados = sum(1 for c in CASOS if estado_de(c['id']) == ESTADOS[1])
descartados = sum(1 for c in CASOS if estado_de(c['id']) == ESTADOS[2])
pendientes = len(CASOS) - aprobados - descartados

st.markdown('<div class="hero-title">Rastro<span>.</span> Radar de integridad en compras públicas</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">La máquina encuentra indicios objetivos. El periodista investiga y decide la historia.</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="statusline">
  <span><span class="dot"></span>RADAR ACTIVO</span>
  <span>FUENTE: OpenARG · BAC CABA</span>
  <span>REGISTROS: 107.441</span>
  <span>REGLAS: {len(tipo_alerta)} activas</span>
  <span>MODO: demo · casos anonimizados</span>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "🛰️  Radar de indicios",
    "📊  Explorador de contratistas",
    "🤖  Copiloto IA",
    "👥  Modo cívico",
])

# ==============================================================================
# TAB 1: RADAR DE INDICIOS + PUERTA HUMANA
# ==============================================================================
with tab1:
    st.markdown(f"""
    <div class="kpis">
      <div class="kpi"><div class="lbl">Contratos en la base</div><div class="val">107.441</div></div>
      <div class="kpi amber"><div class="lbl">Pendientes de verificación</div><div class="val">{pendientes}</div></div>
      <div class="kpi green"><div class="lbl">Verificados por periodista</div><div class="val">{aprobados}</div></div>
      <div class="kpi"><div class="lbl">Descartados</div><div class="val">{descartados}</div></div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Casos ilustrativos y anonimizados. Un indicio no es una acusación: ninguna ficha se publica sin la decisión de un periodista.")

    for c in CASOS:
        est = estado_de(c['id'])
        clase = "ok" if est == ESTADOS[1] else "off" if est == ESTADOS[2] else ""
        tags = "".join(f'<span class="tag">{t}</span>' for t in c['tags'])
        st.markdown(f"""
        <div class="ficha {clase}">
          <div class="ficha-top"><span class="fid">FICHA DE RADAR · {c['codigo']}</span>{badge(est)}</div>
          <h4>{c['nombre']}</h4>
          <div>{tags}</div>
          <p class="patron">{c['patron']}</p>
          <div class="meter"><div class="row"><span>FUERZA DE LA SEÑAL (ilustrativa)</span><span>{c['senal']}/100</span></div>
            <div class="track"><div class="fill" style="width:{c['senal']}%"></div></div></div>
          <div class="grid3">
            <div class="cell"><div class="k">Regla que lo disparó</div><div class="v">{c['regla']}</div></div>
            <div class="cell"><div class="k">Organismo</div><div class="v">{c['organismo']}</div></div>
            <div class="cell"><div class="k">Fuente</div><div class="v mono">{c['fuente']}</div></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f'<div class="gate-title">🧑‍⚖️ Puerta humana · caso {c['id']}</div>', unsafe_allow_html=True)
        st.text_input(
            "Nota de verificación",
            value=st.session_state.decisiones[c['id']]["nota"],
            key=f"nota_{c['id']}",
            placeholder="Qué se revisó, qué falta confirmar…",
            label_visibility="collapsed",
        )
        b1, b2, b3 = st.columns(3)
        b1.button("✔  Verificar y aprobar", key=f"ok_{c['id']}", use_container_width=True,
                  on_click=decidir, args=(c['id'], ESTADOS[1]))
        b2.button("●  Dejar pendiente", key=f"pe_{c['id']}", use_container_width=True,
                  on_click=decidir, args=(c['id'], ESTADOS[0]))
        b3.button("✕  Descartar", key=f"no_{c['id']}", use_container_width=True,
                  on_click=decidir, args=(c['id'], ESTADOS[2]))
        st.write("")

# ==============================================================================
# TAB 2: EXPLORADOR DE CONTRATISTAS
# ==============================================================================
with tab2:
    st.markdown('<div class="section-k">Explorador</div>', unsafe_allow_html=True)
    st.markdown("#### Contratistas con mayor volumen adjudicado en CABA")
    st.caption("Agregación de 107.441 filas en OpenARG. El volumen de contratos por sí solo no es un indicio de irregularidad.")

    df = pd.DataFrame({
        "Contratista": [
            "DROGUERIA COMARSA S.A.",
            "DROGUERIA VARADERO S.A.",
            "REDIMER S.A.",
            "MEDI SISTEM S.R.L.",
            "CORPORACION PARA LA DEFENSA DEL SUR S.A.",
        ],
        "Monto Total ($ ARS)": [3426795644514.97, 1072175964900.15, 440479447733.84, 297599358485.56, 222347837340.00],
        "Contratos Ganados": [9568, 3401, 184, 3770, 60],
    })
    fig = px.bar(df, x="Monto Total ($ ARS)", y="Contratista", orientation="h",
                 color_discrete_sequence=["#F58220"], text="Contratos Ganados",
                 labels={"Monto Total ($ ARS)": "Monto total adjudicado (ARS)", "Contratista": ""})
    fig.update_traces(texttemplate="%{text:,} contratos", textposition="outside", marker_line_width=0)
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      height=380, margin=dict(l=10, r=40, t=10, b=10), yaxis=dict(autorange="reversed"),
                      font=dict(family="Inter, sans-serif", color="#CBD5E1"))
    fig.update_xaxes(gridcolor="#24335F")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(
        df, use_container_width=True, hide_index=True,
        column_config={"Monto Total ($ ARS)": st.column_config.NumberColumn(format="$ %.0f")},
    )

# ==============================================================================
# TAB 3: COPILOTO IA (TERMINAL)
# ==============================================================================
with tab3:
    st.markdown('<div class="section-k">Copiloto IA</div>', unsafe_allow_html=True)
    st.markdown("#### El agente prepara; el periodista decide")

    col_izq, col_der = st.columns([1, 1.35])
    with col_izq:
        proveedor_seleccionado = st.selectbox("Caso", [c['nombre'] for c in CASOS])
        caso = next(c for c in CASOS if c['nombre'] == proveedor_seleccionado)
        st.markdown(badge(estado_de(caso['id'])), unsafe_allow_html=True)
        st.write("")
        accion = st.radio(
            "¿Qué preparo?",
            [
                "📄 Resumen ejecutivo y cronología del caso",
                "⚖️ Redactar Pedido de Acceso a la Información (Ley 27.275)",
                "📊 Análisis de red de competidores recurrentes",
            ],
        )
        btn_generar = st.button("▶  Ejecutar agente", type="primary", use_container_width=True)

    with col_der:
        if not btn_generar:
            st.markdown("""<div class="terminal"><div class="bar"><b>●</b> <i>●</i> <u>●</u> &nbsp; rastro-agent — idle</div>
<div class="body"><span class="t-dim">$ rastro agent --esperando-instrucción</span>
<span class="t-dim">Elegí un caso y una acción, y ejecutá el agente.</span></div></div>""", unsafe_allow_html=True)
        else:
            es_pai = "Acceso a la Información" in accion
            aprobado = estado_de(caso['id']) == ESTADOS[1]
            pasos = [
                ("t-dim", f"$ rastro agent --caso {caso['codigo']}"),
                ("t-acc", f"› Cargando expediente desde OpenARG (datos precargados): {caso['fuente']}"),
                ("t-ok", f"✔ Regla aplicada: {caso['regla']}"),
                ("t-acc", "› Consultando la puerta humana…"),
            ]
            if es_pai:
                pasos += [
                    ("t-ok" if aprobado else "t-warn",
                     "✔ Indicio verificado" if aprobado else "! Indicio pendiente: se permite pedir información para verificarlo"),
                    ("t-acc", "› Validando marco legal: Ley 104 (CABA) · Ley 27.275 (Nacional)"),
                    ("t-acc", "› Generando solicitud de acceso a la información…"),
                    ("t-ok", "✔ Borrador listo para revisión del periodista"),
                ]
            elif aprobado:
                pasos += [
                    ("t-ok", "✔ Verificado por periodista: se habilita la ficha"),
                    ("t-acc", "› Redactando ficha con la nota de verificación…"),
                    ("t-ok", "✔ Ficha lista · incluye paso de derecho de réplica"),
                ]
            else:
                pasos += [
                    ("t-err", "✕ BLOQUEADO: el indicio no tiene verificación humana"),
                    ("t-dim", "  Rastro no genera fichas ni hipótesis publicables sin la decisión de un periodista."),
                ]
            caja = st.empty()
            lineas = []
            for cls, txt in pasos:
                lineas.append(f'<span class="{cls}">{txt}</span>')
                caja.markdown(
                    '<div class="terminal"><div class="bar"><b>●</b> <i>●</i> <u>●</u> &nbsp; rastro-agent — ejecutando</div>'
                    f'<div class="body">{"<br>".join(lineas)}</div></div>',
                    unsafe_allow_html=True,
                )
                time.sleep(0.45)

            st.write("")
            if es_pai:
                st.text_area(
                    "Solicitud de acceso a la información (borrador)",
                    f"""A la Dirección General de Compras y Contrataciones del GCBA:

REF: Solicitud de Información Pública en los términos de la Ley 104 de CABA / Ley Nacional 27.275.

Por medio de la presente, en mi carácter de periodista, solicito se me brinde acceso a la siguiente información respecto a las contrataciones adjudicadas a {caso['nombre']}:

1. Copia digital íntegra de los pliegos de bases y condiciones y actas de apertura de ofertas de los expedientes licitatorios del período 2024-2026.
2. Detalle de los días hábiles otorgados entre la fecha de publicación en el Boletín Oficial y la fecha límite de presentación de ofertas en los concursos con plazo inferior a 72 horas.
3. Informar si se presentaron observaciones o impugnaciones por parte de otros potenciales oferentes respecto a los plazos establecidos.

Fundamento el presente pedido en el derecho a la información pública, la transparencia activa y el control cívico de los fondos públicos.

Quedo a la espera de su respuesta dentro del plazo legal de 15 días hábiles.
Atentamente.""",
                    height=320,
                )
            elif aprobado:
                nota = st.session_state.decisiones[caso['id']]["nota"] or "Sin nota."
                st.markdown(f"""
<div class="ficha ok">
  <div class="ficha-top"><span class="fid">FICHA VERIFICADA · {caso['codigo']}</span>{badge(ESTADOS[1])}</div>
  <h4>{caso['nombre']}</h4>
  <p class="patron"><b>Patrón:</b> {caso['patron']}</p>
  <div class="grid3">
    <div class="cell"><div class="k">Nota del periodista</div><div class="v">{nota}</div></div>
    <div class="cell"><div class="k">Siguiente paso</div><div class="v">Pedir la versión de las empresas y del organismo (derecho de réplica) antes de publicar.</div></div>
    <div class="cell"><div class="k">Fuente</div><div class="v mono">{caso['fuente']}</div></div>
  </div>
</div>""", unsafe_allow_html=True)

# ==============================================================================
# TAB 4: MODO CÍVICO — STORY CARDS
# ==============================================================================
with tab4:
    st.markdown('<div class="section-k">Modo cívico</div>', unsafe_allow_html=True)
    st.markdown("#### Abierto y gratuito: cualquier vecino entiende cómo se gasta en su barrio")
    st.caption("Ejemplos ilustrativos de Tarjetas Ciudadanas. Los indicios son públicos; las historias solo salen con verificación humana.")

    s1, s2, s3 = st.columns(3)
    s1.markdown("""<div class="story"><div class="where">📍 Comuna 4 · ejemplo</div><h5>Bacheo de calles del barrio</h5>
<div class="money">$ 120 M</div><p>Es lo que se pagó este año por arreglar baches en tu comuna.</p>
<div class="who">Ganó: Empresa X · compitieron 3 empresas</div><span class="chip">Sin indicios</span></div>""", unsafe_allow_html=True)
    s2.markdown("""<div class="story"><div class="where">📍 Comuna 7 · ejemplo</div><h5>Mantenimiento de escuelas</h5>
<div class="money">$ 45 M</div><p>Se contrató a una sola empresa con un plazo de dos días para presentar ofertas.</p>
<div class="who">Ganó: Empresa Y · se presentó 1 empresa</div><span class="chip p">Indicio en revisión periodística</span></div>""", unsafe_allow_html=True)
    s3.markdown("""<div class="story"><div class="where">📍 Comuna 1 · ejemplo</div><h5>Iluminación de plazas</h5>
<div class="money">$ 18 M</div><p>Tres empresas compitieron y ganó la oferta más baja. Podés ver el contrato completo.</p>
<div class="who">Ganó: Empresa Z · compitieron 3 empresas</div><span class="chip">Sin indicios</span></div>""", unsafe_allow_html=True)

    st.write("")
    st.markdown("""
| Nivel | Quién | Qué puede hacer |
|---|---|---|
| **Abierto** | Cualquier persona | Consultar contratos y ver indicios con la regla y el documento que los respaldan |
| **Verificación** | Periodistas, organizaciones y comunidad acreditada | Aprobar o descartar indicios y generar fichas |
| **Institucional** | Medios, OSC, órganos de control | Monitoreo, alertas y API |
""")
