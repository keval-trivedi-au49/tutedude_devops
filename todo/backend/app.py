from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

frontendFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", "frontend")
mongo_url = os.getenv("MONGO_URI")

client = MongoClient(mongo_url)
db = client["fullstack_app"]
users = db["todos"]

app = Flask(__name__, template_folder = frontendFolder)


@app.route('/submittodoitem', methods=["POST"])
def submitTodo():
    try:
        name = request.form["name"]
        description = request.form["description"]
        if not name:
            return render_template(
                "index.html",
                error = 'Todo item name required'
            )
        if not description:
            return render_template(
                    "index.html",
                    error = 'Todo item description required'
            )
            
        todo = {
            "name": name,
            "description": description
        }
        users.insert_one(todo)
        return 'Todo ' + name + ' created successfully'
        
    except Exception as error:
            return render_template(
                "index.html",
                error=str(error)
            )
            
@app.route('/')
def home():
 return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)