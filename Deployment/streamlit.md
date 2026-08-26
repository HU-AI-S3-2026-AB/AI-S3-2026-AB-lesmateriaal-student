# Casus deel 3 - streamlit dashboard

In dit deel van de casus ga je een streamlit dashboard maken waarin je de relevante visualisaties gaat tonen (uit casus deel 1) en waarin de gebruiker een datasetje kan uploaden waarna jouw model (uit casus deel 2) een voorspelling teruggeeft.

## Getting started met streamlit
Als het goed is, is streamlit al geinstalleerd in je conda environment ai-s3. Dit kun je controleren door een terminal (of anaconda prompt) te openen, de environment te activeren (`conda activate ai-s3`) en `streamlit hello` te runnen. Nu moet een tabblad in de browser openen met een streamlit dashboard. Is dat niet het geval, dan moet je mogelijk streamlit nog installeren. Hier zijn de instructies: https://docs.streamlit.io/get-started/installation

Volg daarna deze tutorial om een eerste dashboard te maken: https://docs.streamlit.io/get-started/tutorials/create-an-app

## Interactieve visualisaties
Om interactieve visualisaties te maken kun je ook gebruik maken van plotly express, hiermee kun je met heel weinig code interactieve visualisaties krijgen. Kijk hier voor voorbeelden: Om interactieve visualisaties te maken kun je gebruik maken van plotly, kijk hier voor voorbeelden: https://plotly.com/python/plotly-express/#gallery en lees hier over de combi van plotly en streamlit: https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart.

In streamlit_demo.py wordt ook een voorbeeld getoond van een visualisatie gemaakt met seaborn en streamlit widgets en een met plotly express. Die tweede is niet per se mooier, maar wel veel makkelijker te coderen. Bekijk de code en run het dashboard met `streamlit run streamlit_demo.py` (ga hiervoor eerst in een terminal/anaconda prompt naar de juiste folder en zorg dat de conda omgeving ai-s3 is geactiveerd `conda activate ai-s3`). 
