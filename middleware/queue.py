import json
import pika

from middleware.models import VisitLog

class Queue(object):
    def __init__(self, exchange, queue):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost'))
        self.channel = connection.channel()
        self.exchange = exchange
        self.queue = queue
        self.channel.queue_declare(queue=queue,
            durable=True)

    def push_message(self, message):
        self.channel.basic_publish(
            exchange=self.exchange, routing_key=self.queue,
                body=message)

    def consume_message(self, ch, method, _props, body):
        kwargs = json.loads(body)
        VisitLog.objects.create(**kwargs)
        print "{ visit_queue }",kwargs
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.channel.basic_consume(self.consume_message,
            queue=self.queue)
        self.channel.start_consuming()