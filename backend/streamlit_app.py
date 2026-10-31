"""
RASTRO — Radar Agéntico de Integridad en Compras Públicas
Media Party Buenos Aires 2026
Metodología: Giovanny Flores (México) & Gabo
Alimentado por datos públicos oficiales vía OpenARG MCP
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
from openarg_client import client

st.set_page_config(
    page_title="Rastro — Radar Agéntico de Compras Públicas",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos limpios y profesionales
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0E263D;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 20px;
    }
    .alert-card {
        background-color: #FFFFFF;
        border-left: 5px solid #F58220;
        border-radius: 6px;
        padding: 16px;
        margin-bottom: 14px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        border: 1px solid #E2E8F0;
        border-left-width: 5px;
    }
    .badge-red {
        background-color: #FEE2E2;
        color: #991B1B;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .badge-orange {
        background-color: #FFEDD5;
        color: #9A3412;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .badge-blue {
        background-color: #E0F2FE;
        color: #0369A1;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR: Nivel y Alcance (De Menos a Más) -----------------
with st.sidebar:
    st.markdown("## 🔍 **RASTRO**")
    st.markdown("*Radar Agéntico de Integridad en Compras Públicas*")
    st.divider()

    st.markdown("### 📍 Nivel de Consulta")
    nivel = st.selectbox(
        "Seleccioná el ámbito de auditoría:",
        [
            "🏛️ CABA — Buenos Aires Compras (BAC)",
            "🇦🇷 Nacional — Presupuesto & Obra Pública",
            "🇲🇽 México — Compranet / PNT (Demo Regional)"
        ]
    )

    st.markdown("### ⚙️ Filtros de Auditoría")
    tipo_alerta = st.multiselect(
        "Tipo de Alertas a monitorear:",
        ["Concentración de Contratos", "Competencia recurrente", "Plazos cortos (< 72h)", "Vínculos registrales"],
        default=["Concentración de Contratos", "Competencia recurrente"]
    )

    st.divider()
    st.markdown("**Metodología:** Giovanny Flores (México)")
    st.markdown("**Desarrollo & OpenARG:** Gabo")
    st.markdown("🚀 *Media Party Buenos Aires 2026*")

# ----------------- HEADER PRINCIPAL -----------------
st.markdown('<div class="main-header">Rastro: Inteligencia para Periodistas de Investigación</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Auditoría agéntica de compras públicas: la máquina encuentra indicios objetivos, el periodista investiga la historia.</div>', unsafe_allow_html=True)

# Tabs principales
tab1, tab2, tab3, tab4 = st.tabs([
    "🚨 Feed de Alertas Activas",
    "📊 Explorador de Contratistas",
    "🤖 Copiloto Agéntico (Investigar)",
    "👥 Modo Cívico / Audiencias"
])

# ==============================================================================
# CASOS DE LA DEMO (ilustrativos, anonimizados)
# ==============================================================================
CASOS = [
    {
        "id": "A",
        "nombre": "Proveedor A — sector salud",
        "etiquetas": [("INDICIO A VERIFICAR", "badge-orange"), ("COMPETENCIA RECURRENTE", "badge-blue")],
        "patron": "En la mayoría de sus concursos compite contra la misma terna de distribuidoras, que pierden por márgenes mínimos.",
        "organismo": "Ministerio de Salud CABA / Hospitales Públicos",
        "fuente": "raw.caba__buenos_aires_compras__d09720af__v2",
        "regla": "Competencia recurrente: mismo grupo de oferentes en 3 o más procedimientos.",
    },
    {
        "id": "B",
        "nombre": "Proveedor B — servicios urbanos",
        "etiquetas": [("INDICIO A VERIFICAR", "badge-orange"), ("PLAZO CORTO", "badge-blue")],
        "patron": "Varios expedientes con menos de 48 horas hábiles entre la publicación y la apertura de sobres, con un solo oferente.",
        "organismo": "Ministerio de Espacio Público CABA",
        "fuente": "raw.caba__buenos_aires_compras__d09720af__v2",
        "regla": "Plazo corto: menos de 3 días hábiles entre convocatoria y apertura.",
    },
    {
        "id": "C",
        "nombre": "Proveedores C y D — obra vial",
        "etiquetas": [("INDICIO A VERIFICAR", "badge-orange"), ("DATOS DE CONTACTO COMPARTIDOS", "badge-blue")],
        "patron": "Dos empresas que compiten entre sí en licitaciones de pavimentación comparten teléfono comercial en el registro de proveedores.",
        "organismo": "Dirección General de Obras Viales",
        "fuente": "Registro de Proveedores BAC",
        "regla": "Vínculo registral: oferentes del mismo procedimiento con domicilio, teléfono o apoderado en común.",
    },
]
ESTADOS = ["Pendiente", "Aprobado por periodista", "Descartado"]
if "decisiones" not in st.session_state:
    st.session_state.decisiones = {c['id']: {"estado": "Pendiente", "nota": ""} for c in CASOS}


def estado_de(caso_id):
    return st.session_state.decisiones[caso_id]["estado"]


# ==============================================================================
# TAB 1: FEED DE INDICIOS + PUERTA HUMANA
# ==============================================================================
with tab1:
    st.markdown("### 📌 Indicios detectados en compras públicas de CABA")
    st.caption("Demo: casos ilustrativos y anonimizados. Ningún indicio es una acusación: cada uno debe ser verificado por un periodista antes de publicarse.")

    aprobados = sum(1 for c in CASOS if estado_de(c['id']) == ESTADOS[1])
    descartados = sum(1 for c in CASOS if estado_de(c['id']) == ESTADOS[2])
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Contratos en la base", "107.441", "+500k históricos")
    col2.metric("Indicios en esta demo", str(len(CASOS)))
    col3.metric("Aprobados por periodista", str(aprobados))
    col4.metric("Descartados", str(descartados))

    st.divider()

    for c in CASOS:
        etiquetas = " ".join(f'<span class="{cls}">{txt}</span>' for txt, cls in c['etiquetas'])
        st.markdown(f"""
        <div class="alert-card">
            {etiquetas}
            <h4 style="margin: 8px 0 4px 0; color: #0F172A;">{c['nombre']}</h4>
            <p style="color: #475569; font-size: 0.95rem; margin-bottom: 8px;"><b>Patrón:</b> {c['patron']}</p>
            <p style="font-size: 0.85rem; color: #64748B;">
                <b>Regla que lo disparó:</b> {c['regla']}<br>
                <b>Organismo:</b> {c['organismo']} &nbsp;|&nbsp; <b>Fuente:</b> <code>{c['fuente']}</code>
            </p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander(f"🧑‍⚖️ Puerta humana — decisión del periodista sobre el caso {c['id']}", expanded=False):
            d = st.session_state.decisiones[c['id']]
            nuevo = st.radio("Estado", ESTADOS, index=ESTADOS.index(d['estado']), key=f"estado_{c['id']}", horizontal=True)
            nota = st.text_area("Nota de verificación (qué se revisó, qué falta)", value=d['nota'], key=f"nota_{c['id']}")
            st.session_state.decisiones[c['id']] = {"estado": nuevo, "nota": nota}
            if nuevo == ESTADOS[1]:
                st.success("Aprobado: ya se puede generar la ficha en el Copiloto.")
            elif nuevo == ESTADOS[2]:
                st.warning("Descartado: no se generará ninguna ficha.")
            else:
                st.info("Pendiente: el Copiloto solo puede preparar una solicitud de acceso a la información.")


# ==============================================================================
# TAB 2: EXPLORADOR DE CONTRATISTAS
# ==============================================================================
with tab2:
    st.markdown("### 📊 Ranking de Contratistas con Mayor Volumen de Adjudicación")
    st.caption("Agregación de 107.441 filas en OpenARG. El volumen de contratos por sí solo no es un indicio de irregularidad.")

    # Datos reales obtenidos de la herramienta agregar_datos de OpenARG
    data_ranking = {
        "Contratista": [
            "DROGUERIA COMARSA S.A.",
            "DROGUERIA VARADERO S.A.",
            "REDIMER S.A.",
            "MEDI SISTEM S.R.L.",
            "CORPORACION PARA LA DEFENSA DEL SUR S.A."
        ],
        "Monto Total ($ ARS)": [
            3426795644514.97,
            1072175964900.15,
            440479447733.84,
            297599358485.56,
            222347837340.00
        ],
        "Contratos Ganados": [9568, 3401, 184, 3770, 60],
    }
    df = pd.DataFrame(data_ranking)

    # Gráfico interactivo
    fig = px.bar(
        df,
        x="Monto Total ($ ARS)",
        y="Contratista",
        orientation="h",
        color="Contratos Ganados",
        title="Top 5 Proveedores por Monto Adjudicado en CABA (Datos Oficiales OpenARG)",
        labels={"Monto Total ($ ARS)": "Monto Total Adjudicado ($)", "Contratista": ""},
        color_continuous_scale="Oranges"
    )
    fig.update_layout(yaxis=dict(autorange="reversed"), height=350)
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df, use_container_width=True)


# ==============================================================================
# TAB 3: COPILOTO AGÉNTICO (INVESTIGAR CON IA)
# ==============================================================================
with tab3:
    st.markdown("### 🤖 Copiloto Agéntico para Periodistas")
    st.caption("Interactuá con el agente para auditar un expediente, redactar la hipótesis periodística o generar pedidos de acceso a la información.")

    col_izq, col_der = st.columns([1, 1])

    with col_izq:
        proveedor_seleccionado = st.selectbox(
            "Seleccionar caso para profundizar:",
            [c['nombre'] for c in CASOS]
        )
        caso = next(c for c in CASOS if c['nombre'] == proveedor_seleccionado)
        st.caption(f"Estado de la verificación: **{estado_de(caso['id'])}**")

        accion = st.radio(
            "¿Qué querés que prepare el Agente?",
            [
                "📄 Resumen ejecutivo y cronología del caso",
                "⚖️ Redactar Pedido de Acceso a la Información (Ley 27.275)",
                "📊 Análisis de red de competidores recurrentes"
            ]
        )

        btn_generar = st.button("Ejecutar Agente de Auditoría", type="primary")

    with col_der:
        if btn_generar:
            with st.spinner("El Agente está consultando OpenARG y generando el documento..."):
                if "Acceso a la Información" in accion:
                    st.success("✅ Borrador de Pedido de Acceso a la Información generado:")
                    st.text_area(
                        "Texto listo para enviar:",
                        f"""A la Dirección General de Compras y Contrataciones del GCBA:

REF: Solicitud de Información Pública en los términos de la Ley 104 de CABA / Ley Nacional 27.275.

Por medio de la presente, en mi carácter de periodista, solicito se me brinde acceso a la siguiente información respecto a las contrataciones adjudicadas a {caso['nombre']}:

1. Copia digital íntegra de los pliegos de bases y condiciones y actas de apertura de ofertas de los expedientes licitatorios del período 2024-2026.
2. Detalle de los días hábiles otorgados entre la fecha de publicación en el Boletín Oficial y la fecha límite de presentación de ofertas en los concursos con plazo inferior a 72 horas.
3. Informar si se presentaron observaciones o impugnaciones por parte de otros potenciales oferentes respecto a los plazos establecidos.

Fundamento el presente pedido en el derecho a la información pública, la transparencia activa y el control cívico de los fondos públicos.

Quedo a la espera de su respuesta dentro del plazo legal de 15 días hábiles.
Atentamente.""",
                        height=320
                    )
                elif estado_de(caso['id']) != ESTADOS[1]:
                    st.warning("🔒 Este indicio todavía no fue aprobado por un periodista. Rastro no genera fichas ni hipótesis publicables sin verificación humana. Aprobalo en la pestaña de indicios o pedí primero la información pública.")
                else:
                    nota = st.session_state.decisiones[caso['id']]["nota"] or "Sin nota."
                    st.info(f"📋 Ficha verificada: {caso['nombre']}")
                    st.markdown(f"""
- **Patrón:** {caso['patron']}
- **Regla:** {caso['regla']}
- **Nota del periodista:** {nota}
- **Siguiente paso:** pedir la versión de las empresas y del organismo (derecho de réplica) antes de publicar.
- **Fuente:** `{caso['fuente']}`
""")
        else:
            st.info("Elegí un caso y presioná **Ejecutar Agente de Auditoría** para ver al copiloto en acción.")


# ==============================================================================
# TAB 4: MODO CÍVICO — ABIERTO A TODO PÚBLICO
# ==============================================================================
with tab4:
    st.markdown("### 👥 Modo cívico: abierto y gratuito para todo público")
    st.markdown("""
    **Rastro es una herramienta abierta**: cualquier persona puede consultar cómo gasta su municipio o su ciudad.
    > *«¿Qué obras de bacheo o escuelas se licitaron en mi comuna este año y quiénes las ganaron?»*

    | Nivel | Quién | Qué puede hacer |
    |---|---|---|
    | Abierto | Cualquier persona | Consultar contratos y ver indicios con la regla y el documento que los respaldan |
    | Verificación | Periodistas, organizaciones y comunidad acreditada | Aprobar o descartar indicios y generar fichas |
    | Institucional | Medios, OSC, órganos de control | Monitoreo, alertas y API |
    """)
    st.success("💡 **Los indicios son públicos; las historias solo salen con verificación humana.** Código abierto, sostenido con fondos, servicios institucionales y membresías comunitarias.")
