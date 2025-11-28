<p align="center">
 <img width="1536" height="1024" alt="ChatGPT Image Nov 29, 2025, 01_01_19 AM" src="https://github.com/user-attachments/assets/ac2e3d5d-a0f3-4191-9150-3697a0ff1c3d" />
</p>
# 🚀 Myntra Scrape Pro — Review Scraper & Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg" />
  <img src="https://img.shields.io/badge/Scraping-Selenium-blueviolet.svg" />
  <img src="https://img.shields.io/badge/Database-MongoDB-success.svg" />
  <img src="https://img.shields.io/badge/ChromeDriver-Binary-green.svg" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  <img src="https://img.shields.io/github/stars/NeuroNaman/myntra-scrape-pro?style=social" />
</p>
📝 Project Summary

Myntra Scrape Pro is a powerful review scraper and analysis tool built to extract product reviews from the Myntra website.

The application collects:

⭐ Product ratings

💬 Customer comments

👤 Reviewer names

📦 Product details

📊 Review statistics

All scraped data is stored securely in MongoDB and visualized using a modern Streamlit dashboard, allowing users to explore customer feedback quickly and interactively.

✨ Features

🔍 Extract reviews from ANY Myntra product URL

⭐ Capture ratings, comments, reviewer names

🗄️ Save data into MongoDB automatically

⚡ Real-time scraping with Selenium

🎨 Clean and interactive Streamlit UI

🔐 Secure .env environment variable support

🟢 ChromeDriver Binary (no manual setup required)

🛠️ Tech Stack
Frontend/UI

Streamlit

Backend

Python

Selenium

BeautifulSoup (optional)

Database

MongoDB

database-connect library

Utilities

ChromeDriver Binary (PyPI)

python-dotenv

📥 Clone the Repository
git clone https://github.com/NeuroNaman/myntra-scrape-pro.git
cd myntra-scrape-pro

⚙️ Setup Instructions
1️⃣ Create & activate a virtual environment

Using Conda:

conda create -p ./env python=3.10 -y
conda activate ./env


Using venv:

python -m venv .venv
.\.venv\Scripts\activate       # Windows

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add MongoDB environment variable

Create a file named .env in the project root:

MONGO_DB_URL="your-mongodb-connection-string"


Ensure .env is included in .gitignore.

4️⃣ Run the Streamlit App
streamlit run app.py

5️⃣ Open the Web App

👉 http://localhost:8501

🗄️ MongoDB Integration

The app uses MongoDB to store:

Ratings

Comments

Reviewer metadata

Product details

The connection is handled automatically using the database-connect package and environment variables.

🛠️ ChromeDriver Binary Support

Instead of manually downloading chromedriver.exe, this project uses the ChromeDriver Binary PyPI package, which:

✔ Automatically matches Chrome version
✔ Works on all OS
✔ Requires no manual setup

📸 Screenshots (Add Yours Here)

Example format:

![Home Page](screenshots/home.png)
![Reviews](screenshots/reviews.png)

📂 Project Structure
myntra-scrape-pro/
│── app.py                 # Streamlit UI
│── application.py         # Selenium backend scraper
│── src/
│   ├── cloud_io           # Mongo DB handler
│   └── ...
│── requirements.txt
│── README.md
│── .env (ignored)
│── .gitignore

🤝 Contributing

Contributions are welcome!
Feel free to open:

🐞 Issues

💡 Feature Requests

🔧 Pull Requests

⭐ Support the Project

If you found this useful, give the repo a ⭐ star on GitHub!

🚀 Happy Scraping!

Made with ❤️ by Naman Nanda
