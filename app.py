from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
ENVIRONMENT = os.getenv("environment")

app = Flask(__name__)

if ENVIRONMENT == "production":
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
elif ENVIRONMENT == "development":
    print("--dev mode found, no database connected--")
    pass
else:
    print("environment variables did not load correctly")
    print("environment read: ", ENVIRONMENT)


@app.route('/')
def hello():
    return jsonify({"hello": "world"})




if __name__ == '__main__':
    if ENVIRONMENT == "development":
        app.run(debug=True, port=os.getenv("PORT", default=5000))
    elif ENVIRONMENT == "production":
        app.run(port=os.getenv("PORT", default=5000))
    else: 
        print("error running app")