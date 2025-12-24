-- ================================
-- GitHub Repository Analytics DB
-- ================================

-- 1️⃣ Create database
CREATE DATABASE IF NOT EXISTS github_analytics;
USE github_analytics;

-- 2️⃣ Create table
CREATE TABLE IF NOT EXISTS github_repo_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,

    repo_name VARCHAR(100) NOT NULL,
    owner VARCHAR(100) NOT NULL,

    stars INT,
    forks INT,
    open_issues INT,
    watchers INT,

    language VARCHAR(50),

    created_at DATETIME,
    updated_at DATETIME,
    pushed_at DATETIME,

    ingestion_date DATE NOT NULL,

    created_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3️⃣ (Recommended) Prevent duplicate records per day
CREATE UNIQUE INDEX uniq_repo_day
ON github_repo_stats (repo_name, ingestion_date);

-- 4️⃣ Useful indexes for analytics
CREATE INDEX idx_ingestion_date ON github_repo_stats (ingestion_date);
CREATE INDEX idx_repo_name ON github_repo_stats (repo_name);
