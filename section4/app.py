from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {"item": item}, 200 if item is not None else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"message": "An item with name '{}' already exists".format(name)}, 400

        data = request.get_json()
        # get_json의 옵션으로 force=True, silent=True가 있는데 force=True는 header의
        # content-type을 무시한다.
        # silent=True는 에러가 발생해도 None를 return 한다.
        item = {'name': name, 'price': data["price"]}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)
