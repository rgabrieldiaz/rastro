# Metodología de Rastro: Radar Agéntico de Compras Públicas

> **Proyecto:** Rastro  
> **Integrantes:** Giovanny Flores (Periodismo de Investigación - México) & Equipo de Desarrollo e IA  
> **Hackatón:** Media Party Buenos Aires 2026 — «Storytelling en la era de los agentes»  
> **Dashboard:** [hackdash.org/dashboards/mpba26](https://hackdash.org/dashboards/mpba26)  

---

## 1. Misión y Propósito

**Rastro** es una plataforma agéntica diseñada para **ahorrarle cientos de horas de reportería a periodistas de investigación**, detectando automáticamente indicios y señales de alerta (*red flags*) en bases de datos de contrataciones y obras públicas gubernamentales.

> **Principio Rector:** *«La máquina encuentra los indicios objetivos; el periodista humano lidera y decide la investigación.»*

---

## 2. Metodología de Investigación (La Tesis de Giovanny)

El sistema procesa y audita bases de datos de licitaciones y concursos públicos para identificar anomalías en tres niveles:

### Alerta Tipo A: Concentración Anómala de Contratos
* **Qué busca:** Contratistas o empresas que ganan una proporción desmedida de las licitaciones dentro de una misma dependencia o ministerio (ej. un solo licitante adjudicándose más del 50% de las obras).
* **Indicio periodístico:** Posible direccionamiento, monopolio de hecho o falta de apertura en los llamados a concurso.

### Alerta Tipo B: Competencia Simulada / Ofertas de Cortesía (Bid Rigging)
* **Qué busca:** Licitantes que **concursan sistemáticamente juntos** en casi todos los procesos. Por ejemplo: la Empresa A gana el 90% de los concursos y las únicas otras empresas que ofertan son siempre la Empresa B y la Empresa C.
* **Indicio periodístico:** Acuerdos colusorios o "empresas sparring" que cotizan más caro a propósito para cumplir el requisito formal de tener 3 oferentes mínimos.

### Alerta Tipo C: Vínculos Societarios y Coincidencias de Registro
* **Qué busca:** Cruce de datos públicos registrales entre empresas participantes:
  - Domicilio fiscal idéntico o compartido.
  - Mismo CUIT / RFC de representantes legales, apoderados o directores.
  - Mismos números de teléfono o correos electrónicos de contacto registrados en los pliegos.
* **Indicio periodístico:** Empresas pertenecientes al mismo grupo económico simulando ser competidores independientes en licitaciones públicas.

---

## 3. Hoja de Ruta: De Menos a Más (Nacional, Provincial, Municipal)

Para no abrumar al usuario y ofrecer una experiencia progresiva, la plataforma se estructura en capas:

```
[Selección de Nivel Geográfico]
 ├── 1. Nacional (Contratos de Obra Pública de la Nación)
 ├── 2. Provincial (Provincia de Buenos Aires, etc.)
 └── 3. Municipal / CABA (Buenos Aires Compras - Comunas)
           │
           ▼
[Feed de Alertas Destacadas]
 • Top Contratistas con Alertas Activas
 • Filtro por Monto, Organismo o Fecha
           │
           ▼
[Ficha de Evidencia del Caso]
 • Gráfico de red de co-participación
 • Números de licitación y contratos oficiales
           │
           ▼
[Copiloto Agéntico para el Periodista]
 • Chat con el expediente
 • Borrador de Pedido de Acceso a la Información (Ley 27.275)
```

---

## 4. Fuentes de Datos (Alimentado por OpenARG MCP)

En Argentina, el sistema se conecta a través del protocolo MCP a:
- **`raw.bac__buenos_aires_compras_contracts__45b499b0__v2`:** Catálogo de 500.000 contratos de compras y obras públicas bajo estándar internacional OCDS (comprador, proveedor, ítems, montos adjudicados, fechas y oferentes).
- **`raw.cache_ddjj_declaraciones`:** Cruce de declaraciones juradas de funcionarios públicos para descartar o evidenciar conflictos de interés.
- **Plataformas de Transparencia Internacionales (México - Compranet / PNT):** Arquitectura modular pensada para admitir esquemas OCDS de México y otros países de la región.
