import os, time

def mask(s: str | None, keep=4):
    if not s:
        return "None"
    return s[:keep] + "…" + s[-keep:]

if __name__ == "__main__":
    kkey = os.getenv("KRAKEN_API_KEY")
    nkey = os.getenv("NEWSAPI_KEY")

    print("🚀 CrypteumAI is running with APIs...")
    print("Kraken Key:", mask(kkey))
    print("NewsAPI Key:", mask(nkey))

    # Boucle pour garder le service actif sur Render
    while True:
        time.sleep(60)
