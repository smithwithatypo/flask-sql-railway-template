from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

if os.getenv("environment") == "production":
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
elif os.getenv("environment") == "development":
    print("--dev mode found, no database connected--")
    pass
else:
    print("environment variables did not load correctly")
    print("environment read: ", os.getenv("environment"))


@app.route('/')
def hello():
    return {"hello": "world"}




if __name__ == '__main__':
    app.run(debug=True)