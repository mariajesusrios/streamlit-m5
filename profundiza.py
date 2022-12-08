import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt


names = "titanic.csv"
titanic_data = pd.read_csv(names)

st.header("Data Description")
st.dataframe(titanic_data)

fig, ax = plt.subplots()
ax.hist(titanic_data.Fare)
st.header("Histograma de Titanic")
st.pyplot(fig)
st.markdown("___")

fig2, ax2 = plt.subplots()
y_pos = titanic_data['Pclass']
x_pos = titanic_data['Fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')
st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)
st.markdown("___")


fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.Age, titanic_data.Fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)



















