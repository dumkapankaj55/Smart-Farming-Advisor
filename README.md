# Smart Farming Advisor

A responsive Flask web app for farmers that combines modern UI with AI-powered guidance from IBM watsonx.ai Granite models.

## Features
- Crop recommendation
- Soil health analysis
- Fertilizer and farm planning advice
- Pest and disease guidance
- Weather-based advice
- Government scheme information
- Market price insights
- Farmer profile dashboard

## Setup
1. Create a Python virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy the environment template and add your IBM Cloud credentials:
   ```bash
   copy .env.example .env
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Environment Variables
- IBM_API_KEY
- IBM_PROJECT_ID
- IBM_MODEL_ID (optional)
- IBM_WATSONX_URL (optional)
- SECRET_KEY (optional)

If IBM credentials are not configured, the app falls back to offline farming guidance so the interface remains usable.
