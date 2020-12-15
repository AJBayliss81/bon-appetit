import os, datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "is_admin": False
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if the password for existing user matches db
            # and create "session" cookie
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    session["is_admin"] = existing_user["is_admin"]
                    flash("Welcome, {}".format(request.form.get(
                        "username").capitalize()))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                flash("Username and/or password does not match")
                return redirect(url_for("login"))

        else:
            # username not found in db
            flash("Username and/or password does not match")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()
    # grab the recipe list from db for session user
    recipes = list(mongo.db.recipes.find({"submitted_by": session["user"]}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/admin")
def admin():
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()

    cuisines = list(mongo.db.cuisine.find().sort("cuisine", 1))

    if session["is_admin"]:
        return render_template("admin.html", username=username, cuisines=cuisines)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove the session cookie to allow user to logout
    flash("You have successfully been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        date = datetime.datetime.now()
        recipe = {
            "cuisine": request.form.get("cuisine"),
            "dish_name": request.form.get("dish_name"),
            "description": request.form.get("description"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "submitted_by": session["user"],
            "submission_date": date.strftime("%d %B, %Y"),
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    cuisines = mongo.db.cuisine.find().sort("cuisine", 1)
    return render_template("add_recipe.html", cuisines=cuisines)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/manage_recipes/<recipe_id>", methods=["GET", "POST"])
def manage_recipes(recipe_id):
    if request.method == "POST":
        date = datetime.datetime.now()
        update_recipe = {
            "cuisine": request.form.get("cuisine"),
            "dish_name": request.form.get("dish_name"),
            "description": request.form.get("description"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "submitted_by": session["user"],
            "submission_date": date.strftime("%d %B, %Y"),
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update_recipe)
        flash("Recipe Successfully Updated")

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    cuisines = mongo.db.cuisine.find().sort("cuisine", 1)
    return render_template("manage_recipes.html",
        cuisines=cuisines, recipe=recipe, username=username)


@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        cuisine = {
            "cuisine": request.form.get("cuisine")
        }
        mongo.db.cuisine.insert_one(cuisine)
        flash("Cuisine Successfully Added")
        return redirect(url_for("admin", username=session["user"]))

    return render_template("add_cuisine.html")


@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
