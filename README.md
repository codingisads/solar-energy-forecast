# Solar Forecasting Cataluña ☀️

Proyecto de portfolio: predicción de energía solar generada/gestionable en el territorio catalán,
enfocado como si trabajaras en el equipo de datos de una empresa de energía solar que necesita
anticipar cuánta producción va a gestionar la red en los próximos días/horas.

Este repositorio es una **plantilla de workshop**: la estructura de carpetas y las pautas ya están
puestas, pero **todo el código lo escribes tú**. Sigue [`WORKSHOP_GUIDE.md`](./WORKSHOP_GUIDE.md)
fase por fase — ahí encontrarás preguntas guía, pistas y recomendaciones, nunca la solución.

## Cómo usar esto

1. Lee `WORKSHOP_GUIDE.md` completo una vez antes de escribir nada, para tener el mapa mental del proyecto.
2. Crea tu entorno virtual y anota en `requirements.txt` las librerías que vayas decidiendo usar
   (está pensado para que lo rellenes tú, no como lista cerrada).
3. Ve fase por fase. No hace falta que termines una fase "perfecta" antes de pasar a la siguiente —
   este tipo de proyectos son iterativos, ya volverás.
4. Documenta tus decisiones y hallazgos en `docs/notas_investigacion.md` y `reports/informe_final.md`
   a medida que avanzas, no al final. Te lo agradecerás cuando prepares el proyecto para tu portfolio.

## Estructura

```
solar-forecast-catalunya/
├── data/                  # Nunca se edita a mano lo de raw/. Cada subcarpeta = una etapa del dato
│   ├── raw/                # Datos tal cual los descargas, intocados
│   ├── interim/             # Datos a medio limpiar (checkpoints intermedios)
│   ├── processed/           # Datos ya listos para modelar
│   └── external/            # Datos auxiliares de terceros (ej. calendario festivos, geografía)
├── notebooks/              # Exploración y desarrollo, numerados en orden de ejecución
├── src/                    # Código reutilizable, una vez algo del notebook "funciona de verdad"
│   ├── data/                 # Ingesta y limpieza
│   ├── features/              # Construcción de variables
│   ├── models/                 # Entrenamiento, predicción, evaluación
│   └── visualization/           # Gráficos reutilizables
├── dashboard/               # App interactiva (Streamlit) para presentar el modelo
├── models/                  # Artefactos de modelos entrenados (no versionar los pesados en git)
├── reports/                 # Informe final + figuras exportadas
├── docs/                    # Tus notas de investigación propia
└── tests/                   # Alguna prueba mínima de tus funciones de src/
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` está deliberadamente casi vacío — la decisión de qué librerías necesitas
(y por qué) es parte del ejercicio. Ver pistas en `WORKSHOP_GUIDE.md`, fase 0.
