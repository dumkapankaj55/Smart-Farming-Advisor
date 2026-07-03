# 🌱 KrishiMitra AI – Smart Farming Advisor

An AI-powered Smart Farming Advisor built using **IBM watsonx Orchestrate**, **IBM Granite**, **IBM Cloud**, and **Retrieval-Augmented Generation (RAG)**. The application helps farmers make informed agricultural decisions by providing personalized recommendations based on trusted agricultural knowledge.

---

## 🚀 Features

- 🌾 AI-Based Crop Recommendation
- 🌱 Soil Health Analysis
- 🧪 Fertilizer Recommendation
- 🐛 Pest & Disease Management
- ☁️ Weather-Based Farming Advice
- 📈 Market Price Information
- 🏛️ Government Scheme Guidance
- 📚 RAG-Based Knowledge Retrieval
- 🌍 Multilingual Farming Assistance
- 📱 Responsive Farmer-Friendly Interface

---

## 🛠️ Technology Stack

- IBM watsonx Orchestrate
- IBM Granite Foundation Model
- IBM Cloud
- Retrieval-Augmented Generation (RAG)
- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

## 📂 Project Structure

```text
Smart-Farming-Advisor/
│── app.py
│── requirements.txt
│── README.md
│── .env.example
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── crop.html
│   ├── soil.html
│   ├── weather.html
│   ├── schemes.html
│   ├── market.html
│   ├── profile.html
│   └── base.html
│
└── knowledge/
    ├── Crop Recommendation Dataset
    ├── Soil Management Guide
    ├── Fertilizer Handbook
    ├── Pest & Disease Guide
    └── Government Schemes
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/dumkapankaj55/Smart-Farming-Advisor.git
```

2. Move into the project directory

```bash
cd Smart-Farming-Advisor
```

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Create the environment file

```bash
copy .env.example .env
```

7. Add your IBM Cloud credentials in the `.env` file.

8. Run the application

```bash
python app.py
```

---

## 🔑 Environment Variables

```
IBM_API_KEY=
IBM_PROJECT_ID=
IBM_WATSONX_URL=
IBM_MODEL_ID=
SECRET_KEY=
```

---

## 🎯 Project Objectives

- Improve agricultural decision-making using AI.
- Recommend suitable crops based on soil and weather conditions.
- Provide fertilizer and pest management guidance.
- Deliver trusted farming information using RAG.
- Promote sustainable and precision agriculture.

---

## 👨‍💻 Developed By

**Pankaj Dumka**

B.Tech – Computer Science & Engineering

📧 pankajdumka1@gmail.com

---

## 📜 License

This project is developed for academic and educational purposes under the IBM SkillsBuild AI Internship Program.
