# Deployment Guide

## Local Development
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Render / Railway / Heroku
1. Create a new web service from this repository.
2. Set the startup command to:
   ```bash
   gunicorn app:app
   ```
3. Add environment variables in the platform dashboard:
   - IBM_API_KEY
   - IBM_PROJECT_ID
   - IBM_MODEL_ID
   - IBM_WATSONX_URL
   - SECRET_KEY

## IBM watsonx.ai Setup
1. Create an IBM Cloud account.
2. Create an IBM Cloud API key.
3. Create or select a watsonx.ai project.
4. Store your credentials in the `.env` file or deployment environment variables.
