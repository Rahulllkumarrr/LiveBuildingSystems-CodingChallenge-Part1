import random
from datetime import datetime, timedelta

from faker import Faker

from database import db, Meter, MeterData


fake = Faker()


def insert_fake_data(app, db, no_of_labels: int = 20, no_of_values: int = 100):
    # try:
    with app.app_context():
        for _ in range(no_of_labels):
            # generating Fake Meter Name
            label = fake.bothify(text="Meter : ?????-#########")
            meter = Meter(label)
            db.session.add(meter)
            db.session.commit()

            start_timestamp = datetime.utcnow() - timedelta(minutes=no_of_values)
            for _ in range(no_of_values):
                # adding meter_id, value and custom timestamp
                start_timestamp = start_timestamp + timedelta(minutes=1)
                meter_data = MeterData(
                    meter_id=meter.id,
                    value=random.randint(100, 200),
                    timestamp=start_timestamp,
                )
                db.session.add(meter_data)
            db.session.commit()

        return {"success": True, "message": "Data Inserted Successfully"}
    # except Exception as e:
    #     return {"success": False, "message": str(e)}
