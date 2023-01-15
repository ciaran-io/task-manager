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
    categories_all = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories_all)


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


@app.route("/add-task", methods=["GET", "POST"])
def add_task():
    categories_all = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task_name = request.form.get("task_name")
        task_description = request.form.get("task_description")
        is_urgent = bool(True if request.form.get("is_urgent") else False)
        due_date = request.form.get("due_date")
        category_id = request.form.get("category_id")

        task = Task(
            task_name=task_name,
            task_description=task_description,
            is_urgent=is_urgent,
            due_date=due_date,
            category_id=category_id
        )
        print(is_urgent, type(is_urgent))
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("task-add.html", categories=categories_all)


@app.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    categories_all = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        db.session.commit()
    return render_template("task-edit.html", task=task,
                           categories=categories_all)


@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))
