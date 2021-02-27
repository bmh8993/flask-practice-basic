import sqlite3

from flask import request
from flask_restful import Resource, reqparse
from marshmallow import ValidationError

from models.user import UserModel
from schemas.user import UserSchema


user_schema = UserSchema()

class UserRegister(Resource):
    def post(self):
        try:
            usre_data = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if UserModel.find_by_username(usre_data["username"]) is not None:
            return {"message": "A user with that username already exists"}, 400
        # Make sure to have this in front of the connection creatino line

        user = UserModel(**usre_data)
        user.save_to_db()


        return {"message": "User created successfully."}, 201
