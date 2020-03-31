import random
import string

from datetime import datetime


def generate_sequence():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))


def duration_in_ms(timestamp):
    return (datetime.now() - timestamp).total_seconds() * 1000
