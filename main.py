from flask import Flask, render_template, jsonify
import os
from services.kraken_service import get_kraken_balance
from services.news_service import get_latest_news
from utils.logger import logger
from models.database import init_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/api/balance")
def balance():
    try:
        data = get_kraken_balance()
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error fetching Kraken balance: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/news")
def news():
    try:
        data = get_latest_news()
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error fetching news: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
