from flask import Blueprint, request
from flask import render_template, jsonify

from database import Meter, MeterData


meter_routes = Blueprint("meter_blueprint", __name__, template_folder="templates")


@meter_routes.route("/meters", methods=["GET"])
def get_meters_list():
    # Adding pagination
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    query = Meter.query.paginate(page=page, per_page=per_page)
    meters = query.items
    print(meters)
    return render_template(
        "meter.html",
        title="Coding Challenge 1",
        meters=meters,
        page=page,
        pages=query.pages,
        next_num=query.next_num,
        prev_num=query.prev_num,
        has_prev=query.has_prev,
        has_next=query.has_next,
    )


@meter_routes.route("/meters/<int:meter_id>", methods=["GET"])
def get_meter_data(meter_id):
    data = (
        MeterData.query.filter_by(meter_id=meter_id)
        .order_by(MeterData.timestamp.desc())
        .all()
    )
    return jsonify([value.to_dict() for value in data])
