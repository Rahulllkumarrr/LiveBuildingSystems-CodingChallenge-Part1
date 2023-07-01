import os


from flask import Flask
from faker import Faker


from api.meter import meter_routes
from database import db
from add_fake_data import insert_fake_data

basedir = os.path.abspath(os.path.dirname(__file__))
fake = Faker()


def start_app():
    app = Flask(__name__)
    app.register_blueprint(meter_routes)

    db_path = os.path.join(basedir, "meter.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
    response = insert_fake_data(app, db)
    print(response)
    app.run()


if __name__ == "__main__":
    start_app()
