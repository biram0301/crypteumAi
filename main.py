import os

def main():
    print("🚀 CrypteumAI is running with APIs...")
    print("Kraken Key:", os.getenv("KRAKEN_API_KEY"))
    print("NewsAPI Key:", os.getenv("NEWSAPI_KEY"))

if __name__ == "__main__":
    main()
