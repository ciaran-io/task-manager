from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route('/')
def home():
    return render_template("tasks.html")


@app.route('/categories')
def categories():
    # Get all categories from the database return as a list
    categories= list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route('/add-category', methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        name = request.form.get("category_name")
        category = Category(category_name=name)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("category-add.html")
