from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from models import Food, db
import json

views = Blueprint('views', __name__)

@views.route("/",methods=["GET","POST"])
@login_required

def home():
    if request.method == 'POST':
        food = request.form.get('foodName')
        foodDescription = request.form.get('foodDescription')
        if len(food) < 1:
            flash('please enter a food item!', category='error')
        elif len(foodDescription) < 1:
            flash('please enter a food description!', category='error')
        else:
            new_food = Food(food_name=food, description=foodDescription, user_id=current_user.id)
            db.session.add(new_food)
            db.session.commit()
            flash('Food added!', category='success')
    return render_template("home.html", user=current_user)


@views.route('/delete-food', methods=['POST'])
def delete_food():
    print("Recieved")
    foodObject = json.loads(request.data)
    foodId = foodObject['foodId']
    food = Food.query.get(foodId)
    if food:
        if food.user_id == current_user.id:
            db.session.delete(food)
            db.session.commit()
            flash('food deleted', category='success')
        else:
            flash("Error occured, please try again", category='error')
            return jsonify({})
    else:
        flash("Error occured, please try again", category='error')
    return jsonify({})