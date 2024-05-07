import csv
import json
import random
import re
from faker import Faker

def load_sample_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['sample_data']

def generate_test_data(num_records, sample_data):
    fake = Faker()
    test_data = []

    for _ in range(num_records):
        # Generate fake email using Faker
        email = fake.email()

        # Select a random sample from the provided sample data for password
        sample_password = random.choice(sample_data)['password']

        # Generate fake password with at least 8 characters, including letters, numbers, and special characters
        password = fake.password(length=random.randint(8, 16),
                                  special_chars=True,
                                  digits=True,
                                  upper_case=True,
                                  lower_case=True)

        test_data.append({'Email': email, 'Password': password})

    return test_data

def write_to_csv(test_data, filename):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Email', 'Password']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in test_data:
            writer.writerow(row)

def main():
    num_records = 10
    sample_data = load_sample_data('sample_data.json')
    test_data = generate_test_data(num_records, sample_data)
    write_to_csv(test_data, 'test_data.csv')

if __name__ == "__main__":
    main()
