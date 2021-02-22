from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship("ItemModel", lazy="dynamic")

    # when we use lazy equals dynamic, self.items no longer is a list of items
    # now it is a query builder that has the ability to look into the items table
    # 쿼리가 자동으로 실행되지 않는다. 실제 실행까지 로딩이 있다.
    # https://medium.com/@ns2586/sqlalchemys-relationship-and-lazy-parameter-4a553257d9ef

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}

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
