# Proyecto: Regresión Lineal Múltiple con California Housing

Este proyecto aplica regresión lineal múltiple usando el dataset California Housing de scikit-learn.

## Objetivo

Predecir `MedHouseVal`, que representa el valor medio de la vivienda, usando varias variables predictoras:

- `MedInc`: ingreso medio de la zona
- `HouseAge`: edad media de las casas
- `AveRooms`: promedio de habitaciones
- `AveBedrms`: promedio de dormitorios
- `Population`: población de la zona
- `AveOccup`: ocupación promedio
- `Latitude`: latitud
- `Longitude`: longitud

## Estructura

```text
california_housing_regression/
│
├── src/
│   ├── __init__.py
│   ├── cargador_datos.py
│   ├── modelo.py
│   ├── evaluador.py
│   └── principal.py
│
├── requirements.txt
└── README.md
```

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

Desde la carpeta principal del proyecto:

```bash
python src/principal.py
```

## Métricas incluidas

El proyecto incluye las siguientes métricas de evaluación para regresión:

- `MSE`: error cuadrático medio.
- `RMSE`: raíz del error cuadrático medio.
- `MAE`: error absoluto medio.
- `R2`: coeficiente de determinación.

También se imprime una tabla con:

- valor real
- valor predicho
- error
- error absoluto
- error cuadrado

## Interpretación breve

El modelo busca los coeficientes que minimizan el error entre los valores reales y los valores predichos. Esto se hace usando regresión lineal múltiple, porque se usan varias variables independientes para predecir una variable dependiente.

Un modelo con menor RMSE y MAE comete errores promedio más pequeños. Un valor de R2 más cercano a 1 indica que el modelo explica mejor la variabilidad de la variable objetivo.
