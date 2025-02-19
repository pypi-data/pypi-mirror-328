import os
from dotenv import load_dotenv

# Load environment variables from .env.local file
load_dotenv()

# PostgreSQL configuration
database_url = os.getenv('POSTGRES_URL', '')
# Convert postgres:// to postgresql:// if necessary
DATABASE_URL = database_url.replace('postgres://', 'postgresql://', 1) if database_url else ''
