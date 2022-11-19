from flask import jsonify


class User:

    def sign_up(self):

        user = {
            "_id": "",
            "email": "",
            "password": ""
        }

        return jsonify(user), 200
