from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://de_user:Sanket123@localhost:3306/github_analytics"
)

with engine.connect() as conn:
    print("MySQL connection successful 🎉")
