# 🚗 Predicción de Precios de Autos Usados

Este proyecto tiene como objetivo construir modelos de regresión para predecir el precio de autos en el mercado de segunda mano, optimizando precisión, velocidad de predicción y tiempo de entrenamiento.

## 🧠 Objetivo
- Evaluar distintos modelos de regresión.
- Comparar rendimiento en precisión y velocidad.
- Implementar soluciones optimizadas como LightGBM.

## 🛠️ Tecnologías utilizadas
- Python
- pandas, numpy, seaborn, matplotlib, sklearn, joblib, lightgbm

## 📊 Dataset
- [`car_data.csv.gz`](https://github.com/Ramon-Bravo/datasets_publicos/blob/main/car_data.csv.gz)  
  *(Accedido desde el repositorio [`datasets_publicos`](https://github.com/Ramon-Bravo/datasets_publicos))*

## 🤖 Modelos utilizados
- Regresión Lineal
- Random Forest Regressor
- LGBM Regressor

## 📈 Resultados clave
- La Regresión Lineal fue rápida pero menos precisa.
- Random Forest obtuvo buenos resultados pero tardó hasta 20 minutos en entrenar.
- LGBM ofreció alta precisión y rapidez (menos de 10 segundos).

## 📁 Archivos clave
- `pipeline_lgbm_tuned.pkl`
- `app.py`

## 🧩 App o Demo
- ✅ Sí, archivo `app.py` compatible con Streamlit