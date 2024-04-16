import streamlit as st
import pandas as pd
import plotly.express as px

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

# Deskriptive Statistiken
st.write("### 3 Deskriptive Statistiken")

# Kosten pro Produktkategorie
# Radio-Button für die Auswahl der Anzeigeart
cost_display_type = st.radio("Wählen Sie die Anzeigemethode für die Kostenübersicht:",
                             ('Absolut', 'Pro lbs'))

if cost_display_type == 'Absolut':
    # Gesamtkosten pro Produktkategorie
    st.write("#### Gesamtkosten pro Produktkategorie (absolut)")
    total_cost_per_category = data.groupby("Food Product Category")["Total Cost"].sum()
    fig_abs = px.bar(total_cost_per_category, title="Gesamtkosten pro Produktkategorie")
    fig_abs.update_layout(showlegend=False, yaxis_title="Kosten in Euro")  # Legende ausblenden
    st.plotly_chart(fig_abs)
else:
    # Kosten pro lbs pro Produktkategorie
    st.write("#### Kosten pro lbs pro Produktkategorie")
    cost_per_lb_per_category = data.groupby("Food Product Category").apply(lambda df: df["Total Cost"].sum() / df["Total Weight in lbs"].sum())
    fig_per_lb = px.bar(cost_per_lb_per_category, title="Kosten pro lbs pro Produktkategorie")
    fig_per_lb.update_layout(showlegend=False, yaxis_title="Kosten in Euro pro lbs")  # Legende ausblenden
    st.plotly_chart(fig_per_lb)

# Entwicklung der Kosten pro Produktkategorie über die Zeitperioden
st.write("#### Entwicklung der Kosten pro Produktkategorie über die Zeitperioden")
cost_over_time = data.groupby(["Time Period", "Food Product Category"]).agg({'Total Cost': 'sum', 'Total Weight in lbs': 'sum'}).reset_index()

# Radio-Button für die Auswahl der Anzeigeart
cost_display_type2 = st.radio("Wählen Sie die Anzeigemethode für die Kostenentwicklung:",
                             ('Absolut', 'Pro lbs'))

if cost_display_type2 == 'Absolut':
    fig = px.line(cost_over_time, x="Time Period", y="Total Cost", color="Food Product Category", 
                  title="Entwicklung der Gesamtkosten pro Produktkategorie über die Zeitperioden",
                  labels={"Total Cost": "Gesamtkosten in Euro", "Time Period": "Zeitperiode", "Food Product Category": "Produktkategorie"})
else:
    # Berechnung der Kosten pro lbs
    cost_over_time["Cost per lbs"] = cost_over_time["Total Cost"] / cost_over_time["Total Weight in lbs"]
    fig = px.line(cost_over_time, x="Time Period", y="Cost per lbs", color="Food Product Category", 
                  title="Entwicklung der Kosten pro lbs pro Produktkategorie über die Zeitperioden",
                  labels={"Cost per lbs": "Kosten in Euro pro lbs", "Time Period": "Zeitperiode", "Food Product Category": "Produktkategorie"})

fig.update_layout(yaxis_title="Kosten")  # Dynamischer Y-Achsentitel basierend auf der Auswahl
st.plotly_chart(fig)

# Top 10 Lieferanten nach Anzahl der gelieferten Einheiten
st.write("#### Top 10 Lieferanten nach Anzahl der gelieferten Einheiten")
units_per_vendor = data.groupby("Vendor")["# of Units"].sum().nlargest(10)
st.bar_chart(units_per_vendor)

# Entwicklung des Preises pro lbs für eine Produktkategorie
st.write("#### Entwicklung des Preises pro lbs für eine ausgewählte Produktkategorie und unterschiedliche Lieferanten")
category_options = data["Food Product Category"].unique()
selected_category = st.selectbox("Wählen Sie eine Produktkategorie:", category_options)
category_data = data[data["Food Product Category"] == selected_category]

price_per_lb_over_time = category_data.groupby(["Time Period", "Vendor"]).apply(lambda df: (df["Total Cost"].sum() / df["Total Weight in lbs"].sum()))
price_per_lb_over_time = price_per_lb_over_time.unstack().fillna(0)
st.line_chart(price_per_lb_over_time)