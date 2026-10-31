# Media Party BA 2026 — Estrategia, Ideas y Playbook para Ganar

> Documento estratégico para abordar la Hackatón de Media Party Buenos Aires 2026 con un enfoque ganador, técnicamente sólido y alineado con los criterios del jurado internacional y el Investment Club.

---

## 1. Radiografía del Jurado y Qué Están Buscando

El panel evaluador reúne tres mundos clave:
1. **Prensa y Periodismo de Investigación:** *The Guardian*, *Pulitzer Center*, *Fund.ar*.
   - *Qué buscan:* Trazabilidad absoluta de fuentes, respeto al juicio editorial humano (*human-in-the-loop*), no alucinaciones, independencia periodística y combate a la desinformación.
2. **Plataformas de Innovación y Apoyo a Medios:** *Google News Initiative*, *IFPIM*, *Luminate*.
   - *Qué buscan:* Adopción tecnológica real, escalabilidad en redacciones chicas y medianas de Latinoamérica, estándares abiertos, infraestructura cívica.
3. **Inversionistas y Fondos de Impacto:** *MDIF* (Media Development Investment Fund), *North Base Media*.
   - *Qué buscan:* Un modelo de negocio creíble (*unit economics*, B2B SaaS, licencias de código abierto con soporte corporativo, modelo de suscripción) y potencial para ingresar al **Media Party Investment Club**.

---

## 2. Lecciones de los Ganadores de NY y Barcelona (2026)

| Sede | Ganador | Por qué ganó | Clave para replicar |
| :--- | :--- | :--- | :--- |
| **Nueva York** (Brown Institute) | **Citizen Journalism Network (CJN)** | Agrupó reportes ciudadanos locales en tiempo real con IA para dar contexto a periodistas de redacciones comunitarias. | **Resolvió un dolor de cobertura hiperlocal** y conectó a la comunidad con los periodistas. |
| **Barcelona** (BIT Habitat / Cloudflare) | **AIdas (AI Drift & Alignment Scanner)** | Auditó sesgos ideológicos comparando respuestas de múltiples LLMs sobre noticias polémicas. | **Enfocado en auditoría de IA y transparencia algorítmica** (muy valorado por investigadores y reguladores). |

---

## 3. Matriz de los 4 Criterios Oficiales de Evaluación

Para maximizar la puntuación, el proyecto debe marcar "Check" en estos 4 casilleros:

```
┌────────────────────────────────────────────────────────────────────────┐
│                          CRITERIOS OFICIALES                           │
├──────────────────────────┬─────────────────────────────────────────────┤
│ 1. Calidad Técnica       │ Arquitectura multi-agente real (orquestación│
│                          │ con herramientas, recuperación y memoria). │
├──────────────────────────┼─────────────────────────────────────────────┤
│ 2. Innovación Narrativa  │ No es un simple dashboard: crea una nueva   │
│                          │ forma de interactuar con la información.    │
├──────────────────────────┼─────────────────────────────────────────────┤
│ 3. Trazabilidad/Integridad│ Cada dato generado tiene un link/fragmento │
│                          │ verificable a la fuente primaria original. │
├──────────────────────────┼─────────────────────────────────────────────┤
│ 4. Viabilidad Comercial  │ Pricing claro (B2B SaaS / Managed Open Core)│
│                          │ y target de clientes definido.              │
└──────────────────────────┴─────────────────────────────────────────────┘
```

---

## 4. Banco de Ideas de Alto Impacto para Prototipar

A continuación se presentan 4 ideas diseñadas para construirse en una jornada de 6 horas:

### Idea 1: «AuditaNews» — Agente Auditor de Atribución y Alucinaciones en Redacciones
- **Track:** Track 2 (Herramientas B2B de Integridad) / Track 1 (SaaS).
- **El Dolor:** Los periodistas usan LLMs para redactar borradores o resumir informes extensos, arriesgándose a publicar datos alucinados o citas tergiversadas.
- **La Solución Agéntica:**
  - El periodista ingresa el borrador de su nota junto con los documentos fuente (PDFs, transcripciones, notas de prensa).
  - Un equipo de agentes realiza una auditoría cruzada:
    1. **Extractor Agent:** Identifica cada afirmación factual, cifra y cita textual.
    2. **Fact-Matcher Agent:** Busca la evidencia exacta en los documentos fuente.
    3. **Integrity Scorer:** Genera un mapa de calor tipo "semáforo" (Verde = respaldado con cita exacta; Amarillo = inferencia ambigua; Rojo = sin evidencia / posible alucinación).
- **Human-in-the-loop:** El periodista hace clic en la frase dudosa y ve el fragmento exacto del documento original para aprobar o corregir.
- **Monetización:** SaaS B2B para redacciones con cobro por número de periodistas o volumen de artículos auditados.

---

### Idea 2: «DeepStory / Hablá con la Investigación» — Agente Conversacional Interactivo para Lectores
- **Track:** Track 4 (Monetización Comunitaria) / Innovación Narrativa.
- **El Dolor:** Las grandes investigaciones periodísticas (Pandora Papers, causas judiciales, presupuestos) son documentos de 50 páginas que muy poca gente lee completa, perdiendo impacto y monetización de audiencia.
- **La Solución Agéntica:**
  - Widget interactivo embebible en la web del medio donde los lectores pueden "conversar" con la investigación.
  - El agente está restringido estrictamente al corpus de la investigación con citas a pie de página navegables.
  - El agente propone preguntas críticas sugeridas según el perfil del lector (ej. "¿Cómo afecta esta licitación a mi barrio?", "¿Quiénes fueron los testaferros identificados?").
  - Módulo de voz (Text-to-Speech) para escuchar resúmenes ejecutivos en audio interactivo.
- **Monetización:** Funcionalidad exclusiva para suscriptores / miembros de pago del medio (mecanismo directo de fidelización y conversión de suscriptores).

---

### Idea 3: «RadarLicitaciones AI» — Agente Detector de Carteles y Anomalías en Compras Públicas
- **Track:** Track 2 (Integridad) / Track 3 (Open Core).
- **El Dolor:** Las contrataciones públicas en América Latina publican miles de pliegos en PDFs escaneados donde se esconden sobreprecios y licitaciones arregladas que los periodistas locales no llegan a revisar a tiempo.
- **La Solución Agéntica:**
  - Pipeline de agentes que:
    1. Descarga boletines y pliegos oficiales.
    2. Extrae tablas de ítems, montos, plazos y oferentes.
    3. Cruza CUITs/RFCs de las empresas para detectar si comparten socios, direcciones fiscales o apoderados.
    4. Emite alertas automatizadas en Slack/Discord/Email a la redacción cuando una licitación tiene un solo oferente o plazos sospechosamente cortos (menos de 48 hs).
- **Monetización:** Suscripción mensual para redacciones regionales, observatorios cívicos y ONGs de transparencia.

---

### Idea 4: «OmniPress / StoryMorph» — Agente de Adaptación Narrativa Multi-Formato
- **Track:** Track 1 (SaaS para Redacciones).
- **El Dolor:** Una redacción produce una nota de investigación profunda, pero adaptarla a formatos de alto impacto (hilo interactivo en X/Bluesky, guión de TikTok/Reels, carrusel de Instagram, newsletter de audio) insume 4 horas por nota a un equipo desgastado.
- **La Solución Agéntica:**
  - Agente que ingiere la investigación y genera automáticamente:
    1. Guión audiovisual con *prompts* de video/imágenes contextuales.
    2. Hilo periodístico con citas y capturas de pantalla de documentos adjuntos.
    3. Preguntas de debate para la comunidad.
  - Todas las adaptaciones mantienen la fidelidad al estilo editorial y las pautas éticas del medio mediante un archivo de configuración (*Editorial Guidelines*).
- **Monetización:** SaaS B2B con planes escalonados según volumen de notas transformadas.

---

## 5. Arquitectura Técnica Sugerida para Prototipar en 6 Horas

Para terminar un prototipo funcional antes de las 17:00 hs:

```
  ┌────────────────────────────────────────────────────────┐
  │                 INTERFAZ DE USUARIO                     │
  │     Streamlit / Next.js / Gradio / Tailwind UI         │
  └───────────────────────────┬────────────────────────────┘
                              │
  ┌───────────────────────────▼────────────────────────────┐
  │                 ORQUESTADOR AGÉNTICO                   │
  │      LangGraph / Python tool-loop / n8n workflows      │
  ├───────────────────────────┬────────────────────────────┤
  │   1. Agente Investigador  │  2. Agente Auditor / Citas │
  │      (Retrieval / OCR)    │     (Fact-Checking)        │
  └───────────────────────────┬────────────────────────────┘
                              │
  ┌───────────────────────────▼────────────────────────────┐
  │             MODELOS & REPOSITORIO DE DATOS             │
  │     LLMs Rápidos (Gemini Flash / Claude / Groq)        │
  │     Vector DB liviana: Chroma / SQLite / In-Memory     │
  └────────────────────────────────────────────────────────┘
```

### Tips de Aceleración:
- **Priorizar velocidad de inferencia:** Usar modelos rápidos (como Gemini 1.5 Flash o Groq Llama-3) para que la demo en vivo no tarde más de 3 segundos en responder ante el jurado.
- **Tener un dataset "mock" o real preparado:** Si la red wifi del Konex se satura o una API externa falla, contar con 3 expedientes/artículos precargados en local para la demo.
- **Evitar sobre-ingeniería:** Mejor un flujo de 2 agentes que funcione impecable de punta a punta, que un sistema complejo de 8 agentes que tire error en la presentación final.

---

## 6. La Fórmula del Pitch Final (3 Minutos)

En la Etapa 03 de presentación, el tiempo suele ser muy estricto (3 minutos + 1 de preguntas). Estructura recomendada:

1. **El Gancho y el Problema (0:00 - 0:35):**
   - *"Hoy las redacciones enfrentan una paradoja: mientras la IA genera contenido a escala masiva, la confianza del público en las noticias está en su mínimo histórico. ¿Cómo usamos agentes de IA sin perder la verdad periodística?"*
2. **La Solución y Demo en Vivo (0:35 - 1:50):**
   - Mostrar la pantalla, cargar un documento real, presionar el botón y mostrar cómo los agentes trabajan en tiempo real.
   - Resaltar la trazabilidad: *"Miren cómo el agente resalta este dato y nos muestra la página exacta del informe original de donde salió."*
3. **El Enfoque Human-in-the-Loop y Modelo de Negocio (1:50 - 2:30):**
   - *"La máquina encuentra y propone, el periodista o editor aprueba y decide."*
   - *"Nuestro modelo es un SaaS B2B con un costo de $49/mes por redacción local, accesible para medios independientes pero escalable internacionalmente."*
4. **Cierre y Escalabilidad / Investment Club (2:30 - 3:00):**
   - *"Desarrollamos el núcleo hoy en código abierto bajo licencia MIT, y estamos listos para iniciar pruebas de concepto (POC) en redacciones durante el próximo mes y postular al Media Party Investment Club."*
