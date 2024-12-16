import streamlit as st
import pandas as pd
from openpyxl import Workbook

# Función para guardar respuestas en Excel
def guardar_en_excel(respuestas, archivo="respuestas_negocios.xlsx"):
    try:
        # Cargar el archivo si existe, si no crear uno nuevo
        try:
            df_existente = pd.read_excel(archivo)
            df_actualizado = pd.concat([df_existente, respuestas], ignore_index=True)
        except FileNotFoundError:
            df_actualizado = respuestas
        
        # Guardar en Excel
        df_actualizado.to_excel(archivo, index=False)
        st.success(f"Respuestas guardadas exitosamente en {archivo}")
    except Exception as e:
        st.error(f"Error al guardar las respuestas: {e}")

# Título de la aplicación
st.title("Formulario de Negocios - Génesis Empresarial")

# Descripción inicial
st.write("Por favor, complete el formulario respondiendo las preguntas correspondientes al tipo de negocio seleccionado.")

# Primera pregunta: Selección del tipo de negocio
st.header("Pregunta 1: Tipo de Negocio")
negocios = [
    "Agricultura / Cultivo de Maíz",
    "Tienda",
    "Crianza de Animales",
    "Venta de Ropa",
    "Venta de Animales",
    "Cardamomo",
    "Venta de Ropa Típica",
    "Venta de Comida",
    "Crianza de Pollos",
    "Bordados y Guipiles"
]

negocio_seleccionado = st.selectbox(
    "Indique el tipo de negocio correspondiente según la clasificación utilizada en la base de datos de Génesis Empresarial:",
    negocios
)

# Mostrar la selección realizada
st.write(f"**Negocio seleccionado:** {negocio_seleccionado}")

# Variables para almacenar respuestas
respuestas = {}

# Lógica específica para "Crianza de Pollos"
if negocio_seleccionado == "Crianza de Pollos":
    st.info("Es importante separar negocios por subcategoría: crianza de pollos puede ser de 4 modelos básicos.")
    
    # Pregunta: ¿Cuál de estos elementos es el que más vende?
    producto_vendido = st.radio(
        "¿Cuál de estos elementos es el que más vende (en dinero)?",
        ["Pollos vivos", "Carne de pollo", "Huevos", "Otro derivado de pollo"]
    )
    respuestas["Negocio"] = negocio_seleccionado
    respuestas["Producto más vendido"] = producto_vendido
    
    # Preguntas adicionales según el producto seleccionado
    if producto_vendido == "Pollos vivos":
        precio_pollos = st.number_input("¿Cuál es el precio de los pollos vivos? (En quetzales)", min_value=0.0, step=1.0)
        cantidad_pollos = st.number_input("¿Cuántos pollos vivos vende al mes?", min_value=0, step=1)
        respuestas["Precio Pollos Vivos"] = precio_pollos
        respuestas["Cantidad Pollos Vivos"] = cantidad_pollos
    elif producto_vendido == "Carne de pollo":
        precio_carne = st.number_input("¿A cuánto vende la libra de carne de pollo actualmente? (En quetzales)", min_value=0.0, step=1.0)
        cantidad_carne = st.number_input("¿Cuántas libras de carne de pollo vende al mes?", min_value=0, step=1)
        respuestas["Precio Carne Pollo"] = precio_carne
        respuestas["Cantidad Carne Pollo"] = cantidad_carne
    elif producto_vendido == "Huevos":
        precio_huevos = st.number_input("¿A cuánto vende el cartón de 12 huevos? (En quetzales)", min_value=0.0, step=1.0)
        cantidad_huevos = st.number_input("¿Cuántos cartones de 12 huevos vende al mes?", min_value=0, step=1)
        respuestas["Precio Cartón Huevos"] = precio_huevos
        respuestas["Cantidad Cartones Huevos"] = cantidad_huevos
    elif producto_vendido == "Otro derivado de pollo":
        ventas_derivados = st.number_input("¿Cuánto vende en quetzales de sus productos?", min_value=0.0, step=1.0)
        respuestas["Ventas Derivados Pollo"] = ventas_derivados

# Botón para guardar las respuestas
if st.button("Guardar respuestas"):
    if "Negocio" in respuestas:
        df_respuestas = pd.DataFrame([respuestas])
        guardar_en_excel(df_respuestas)
    else:
        st.error("Por favor, responda todas las preguntas antes de guardar.")
