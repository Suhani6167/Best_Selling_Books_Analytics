# Step 1: Generate realistic book sales data
import pandas as pd
from faker import Faker
import random

fake = Faker()

# Define genres
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Sci-Fi', 'Romance', 'Self-Help', 'Business']

# Generate 1000 book sales records
data = []
for i in range(1, 1001):
    book_id = i
    title = fake.sentence(nb_words=4).replace('.', '')
    author = fake.name()
    genre = random.choice(genres)
    price = round(random.uniform(5, 50), 2)  # realistic book price
    copies_sold = random.randint(50, 1000)   # realistic sales numbers
    sale_date = fake.date_between(start_date='-1y', end_date='today')
    revenue = round(price * copies_sold, 2)
    data.append([book_id, title, author, genre, price, copies_sold, revenue, sale_date])

# Create DataFrame
df = pd.DataFrame(data, columns=['Book_ID', 'Title', 'Author', 'Genre', 'Price', 'Copies_Sold', 'Revenue', 'Sale_Date'])

# Save CSV inside your project folder
df.to_csv('book_sales.csv', index=False)
print("Dataset created successfully!")
