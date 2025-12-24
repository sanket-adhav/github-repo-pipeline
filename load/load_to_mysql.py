from sqlalchemy import create_engine

def load_to_db(df):
    engine = create_engine(
        "mysql+pymysql://de_user:Sanket123@localhost:3306/github_analytics"
    )

    df.to_sql(
        "github_repo_stats",
        engine,
        if_exists="append",
        index=False
    )
