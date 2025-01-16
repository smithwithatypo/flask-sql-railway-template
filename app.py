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
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)
    print(os.getenv("PORT"))
    print(os.getenv("DATABASE_URL"))
    pass
elif ENVIRONMENT == "development":
    print("--dev mode found, no database connected--")
    pass
else:
    print("environment variables did not load correctly")
    print("environment read: ", ENVIRONMENT)


@app.route('/')
def hello():
    return jsonify({"hello": "world"})

@app.route('/api/get_messages')
def get_messages():
    if ENVIRONMENT == "production":
        db = SQLAlchemy(app)
        class Message(db.Model):
            __tablename__ = 'test-table'
            id = db.Column(db.Integer, primary_key=True)
            message = db.Column(db.String, nullable=False)

        messages = Message.query.all()
        return jsonify([{"id": message.id, "content": message.content} for message in messages])
    else:
        return jsonify({"error": "Not in production environment"})





if __name__ == '__main__':
    if ENVIRONMENT == "development":
        app.run(debug=True, port=os.getenv("PORT", default=5000))
    elif ENVIRONMENT == "production":
        app.run(debug=False, host='0.0.0.0', port=os.getenv("PORT", default=5000))
    else: 
        print("error running app")