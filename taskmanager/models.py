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
