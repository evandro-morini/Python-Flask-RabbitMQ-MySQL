from app import db
from flask import jsonify
from ..models.message import Message, message_schema


class Operations:
    def __init__(self, message):
        self.func_name = message['method']
        self.number_list = message['list']
        self.raw_content = message
        self.result = 0

    def calculate(self):
        if self.func_name == 'sum':
            for index, item in enumerate(self.number_list):
                if index == 0:
                    self.result = item
                else:
                    self.result += item
        elif self.func_name == 'subtract':
            for index, item in enumerate(self.number_list):
                if index == 0:
                    self.result = item
                else:
                    self.result -= item
        elif self.func_name == 'divide':
            for index, item in enumerate(self.number_list):
                if index == 0:
                    self.result = item
                else:
                    self.result /= item
        elif self.func_name == 'multiply':
            for index, item in enumerate(self.number_list):
                if index == 0:
                    self.result = item
                else:
                    self.result *= item
        self.saveMessage()


    def saveMessage(self):
        message = Message(self.func_name, self.raw_content, self.result)
        try:
            db.session.add(message)
            db.session.commit()
            message_schema.dump(message)
        except:
            return jsonify({'Message': 'MySQL error while inserting data'}), 500