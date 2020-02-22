import pika, json
from flask import request, jsonify, current_app
from .operations import Operations


def send():
    url = current_app.config['RABBIT_MQ_URI']
    connection = pika.BlockingConnection(pika.ConnectionParameters(url))
    channel = connection.channel()
    channel.queue_declare(queue='operations', durable=True)

    try:
        channel.basic_publish(exchange='',
                              routing_key='operations',
                              body=json.dumps(request.json),
                              properties=pika.BasicProperties(
                              delivery_mode=2,
                              ))
        connection.close()

        return jsonify({'Message': 'Data sent to consumer'}), 200
    except:
        return jsonify({'Message': 'Error sending data to consumer'}), 500


def receive():
    url = current_app.config['RABBIT_MQ_URI']
    connection = pika.BlockingConnection(pika.ConnectionParameters(url))
    channel = connection.channel()
    channel.queue_declare(queue='operations', durable=True)

    try:
        def callback(ch, method, properties, body):
            data = json.loads(body)
            op = Operations(data)
            op.calculate()

        channel.basic_consume(queue='operations', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
    except:
        return jsonify({'Message': 'Error while consuming queue'}), 500