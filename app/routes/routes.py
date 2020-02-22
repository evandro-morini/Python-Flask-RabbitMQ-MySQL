from app import app
from ..controllers import main, rabbit_mq


@app.route('/', methods=['GET'])
def home():
    return main.home()

@app.route('/publish', methods=['POST'])
def publish():
    return rabbit_mq.send()

@app.route('/consume', methods=['GET'])
def receive():
    return rabbit_mq.receive()