import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "smart-farming-secret")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            response = get_ai_response(question)
        else:
            flash("Please enter a farming question.")
    return render_template("chat.html", response=response)


@app.route("/crop-recommendation", methods=["GET", "POST"])
def crop_recommendation():
    result = None
    if request.method == "POST":
        region = request.form.get("region", "")
        soil = request.form.get("soil", "")
        rainfall = request.form.get("rainfall", "")
        budget = request.form.get("budget", "")
        prompt = (
            f"Recommend the best crops for a farmer in {region} with {soil} soil, "
            f"{rainfall} rainfall and a {budget} budget. Give 3 practical recommendations "
            f"with why they fit and a short cultivation note."
        )
        result = get_ai_response(prompt)
    return render_template("crop.html", result=result)


@app.route("/soil-analysis", methods=["GET", "POST"])
def soil_analysis():
    result = None
    if request.method == "POST":
        ph = request.form.get("ph", "")
        organic = request.form.get("organic", "")
        moisture = request.form.get("moisture", "")
        crop = request.form.get("crop", "")
        prompt = (
            f"Analyze soil health for a field with pH {ph}, organic matter {organic}, "
            f"moisture {moisture}, and a crop of {crop}. Provide a concise health score, "
            f"risks, and improvement actions."
        )
        result = get_ai_response(prompt)
    return render_template("soil.html", result=result)


@app.route("/weather")
def weather():
    return render_template("weather.html")


@app.route("/schemes")
def schemes():
    return render_template("schemes.html")


@app.route("/market")
def market():
    return render_template("market.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/agent-instructions")
def agent_instructions():
    return render_template("agent_instructions.html")


def get_ai_response(prompt):
    api_key = os.getenv("IBM_API_KEY")
    project_id = os.getenv("IBM_PROJECT_ID")
    model_id = os.getenv("IBM_MODEL_ID", "ibm/granite-13b-chat-v2")

    if api_key and project_id:
        try:
            token = get_watsonx_token(api_key)
            endpoint = os.getenv("IBM_WATSONX_URL", "https://us-south.ml.cloud.ibm.com") + "/ml/v1/text/generation?version=2023-05-29"
            payload = {
                "model_id": model_id,
                "project_id": project_id,
                "input": prompt,
                "parameters": {
                    "decoding_method": "greedy",
                    "max_new_tokens": 250,
                    "min_new_tokens": 30,
                    "temperature": 0.7,
                },
            }
            response = requests.post(endpoint, headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            if data.get("results"):
                return data["results"][0].get("generated_text", "No response received.")
        except Exception as exc:
            return f"Watsonx.ai connection was unavailable. Using offline guidance instead. Error: {exc}"

    return fallback_response(prompt)


def get_watsonx_token(api_key):
    token_url = "https://iam.cloud.ibm.com/identity/token"
    response = requests.post(
        token_url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key},
        timeout=20,
    )
    response.raise_for_status()
    payload = response.json()
    token = payload.get("access_token")
    if not token:
        raise ValueError("IBM token response did not contain an access token")
    return token


def fallback_response(prompt):
    prompt_lower = prompt.lower()
    if "crop" in prompt_lower:
        return (
            "Recommended crops: maize, millet, and pulses are strong options for mixed-risk farms. "
            "Use soil testing, irrigation scheduling, and short-duration varieties to improve resilience."
        )
    if "soil" in prompt_lower:
        return (
            "Soil health should be improved by adding compost, balancing pH, and using cover crops. "
            "Aim for regular testing, moisture retention, and targeted nutrient supplementation."
        )
    if "weather" in prompt_lower:
        return (
            "Use weather forecasts to plan sowing, irrigation, and harvesting windows. "
            "For high heat, protect seedlings and increase mulching to reduce evaporation."
        )
    if "scheme" in prompt_lower or "government" in prompt_lower:
        return (
            "Check local agricultural department portals for subsidy, credit, and crop insurance programs. "
            "Many regions offer seasonal support for irrigation, seeds, and soil health improvement."
        )
    if "market" in prompt_lower or "price" in prompt_lower:
        return (
            "Market timing matters. Sell after quality grading and compare local mandi prices, storage conditions, "
            "and transport cost before committing to a sale."
        )
    return (
        "A smart farming plan should prioritize soil testing, crop selection, weather readiness, and market timing. "
        "I can help you build a practical plan for your farm."
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
