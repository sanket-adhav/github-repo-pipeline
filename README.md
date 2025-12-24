# 🚀 GitHub Repository Analytics Pipeline

An end-to-end **Data Engineering ETL pipeline** that ingests GitHub repository metadata using the GitHub REST API, transforms raw JSON data into structured format, and loads **daily snapshot data into MySQL** for analytics and trend analysis.

This project demonstrates real-world data engineering concepts such as snapshot-based ingestion, datetime normalization, database schema design, and SQL analytics.

---

## 📌 Problem Statement

GitHub repository metrics such as stars, forks, open issues, and activity timestamps change over time.
To analyze repository growth and trends, we need a pipeline that:

* Fetches repository data from GitHub
* Stores historical snapshots
* Enables SQL-based time-series analytics

---

## 🧠 Solution Overview

This project implements a **snapshot-based ETL pipeline**.
Each pipeline execution captures the **current state** of a GitHub repository and stores it in MySQL. Running the pipeline daily builds historical data for analysis.

---

## 🏗️ Architecture

```
GitHub REST API
      ↓
Python (requests)
      ↓
Data Transformation (pandas)
      ↓
MySQL (Snapshot Table)
      ↓
SQL Analytics
```

---

## ⚙️ Tech Stack

* **Language:** Python 3
* **API:** GitHub REST API
* **Database:** MySQL 8
* **Libraries:**

  * requests
  * pandas
  * sqlalchemy
  * pymysql
  * cryptography
* **Concepts:**

  * ETL pipeline
  * Snapshot-based ingestion
  * Datetime normalization (ISO 8601 → MySQL)
  * SQL window functions
  * Database indexing & constraints

---

## 📂 Project Structure

```
GITHUB_REPO_PIPELINE/
│
├── config/
│   └── db_config.py               # Database configuration (credentials, URL)
│
├── extract/
│   └── fetch_github_data.py       # Fetch data from GitHub REST API
│
├── transform/
│   └── clean_transform.py         # Data cleaning & datetime normalization
│
├── load/
│   ├── load_to_mysql.py           # Load transformed data into MySQL
│   └── test_connection.py         # Test MySQL connectivity
│
├── sql/
│   ├── analytics_queries.sql      # SQL analytics & reporting queries
│   └── mysql_schema.sql           # Database & table creation script
│
├── main.py                        # ETL pipeline orchestration
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 🔄 ETL Workflow

1. **Extract**
   - Fetch repository metadata from GitHub REST API.

2. **Transform**
   - Convert JSON response to structured DataFrame.
   - Normalize ISO 8601 timestamps to MySQL-compatible datetime.
   - Add ingestion date for snapshot tracking.

3. **Load**
   - Insert snapshot data into MySQL using SQLAlchemy.
   - Enforce one-record-per-day using a unique constraint.

---

## 🗄️ Database Schema

Key table: `github_repo_stats`

| Column Name    | Description |
|---------------|-------------|
| repo_name      | Repository name |
| owner          | Repository owner |
| stars          | Star count |
| forks          | Fork count |
| open_issues    | Open issues |
| watchers       | Watchers count |
| language       | Primary language |
| created_at     | Repository creation time |
| updated_at     | Last update time |
| pushed_at      | Last push time |
| ingestion_date | Snapshot date |

A **composite unique index** ensures only one snapshot per repository per day.

---

## 📊 Sample SQL Analytics

### Daily Star Growth
```sql
SELECT
  ingestion_date,
  stars,
  stars - LAG(stars) OVER (ORDER BY ingestion_date) AS daily_growth
FROM github_repo_stats;
````

### Latest Repository Snapshot

```sql
SELECT *
FROM github_repo_stats
ORDER BY ingestion_date DESC
LIMIT 1;
```

### Repository Activity

```sql
SELECT repo_name, MAX(pushed_at) AS last_commit
FROM github_repo_stats
GROUP BY repo_name;
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Create Database & Table

```bash
mysql -u de_user -p < sql/mysql_schema.sql
```

### 3️⃣ Test MySQL Connection

```bash
python load/test_connection.py
```

### 4️⃣ Run ETL Pipeline

```bash
python main.py
```

---

## ⏰ Automation

The pipeline can be scheduled to run daily using:

* Windows Task Scheduler
* cron (Linux)

Each run captures a new snapshot for historical analysis.

---

## 🚧 Challenges Solved

* MySQL 8 authentication with PyMySQL
* ISO 8601 datetime conversion
* Snapshot-based data modeling
* Database user security (non-root access)

---

## 🔮 Future Enhancements

* Multi-repository ingestion
* Incremental ingestion based on data changes
* Retry & alerting mechanisms
* Cloud deployment (AWS S3 + RDS)
* BI dashboard integration

---

## 💼 Resume Description

Built an end-to-end Data Engineering ETL pipeline using GitHub REST API, Python, Pandas, and MySQL. Implemented snapshot-based ingestion, normalized API timestamps, handled MySQL authentication, and enabled SQL analytics using window functions to track repository growth trends.

---

## 👤 Author

**Sanket Aba Adhav**
Aspiring Data Engineer
