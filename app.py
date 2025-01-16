from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
ENVIRONMENT = os.getenv("ENVIRONMENT")

app = Flask(__name__)

if ENVIRONMENT == "production":
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    class Message(db.Model):
        __tablename__ = 'test-table'
        id = db.Column(db.Integer, primary_key=True)
        message = db.Column(db.String, nullable=False)

elif ENVIRONMENT == "development":
    print("-- dev mode found, no database connected --")
else:
    print("environment variables did not load correctly")
    print("environment read: ", ENVIRONMENT)


@app.route('/')
def hello():
    return jsonify({"hello": "world"})


@app.route('/api/get_messages')
def get_messages():
    if ENVIRONMENT == "production":
        messages = Message.query.all()
        return jsonify([{"id": message.id, "message": message.message} for message in messages])
    else:
        return jsonify({"error": "Not in production environment, no db connected"})


@app.route('/api/add_message', methods=['POST'])
def add_message():
    if ENVIRONMENT == "production":
        data = request.get_json()
        new_message = Message(message=data['message'])
        db.session.add(new_message)
        db.session.commit()
        return jsonify({"id": new_message.id, "message": new_message.message}), 201
    else:
        return jsonify({"error": "Not in production environment, no db connected"})


if __name__ == '__main__':
    if ENVIRONMENT == "development":
        app.run(debug=True, port=os.getenv("PORT", default=5000))
    elif ENVIRONMENT == "production":
        app.run(debug=False, host='0.0.0.0', port=os.getenv("PORT", default=5000))
    else: 
        print("error running app")