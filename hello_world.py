import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as ptl

st.title('Maria Jesus Rios Blancas')
st.header("Información sobre el conjunto de datos")
st.header("Descripción de los datos")
st.write("""
Este es un simple ejemplo de una app para predecir

¡Esta app predice mis datos!
""")

sidebar = st.sidebar
sidebar.title("Esta es la barra lateral")
sidebar.write("Aquí van los elementos de entrada.")

# Botones de opciones
names = "titanic.csv"
titanic_data = pd.read_csv(names)

selected_class = st.radio("Select Class", titanic_data["Pclass"].unique())
st.write("Select Class:", selected_class)

# Casilla de verificacion
selected_sex = st.selectbox("Select Sex", titanic_data["Sex"].unique())
st.write(f"Selected Option: {selected_sex!r}")

# Controles deslizantes
optionals = st.expander("Optional Configurations", True)

fare_select = optionals.slider(
    "Select the Fare",
    min_value=float(titanic_data['Fare'].min()),
    max_value=float(titanic_data['Fare'].max())
)

subset_fare = titanic_data[(titanic_data['Fare'] >= fare_select)]

st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")


# mostrar la tabla
st. title("Streamlit con pandas")
st.dataframe(titanic_data)
























