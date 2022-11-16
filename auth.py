from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth",__name__)

@auth.route('/login',methods = ["GET","POST"])

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('you are logged in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again.', category='error')
        else:
            flash('Email not reconized.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        password = request.form.get("password")
        passwordConfirm = request.form.get("passwordConfirm")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        zip = request.form.get("zip")
        print(email,firstName,lastName,password,passwordConfirm,address,city,state,zip)
        if len(email) < 5:
            flash("Invalid email", category='error')
        elif len(firstName) < 1:
            flash("Invalid name", category='error')
        elif password != passwordConfirm:
            flash("passwords don't match", category='error')
        elif len(address) < 5:
            flash("Invalid address", category='error')
        elif len(city) < 1:
            flash("Invalid city", category='error')
        elif len(state) < 1:
            flash("Invalid state", category='error')
        elif len(zip) < 5:
            flash("Invalid zip code", category='error')
        else:
            new_user = User(email=email, first_name=firstName, last_name=lastName, password=generate_password_hash(
            password, method='sha256'), address=address, city=city, state=state, zip=zip)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    else:
        return render_template("signup.html")
