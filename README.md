# Weather API with Redis Caching

This is a solution to the [Weather API](https://roadmap.sh/projects/weather-api) project on roadmap.sh.

A RESTful API built with Flask that fetches weather data from a 3rd party service (Visual Crossing) and caches the results using Redis to improve performance and reduce API costs.

## 🚀 Features

* **Weather Data**: Fetches current temperature and conditions for any city.
* **Caching**: Implements **Redis** caching. 
    * First request takes ~1000ms (fetches from external API).
    * Subsequent requests take ~5ms (fetches from Redis cache).
    * Cache expires automatically after 12 hours.
* **Rate Limiting**: Restricts users to 5 requests per minute to prevent abuse.
* **Security**: Uses environment variables to store sensitive API keys.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Flask** (Web Framework)
* **Redis** (In-memory data structure store)
* **Visual Crossing API** (Weather provider)

## 📂 Project Structure

```text
weather-api/
├── app.py              # Main Flask application & Rate Limiting
├── weather_service.py  # Business logic (API calls + Caching logic)
├── cache.py            # Redis connection setup
├── config.py           # Configuration & Env variables loading
├── .env                # API Keys (Not included in repo)
└── requirements.txt    # List of dependencies
Developed by 100kgtrotila.