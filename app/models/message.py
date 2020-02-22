import datetime
from app import db, ma


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_received = db.Column(db.DateTime, default=datetime.datetime.now())
    method = db.Column(db.String(11), nullable=False)
    body = db.Column(db.String(255), nullable=False)
    result = db.Column(db.Float, nullable=False)

    def __init__(self, method, body, result):
        self.method = method
        self.body = body
        self.result = result


class MessageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_received', 'method', 'body', 'result')


message_schema = MessageSchema()