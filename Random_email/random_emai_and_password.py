import pandas as pd
import random
import string
from faker import Faker

# Initialize Faker for generating random names
fake = Faker()

# Function to generate a random email
def generate_random_email(name):
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'example.com']
    domain = random.choice(domains)
    email = f"{name.lower().replace(' ', '.')}.{random.randint(1, 1000)}@{domain}"
    return email

# Function to generate a random password
def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate random data
def generate_random_data(num_entries=10):
    data = []
    for _ in range(num_entries):
        name = fake.name()
        email = generate_random_email(name)
        password = generate_random_password()
        data.append([name, email, password])
    return data

# Generate data
num_entries = 1000 # You can change the number of entries here
data = generate_random_data(num_entries)

# Create a DataFrame
df = pd.DataFrame(data, columns=['Name', 'Email', 'Password'])

# Save to Excel
output_file = 'random_email_and_password.xlsx'
df.to_excel(output_file, index=False, engine='xlsxwriter')

print(f"Random data generated and saved to {output_file}")
