import pandas as pd
from datetime import datetime

def transform_data(data):
    df = pd.DataFrame([{
        "repo_name": data["name"],
        "owner": data["owner"]["login"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "open_issues": data["open_issues_count"],
        "watchers": data["watchers_count"],
        "language": data["language"],

        # 🔥 FIX HERE
        "created_at": pd.to_datetime(data["created_at"]),
        "updated_at": pd.to_datetime(data["updated_at"]),
        "pushed_at": pd.to_datetime(data["pushed_at"]),

        "ingestion_date": datetime.now().date()
    }])

    return df
