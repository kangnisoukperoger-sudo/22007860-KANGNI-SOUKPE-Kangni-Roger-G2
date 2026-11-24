
import yfinance as yf
import pandas as pd
from pathlib import Path

# Définition de la période d'étude
date_debut = "2016-11-17"
date_fin = "2026-11-17"

# Téléchargement des données du Nasdaq
nasdaq = yf.download(
    "^IXIC",
    start=date_debut,
    end=date_fin,
    auto_adjust=True,
    progress=False
)

# Téléchargement des données du S&P 500
sp500 = yf.download(
    "^GSPC",
    start=date_debut,
    end=date_fin,
    auto_adjust=True,
    progress=False
)

# Vérification des téléchargements
if nasdaq.empty or sp500.empty:
    raise ValueError("Le téléchargement des données a échoué.")

# Extraction des prix ajustés de clôture
donnees = pd.DataFrame({
    "Nasdaq": nasdaq["Close"].squeeze(),
    "SP500": sp500["Close"].squeeze()
})

# Conservation des dates communes
donnees = donnees.dropna()

# Enregistrement local des données
dossier = Path(__file__).resolve().parent
fichier = dossier / "donnees_indices.csv"

donnees.to_csv(fichier, index_label="Date")

# Affichage des informations
print("Téléchargement terminé.")
print("Dimensions :", donnees.shape)
print("Date de début :", donnees.index.min())
print("Date de fin :", donnees.index.max())
print("Fichier enregistré :", fichier)
