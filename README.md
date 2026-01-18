# NLP-to-SQL Converter

A lightweight analytics tool that allows non-technical users to query structured datasets using natural language.  
The system translates English queries such as:

> "total quantity by country"  
> "count orders by description"  

into valid SQL queries and executes them against user-uploaded CSV datasets.

This enables fast, self-service data insights without requiring SQL knowledge.

---

## 🎯 Motivation

Business teams often ask analytical questions in natural language, such as:

- "How many orders came from the UK?"
- "What are the top selling products?"
- "Which city generated the highest revenue?"

This tool bridges the gap between **business language → SQL** by automatically generating analytical queries and showing results directly.

---

## ✨ Key Features

- 🗂 **Upload any CSV dataset**
- 🔎 **Detect columns automatically**
- 💬 **Parse natural language queries**
- 🧮 **Supports analytical operations**
  - SUM / TOTAL
  - COUNT
  - AVERAGE
- 📊 **Supports grouping (via 'by')**
  - e.g., `total quantity by country`
- 🧾 **Shows generated SQL**
  - useful for debugging + transparency
- 📂 **Runs the SQL on SQLite backend**
- 🖥 **Interactive UI using Streamlit**

---

## 🧠 Example Queries

Supported natural language patterns:

```
total quantity by country
total quantity by description
count orders by country
count orders by description
average quantity by country
```

Example output SQL:

```sql
SELECT Country, SUM(Quantity)
FROM uploaded
GROUP BY Country;
```

---

## 🛠 Tech Stack

| Component | Tech |
|---|---|
| UI | Streamlit |
| Backend | Python |
| Engine | SQLite |
| Data Processing | Pandas |
| NLP | Template-based parsing |
| Querying | SQL |

---

## 📂 Folder Structure

```
nlp-to-sql-converter/
  ├── app.py
  ├── parser.py
  ├── sql_generator.py
  ├── executor.py
```

---

## 🏗 Architecture

```
User Query
     ↓
NLP Parser (operation + metric + group)
     ↓
SQL Generator
     ↓
SQLite Execution
     ↓
Result Table
```

---

## 📁 Dataset Example (E-Commerce)

Used the **Online Retail (E-Commerce)** dataset from Kaggle:  
https://www.kaggle.com/datasets/lakshmi25npathi/online-retail-dataset

Sample columns:

```
InvoiceNo, Description, Quantity, UnitPrice, CustomerID, Country, InvoiceDate
```

---

## 🔍 How It Works

1. User uploads CSV file  
2. DataFrame → SQLite table  
3. User enters natural language query  
4. Parser extracts:
   - operation (sum/count/avg)
   - metric (quantity)
   - grouping (country)
5. SQL generated
6. Results displayed

---

## 🚀 Running Locally

```bash
pip install streamlit pandas
streamlit run app.py
```

---

## 🌱 Future Enhancements

- Support filters:  
  e.g., `total sales in UK`
- Support revenue metric (price × quantity)
- Support time analytics (month, year)
- Support multiple datasets
- Support JOINs
- LLM-based SQL generation

---

## 🎤 Why This Project?

This project demonstrates:

✔ natural language understanding  
✔ analytical & business reasoning  
✔ solution engineering mindset  
✔ debugging & transparency (SQL shown)  
✔ user-focused tooling  
✔ data insights workflow  

---

## 👤 Author

**Nishtha Mendiratta**  
B.Tech Computer Science (Data Science)  
Passionate about data, analytics, tooling & business problem solving.  

---

