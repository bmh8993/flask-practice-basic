from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
        return {"item": None}, 404

    def post(self, name):
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
