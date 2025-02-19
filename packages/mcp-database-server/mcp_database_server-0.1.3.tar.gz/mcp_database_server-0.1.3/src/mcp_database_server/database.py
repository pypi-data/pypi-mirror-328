from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool

from .config import DATABASE_URL

# Create engine with custom pool settings
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "sslmode": "require"
    },
    # 增加连接池配置
    poolclass=QueuePool,
    pool_size=20,  # 增加池大小
    max_overflow=30,  # 增加最大溢出连接数
    pool_timeout=60,  # 增加超时时间
    pool_pre_ping=True,  # 启用连接检查
    pool_recycle=3600,  # 一小时后回收连接
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a session for use in scripts
def get_session():
    return SessionLocal() 