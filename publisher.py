import pika
import json


class RabbitMQPublisher:
    def __init__(self):
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__exchange = "_minha_exchange"
        self.__rounting_key = ""
        self.__channel = self.create_channel()

    def create_channel(self) -> None:
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )
        channel = pika.BlockingConnection(connection_parameters).channel()
        print(channel)
        return channel

    def send_message(self, body: dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__rounting_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )


rabbit_mq_publisher = RabbitMQPublisher()
rabbit_mq_publisher.send_message({"msg": "Outra mensagem de teste"})
