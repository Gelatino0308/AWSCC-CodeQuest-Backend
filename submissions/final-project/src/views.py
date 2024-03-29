from flask import Blueprint, render_template, request, redirect, url_for
from .model import Password
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    passwords = Password.query.all()
    return render_template("home.html", passwords=passwords)

@views.route("/add", methods=["POST"])
def add_pass():
    website = request.form.get('website')
    email = request.form.get('email')
    password = request.form.get('password')
    new_pass = Password(website=website, email=email, password=password)
    db.session.add(new_pass)
    db.session.commit()
    return redirect(url_for('views.home'))

@views.route("/update/<id>", methods=["PATCH"])
def update_pass(id):
    
    website = request.json.get('website')
    email = request.json.get('email')
    password = request.json.get('password')
    
    Pass = Password.query.get(id)
    Pass.website = website
    Pass.email = email
    Pass.password = password
    db.session.commit()
    return ({"result": "success"})

@views.route("/delete/<id>", methods=["DELETE"])
def delete_pass(id):
    Pass = Password.query.get(id)
    if Pass:
        db.session.delete(Pass)
        db.session.commit()
        return ({"results": "success"})
    return ({"results": "error"})
    