import os
import datetime
from flask import (
    Flask, flash, render_template, jsonify,
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


# Search functionality
@app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    comments = list(mongo.db.comments.find({"recipe_id": recipe_id}))
    return render_template("recipes.html", recipe=recipe, comments=comments)


# List the cuisines found in the database
@app.route("/browse")
def browse():
    cuisines = list(mongo.db.cuisine.find().sort("cuisine", 1))
    return render_template("browse.html", cuisines=cuisines)


# Take the cuisine name from the "browse" form and use that
# to search the db
@app.route("/cuisine_recipes", methods=["GET", "POST"])
def cuisine_recipes():
    browse = request.form.get("browse")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": browse}}))
    cuisine = browse
    return render_template(
        "cuisine_recipes.html", recipes=recipes, cuisine=cuisine)


# A simple search function to find all the recipes in the db
@app.route("/search")
def search():
    recipes = list(mongo.db.recipes.find())
    return render_template("search.html", recipes=recipes)


# A search function to check if a specific dish is in the db
@app.route("/search_dish", methods=["GET", "POST"])
def search_dish():
    dish = request.form.get("dish")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": dish}}))
    return render_template("search.html", recipes=recipes)


# A search function to check if a dish containing specific ingredients
# is in the db
@app.route("/search_ingredients", methods=["GET", "POST"])
def search_ingredients():
    ingredients = request.form.get("ingredients")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": ingredients}}))
    return render_template("search.html", recipes=recipes)


# Login/out & register functionality
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


# Functionality to log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if the password for existing user matches db
            # and create "session" cookie
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
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


# Logout functionality
@app.route("/logout")
def logout():
    # remove the session cookie to allow user to logout
    flash("You have successfully been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Profile and admin functionality
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()
    # grab the recipe list from db for session user
    recipes = list(mongo.db.recipes.find({"submitted_by": session["user"]}))
    # grab the session user comments from db
    comments = list(mongo.db.comments.find({"submitted_by": session["user"]}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes,
            comments=comments)

    return redirect(url_for("login"))


# Display the admin panel and CRUD functions
@app.route("/admin")
def admin():
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()

    cuisines = list(mongo.db.cuisine.find().sort("cuisine", 1))

    if session["is_admin"]:
        return render_template(
            "admin.html", username=username, cuisines=cuisines)

    return redirect(url_for("login"))


# CRUD functionality for recipes
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


# To delete recipes from db
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


# Edit recipe functionality
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
    return render_template(
        "manage_recipes.html", cuisines=cuisines, recipe=recipe,
        username=username)


# CRUD functionality for cuisines

# Add new cuisines - Admin only
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


# Delete cuisines from db - Admin only
@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine Successfully Deleted")
    return redirect(url_for("admin", username=session["user"]))


# Edit cuisines in the db - Admin only
@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    if request.method == "POST":
        submit = {
            "cuisine": request.form.get("cuisine")
        }
        mongo.db.cuisine.update({"_id": ObjectId(cuisine_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("admin", username=session["user"]))

    cuisine = mongo.db.cuisine.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


# CRUD functionality for comments

# Add new comments to specific recipes
@app.route("/add_comment/<recipe_id>", methods=["GET", "POST"])
def add_comment(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    comments = list(mongo.db.comments.find({"recipe_id": recipe_id}))
    if request.method == "POST":
        date = datetime.datetime.now()
        comment = {
            "comment": request.form.get("add_comment"),
            "recipe_id": recipe_id,
            "submitted_by": session["user"],
            "submission_date": date.strftime("%d %B, %Y"),
        }
        mongo.db.comments.insert_one(comment)
        flash("Comment Successfully Added")
        comments = list(mongo.db.comments.find({"recipe_id": recipe_id}))
        return render_template(
            "recipes.html", recipe=recipe, comments=comments)

    return render_template("recipes.html", recipe=recipe, comments=comments)


# Delete users own specific comments
@app.route("/delete_comment/<comment_id>")
def delete_comment(comment_id):
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    flash("Comment Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


# Edit user's own comments
@app.route("/edit_comment/<comment_id>", methods=["GET", "POST"])
def edit_comment(comment_id):
    if request.method == "POST":
        date = datetime.datetime.now()
        submit = {
            "comment": request.form.get("edit_comment"),
            "recipe_id": request.form.get("recipe_id"),
            "submitted_by": session["user"],
            "submission_date": date.strftime("%d %B, %Y"),
        }
        mongo.db.comments.update({"_id": ObjectId(comment_id)}, submit)
        flash("Comment Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))

    comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    return render_template(
        "edit_comment.html", comment=comment, username=session["user"])


# Custom Error Handling
# 404 Error Page not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# 500 Error Server Error
@app.errorhandler(500)
def internal_server(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
