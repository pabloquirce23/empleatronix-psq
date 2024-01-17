import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('EMPLEATRONIX')
st.text("Todos los datos sobre los empleados en una aplicación")

file_path = 'csv/employees.csv'
df = pd.read_csv(file_path)
st.write(df)

st.divider()

col1, col2, col3 = st.columns([1, 1, 2]) # organiza los elementos horizontalmente

bar_color = col1.color_picker('Elige un color para las barras', '#3475B3') # sirve para cambiar el color de las barras

name_feature = col2.toggle('Mostrar el nombre') # sirve para mostrar o quitar el nombre de los empleados en la gráfica
salary_feature = col3.toggle('Mostrar sueldo en la barra') # sirve para mostrar o quitar el sueldo al lado de las barras en la gráfica

if (name_feature == True) and (salary_feature == True):
    plt.barh(df['full name'], df['salary'], color=bar_color)

    for index, value in enumerate(df['salary']):
        plt.text(value, index, str(value), ha='left', va='center')
    
    st.set_option('deprecation.showPyplotGlobalUse', False) # desactiva un warning de streamlit
    st.pyplot()
elif (name_feature == False) and (salary_feature == False):
    plt.barh(df['full name'], df['salary'], color=bar_color)

    plt.tick_params(axis='y', which='both', left=False, labelleft=False) # desactivar la visualización de ticks y etiquetas en el eje y

    st.set_option('deprecation.showPyplotGlobalUse', False) # desactiva un warning de streamlit
    st.pyplot()
elif (name_feature == True) and (salary_feature == False):
    plt.barh(df['full name'], df['salary'], color=bar_color)
    st.set_option('deprecation.showPyplotGlobalUse', False) # desactiva un warning de streamlit
    st.pyplot()
else:
    plt.barh(df['full name'], df['salary'], color=bar_color)

    plt.tick_params(axis='y', which='both', left=False, labelleft=False) # desactivar la visualización de ticks y etiquetas en el eje y

    for index, value in enumerate(df['salary']): # sirve para que aparezca el valor del sueldo al lado de las barras
        plt.text(value, index, str(value) + "€", ha='left', va='center')

    st.set_option('deprecation.showPyplotGlobalUse', False) # desactiva un warning de streamlit
    st.pyplot()