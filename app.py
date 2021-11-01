from flask import Flask
from flask_ngrok import run_with_ngrok

# Configure application
app = Flask(__name__)
run_with_ngrok(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
