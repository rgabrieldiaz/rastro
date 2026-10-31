# Rastro en México: Plataforma Nacional de Transparencia (PNT)

## Por qué la PNT

- ComprasMX solo cubre compras federales. En la PNT, municipios, gobiernos estatales y organismos
  están obligados a publicar los resultados de sus contrataciones.
- Los datos vienen en formatos tabulares estandarizados: resultados de licitación pública e invitación
  a cuando menos tres personas, y resultados de adjudicación directa.
- Suelen incluir participantes, ganador, montos y fechas, lo que permite aplicar el trío recurrente
  (R1) y el domicilio compartido (R2).

## Cuidados

- Calidad desigual: campos vacíos y nombres escritos de distintas formas. Hay que normalizar nombres
  antes de cruzar.
- La reforma de 2025 cambió la ley de transparencia: la numeración de artículos y fracciones puede
  variar; conviene guiarse por el nombre del formato en la plataforma.
- Publicación trimestral: no es información en tiempo real.
- La plataforma bloquea consultas automáticas; para el prototipo, la vía es la descarga manual en Excel.

## Cómo integrarlo

1. En la consulta pública de la PNT, filtrar entidad, sujeto obligado y ejercicio, y descargar en Excel
   los formatos de licitaciones y adjudicaciones directas.
2. Convertir el archivo a la tabla del lector (una fila por propuesta).
3. Correr R1 y R2 y revisar los resultados con criterio periodístico.
4. Conectar la opción "México — Compranet / PNT" del menú de la app, con los datos anonimizados.
