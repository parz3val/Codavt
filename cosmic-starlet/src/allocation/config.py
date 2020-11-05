import os

#configuration for the database and API layers

def get_postgress_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 5432
    password = os.environ.get('DB_PASSWORD', '1234')
    user, db_name = 'harry', 'harrykd'
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

def get_api_url():
    host = os.environ.get("API_HOST", 'localhost')
    port = 50000
    return f"http://{host}:{port}"