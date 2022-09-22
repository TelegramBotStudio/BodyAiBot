from tgbot.models.db import TimedBaseModel, db


class Subscription(TimedBaseModel):
    __tablename__ = "subscriptions"

    id = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False)
    duration = db.Column(db.Interval, nullable=False)
