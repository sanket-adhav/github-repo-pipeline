-- Latest snapshot
SELECT *
FROM github_repo_stats
ORDER BY ingestion_date DESC
LIMIT 1;

-- Star growth over time
SELECT
  ingestion_date,
  stars,
  stars - LAG(stars) OVER (ORDER BY ingestion_date) AS daily_growth
FROM github_repo_stats;

-- Repo activity
SELECT repo_name, MAX(pushed_at) AS last_commit
FROM github_repo_stats
GROUP BY repo_name;
