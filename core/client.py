import random
import uuid
from threading import Thread
from time import sleep

from core.hook import EventHook


class DemoClient:
    def __init__(self) -> None:
        self.on_message = EventHook()
        self.mapping = {}

    @staticmethod
    def __with_delay(function, delay):
        def target():
            sleep(delay)
            function()

        Thread(target=target, daemon=True).start()

    def make_business(self, business_id):
        if business_id in self.mapping.keys():
            return Response(400, 'Business id exists in mapping')
        sequence_id = uuid.uuid4().int
        self.mapping[business_id] = sequence_id

        accept_delay = random.randrange(0, 1000) / 1000
        confirm_delay = random.randrange(0, 1000) / 1000

        self.__with_delay(lambda: self.accept(business_id, sequence_id), accept_delay)
        self.__with_delay(lambda: self.confirm(sequence_id), confirm_delay)

        return Response(200, 'OK')

    def accept(self, business_id, sequence_id):
        self.on_message.fire({
            'messageType': 'ACCEPT',
            'businessId': business_id,
            'id': sequence_id
        })

    def confirm(self, sequence_id):
        self.on_message.fire({
            'messageType': 'CONFIRM',
            'id': sequence_id
        })


class Response:
    def __init__(self, code, text) -> None:
        self.code = code
        self.text = text
