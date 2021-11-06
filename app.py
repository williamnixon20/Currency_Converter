from flask import Flask
from flask_ngrok import run_with_ngrok

# Konfigurasi aplikasi, run_with_ngrok dibutuhkan jika web ingin diakses lewat internet
app = Flask(__name__)
# run_with_ngrok(app)

# Pastikan template terreload otomatis
app.config["TEMPLATES_AUTO_RELOAD"] = True
