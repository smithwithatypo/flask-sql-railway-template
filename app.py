from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a simple model for demonstration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/create-table/<table_name>')
def create_table(table_name):
    try:
        # Dynamically create a new table model
        class NewTable(db.Model):
            __tablename__ = table_name
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(50))
            description = db.Column(db.String(200))

        # Create the table in the database
        db.create_all()
        return f'Table {table_name} created successfully.'
    except Exception as e:
        return str(e)
    
@app.route('/add-message/<table_name>/<message>', methods=['POST'])
def add_message(table_name, message):
    try:
        # Dynamically map the table name to the model
        class NewTable(db.Model):
            __tablename__ = table_name
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(50))
            description = db.Column(db.String(200))

        # Add the message to the table
        new_entry = NewTable(name=message, description="A new message")
        db.session.add(new_entry)
        db.session.commit()
        return f'Message "{message}" added to table {table_name} successfully.'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)