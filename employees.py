import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import codecs
import seaborn as sns


DATE_COLUMN = 'released'
DATA_URL = ('Employees.csv')

st.title("Aplicación para deserción de empleados")
st.header("Descripción de los datos")
st.write("""
Este aplicativo del reto 5 tiene como objetivo realizar un análisis de 
fenómeno de la deserción laboral que afecta a las empresas y organizaciones
""")

@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_filme(filme):
    filtered_data_filme = data[data['Employee_ID'].str.upper().str.contains(filme)]
    return filtered_data_filme

def filter_data_by_director(director):
    filtered_data_director = data[data['Hometown'] == director]
    return filtered_data_director

def filter_data_by_director_(director2):
    filtered_data_director_ = data[data['Unit'] == director2]
    return filtered_data_director_

def filter_data_by_director_3(director3):
    filtered_data_director_3 = data[data['Education_Level'] == director3]
    return filtered_data_director_3


data_load_state = st.text('Loading cicle nyc data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

### Barra lateral
sidebar = st.sidebar
sidebar.title("Barra lateral")

#### Check box para mostrar dataframe (filtro de 500 renglones)
if sidebar.checkbox('Mostrar dataframe'):
    st.dataframe(data)

#### Buscadores

# ID del empleado:
titulofilme = st.sidebar.text_input('ID del empleado :')
btnBuscar = st.sidebar.button('Buscar ID')

if (btnBuscar):
   data_filme = filter_data_by_filme(titulofilme.upper())
   count_row = data_filme.shape[0]  # Gives number of rows
   st.write(f"Total ID de empleados mostrados  : {count_row}")
   st.write(data_filme)

# Hometown
selected_director = st.sidebar.selectbox("Seleccionar Hometown", data['Hometown'].unique())
btnFilterbyDirector = st.sidebar.button('Filtrar Hometown ')

if (btnFilterbyDirector):
   filterbydir = filter_data_by_director(selected_director)
   count_row = filterbydir.shape[0]  # Gives number of rows
   st.write(f"Total de Hometown : {count_row}")

   st.dataframe(filterbydir)

# Unit
selected_director_ = st.sidebar.selectbox("Seleccionar Unit", data['Unit'].unique())
btnFilterbyDirector_ = st.sidebar.button('Filtrar Unit ')

if (btnFilterbyDirector_):
   filterbydir_ = filter_data_by_director_(selected_director_)
   count_row = filterbydir_.shape[0]  # Gives number of rows
   st.write(f"Total Unit : {count_row}")

   st.dataframe(filterbydir_)

### Filtrar por nivel educativo
selected_director_3 = st.sidebar.selectbox("Seleccionar nivel educativo", data['Education_Level'].unique())
btnFilterbyDirector_3 = st.sidebar.button('Filtrar nivel ')

if (btnFilterbyDirector_3):
   filterbydir_3 = filter_data_by_director_3(selected_director_3)
   count_row = filterbydir_3.shape[0]  # Gives number of rows
   st.write(f"Total del nivel educativo : {count_row}")

   st.dataframe(filterbydir_3)

# Histograma de los empleados agrupados por edad
st.markdown("___")

DATE_COLUMN = 'Age'
if st.sidebar.checkbox('Histograma de la edad'):
    st.subheader('Histograma de la edad del empleado')

    fig, ax = plt.subplots()
    ax.hist(data[DATE_COLUMN])
    st.pyplot(fig)

# Gráfica de frecuencia de Unit
st.markdown("___")
if st.sidebar.checkbox("Frecuencia de Unit"):
    st.subheader("Gráfica de frecuencia de Unit")

    val_count = data[["Unit"]].value_counts()
    x = ["IT", "Logistics", "Sales", "Operarions", "Accounting and Finance", "Purchasing", "R&D", "Human Resource Management", "Marketing", "Quality", "Production", "Security"] 
    y = [104, 79, 65, 53, 45, 36, 34, 22, 19, 16, 14, 13]

    fig2, ax2 = plt.subplots()
    ax2.barh(x, y)
    ax2.set_ylabel("Units")
    ax2.set_xlabel("Frecuencia")
    st.pyplot(fig2)

# Visualizar ciudades con mayor índice de deserción
st.markdown("___")
df = data[["Attrition_rate", "Hometown"]]
employees_by_hometown = data.groupby("Hometown").mean()

if st.sidebar.checkbox("Ciudades VS Índice de deserción"):
    st.subheader("Gráfica de ciudades VS Índice de deserción")
    st.text("La ciudad con mayor Índice de deserción fue Clinton")

    employees_by_hometown = data.groupby("Hometown").mean()
    #t.dataframe(employees_by_hometown)

    x = ["Clinton", "Franklin", "Lebanon", "Springfield", "Washington"] 
    y = [0.203295555555555, 0.186783050847457, 0.193160606060606, 0.175687022900763, 0.196816216216216]

    fig3, ax3 = plt.subplots()
    ax3.barh(x, y)
    ax3.set_ylabel("Hometown")
    ax3.set_xlabel("Promedio de la tasa de deserción")
    st.pyplot(fig3)

# Visualizar edad con índice de deserción
st.markdown("___")
if st.sidebar.checkbox("Edad VS Índice de deserción"):
    st.subheader("Gráfica de la Edad VS Índice de deserción")
    st.text("No se observa una asociación entre la edad y el índice de deserción")

    fig4, ax4 = plt.subplots()
    ax4.scatter(data.Age, data.Attrition_rate)
    ax4.set_xlabel("Edad")
    ax4.set_ylabel("Índice de deserción")
    st.pyplot(fig4)

# Visualizar edad con índice de deserción
st.markdown("___")
if st.sidebar.checkbox("Tiempo de servicio VS Índice de deserción"):
    st.subheader("Gráfica del tiempo de servicio VS Índice de deserción")
    st.text("No se observa una asociación entre el tiempo de servicios y el índice de deserción")

    fig5, ax5 = plt.subplots()
    ax5.scatter(data.Time_of_service, data.Attrition_rate)
    ax5.set_xlabel("Tiempo de servicio")
    ax5.set_ylabel("Índice de deserción")
    st.pyplot(fig5)

















