## flask postgresql template to be hosted on railway

# Flask Supabase Template

This is a basic template for a Flask application that connects to Supabase.

## Getting Started

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flask-supabase-template.git
    cd flask-supabase-template
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Rename `.env.sample` to `.env` and enter your Supabase API keys:
    ```sh
    mv .env.sample .env
    ```

5. Run the Flask application:
    ```sh
    python3 app.py
    ```


## Tutorial for students connecting to Supabase
- make an account on Railway
- make an account on GitHub
- install Postman
- make github repo (completely blank, not even Readme) and push codebase
- make new project on railway
- on railway, create a new Service
    - connect to your GitHub Repo and select the Main branch
- on Railway, create new Postgresql service from db dropdown menu
    - show how to see db info on Railway (environment variables)
- in Postgresql service, create new table with schema you want. easiest way is the GUI, or you can open terminal and use psql
    - you can see username/password and db info in “Variables” tab when you click on the eyeball icon
    - in this example, 
        - table == “test-table”
        - col1 == (name:“id”, type:”serial”, Default:”no default”, constraint:”Primary key”)
        - col2 == (name: “message”, type: “text”, Default: “no default”, Constraint: “no constraint”)
    - ![db create table]()
    - ![db table schema]()
- set environment variable for flask service
    - follow popups.  “database_url”  (internal ip, not “public”)
- set environment variables in railway (db_URL, and environment=production)
    - ![flask env variables]()
- navigate to railway > click on flask service > settings > copy “Public Networking” url > paste into Postman
- in [app.py](http://app.py), make sure host is “0.0.0.0” in app.run()
- in Postman, make sure you’re sending POST request over https (not http)
    - how to construct a POST
        - click POST, enter your url including https://
        - click Body tab
        - click raw, make sure JSON is selected
        - type your JSON  {message: "this is a message"}
            - every key must be a string or collection of strings
            - You can collect strings using curly brackets or square brackets
    - ![postman POST]()
- Resources
    - Discord:   https://discord.gg/railway
    - Railway Docs:    https://docs.railway.com/
    - Flask_sqlalchemy docs:   https://flask-sqlalchemy.readthedocs.io/en/stable/