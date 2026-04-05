import pandas as pd

df = pd.read_csv("commandes.csv")

# Modèles les plus vendus
print(df["Modele"].value_counts())

# Tailles les plus demandées
print(df["Taille"].value_counts())