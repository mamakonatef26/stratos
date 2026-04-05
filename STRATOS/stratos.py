import os
import pandas as pd
import streamlit as st

# Trouver le chemin du dossier où se trouve le script actuel
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "commandes.csv")

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    st.error("Le fichier 'commandes.csv' est introuvable. Vérifiez qu'il est bien sur GitHub !")
    # Créer un DataFrame vide pour éviter que l'app ne plante totalement
    df = pd.DataFrame()
