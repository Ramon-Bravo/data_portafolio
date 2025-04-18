import streamlit as st
import pandas as pd
import joblib  # o pickle
import numpy as np

# Carga del modelo entrenado (asegúrate de haberlo guardado antes)
pipeline = joblib.load('pipeline_lgbm_tuned.pkl')

# Título de la app
st.title("🚗 Predicción de Precio de Vehículos Usados")
st.write("Completa los campos y obtén el precio estimado de tu coche.")

# Entradas del usuario
brand = st.selectbox(
    "Marca", ['volkswagen', 'bmw', 'audi', 'mercedes_benz', 'ford'])
model = st.selectbox(
    "Modelo", ['golf', '3er', 'a4', 'c_klasse', 'focus', 'unknown_model'])
vehicle_type = st.selectbox(
    "Tipo de Vehículo", ['sedan', 'small', 'wagon', 'suv', 'unknown_type'])
gearbox = st.selectbox("Transmisión", ['manual', 'auto'])
fuel_type = st.selectbox("Combustible", ['petrol', 'diesel', 'lpg'])
not_repaired = st.selectbox("¿Tiene daños sin reparar?", [
                            'no', 'yes', 'unknown_repair'])

registration_year = st.slider("Año de registro", 1950, 2022, 2015)
mileage = st.slider("Kilometraje (en km)", 0, 300000, 100000, step=1000)
power = st.slider("Potencia (HP)", 30, 500, 120)

# Botón de predicción
if st.button("📈 Predecir Precio"):
    # Crear DataFrame con los inputs
    input_data = pd.DataFrame([{
        'Brand': brand,
        'Model': model,
        'VehicleType': vehicle_type,
        'Gearbox': gearbox,
        'FuelType': fuel_type,
        'NotRepaired': not_repaired,
        'RegistrationYear': registration_year,
        'Mileage': mileage,
        'Power': power
    }])

    # Realizar predicción
    pred_price = pipeline.predict(input_data)[0]

    # Mostrar resultado
    st.success(f"💰 Precio estimado: €{pred_price:,.2f}")
