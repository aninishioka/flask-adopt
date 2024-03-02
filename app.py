"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db
from forms import AddPetForm, EditPetForm
from pet_finder import token, get_pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_homepage():
    """Renders root route"""
    pets = Pet.query.all()
    random_pet = get_pet(token)
    return render_template('home.html', pets=pets, random_pet = random_pet)


@app.route("/add", methods=["POST", "GET"])
def add_pet():
    """Renders Pet add form. Handles submission"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url,
                  age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("add_pet_form.html", form=form)


@app.route('/<int:pet_id>', methods=['POST', 'GET'])
def edit_pet(pet_id):
    """Renders pet edit form, handles submission and changes to db"""
    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available
        db.session.commit()

        return redirect('/')

    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)
