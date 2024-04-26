import streamlit as st
import numpy as np
import plotly.express as px

def simulate_delivery_times():
    mu, sigma = 3, 0.5
    return np.random.lognormal(mu, sigma, 1000)

def simulate_price_changes():
    mu, sigma = 50, 8
    return np.random.normal(mu, sigma, 1000)

def simulate_order_counts():
    lambda_ = 3.5
    return np.random.poisson(lambda_, 1000)

# App Titel
st.title('Simulations-App für Digital Procurement')

# Auswahl des Szenarios
option = st.selectbox(
    'Wählen Sie ein Szenario für die Simulation:',
    ('Lieferzeiten', 'Preisvolatilität', 'Nachfrageprognose')
)

if option == 'Lieferzeiten':
    data = simulate_delivery_times()
    fig = px.histogram(data, nbins=50, title="Simulierte Lieferzeiten", labels={'value': 'Tage'}, opacity=0.8)
    st.plotly_chart(fig)

elif option == 'Preisvolatilität':
    data = simulate_price_changes()
    fig = px.histogram(data, nbins=50, title="Simulierte Preisvolatilität", labels={'value': 'Preisänderung in %'}, opacity=0.8)
    st.plotly_chart(fig)

elif option == 'Nachfrageprognose':
    data = simulate_order_counts()
    nbins = int(np.ptp(data)) + 1  # np.ptp gibt die "peak to peak" (max - min) Differenz
    fig = px.histogram(data, nbins=nbins, title="Simulierte Tagesbestellungen", labels={'value': 'Anzahl der Bestellungen'}, opacity=0.8)
    st.plotly_chart(fig)

