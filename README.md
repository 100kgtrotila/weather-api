# 🌦️ Weather API with Redis Caching

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-black?logo=flask&logoColor=white)
![Redis](https://img.shields.io/badge/Cache-Redis-red?logo=redis&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

> A high-performance RESTful API that fetches weather data and implements intelligent caching.

## Project URL
https://github.com/100kgtrotila/weather-api
---

## 📖 About
This project is a solution to the **[Weather API](https://roadmap.sh/projects/weather-api)** challenge on [roadmap.sh](https://roadmap.sh).

It is a RESTful API built with **Flask** that integrates with a 3rd party service (Visual Crossing) to provide weather data. Key focus areas include performance optimization via **Redis caching**, request rate limiting, and secure environment configuration.

## 🚀 Features

* **Real-time Weather Data**: Fetches current temperature and conditions for any requested city.
* **High Performance Caching**: Implements **Redis** to minimize latency and external API usage.
    * ❄️ **Cold Start**: ~1000ms (Fetches from Visual Crossing).
    * 🔥 **Cached**: ~5ms (Serves directly from Redis memory).
    * *Cache automatically expires after 12 hours.*
* **Rate Limiting**: Restricts users to **5 requests per minute** to prevent abuse and ensure stability.
* **Security**: Sensitive API keys and configuration are managed securely via environment variables.

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Web Framework**: Flask
* **Caching**: Redis (In-memory data structure store)
* **External API**: Visual Crossing Weather API

## 📂 Project Structure

```text
weather-api/
├── app.py              # Main Flask application & Rate Limiting configuration
├── weather_service.py  # Business logic (External API calls + Caching strategy)
├── cache.py            # Redis connection setup
├── config.py           # Configuration & Environment variables loading
├── .env                # API Keys (Excluded from version control)
└── requirements.txt    # Project dependencies