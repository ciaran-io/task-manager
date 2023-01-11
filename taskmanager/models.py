from taskmanager import db


class Category(db.Model):
    # schema for the category Model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False, unique=True)
    tasks = db.relationship("Task", backref="category", cascade="all, delete",
                            lazy=True)

    def __repr__(self):
        # return the category name
        return self.category_name


class Task(db.Model):
    # schema for the task Model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), nullable=False, unique=True)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, nullable=False, default=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id", ondelete="CASCADE"),
        nullable=False
    )

    def __repr__(self):
        return f"""{self.task_name} 
        {self.task_description}
        {self.is_urgent}
        {self.due_date} 
        {self.category_id}"""
