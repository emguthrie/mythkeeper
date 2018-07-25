from flask import Flask, render_template
from db import init_app, init_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/creature/adopt', methods=['GET', 'POST'])
def adopt():
    return render_template('adopt.html')

def create_app():
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE='db.sqlite'
            )
    
    return app

if __name__ == '__main__':
    #init_app(app)
    #init_db()
    with app.app_context():
        init_db()
    app.run(debug = True)
