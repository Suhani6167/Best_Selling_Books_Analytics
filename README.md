# 📚 Best Selling Books Analytics  

## 📌 Overview  
This project analyzes **1,000+ book sales records** to identify top-selling books, authors, and genres.  
It covers **data generation, cleaning, SQL analysis, and a Power BI dashboard** for visualization.

---

## 🚀 Features  
- Generate and clean book sales data using **Python**  
- Store and query data in **MySQL**  
- Perform **data analysis** with SQL  
- Build an **interactive Power BI Dashboard**  

### **Dashboard Highlights**:
📌 Top 10 Books by Revenue  
📌 Revenue by Genre  
📌 Top Authors by Copies Sold  
📌 Monthly Revenue Trend  
📌 Average Book Price  

---

## 🛠 Skills Used  
**Python** | **Pandas** | **SQL** | **MySQL** | **Power BI** | **Data Analysis** | **Data Visualization**

---

## ⚡ How to Run the Project  

### **Step 1 — Install Required Packages**  
```bash
pip install pandas faker
Step 2 — Generate Dataset
bash
Copy code
python generate_dataset.py
This will create book_sales.csv.

Step 3 — Preprocess the Data
bash
Copy code
python preprocess_books.py
This will clean the dataset and save it as book_sales_clean.csv.

Step 4 — Load Data into MySQL
Open MySQL Workbench or Command Line

Create a database (e.g., book_sales_db)

Import book_sales_clean.csv into a table

Step 5 — Open Power BI Dashboard
Open dashboard.pbix in Power BI

Explore the interactive charts and insights

📊 Power BI Dashboard Preview
<a href="https://github.com/Suhani6167/Best_Selling_Books_Analytics/blob/main/dashboard_screenshot.png" target="_blank"> <img src="dashboard_screenshot.png" alt="Power BI Dashboard" width="800"> </a> ```