# Adroit Data Engineer Capability Assessment

**Duration:** ~1 hour**Deliverable:** A GitHub repository containing:

- Your code (PySpark, Python, SQL/DBT models)
- Any supporting files or scripts
- A `README.md` explaining your approach, reasoning, and data model diagram

This assessment is designed to evaluate your ability to:

- Engineer data pipelines using Spark and Python
- Design robust data models for analytics
- Work with modern ELT tools like DBT
- Optimise for large-scale datasets and justify technical decisions

---

## **Scenario**

You are a Data Engineer at a retail company selling products online and in stores.
Management wants to **analyse daily sales** to identify top products and underperforming stores.

You are given two CSV files (generated locally using the provided Python script):

1. **`sales.csv`**

   - `transaction_id`
   - `store_id`
   - `product_id`
   - `quantity`
   - `price`
   - `timestamp` (UTC)
2. **`products.csv`**

   - `product_id`
   - `category`
   - `product_name`

Your task is to create a **local data pipeline** using PySpark and DBT concepts to analyse the data and design a scalable model.

---

## **Tasks**

### **1. Data Ingestion and Cleaning (PySpark)**

- Load the two CSVs into Spark DataFrames.
- Ensure proper data types (numeric, timestamp).
- Remove duplicate transactions and handle null values.

**Justify in your README:**

- How you handled missing or inconsistent data.
- Why you chose your approach for schema enforcement.

---

### **2. Data Transformation and Aggregation**

- Calculate **total sales per store per day**.
- Identify the **top 5 products by revenue** across all stores.
- Identify **stores with zero sales on any given day**.

**Justify:**

- Which Spark functions you used for aggregation and why.
- How your approach would scale for millions of rows.

---

### **3. Data Modelling**

- Propose a **dimensional data model** (Star Schema or similar) to support analytics.
- Include a **diagram** in your repo (image or PDF is fine).

**Justify:**

- Why this model supports efficient analytics.
- Key design decisions and trade-offs.

---

### **4. Optimisation & Spark Internals**

- Explain in your `README.md` how you would **optimise** this pipeline for very large datasets:
  - Partitioning or bucketing strategy
  - File formats and storage considerations
  - Spark execution optimisations (caching, shuffles, etc.)

**Justify:**

- Specific Spark internal behaviours that inform your choices.

---

### **5. DBT & SQL Transformation Task**

- Assume you are building a **daily sales mart** for Snowflake or Databricks using DBT.
- Create a **DBT model** (just the `.sql` file and a `schema.yml`) that:
  1. Aggregates `sales.csv` by `store_id` and `date(timestamp)` to calculate `daily_revenue`.
  2. Joins product information from `products.csv` to provide a human-readable report.
- Write a short explanation in `README.md`:
  - How DBT helps in a modern ELT pipeline.
  - How you would use **tests** and **documentation** in DBT for this model.

**Justify:**

- Why DBT is valuable in managing transformations.
- How this approach integrates with Snowflake or Databricks.

---

### **6. Submission Instructions**

1. Create a **GitHub repository** (public or private).
2. Include:
   - Your PySpark and Python code
   - DBT `.sql` model and `schema.yml`
   - Data model diagram
   - Updated `README.md` with your justifications
3. Send the repository link to the Adroit team.

---

## **Assessment Expectations**

- Use **PySpark** locally (no cloud infra needed).
- DBT models can be created as files without execution.
- You **may use AI tools** to assist, but you **must explain any AI-generated code** and why it was useful.
- Your code should be clear, modular, and runnable by a reviewer with local Spark.

---

## **Follow-Up Interview**

- A senior Adroit engineer will review your solution with you.
- Be prepared to **justify your decisions**, including:
  - Data cleaning approach
  - Spark internals and performance
  - Data model and DBT usage

**Good luck, and thank you for taking the time to complete this assessment!**
