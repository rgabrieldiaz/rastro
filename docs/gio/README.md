# Rastro — trabajo editorial y de producto

Material producido por Giovanny Flores (periodista de datos, Criterio Hidalgo, México) durante la
hackatón de Media Party Buenos Aires 2026, el 31 de octubre de 2026. Complementa el código de Gabo.

**Autoría:** la idea, la metodología de banderas rojas y el caso de origen (Hidalgo) son de
Giovanny Flores. El desarrollo técnico es de Gabo. Rastro es un proyecto conjunto.

## Contenido de esta carpeta

| Archivo | Qué es |
|---|---|
| `README.md` | Este resumen: propuesta, principio, reglas, modelo, riesgos, equipo y hoja de ruta |
| `PITCH.md` | Guiones del pitch (30 segundos, 1 minuto y estructura del pitch final) |
| `MEXICO_PNT.md` | Cómo aplicar Rastro a la Plataforma Nacional de Transparencia de México |
| `DISENO_TECNICO_ORIGINAL.md` | Especificación técnica original del flujo en cuatro etapas y las reglas R1–R7 |

Las presentaciones están en `/deck` y las capturas del prototipo en `/docs/demo`.

---

## La propuesta

**Problema.** Los contratos públicos son públicos, pero casi nadie puede leerlos. En México, los
contratos de obra pública municipal no se publican como datos abiertos; la plataforma federal de
compras (ComprasMX) no cubre municipios, y lo que existe son PDF y tablas dispersas en portales de
transparencia.

**Origen.** Giovanny revisó a mano 22 contratos de obra pública de un municipio de Hidalgo y encontró
a los mismos licitantes compitiendo una y otra vez, algunos con el mismo domicilio fiscal. Le tomó
semanas. Rastro hace ese cruce en minutos.

**Solución.** Rastro lee contratos, detecta banderas rojas con reglas explícitas y pasa cada hallazgo
a un periodista antes de publicar. Lo aprobado se convierte en una ficha y en preguntas para derecho
de réplica y solicitudes de acceso a la información.

## Principio rector

> La IA lee y redacta. Las reglas detectan. El periodista decide.

Rastro no acusa a nadie: muestra indicios en datos públicos. Las fichas solo se generan después de una
verificación humana.

## Flujo en cuatro etapas

1. **Lector:** convierte PDF o Excel en una tabla; cada dato conserva su archivo y su página de origen.
2. **Cruzador:** reglas fijas, deterministas y auditables, sin IA.
3. **Puerta humana:** cada bandera llega con su evidencia; el periodista aprueba, descarta o deja
   pendiente, con una nota.
4. **Narrador:** solo con lo aprobado, redacta ficha, entrada y preguntas de réplica y transparencia.

## Reglas (inspiradas en la guía de banderas rojas de Open Contracting Partnership)

| Código | Regla |
|---|---|
| R1 | Trío recurrente: el mismo conjunto de licitantes en 2 o más procedimientos |
| R2 | Domicilio fiscal compartido entre licitantes del mismo procedimiento |
| R3 | Propuestas espejo: diferencia menor a 3 % entre propuestas |
| R4 | Ganador rotativo dentro de un grupo recurrente |
| R5 | Posible fraccionamiento: mismo proveedor, objeto similar, fechas cercanas |
| R6 | Documentación faltante (acta de fallo, junta de aclaraciones) |
| R7 | Plazo corto entre convocatoria y apertura |

Referencias: guía *Red Flags in Public Procurement* (Open Contracting Partnership, 2024) y la
librería abierta Cardinal, que calcula indicadores sobre datos en estándar OCDS.

## Modelo: abierto, gratuito y de código abierto

| Nivel | Quién | Qué puede hacer |
|---|---|---|
| Abierto | Cualquier persona | Consultar contratos y ver indicios con su regla y su documento |
| Verificación | Periodistas, OSC y comunidad acreditada | Aprobar o descartar indicios y generar fichas |
| Institucional | Medios, OSC, órganos de control | Monitoreo, alertas y API (de pago) |

Sostenibilidad: fondos y donaciones, servicios institucionales y membresías comunitarias
("adopta un municipio"). Los indicios son públicos; las historias solo salen con verificación humana.

## Riesgos y mitigaciones

- **Falsos positivos y difamación:** lenguaje de "indicio, no prueba"; regla y evidencia visibles;
  canal de réplica para las empresas señaladas.
- **Uso malicioso:** los documentos que suben usuarios quedan "sin verificar" hasta confirmar su origen
  oficial; reglas públicas y registro de quién aprobó cada hallazgo.
- **Datos personales:** solo se muestran personas morales y servidores públicos en funciones; los datos
  de personas físicas se ocultan.
- **Anonimización** en demos y presentaciones públicas.

## Equipo y roles

| Rol | Responsable de |
|---|---|
| Líder editorial (Giovanny) | Qué es bandera y qué no, verificación, puerta humana, anonimización, pitch |
| Desarrollo (Gabo) | Lector, reglas, conexión a datos (OpenARG), app |
| Interfaz | App en Streamlit y versión web |
| Diseño | Fichas visuales, grafo, presentación |
| Negocio y pitch | Modelo, guion y cronometraje |

Regla de trabajo: lo editorial lo decide el periodista; lo técnico, quien construye.

## Hoja de ruta

- **Hoy:** prototipo con datos de compras de la Ciudad de Buenos Aires (OpenARG), puerta humana,
  copiloto que se bloquea sin verificación y modo cívico. Casos ilustrativos y anonimizados.
- **30 días:** medir el lector contra los 22 contratos revisados a mano; municipio piloto; asesoría legal.
- **6 semanas:** lectura automática de portales y PDF (con OCR), base de datos, mapa de redes de
  licitantes y registro auditable de cada paso, todo con herramientas de código abierto.
- **3 meses:** de 3 a 5 municipios de Hidalgo vía la PNT; medios aliados como verificadores; primeras
  fichas publicadas con réplica.
- **6 a 12 meses:** más estados y provincias; alertas y API.
