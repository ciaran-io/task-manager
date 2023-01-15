from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route('/')
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


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


@app.route('/edit-category/<int:category_id>', methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("category-edit.html", category=category)


@app.route('/delete-category/<int:category_id>', methods=["GET", "POST"])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        db.session.delete(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("category-delete.html", category=category)