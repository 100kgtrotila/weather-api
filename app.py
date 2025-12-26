from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import weather_service

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

@app.route("/weather/<city>", methods=['GET'])
@limiter.limit("5 per minute")
def weather(city):
    result = weather_service.weathercast_in_city(city)
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "City not found"}), 404

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Rate limit exceeded. Try again later."}), 429

if __name__ == "__main__":
    app.run(debug=True)