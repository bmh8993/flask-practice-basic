from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    # SELECT * FROM __tablename__ WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    # this method has two rolls, insert data and update data.

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

# resources is endpoint that interact client such as web or mobile.
# The change in methods created through classmethod does not directly affect API.
# therefore, I will separate the methods.
