# 🔍 RASTRO — Radar Agéntico de Integridad en Compras Públicas

> **Hackatón Media Party Buenos Aires 2026** — *«Storytelling en la era de los agentes»*  
> **Lema:** *«La máquina encuentra indicios objetivos; el periodista investiga la historia.»*  
> **Demo en Vivo:** [rastro-datos.vercel.app](https://rastro-datos.vercel.app/)  
> **Presentación (Pitch Deck):** [rastro-datos.vercel.app/deck](https://rastro-datos.vercel.app/deck)  
> **Ficha Oficial en HackDash:** [hackdash.org/projects/6ae2d87c6e0bb87e31d31598](https://hackdash.org/projects/6ae2d87c6e0bb87e31d31598)  

---

## 👥 Equipo (Media Party BA 2026)

* **Giovanny Flores** (México) — Líder Editorial, Periodista de Datos e Investigación (*Criterio Hidalgo*). Metodología de auditoría, definición de banderas rojas y pitch.
* **Ricardo Gabriel Diaz** (Argentina) — Desarrollo, Arquitectura de IA, Conexión OpenARG MCP e Interfaz Web.
* **Pedro Lionel Marsetti** (Argentina) — Desarrollo, Infraestructura y Colaboración Técnica.

---

## 📌 ¿Qué es Rastro?

**Rastro** es un agente de auditoría que lee y analiza expedientes de contrataciones y licitaciones públicas (concursos de gobiernos provinciales, municipales y entes descentralizados), cruza empresas oferentes, domicilios fiscales, teléfonos y fechas, y detecta automáticamente señales de alerta (*red flags*):

1. **Competencia Simulada (*Bid Rigging*):** Grupos de empresas que se presentan sistemáticamente a los mismos concursos con diferencias mínimas de cotización para asegurar la adjudicación.
2. **Vínculos Registrales y Domicilios Compartidos:** Contratistas supuestamente independientes que comparten el mismo domicilio fiscal, teléfono comercial o apoderados societarios en el registro de proveedores.
3. **Plazos Exprés y Trámites Urgentes:** Licitaciones publicadas con menos de 48 a 72 horas hábiles entre la convocatoria y la apertura de sobres, favoreciendo a oferentes preacordados.
4. **Concentración Anómala:** Proveedores que acumulan un porcentaje desproporcionado del presupuesto de un ministerio u hospital público.

Alimentado por **OpenARG MCP** con más de **107.000 contrataciones oficiales de CABA** y 500.000 registros históricos, Rastro no emite acusaciones: **entrega la prueba documental exacta y redacta pedidos formales de acceso a la información pública en un solo clic.**

---

## 🛡️ Principio Rector: La Puerta Humana (*Human-in-the-Loop*)

> **«La IA lee y redacta. Las reglas deterministas detectan. El periodista decide.»**

En Rastro, un indicio algorítmico **nunca es una acusación**:
* **Sin "alucinaciones" punitivas:** Las alertas no provienen de la intuición probabilística de un LLM, sino de reglas deterministas y auditables basadas en los estándares internacionales de la *Open Contracting Partnership (OCP)*.
* **Candado Ético:** El Copiloto de IA tiene un bloqueo por diseño. No redacta borradores de investigación ni genera fichas públicas si el caso no cuenta con la validación de un periodista que haya cotejado los pliegos originales en la **Puerta Humana**.
* **Derecho de Réplica:** Toda ficha periodística generada incluye el requerimiento obligatorio de descargo oficial a las empresas señaladas y a los organismos contratantes antes de su publicación.

---

## ⚙️ Arquitectura en 4 Etapas

```
┌─────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐      ┌──────────────────────┐
│   1. LECTOR     │ ───► │  2. CRUZADOR DE REGLAS  │ ───► │    3. PUERTA HUMANA     │ ───► │     4. NARRADOR      │
│ Ingesta OpenARG │      │ 7 Reglas OCP sin sesgo  │      │ Verificación obligatoria│      │ Copiloto FOIA y Ficha│
│ (107k contratos)│      │ auditoría determinista  │      │  del periodista a cargo │      │ con derecho a réplica│
└─────────────────┘      └─────────────────────────┘      └─────────────────────────┘      └──────────────────────┘
```

1. **Lector:** Ingesta y normalización de datos abiertos mediante OpenARG MCP (Buenos Aires Compras) y extracción de metadatos de expedientes.
2. **Cruzador de Reglas (Auditoría basada en OCP):**
   * **R1 — Trío Recurrente:** El mismo conjunto de licitantes compite en 3 o más procedimientos.
   * **R2 — Domicilio Compartido:** Oferentes del mismo concurso con idéntica sede social, teléfono o apoderado común.
   * **R3 — Ofertas Espejo:** Diferencia menor al 3% entre propuestas para simular puja de precios.
   * **R4 — Ganador Rotativo:** Alternancia coordinada de ganadores dentro del mismo grupo de proveedores.
   * **R5 — Fraccionamiento de Gasto:** Mismo proveedor, mismo rubro y compras consecutivas para esquivar la licitación pública.
   * **R6 — Documentación Faltante:** Procedimientos que omiten actas de apertura, pliegos o cuadros comparativos.
   * **R7 — Plazos Cortos:** Menos de 3 días hábiles entre publicación y apertura.
3. **Puerta Humana:** Módulo interactivo donde el periodista revisa los contratos citados, introduce sus notas de campo y aprueba o descarta el indicio.
4. **Narrador y Copiloto:** Generación de resúmenes ejecutivos, análisis de redes de competidores y redacción automatizada de solicitudes bajo la **Ley 104 de CABA** y la **Ley Nacional 27.275 de Acceso a la Información Pública**.

---

## 💼 Modelo de Sostenibilidad y Niveles de Acceso

| Nivel | Destinatarios | Funcionalidades |
|---|---|---|
| **Abierto (Gratuito)** | Ciudadanía y vecinos | **Modo Cívico:** Tarjetas en lenguaje cotidiano con las obras y gastos de cada comuna (*bacheo, escuelas, luminarias*). |
| **Verificación** | Periodistas acreditados, OSCs y comunidad de datos | Puerta humana activa, revisión de expedientes, notas de verificación y exportación de fichas. |
| **Institucional (SaaS B2B)** | Salas de redacción locales, ONGs y órganos de control | Monitoreo continuo de licitaciones, alertas en tiempo real, análisis masivo y API (suscripciones de $30 a $90 USD/mes). |

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Aplicación Web en Producción (Vercel)
La aplicación web completa corre de forma estática y ultrarrápida:
* **Radar Principal:** [https://rastro-datos.vercel.app/](https://rastro-datos.vercel.app/)
* **Presentación de Diapositivas:** [https://rastro-datos.vercel.app/deck](https://rastro-datos.vercel.app/deck)

### 2. Ejecución Local (Streamlit)
```bash
# 1. Clonar el repositorio
git clone https://github.com/rgabrieldiaz/rastro.git
cd rastro

# 2. Crear entorno virtual e instalar dependencias
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements-streamlit.txt

# 3. Iniciar el prototipo local
streamlit run backend/streamlit_app.py
```

---

## 📂 Estructura del Repositorio

```text
├── index.html                     # Portal Web interactivo principal (Tailwind CSS + Chart.js en Vercel)
├── deck.html                      # Presentación del pitch de 10 diapositivas (/deck)
├── deck/
│   ├── index.html                 # Código interactivo del pitch deck
│   ├── rastro-pitch.pdf           # Presentación en formato PDF
│   └── rastro-pitch.pptx          # Presentación en formato PowerPoint
├── vercel.json                    # Configuración de despliegue y rewrites para Vercel
├── backend/
│   ├── streamlit_app.py           # Aplicación en Python / Streamlit
│   ├── openarg_client.py          # Cliente nativo para OpenARG MCP
│   └── requirements-streamlit.txt # Dependencias de Python
├── CLAUDE.md                      # Contexto y directrices para agentes autónomos
├── docs/
│   ├── gio/                       # Documentación metodológica de Giovanny Flores
│   │   ├── README.md              # Marco general de investigación
│   │   ├── DISENO_TECNICO_ORIGINAL.md # Especificación del pipeline
│   │   ├── PITCH.md               # Guiones y estructura del pitch
│   │   └── MEXICO_PNT.md          # Plan de escalado a la Plataforma Nacional de Transparencia (México)
│   └── METODOLOGIA_RASTRO.md      # Tesis periodística de Rastro
└── hackathon_guia_oficial.md      # Reglas y criterios de evaluación de Media Party 2026
```

---

## 🧭 Hoja de Ruta

- **Hoy (Media Party BA 2026):** Prototipo funcional con 107.441 contrataciones de CABA vía OpenARG MCP, puerta humana activa, copiloto bloqueado por ética y modo cívico.
- **30 días:** Validación del lector contra contratos de obra pública municipal y prueba de concepto en redacciones aliadas.
- **3 meses:** Integración con la Plataforma Nacional de Transparencia (PNT) de México (municipios piloto en Hidalgo).
- **6 a 12 meses:** Alertas automáticas para redacciones de América Latina, API institucional y red de periodistas verificadores.

---

## ⚖️ Licencia y Propiedad Intelectual
Proyecto desarrollado bajo el marco de innovación y propiedad intelectual de **Media Party Buenos Aires 2026**: 100% soberanía de los creadores (Licencia MIT sugerida).
