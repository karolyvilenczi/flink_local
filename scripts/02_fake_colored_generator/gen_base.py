import time
from faker import Faker
import csv
import os
from datetime import datetime
import random

class DataFeeder:
    def __init__(self, output_path, feed_rate):
        self.fake = Faker()
        self.output_path = output_path
        self.feed_rate = feed_rate  # records per second
        self.id_counter = 0
        self.colors = [
            'red',
            'blue',
            'green',
            'yellow',
            'purple',
            'orange',
            'pink',
            'brown',
            'black',
            'white'
        ]

    def generate_record(self):
        self.id_counter += 1
        return {
            'id': self.id_counter,
            'name': self.fake.first_name(),
            'age': random.randint(18, 80),
            'color': random.choice(self.colors)
        }

    def write_record(self, record):
        with open(self.output_path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'name', 'age', 'color'])
            writer.writerow(record)

    def run(self):
        while True:
            record = self.generate_record()
            self.write_record(record)
            time.sleep(1/self.feed_rate)