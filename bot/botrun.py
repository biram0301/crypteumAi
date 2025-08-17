# bot/run.py
import os, time

def tick():
    # TODO: place ta logique de trading ici (lecture des envs, ccxt, etc.)
    # Exemple provisoire :
    print("🟢 trader tick | EXCHANGE=Kraken | KEY?:", bool(os.getenv("KRAKEN_API_KEY")))
    # … exécuter stratégies, vérifs guard, etc.

def main():
    print("🚀 CrypteumAI Worker démarré")
    while True:
        try:
            tick()
        except Exception as e:
            print("⚠️ erreur tick:", e)
        time.sleep(5)

if __name__ == "__main__":
    main()
