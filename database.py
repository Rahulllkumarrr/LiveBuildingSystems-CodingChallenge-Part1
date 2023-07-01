from datetime import datetime


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Meter(db.Model):
    __tablename__ = "meters"

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)

    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return self.label


class MeterData(db.Model):
    __tablename__ = "meter_data"

    id = db.Column(db.Integer, primary_key=True, index=True)
    meter_id = db.Column(db.Integer, db.ForeignKey("meters.id"), nullable=False)
    timestamp = db.Column(db.DateTime)
    value = db.Column(db.Integer)

    meter = db.relationship("Meter", backref="meter_data")

    def __init__(self, meter_id, value, timestamp: datetime = None):
        self.meter_id = meter_id
        self.timestamp = datetime.utcnow() if not timestamp else timestamp
        self.value = value

    def __repr__(self):
        return f"{self.meter_id}[{self.timestamp}] : {self.value}"

    def to_dict(self):
        return {
            "id": self.id,
            "meter_id": self.meter_id,
            "timestamp": self.timestamp,
            "value": self.value,
        }
