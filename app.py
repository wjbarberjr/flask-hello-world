import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://wiba6472_lab10_db_user:xKD5qwOHsvmx26un0PZPkWoIdAF0IE9a@dpg-cl3evjiuuipc738c6tkg-a/wiba6472_lab10_db")
    conn.close()
    return 'Database Connection Successful'