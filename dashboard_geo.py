import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def generate_geo_data(num_points=100):
    # Zufällige Erzeugung von Geodaten für Lieferanten in Deutschland
    np.random.seed(42)  # Für Reproduzierbarkeit der Daten
    latitudes = np.random.uniform(low=47.2701, high=55.0583, size=num_points)  # Bereich für Deutschland
    longitudes = np.random.uniform(low=5.8663, high=15.0419, size=num_points)
    mean = np.log(100)  # Mittelwert im Log-Raum, basierend auf dem gewünschten Mittelwert im Originalraum
    sigma = 0.75  # Standardabweichung im Log-Raum
    shipping_costs = np.random.lognormal(mean=mean, sigma=sigma, size=num_points) # Zufällige Versandkosten
    reliability_scores = np.random.uniform(low=70, high=100, size=num_points)  # Lieferanten Zuverlässigkeitsbewertung
    return pd.DataFrame({
        'Latitude': latitudes,
        'Longitude': longitudes,
        'Shipping Costs': shipping_costs,
        'Reliability': reliability_scores
    })

def plot_geo_data(data):
    fig = px.scatter_geo(data, lat='Latitude', lon='Longitude',
                         color='Shipping Costs', size='Shipping Costs', # Größe basierend auf den Versandkosten
                         hover_name='Reliability', projection="natural earth",
                         title='Geografische Verteilung der Lieferanten und Logistikkosten',
                         scope="europe")  # Beschränke die Karte auf Europa für bessere Fokussierung auf Deutschland
    return fig

# Streamlit App starten
st.title('Analyse der Lieferantenstandorte und Logistikkosten')
st.write("""
## Unternehmenshintergrund
Unser Unternehmen bezieht Produkte von verschiedenen Lieferanten weltweit. Die Analyse ihrer geografischen Standorte und Logistikkosten ist entscheidend für die Optimierung unserer Lieferkette.

## Problemstellung
Das Hauptziel ist es, die Gesamtlogistikkosten zu minimieren und gleichzeitig die Zuverlässigkeit unserer Lieferanten zu gewährleisten.

## Daten und Methodik
Die simulierte Datenanalyse umfasst geografische Standorte und zugehörige Logistikkosten sowie die Zuverlässigkeitsbewertungen der Lieferanten.

## Implementierung und Visualisierung
Die folgende Visualisierung zeigt die geografische Verteilung unserer Lieferanten sowie die mit jedem Standort verbundenen Logistikkosten.
""")

# Daten generieren und Diagramm erzeugen
geo_data = generate_geo_data()
geo_fig = plot_geo_data(geo_data)

# Streamlit Komponenten zum Anzeigen des Diagramms
st.plotly_chart(geo_fig)

st.write("""
## Ergebnisse und Diskussion
Durch die Visualisierung können wir Muster in den Logistikkosten erkennen und Bereiche identifizieren, in denen möglicherweise Optimierungen erforderlich sind. 

## Schlussfolgerungen
Die Standortanalyse ermöglicht es uns, strategische Entscheidungen über die Auswahl neuer Lieferanten oder die Neugestaltung unserer Logistikrouten zu treffen, um Effizienz und Kosteneffektivität zu steigern.
""")
