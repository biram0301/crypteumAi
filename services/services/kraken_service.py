import os
import requests

KRAKEN_API_KEY = os.getenv("KRAKEN_API_KEY")
KRAKEN_API_SECRET = os.getenv("KRAKEN_API_SECRET")

def get_kraken_balance():
    # ⚠️ Exemple simplifié : normalement il faut signer les requêtes
    # avec l’API_SECRET. Ici on simule un appel d’API.
    return {"BTC": 0.05, "ETH": 1.2, "USDT": 100}
