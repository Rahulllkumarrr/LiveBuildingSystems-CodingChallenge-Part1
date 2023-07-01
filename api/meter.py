from flask import Blueprint
from flask import render_template, jsonify

from database import Meter, MeterData


meter_routes = Blueprint("meter_blueprint", __name__, template_folder="templates")


@meter_routes.route("/meters")
def get_meters_list():
    meters = Meter.query.all()
    print(meters)
    return render_template(
        "meter.html", title="Coding Challenge 1", meters=Meter.query.all()
    )


@meter_routes.route("/meters/<int:meter_id>")
def get_meter_data(meter_id):
    data = (
        MeterData.query.filter_by(meter_id=meter_id)
        .order_by(MeterData.timestamp.desc())
        .all()
    )
    return jsonify([value.to_dict() for value in data])
