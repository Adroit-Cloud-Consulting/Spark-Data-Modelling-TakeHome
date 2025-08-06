import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Generate sample products
products = pd.DataFrame({
    "product_id": range(1, 21),
    "category": [random.choice(["Electronics", "Clothing", "Food"]) for _ in range(20)],
    "product_name": [f"Product_{i}" for i in range(1, 21)]
})
products.to_csv("products.csv", index=False)

# Generate sample sales
rows = []
start_date = datetime(2024, 1, 1)
for day in range(10):  # 10 days of data
    for _ in range(200):  # 200 transactions per day
        rows.append({
            "transaction_id": len(rows) + 1,
            "store_id": random.randint(1, 5),
            "product_id": random.randint(1, 20),
            "quantity": random.randint(1, 5),
            "price": round(random.uniform(5, 100), 2),
            "timestamp": (start_date + timedelta(days=day, hours=random.randint(0,23))).isoformat()
        })

sales = pd.DataFrame(rows)
sales.to_csv("sales.csv", index=False)

print("Sample CSVs generated: sales.csv & products.csv")
