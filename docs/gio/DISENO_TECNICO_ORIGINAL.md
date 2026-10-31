# Rastro

Prototipo para la hackatón de Media Party Buenos Aires 2026 ("Storytelling en la era de los agentes").
Se construye desde cero el sábado 31 de octubre de 2026. La demo final es a las ~17:30.

## Qué hace

Rastro lee contratos de obra pública municipal (PDF o Excel), detecta banderas rojas con reglas
explícitas y pasa cada hallazgo a un periodista antes de publicar. Lo aprobado se convierte en una
ficha visual y una entrada periodística.

Principio rector: **la IA lee y redacta; las reglas detectan; el humano decide.**

## Flujo (cuatro etapas)

1. **Lector** (`rastro/lector.py`): convierte documentos en una tabla con una fila por propuesta:
   `procedimiento_id, tipo_procedimiento, objeto, fecha_convocatoria, fecha_apertura, fecha_fallo,
   empresa, rfc, domicilio_fiscal, monto_propuesta, ganador (bool), monto_contrato,
   documentos_presentes, fuente_archivo, fuente_pagina`.
   - Excel/CSV: lectura directa con pandas.
   - PDF: extraer texto con pdfplumber; si hace falta, usar la API de Claude para estructurar.
     Cada dato extraído conserva `fuente_archivo` y `fuente_pagina`.
2. **Cruzador** (`rastro/reglas.py`): funciones puras y deterministas, sin IA. Cada regla devuelve
   banderas con: `regla_id, nombre, procedimientos, empresas, explicacion, evidencia` (lista de
   archivo + página + dato). Reglas iniciales, inspiradas en la guía de banderas rojas de Open
   Contracting Partnership:
   - R1 Trío recurrente: el mismo conjunto de licitantes aparece en 2 o más procedimientos.
   - R2 Domicilio compartido: dos o más licitantes del mismo procedimiento con igual domicilio fiscal (normalizar texto).
   - R3 Propuestas espejo: diferencia menor a 3 % entre propuestas del mismo procedimiento.
   - R4 Ganador rotativo: dentro de un grupo recurrente, el ganador se alterna.
   - R5 Posible fraccionamiento: mismo proveedor, objeto similar, fechas cercanas (30 días).
   - R6 Documentación faltante: procedimiento sin acta de fallo o sin junta de aclaraciones.
   - R7 Plazo corto: menos de N días entre convocatoria y apertura (N configurable).
   Umbrales en `config.yaml`.
3. **Puerta humana** (app): cada bandera se muestra con su evidencia y botones Aprobar / Descartar /
   Pendiente, con campo de nota. Las decisiones se guardan en `salidas/decisiones.json`.
   Nada pasa a la etapa 4 sin aprobación.
4. **Narrador** (`rastro/narrador.py`): solo para banderas aprobadas, genera con la API de Claude:
   una ficha (título, dato clave, evidencia citada), una entrada periodística y preguntas para
   derecho de réplica y solicitudes de transparencia.
   Estilo: directo, objetivo, párrafos cortos, lo más relevante primero, sin adjetivos innecesarios,
   sin afirmar delitos: hablar de "patrones" e "indicios", nunca de culpables.

Extra para la demo: grafo empresa–domicilio–procedimiento con networkx + pyvis.

## Stack

- Python 3.11+, pandas, pdfplumber, networkx, pyvis, pyyaml, anthropic, streamlit.
- Interfaz en Streamlit (`app.py`), en español.
- Clave de API en variable de entorno `ANTHROPIC_API_KEY` (archivo `.env`, nunca en el repo).

## Reglas de trabajo

- Construir por etapas y probar cada una con los datos de `datos/` antes de seguir.
- Las reglas deben ser explicables: cada bandera dice qué regla la disparó y con qué datos.
- **Modo demo**: si no hay clave de API o falla la red, la app carga resultados precalculados de
  `salidas/demo/`. La demo nunca debe depender de internet.
- **Anonimización**: opción `anonimizar: true` en `config.yaml` que reemplaza nombres de empresas,
  RFC y domicilios por "Empresa A", "Domicilio 1", etc. Activada por defecto para la presentación
  pública.
- No inventar datos. Si un campo no está en el documento, queda vacío.
- Código simple y legible; es un prototipo de un día.
