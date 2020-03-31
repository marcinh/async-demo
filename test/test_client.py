from time import sleep
from typing import List
from unittest import TestCase

from core.client import DemoClient
from core.timing import Timing
from test import generate_sequence


class TestClientDemo(TestCase):
    mapping = {}
    timings = []  # type: List[Timing]

    def test_client_example(self):
        client = DemoClient()
        client.on_message += self.just_print

        for i in range(0, 10):
            business_id = generate_sequence()
            client.make_business(business_id)

            print('Making business with business id: ' + business_id)
            sleep(1)

    def test_timing(self):
        self.assertEqual(len(self.timings), 10)
        self.assertEqual(0, len([t for t in self.timings if t.accept_duration is None or t.confirm_duration is None]))

    @staticmethod
    def just_print(json):
        print(json)
