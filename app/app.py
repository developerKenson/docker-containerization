from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Congratulations! My first Docker application is running on AWS CloudShell!"

@app.route("/info")
def info():
    return {
        "application": "Docker Web Application",
        "environment": os.getenv("APP_ENV", "development"),
        "platform": "AWS CloudShell"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
