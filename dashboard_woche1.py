import streamlit as st
import pandas as pd

# Titel des Dashboards
st.title('Einführung in Streamlit')

# Etwas Text
st.write("Willkommen zu unserem ersten Streamlit-Dashboard.")

# Daten einlesen
data = pd.read_csv("Good_Food_Purchasing_Data.csv")

# Einführungstext
st.write("Dies ist ein einfaches Dashboard, um die Daten aus der Good Food Purchasing Datenbank anzuzeigen.")

# Daten anzeigen
st.write("### 1 Daten")
st.write("Hier sind die ersten fünf Zeilen unserer Daten:")
st.dataframe(data.head())

# Bild einbinden
st.write("### 2 Bild")
st.write("Hier sind ist ein Bild, das wir eingebunden haben:")
st.image("good_food.jpg", caption="Good Food Bild")