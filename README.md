# 🔍 RASTRO — Radar Agéntico de Integridad en Compras Públicas

> **Hackatón Media Party Buenos Aires 2026** — *«Storytelling en la era de los agentes»*  
> **Lema:** *«La máquina encuentra indicios objetivos; el periodista investiga la historia.»*  
> **Demo en Vivo:** [rastro-datos.vercel.app](https://rastro-datos.vercel.app/)  
> **Presentación (Pitch Deck):** [rastro-datos.vercel.app/deck](https://rastro-datos.vercel.app/deck)  
> **Dashboard Oficial:** [hackdash.org/dashboards/mpba26](https://hackdash.org/dashboards/mpba26)  

---

## 👥 Equipo (Media Party BA 2026)

* **Giovanny Flores** (México) — Líder Editorial, Periodista de Datos e Investigación (*Criterio Hidalgo*). Metodología de auditoría, definición de banderas rojas y pitch.
* **Ricardo Gabriel Diaz** (Argentina) — Desarrollo, Arquitectura de IA, Conexión OpenARG MCP e Interfaz Web.
* **Pedro Lionel Marsetti** (Argentina) — Desarrollo, Infraestructura y Colaboración Técnica.

---

## 📌 ¿Qué es Rastro?

**Rastro** es una plataforma agéntica que audita bases de datos de contrataciones gubernamentales para **ahorrarle semanas de reportería manual a periodistas de investigación**, detectando automáticamente señales de alerta (*red flags*) en compras públicas:

1. **Concentración Anómala:** Proveedores que acumulan un porcentaje desproporcionado de contratos en un organismo.
2. **Competencia Simulada (Bid Rigging):** Contratistas que en casi todas sus licitaciones compiten sistemáticamente contra los mismos 2 competidores de cortesía.
3. **Coincidencias Registrales:** Empresas formalmente competidoras que comparten el mismo domicilio fiscal, teléfono o apoderados.

Alimentado por **OpenARG MCP** con más de 107.000 contrataciones oficiales de CABA y 500.000 contratos históricos, Rastro no solo muestra datos: **entrega la prueba documental y redacta pedidos formales de acceso a la información pública en un clic.**

---

## 🚀 Cómo Ejecutar la Web App

```bash
# 1. Clonar el repositorio
git clone https://github.com/rgabrieldiaz/rastro.git
cd rastro

# 2. Crear entorno virtual e instalar dependencias
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements-streamlit.txt

# 3. Iniciar la aplicación Streamlit local (opcional)
streamlit run backend/streamlit_app.py
```
La aplicación local se abrirá en `http://localhost:8501`. La versión web para producción corre directamente en Vercel a través de `index.html`.

---

## 📂 Estructura del Proyecto

```text
├── index.html                  # Aplicación Web principal (Vercel)
├── deck.html                   # Presentación del Pitch de 10 slides (Vercel /deck)
├── deck/
│   ├── index.html              # Código fuente de las diapositivas
│   ├── rastro-pitch.pdf        # Presentación en formato PDF
│   └── rastro-pitch.pptx       # Presentación en formato PowerPoint
├── vercel.json                 # Configuración de despliegue y rewrites en Vercel
├── backend/
│   ├── streamlit_app.py        # Prototipo local en Streamlit
│   ├── openarg_client.py       # Cliente Python nativo para OpenARG MCP
│   └── requirements-streamlit.txt # Dependencias de Python
├── CLAUDE.md                   # Guía de contexto para asistentes de IA (Claude / Cursor)
├── .mcp.json                   # Configuración del servidor MCP OpenARG
├── docs/
│   ├── gio/                    # Documentación editorial y metodológica de Giovanny Flores
│   └── METODOLOGIA_RASTRO.md   # Metodología de investigación y tesis del proyecto
└── hackathon_guia_oficial.md   # Reglas oficiales de Media Party 2026
```

---

## 🧭 Hoja de Ruta: De Menos a Más

1. **Fase 1 (MVP Hackatón - B2B Periodistas):** Feed de alertas de compras públicas, buscador de contratistas y copiloto que redacta pedidos de acceso a la información.
2. **Fase 2 (Regional):** Integración de bases de datos de contrataciones de México (Compranet / PNT) y otras provincias argentinas.
3. **Fase 3 (Modo Cívico para Ciudadanos):** Story cards visuales y accesibles para que cualquier vecino consulte qué obras se licitaron en su barrio.

---

## ⚖️ Licencia y Propiedad Intelectual
Desarrollado bajo el marco de propiedad intelectual de Media Party 2026: 100% soberanía de los creadores (Open Source / MIT License sugerida).
