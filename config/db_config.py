# Database configuration file
# ---------------------------
# Central place to manage DB credentials and connection URL

DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "github_analytics"
DB_USER = "de_user"
DB_PASSWORD = "Sanket123"   # replace with your actual password

# SQLAlchemy connection URL
DATABASE_URL = (
    f"mysql+pymysql://de_user:Sanket123"
    f"@localhost:3306/github_analytics"
)
