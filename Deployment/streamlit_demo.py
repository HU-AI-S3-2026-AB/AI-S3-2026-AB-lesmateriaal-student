import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Streamlit demo')

#Schrijf tekst naar het dashboar
st.write('Hoi S3 student! Welkom op dit streamlit dashboard.\n Als je iets aanpast in dit bestand, moet je in je dashboard op Rerun klikken om de veranderingen te zien.')

# Laden van de dataset en cachen voor betere performance
@st.cache_data
def load_data():
    penguins = pd.read_csv('./databronnen/pinguins.csv')
    return penguins

df = load_data()

# Een seaborn visualisatie met een keuzemenu van streamlit

st.write('Hier tonen we een seaborn visualisatie met een keuzemenu van streamlit')

# Keuzemenu voor de soorten
selected_species = st.multiselect(
    'Kies een of meerdere pinguïnsoorten om te tonen:',
    options=df['species'].unique(),
    default=df['species'].unique()
)

# Filter de data op basis van de selectie
filtered_df = df[df['species'].isin(selected_species)]

# Creëer de scatterplot
fig, ax = plt.subplots()
sns.scatterplot(
    data=filtered_df,
    x='flipper_length_mm',
    y='bill_length_mm',
    hue='species',
    palette='viridis',
    ax=ax
)
ax.set_title('Scatterplot van Flipper Length vs. Bill Length')
ax.set_xlabel('Flipper Length (mm)')
ax.set_ylabel('Bill Length (mm)')

# Toon de plot in Streamlit
st.pyplot(fig)


# Hier een voorbeeld van hoe dit heel makkelijk kan met plotly express
st.write('Dezelfde visualisatie maar dan met plotly')
fig = px.scatter(df, x='flipper_length_mm', y='bill_length_mm', color='species', title='Pinguins dataset')
st.plotly_chart(fig)


