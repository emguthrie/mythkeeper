from flask import Flask, render_template, request, redirect, url_for
from db import init_app, init_db, get_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/creature/adopt', methods=['GET', 'POST'])
def adopt():
    if request.method == 'POST':
        name=request.form['name']
        species=request.form['species']
        db = get_db()
        db.execute(
                'INSERT INTO creature (name, health, max_health, alive, owner_id, species_id)'
                'VALUES (?, ?, ?, ?, ?, ?)',
                (name, 100, 100, 0, 1, 1)
                )
        db.commit()
        return redirect(url_for('index'))
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
