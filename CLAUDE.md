# RASTRO — Instructions for Claude / AI Assistants

Welcome to **Rastro**, an AI-powered public procurement integrity radar built during **Media Party Buenos Aires 2026**.

## 🎯 Project Overview
- **Name:** Rastro (Radar Agéntico de Integridad en Compras Públicas)
- **Team:** Giovanny Flores (Investigative Journalist - Mexico) & Gabo (AI / Software Engineer)
- **Hackathon:** Media Party Buenos Aires 2026 («Storytelling en la era de los agentes»)
- **Dashboard:** [hackdash.org/dashboards/mpba26](https://hackdash.org/dashboards/mpba26)
- **Motto:** *"La máquina encuentra indicios objetivos; el periodista investiga la historia."*

---

## 🔬 Core Investigative Methodology (Giovanny's Framework)
The platform audits government procurement and public works to detect three primary red flags:
1. **Contract Concentration (Acumulación):** Single contractor capturing disproportionate volume/amount of contracts within a ministry or agency.
2. **Bid Rigging / Courtesy Bids (Competencia Simulada):** The same contractor systematically competing against the same 2-3 bidders who always lose with marginal price differences.
3. **Shared Registration Entities (Vínculos Registrales):** Competitors sharing fiscal addresses, phone numbers, contact emails, or cross-board members (RFC/CUIT).

---

## 📂 Repository Structure
- `index.html`: Main Web Application for Vercel deployment (Tailwind CSS, Chart.js).
- `vercel.json`: Vercel deployment configuration.
- `backend/streamlit_app.py`: Streamlit prototype. Contains the 4 core tabs (Alerts Feed, Contractor Explorer, Agentic Copilot, Civic Mode).
- `backend/openarg_client.py`: Zero-dependency Python client for OpenARG MCP tools (accessing +33,000 Argentine public datasets).
- `backend/requirements.txt`: Python package dependencies.
- `.mcp.json`: MCP server configuration for OpenARG (`https://mcp.openarg.org/mcp`).
- `.env.example`: Template for environment variables.
- `docs/METODOLOGIA_RASTRO.md`: Full methodology and roadmap from less to more.
- `hackathon_guia_oficial.md`: Hackathon rules, jury criteria, and tracks.

---

## 🛠️ How to Run and Develop
```bash
# Setup environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt

# Run the Streamlit web application
streamlit run backend/streamlit_app.py
```
App will open at `http://localhost:8501`.

---

## 📊 OpenARG Datasets Used
- Main Table: `raw.caba__buenos_aires_compras__d09720af__v2` (107,441 rows of public tenders with suppliers, amounts, duration in days, and document URLs).
- Historical Contracts: `raw.bac__buenos_aires_compras_contracts__45b499b0__v2` (500,000 contracts, OCDS standard).
- Asset Declarations: `raw.cache_ddjj_declaraciones` (727,999 public official declarations).

---

## 🚀 Key Tasks to Continue Building
When asked to improve or extend the project, focus on:
1. **Network Visualization:** Enhance the bidder network graph showing contractors that bid together (using Plotly network or Streamlit components).
2. **Dynamic Filters:** Add search by tender title, category, or procuring entity.
3. **Agentic FOIA Generator:** Polish the prompt for drafting custom Access to Public Information requests (Ley 27.275 in Argentina / Ley General de Transparencia in Mexico).
4. **Regional Scalability:** Keep the architecture modular so Mexican Compranet/PNT datasets can be loaded seamlessly alongside Argentine OpenARG.
