# 5 Ideas Ganadoras con OpenARG + Flujos Agénticos
### Hackatón Media Party Buenos Aires 2026 — «Storytelling en la Era de los Agentes»

Este documento presenta 5 propuestas de alto impacto diseñadas específicamente para el jurado internacional (The Guardian, Pulitzer Center, Fund.ar, Google News Initiative, IFPIM, MDIF), basadas en **agentes de IA autónomos que consumen el catálogo de datos públicos de OpenARG (+33.000 datasets oficiales de Argentina)** mediante el protocolo MCP.

---

## 📐 Marco de Puntuación (50 Puntos Totales)

Cada idea es evaluada en 5 dimensiones (1 a 10 pts cada una):
1. **Calidad Técnica & Flujo Agéntico:** Complejidad y solidez del sistema multi-agente, uso de herramientas MCP, y factibilidad de tener un MVP funcionando en 6 horas.
2. **Innovación Narrativa & Storytelling:** Qué tanto revoluciona la experiencia informativa frente a notas tradicionales o dashboards estáticos.
3. **Trazabilidad, Rigor e Integridad:** Respaldo empírico irrefutable con datasets de OpenARG y mitigación de alucinaciones (*human-in-the-loop*).
4. **Viabilidad Comercial & Modelo de Negocio:** Potencial de venta B2B SaaS, modelo Open Core o suscripción para el *Media Party Investment Club*.
5. **Impacto en Demo en Vivo (Pitch Factor):** Claridad, rapidez y efecto "wow" en la presentación de 3 minutos ante el jurado.

---

## 💡 Idea 1: «Veedor Cívico — Auditor Agéntico de Patrimonio y Contratos»
> **Track:** Track 2 (Herramientas B2B de Integridad y Trazabilidad)  
> **Lema:** *"La máquina detecta inconsistencias patrimoniales en segundos, el periodista investiga la historia."*

### 1. El Problema Real
Las redacciones de investigación tardan semanas en cruzar las declaraciones juradas de funcionarios con los proveedores que ganan licitaciones públicas. Muchos conflictos de interés o saltos patrimoniales quedan impunes porque la información está dispersa en miles de registros públicos.

### 2. Cómo usa OpenARG (Respaldo Empírico)
- **Declaraciones Juradas Patrimoniales:** `raw.cache_ddjj_declaraciones` (727.999 declaraciones de la Oficina Anticorrupción y CABA) y `raw.cache_ddjj_deudas` (683.870 registros de acreedores).
- **Contrataciones Públicas:** `raw.bac__buenos_aires_compras_contracts__45b499b0__v2` (500.000 contratos de compras públicas con montos y proveedores) y `raw.caba__buenos_aires_compras__d09720af__v2`.

### 3. Arquitectura Multi-Agente
```
[Periodista ingresa nombre de funcionario o empresa]
                       │
                       ▼
            ┌──────────────────────┐
            │   Orquestador Lead   │
            └──────────┬───────────┘
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
┌──────────────────┐       ┌──────────────────┐
│  Agente DDJJ     │       │  Agente Compras  │
│ (Invoca OpenARG  │       │ (Invoca OpenARG  │
│  cache_ddjj)     │       │  bac_contracts)  │
└────────┬─────────┘       └─────────┬────────┘
         │                           │
         └─────────────┬─────────────┘
                       ▼
            ┌──────────────────────┐
            │ Agente Cruzador OSINT│ ──► Detecta alertas: saltos patrimoniales,
            └──────────┬───────────┘     adjudicaciones a familiares o socios.
                       ▼
            ┌──────────────────────┐
            │  Agente Narrador con │ ──► Redacta memo confidencial con links
            │   Citas y Evidencia  │     y fragmentos oficiales verificables.
            └──────────────────────┘
```

### 4. Human-in-the-Loop
El sistema nunca publica de forma autónoma. Entrega una *"Ficha de Evidencia"* con semáforo de riesgo y los links oficiales de descarga en OpenARG para que el periodista humano verifique antes de publicar.

### 5. Puntuación Detallada
- **Calidad Técnica & Flujo Agéntico:** **9.0 / 10** (Orquestación elegante de 3 sub-agentes con llamadas MCP concretas a tablas existentes).
- **Innovación Narrativa:** **8.5 / 10** (Transforma bases de datos áridas en un expediente narrativo interactivo con línea de tiempo).
- **Trazabilidad e Integridad:** **10.0 / 10** (100% fuentes primarias oficiales de la Oficina Anticorrupción y BAC).
- **Viabilidad Comercial:** **9.5 / 10** (SaaS B2B perfecto para redacciones de investigación, ONGs de transparencia y áreas de compliance).
- **Efecto Demo en Vivo:** **9.5 / 10** (Buscar a un funcionario conocido y ver cómo el agente dibuja su evolución patrimonial y contratos en 3 segundos deja mudo al jurado).
- **PUNTAJE TOTAL: 46.5 / 50**

---

## 💡 Idea 2: «PautaScope — Monitor Agéntico de Pauta Oficial y Dependencia Mediática»
> **Track:** Track 1 (SaaS para Redacciones) & Track 2 (Integridad)  
> **Lema:** *"Transparencia radical en el financiamiento público de medios de comunicación."*

### 1. El Problema Real
La asignación discrecional o corte abrupto de la pauta publicitaria oficial es una de las mayores presiones sobre la independencia de los medios en América Latina. No existe una herramienta que procese las decenas de miles de órdenes de compra del Estado para evidenciar patrones de concentración o discriminación publicitaria.

### 2. Cómo usa OpenARG
- **Publicidad Oficial:** `cache_datos_gob_ar_publicidad_oficial_rcf7a17be60` (+34.000 órdenes de pauta), `cache_datos_gob_ar_publicidad_oficial_r4424aecf65`, etc.
- **Presupuesto Ejecutado:** `raw.cache_presupuesto_credito_2026` (partidas de prensa y comunicación de Jefatura de Gabinete).

### 3. Arquitectura Multi-Agente
- **Agente Ingestor:** Escanea órdenes de pauta oficial y las agrupa por medio, proveedor y campaña.
- **Agente Analista de Concentración:** Calcula el índice Herfindahl-Hirschman (HHI) para medir si la pauta se está concentrando en 2 o 3 grupos económicos.
- **Agente Generador de Historias Visuales:** Redacta notas automatizadas con gráficos interactivos para que medios comunitarios puedan publicar cómo se reparte el presupuesto de su provincia o municipio.

### 4. Puntuación Detallada
- **Calidad Técnica & Flujo Agéntico:** **8.0 / 10** (Sólido, aunque depende de la actualización periódica de los datasets de pauta).
- **Innovación Narrativa:** **8.0 / 10** (Generación de gráficos y textos explicativos para audiencias).
- **Trazabilidad e Integridad:** **9.5 / 10** (Datos 100% de la Jefatura de Gabinete).
- **Viabilidad Comercial:** **7.5 / 10** (Muchos medios tradicionales prefieren no hablar de pauta; el mercado target son medios independientes y ONGs).
- **Efecto Demo en Vivo:** **8.5 / 10** (Visualmente muy potente, pero puede generar debate político espinoso durante el pitch).
- **PUNTAJE TOTAL: 41.5 / 50**

---

## 💡 Idea 3: «DataCheq Live — Fact-Checking Agéntico de Discursos en Tiempo Real»
> **Track:** Track 2 (Herramientas B2B de Integridad)  
> **Lema:** *"Del audio del político a la verificación con el dato oficial del INDEC o Presupuesto en 5 segundos."*

### 1. El Problema Real
Durante debates presidenciales, sesiones del Congreso o entrevistas en vivo, los políticos disparan decenas de cifras falsas o manipuladas ("la inflación bajó al mínimo histórico", "triplicamos las obras en educación"). Los chequeadores humanos tardan horas en desmentir, cuando la desinformación ya se viralizó.

### 2. Cómo usa OpenARG
- **Indicadores Económicos y Sociales:** `raw.cache_indec_eph_tasas_cuadro_3_1` (desempleo, ocupados demandantes), series de tiempo de inflación del INDEC.
- **Presupuesto Abierto:** `raw.cache_presupuesto_credito_2026` (crédito devengado y pagado en tiempo real).
- **Herramienta Natural:** `consultar_datos_publicos` y `agregar_datos` para contrastar cifras exactas al vuelo.

### 3. Arquitectura Multi-Agente
- **Speech/Text Claim Detector:** Extrae en vivo afirmaciones cuantitativas verificables de una transcripción o texto.
- **OpenARG Query Synthesizer:** Traduce la afirmación a la consulta precisa en las tablas de OpenARG.
- **Verdict & Evidence Judge:** Compara el valor dicho vs el valor registrado en la fuente oficial.
- **Fast-Card Formatter:** Genera una placa estilo "Verdadero / Engañoso / Falso" con el gráfico y link oficial a la fuente para tuitear o proyectar en la transmisión en vivo.

### 4. Puntuación Detallada
- **Calidad Técnica & Flujo Agéntico:** **9.5 / 10** (Pipeline de baja latencia con procesamiento de texto y llamadas dinámicas a MCP).
- **Innovación Narrativa:** **9.0 / 10** (Formato en vivo para streaming, canales de noticias y redes sociales).
- **Trazabilidad e Integridad:** **10.0 / 10** (La definición pura de fact-checking con fuente primaria).
- **Viabilidad Comercial:** **9.0 / 10** (SaaS de alto valor para canales de TV, radios y agencias de noticias en períodos electorales).
- **Efecto Demo en Vivo:** **9.5 / 10** (Reproducir un audio corto de un político, el agente lo escucha, consulta OpenARG y muestra el veredicto en la pantalla).
- **PUNTAJE TOTAL: 47.0 / 50**

---

## 💡 Idea 4: «Hablemos de Plata — Agente Narrativo del Presupuesto para el Ciudadano»
> **Track:** Track 4 (Monetización Comunitaria y Nuevas Audiencias)  
> **Lema:** *"Tu municipio y tu provincia gastaron millones: preguntale al agente a dónde fue a parar tu dinero."*

### 1. El Problema Real
El Presupuesto Nacional y los presupuestos provinciales son indescifrables para el 99% de los ciudadanos. La gente siente que paga impuestos y no sabe a dónde van, desconectándose de la política cívica. Los medios pierden lectores porque el periodismo de datos suele ser aburrido o árido.

### 2. Cómo usa OpenARG
- **Presupuesto Nacional 2026:** `raw.cache_presupuesto_credito_2026` (desagregado por jurisdicción, entidad, programa, finalidad y ubicación geográfica).
- **Presupuesto Ejecutado CABA:** `raw.caba__presupuesto_ejecutado__0737c310__v2` (48.514 filas de gastos detallados por comuna).
- **Gastos Municipales:** `raw.ciudad_mendoza__ejecucion_presupuestaria_de_gasto__16dcb3db__v5`, etc.

### 3. Arquitectura Multi-Agente
- **Agente de Localización & Empatía:** Identifica dónde vive el lector y qué temas le interesan (salud, escuelas, transporte, bacheo).
- **Agente Fiscal OpenARG:** Filtra y suma partidas presupuestarias por ubicación geográfica y función.
- **Agente de Metáforas & Storytelling:** Convierte cifras abstractas ($15.000 millones) en equivalencias tangibles (*"equivale a equipar 45 salas de primeros auxilios en tu barrio"*).
- **Interactive Story Builder:** Permite al lector hacer repreguntas por chat o voz (*"¿Y cuánto se gastó en publicidad en comparación con las escuelas de mi zona?"*).

### 4. Puntuación Detallada
- **Calidad Técnica & Flujo Agéntico:** **9.0 / 10** (Conversacional, usa `agregar_datos` de OpenARG para agrupar en servidor sin latencia).
- **Innovación Narrativa:** **10.0 / 10** (Cumple al 100% con la consigna de *Storytelling en la era de los agentes*).
- **Trazabilidad e Integridad:** **9.5 / 10** (Basado en partidas oficiales de Presupuesto Abierto).
- **Viabilidad Comercial:** **9.0 / 10** (Módulo embebible que los medios ofrecen como beneficio exclusivo para suscriptores pagos / miembros).
- **Efecto Demo en Vivo:** **9.0 / 10** (Demostración interactiva donde el jurado pide buscar su propia localidad y ve la respuesta adaptada).
- **PUNTAJE TOTAL: 46.5 / 50**

---

## 💡 Idea 5: «Lobo Parlamentario — Radar Agéntico de Leyes y Costo Fiscal»
> **Track:** Track 1 (SaaS para Redacciones) & Track 3 (Open Core)  
> **Lema:** *"La primera IA que audita qué leyes se debaten en el Congreso y cuánto le costarán al país."*

### 1. El Problema Real
En la Cámara de Diputados y el Senado se presentan cientos de proyectos de ley cada semana. Muchos proyectos demagógicos prometen beneficios o subsidios sin explicar de dónde saldrán los fondos, y las redacciones parlamentarias no dan abasto para analizar el impacto económico de cada expediente.

### 2. Cómo usa OpenARG
- **Proyectos Parlamentarios:** `raw.diputados__proyectos_parlamentarios__ecffe8be__v1` (111.091 expedientes con autores, comisiones y textos) y `raw.diputados__resultado_de_proyectos__bcefbbb8__v1`.
- **Leyes Sancionadas:** `raw.diputados__leyes_sancionadas__11b91158__v2`.
- **Presupuesto Vigente:** `raw.cache_presupuesto_credito_2026`.

### 3. Arquitectura Multi-Agente
- **Agente Parliamentary Crawler:** Detecta nuevos proyectos ingresados en comisiones clave (Presupuesto y Hacienda).
- **Agente Auditor Fiscal:** Lee los artículos del proyecto, detecta creaciones de partidas o exenciones impositivas y las contrasta con el presupuesto vigente en OpenARG.
- **Agente Briefing Generator:** Redacta una alerta matutina para periodistas políticos: *"Hoy entra en comisión el proyecto X de la diputada Y: costaría el 8% del presupuesto anual de Seguridad Social"*.

### 4. Puntuación Detallada
- **Calidad Técnica & Flujo Agéntico:** **8.5 / 10** (Parsing de texto de proyectos + cruce presupuestario con OpenARG).
- **Innovación Narrativa:** **8.0 / 10** (Formato de newsletter inteligente y asistente analítico).
- **Trazabilidad e Integridad:** **9.5 / 10** (Datos oficiales de la Cámara de Diputados de la Nación).
- **Viabilidad Comercial:** **8.5 / 10** (Excelente para consultoras de asuntos públicos, redacciones políticas y legisladores).
- **Efecto Demo en Vivo:** **8.5 / 10** (Muy serio e institucional, ideal para referentes como *Fund.ar*).
- **PUNTAJE TOTAL: 43.0 / 50**

---

## 📊 Matriz Comparativa y Veredicto Final

| Puesto | Idea | Calidad Técnica | Innovación Narrativa | Integridad | Viabilidad B2B | Pitch Demo | **Puntaje Total** | Track Recomendado |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 🥇 **1°** | **DataCheq Live** (Fact-Checking en Vivo) | 9.5 | 9.0 | 10.0 | 9.0 | 9.5 | **47.0 / 50** | **Track 2: Integridad B2B** |
| 🥈 **2°** | **Veedor Cívico** (Patrimonio DDJJ vs Contratos) | 9.0 | 8.5 | 10.0 | 9.5 | 9.5 | **46.5 / 50** | **Track 2: Integridad B2B** |
| 🥈 **2°** | **Hablemos de Plata** (Storytelling del Presupuesto) | 9.0 | 10.0 | 9.5 | 9.0 | 9.0 | **46.5 / 50** | **Track 4: Monetización Comunitaria** |
| 4° | **Lobo Parlamentario** (Radar de Leyes y Costo) | 8.5 | 8.0 | 9.5 | 8.5 | 8.5 | **43.0 / 50** | **Track 1: SaaS Redacciones** |
| 5° | **PautaScope** (Monitor de Pauta Publicitaria) | 8.0 | 8.0 | 9.5 | 7.5 | 8.5 | **41.5 / 50** | **Track 1: SaaS Redacciones** |

---

## 🏆 Veredicto Estratégico para Ganar Media Party 2026

Si el objetivo es **ganar la hackatón y conseguir mentoría/aceleración del Media Party Investment Club**, las dos opciones ganadoras son:

1. **La Opción Más Contundente: «DataCheq Live» (Puntaje: 47.0)**  
   - *Por qué:* El jurado (The Guardian, Pulitzer Center, Google News Initiative) prioriza la lucha contra la desinformación y el *human-in-the-loop*. La demo de escuchar una frase política y desmentirla con OpenARG en vivo en 3 segundos es imbatible visualmente.

2. **La Opción Más Periodística y de Investigación: «Veedor Cívico» (Puntaje: 46.5)**  
   - *Por qué:* Cruza las 720.000 declaraciones juradas con los 500.000 contratos de compras públicas. Toca una fibra neurálgica en Argentina y es un SaaS que cualquier redacción grande o chica querría pagar.

3. **La Opción de Mayor Innovación Narrativa: «Hablemos de Plata» (Puntaje: 46.5)**  
   - *Por qué:* Encaja de forma literal en la consigna *"Storytelling en la era de los agentes"*, poniendo al lector en el centro mediante lenguaje natural y metáforas financieras comprensibles.
