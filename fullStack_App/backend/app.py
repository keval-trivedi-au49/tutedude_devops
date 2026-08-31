from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

frontend_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")

app = Flask(__name__, template_folder=frontend_folder)
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["fullstack_app"]
users = db["drivers"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():

    try:
        name = request.form["name"]
        email = request.form["email"]
        if not name:
            return render_template(
                        "index.html",
                        error='Name is required'
                    )
        if not email:
             return render_template(
                                    "index.html",
                                    error='Email is required'
                                )
        user_data = {
            "name": name,
            "email": email
        }

        users.insert_one(user_data)
        return redirect(url_for("success"))

    except Exception as error:
        return render_template(
            "index.html",
            error=str(error)
        )

@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)