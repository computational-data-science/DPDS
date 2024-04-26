import streamlit as st
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

# Daten simulieren
np.random.seed(42)
x = np.random.normal(100, 20, 200)  # Bestellmengen
y = 5 * x + np.random.normal(0, 50, 200)  # Kosten

# Daten für die Darstellung vorbereiten
X = x.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Streamlit App
st.title('Fallstudie: Kostenoptimierung im Digital Procurement')
st.write("""
## Unternehmenshintergrund
Firma B ist ein großes Unternehmen in der Fertigungsindustrie, das vor der Herausforderung steht, seine Einkaufskosten effizient zu managen, um Wettbewerbsfähigkeit zu sichern und Kosten zu minimieren.

## Problemstellung
Das Management möchte die Einkaufskosten vorhersagen, basierend auf variierenden Bestellmengen, um bessere Budgetentscheidungen treffen zu können.

## Daten und Methodik
Es wurden simulierte Daten verwendet, um die Beziehung zwischen Bestellmenge und Einkaufskosten zu modellieren. Die Daten umfassen Bestellmengen und die damit verbundenen Kosten, aufgezeichnet über mehrere Monate.

## Implementierung und Visualisierung
Die nachfolgende Visualisierung zeigt die Beziehung zwischen Bestellmenge und Kosten, einschließlich einer linearen Regressionslinie zur Vorhersage zukünftiger Kosten.
""")

# Datenpunkte und Regressionslinie plotten
fig = px.scatter(x=x, y=y, labels={'x': 'Bestellmenge', 'y': 'Kosten'}, title="Kosten vs. Bestellmenge")
fig.add_scatter(x=x, y=y_pred, mode='lines', name='Regressionslinie')
st.plotly_chart(fig)

# Vorhersagefunktion
quantity = st.number_input('Geben Sie die Bestellmenge ein, um die Kosten vorherzusagen:', min_value=0, max_value=500, value=100)
predicted_cost = model.predict([[quantity]])[0]
st.write(f"Vorhergesagte Kosten für eine Bestellmenge von {quantity}: ${predicted_cost:.2f}")

st.write("""
## Ergebnisse und Diskussion
Die Visualisierung verdeutlicht die direkte Beziehung zwischen Bestellmenge und Kosten. Diese Information ermöglicht es Firma B, Bestellungen strategisch zu planen und zu optimieren, um die Gesamtkosten zu reduzieren.

## Schlussfolgerungen
Durch die Anwendung der linearen Regression kann Firma B seine Einkaufskosten effektiv vorhersagen und seine Einkaufsstrategie entsprechend anpassen. Dies führt zu einer verbesserten Budgetkontrolle und zu signifikanten Einsparungen im Einkauf.
""")
