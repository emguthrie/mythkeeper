from flask import Flask, render_template, request, redirect, url_for
# from db import init_app, init_db, get_db
from db import get_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
#TODO: account registration

@app.route('/account/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
#TODO: account login

@app.route('/task/add', methods=['GET', 'POST'])
def newtask():
    return render_template('newtask.html')
#TODO: adding tasks

@app.route('/creature/adopt', methods=['GET', 'POST'])
def adopt():
    # if the form is submitted...
    if request.method == 'POST':

        #TODO: Matching owner ID
        owner_id = 1

        # get name and species from the form
        name=request.form['name']
        species=request.form['species']


        db = get_db()
        # determine id for the chosen species
        fetched_row = db.execute('SELECT id '
                                'FROM species '
                                'WHERE name = ?',
                                (species,)
                                ).fetchone()

        for i in fetched_row:
            species_id=i

        # determine starting health for the chosen species
        fetched_row = db.execute('SELECT starting_health '
                                     'FROM species '
                                     'WHERE id = ?',
                                     #(str(species_id),)
                                     (species_id,)
                                     ).fetchone()
        for i in fetched_row:
            starting_health=i

        # add the creature to the database
        db.execute(
                'INSERT INTO creature (name, health, max_health, alive, owner_id, species_id)'
                'VALUES (?, ?, ?, ?, ?, ?)',
                (name, starting_health, starting_health, 1, owner_id, species_id)
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
