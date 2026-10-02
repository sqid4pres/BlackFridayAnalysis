import pandas as pd
import sqlite3

print(" Starting your Black Friday category aggregation pipeline...")

#Remember to start by connecting to the database
conn = sqlite3.connect('project_database.db')

#grouping product IDs by category then finding the average discount of each category
category_query = """
SELECT 
    product_category,
    ROUND(AVG(discount_pct), 2) as Avg_Discount_Percentage,
    
    COUNT(Product_ID) as Total_Products_In_Category
FROM sales_table
WHERE is_black_friday = 1
GROUP BY product_category
ORDER BY Avg_Discount_Percentage DESC;
"""

print("Grouping products by shared category and calculating averages...")
df_categories = pd.read_sql_query(category_query, conn)

#Export for Tableau
output_filename = 'tableau_dashboard_data.csv'
df_categories.to_csv(output_filename, index=False)

print(f"\n Complete! Grouped data exported to '{output_filename}'")
print(df_categories)

conn.close()

