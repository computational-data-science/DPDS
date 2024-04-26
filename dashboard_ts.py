import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def generate_data():
    # Erzeugen eines Datumsbereichs
    date_range = pd.date_range(start="2020-01-01", end="2022-12-31", freq='D')
    # Generieren der Trendkomponente (leicht ansteigend)
    trend = np.linspace(start=100, stop=120, num=len(date_range))
    # Generieren der Saisonkomponente (stärker im Sommer)
    seasonality = 20 * np.sin(2 * np.pi * (date_range.dayofyear / 365) * 2)
    # Zufällige Störung für Realismus
    noise = np.random.normal(loc=0, scale=10, size=len(date_range))
    # Kombinieren der Komponenten
    prices = trend + seasonality + noise
    return pd.DataFrame({'Date': date_range, 'Price': prices})

def plot_data(data):
    return px.line(data, x='Date', y='Price', title='Dynamische Preisentwicklung bei Firma A')

# Streamlit App starten
st.title('Fallstudie: Dynamische Preisgestaltung bei Firma A')
st.write("""
## Unternehmenshintergrund
Firma A ist ein spezialisierter Einzelhändler für Haushaltsgeräte, der vor der Herausforderung steht, seine Preise dynamisch anzupassen, um wettbewerbsfähig zu bleiben.

## Problemstellung
Die Herausforderung besteht darin, zukünftige Preistrends genau vorherzusagen, um die Bestandsverwaltung zu optimieren und die Preisstrategie proaktiv zu gestalten.

## Daten und Methodik
Die simulierte Zeitreihe umfasst Verkaufspreise über drei Jahre mit saisonalen Schwankungen, einem ansteigenden Trend und zufälligen Störungen.

## Implementierung und Visualisierung
Die nachfolgende Visualisierung zeigt die simulierte dynamische Preisentwicklung, die Firma A zur Planung ihrer Einkaufs- und Preisstrategien nutzen kann.
""")

# Daten generieren und Diagramm erzeugen
data = generate_data()
fig = plot_data(data)

# Streamlit Komponenten zum Anzeigen des Diagramms
st.plotly_chart(fig)

st.write("""
## Ergebnisse und Diskussion
Die Visualisierung verdeutlicht die saisonalen Schwankungen und den Trend in den Preisen. Diese Informationen helfen Firma A, besser auf Marktveränderungen zu reagieren und strategische Entscheidungen zu treffen.

## Schlussfolgerungen
Durch die Analyse der Zeitreihendaten kann Firma A seine Preisstrategien effektiv planen und anpassen, um seine Marktstellung zu verbessern und die Profitabilität zu steigern.
""")

