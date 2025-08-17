import os
import time
from flask import Flask

app = Flask(__name__)

def mask(s: str | None, keep=4):
    if not s:
        return "None"
    return s[:keep] + "…" + s[-keep:]

@app.route("/")
def home():
    return {
        "status": "🚀 CrypteumAI is running with APIs...",
        "Kraken Key": mask(os.getenv("KRAKEN_API_KEY")),
        "NewsAPI Key": mask(os.getenv("NEWSAPI_KEY"))
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
