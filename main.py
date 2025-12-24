from extract.fetch_github_data import fetch_repo_data
from transform.clean_transform import transform_data
from load.load_to_mysql import load_to_db

def run_pipeline():
    raw_data = fetch_repo_data("apache", "spark")
    df = transform_data(raw_data)
    load_to_db(df)

if __name__ == "__main__":
    run_pipeline()
