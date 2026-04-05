import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="STRATOS", layout="wide")

logo_path = "LOGO.JPEG"
file_path = "commandes.csv"

if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=200)
else:
    st.sidebar.error("LOGO.JPEG introuvable sur GitHub")

if not os.path.exists(file_path):
    df_empty = pd.DataFrame(columns=["Nom", "Modele", "Mesures", "Contact"])
    df_empty.to_csv(file_path, index=False)

try:
    df = pd.read_csv(file_path)
except Exception:
    df = pd.DataFrame(columns=["Nom", "Modele", "Mesures", "Contact"])

st.title("STRATOS : Le Sommet de l'Élégance")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Nouvelle Commande")
    with st.form("form_commande", clear_on_submit=True):
        nom = st.text_input("Nom Complet")
        modele = st.selectbox("Modèle", ["Elite Stratos", "Signature Or", "Tradition Business"])
        mesures = st.text_area("Mesures (Épaules, Cou, Poitrine...)")
        contact = st.text_input("Numéro WhatsApp")
        
        submit = st.form_submit_button("Valider la commande")
        
        if submit:
            if nom and contact:
                new_data = pd.DataFrame([[nom, modele, mesures, contact]], columns=["Nom", "Modele", "Mesures", "Contact"])
                df = pd.concat([df, new_data], ignore_index=True)
                df.to_csv(file_path, index=False)
                st.success("Commande enregistrée avec succès.")
                st.rerun()
            else:
                st.error("Veuillez remplir le nom et le contact.")

with col2:
    st.subheader("Tableau de Bord")
    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Aucune commande pour le moment.")

st.markdown("---")
st.caption("STRATOS Platform v1.0 | Géomatique & Élégance")
