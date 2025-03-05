import csv
import random
from faker import Faker

# Initialize Faker for generating names
fake = Faker()

def gen_fake_data():
    print("Generating data...")

    # Create 50 sample records
    records = []
    for i in range(50):
        record = [
            i + 1,  # id
            fake.first_name(),  # name
            random.randint(18, 80)  # age
        ]
        records.append(record)

    # Write to CSV file
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for record in records:
            writer.writerow(record)

    print("Done...")
    

if __name__ == "__main__":
    print("Started directly..")
    gen_fake_data()
else:
    print("Started as a module...")    
    gen_fake_data()
