import pandas as pd

# Load CSV
df = pd.read_csv('book_sales.csv')

# Quick cleaning
df.dropna(inplace=True)  # Remove missing values if any
df['Title'] = df['Title'].str.strip()  # Remove extra spaces
df['Author'] = df['Author'].str.title()  # Standardize author names

# Add new column: Revenue check (optional, for demonstration)
df['Revenue_Check'] = df['Price'] * df['Copies_Sold']

# Keep only relevant columns
df = df[['Book_ID', 'Title', 'Author', 'Genre', 'Price', 'Copies_Sold', 'Revenue', 'Sale_Date']]

# Save cleaned CSV
df.to_csv('book_sales_clean.csv', index=False)
print("Preprocessing complete, cleaned CSV saved!")
