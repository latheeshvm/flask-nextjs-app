from flask import Flask
from flask import session
import os
from app.models.database import Database


app = Flask(__name__, static_url_path="/_next", static_folder='_next')
app.secret_key = str(os.environ.get('flask1appsecret'))

# Sets up the database
mydb = Database(type='mongodb', username='mongousername', password='mongopassword',
                url='mongouri', laodfromenv=True, database='Users', table='user')
app.config['db'] = mydb.mongodb_load()
app.config['session'] = session

# DEBUG
# db.insert_one({"name": "Lathesh", "address": "kskk 37"})

with app.app_context():
    from app.routes.index_route import bp_index
    from app.routes.user_routes import bp_user
    app.register_blueprint(bp_index)
    app.register_blueprint(bp_user)


if __name__ == "__main__":

    app.run(debug=True)
