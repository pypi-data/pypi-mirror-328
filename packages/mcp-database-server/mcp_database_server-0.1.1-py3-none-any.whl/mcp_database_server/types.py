from datetime import datetime
from typing import List
from typing import TypedDict, Optional

from slugify import slugify
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class McpServer(TypedDict):
    name: str
    author: str
    package_name: str
    slug: str
    description: str
    category: str
    features: List[str]
    github_url: Optional[str]
    stars: Optional[int]
    watchers: Optional[int]
    forks: Optional[int]
    created_at: datetime
    config: Optional[str]


class McpClient(TypedDict):
    id: Optional[int]
    name: str
    author: str
    package_name: str
    slug: str
    description: str
    features: Optional[List[str]]
    github_url: Optional[str]
    stars: Optional[int]
    watchers: Optional[int]
    forks: Optional[int]
    created_at: Optional[datetime]
    config: Optional[str]


class GitHubStats(TypedDict):
    stars: int
    watchers: int
    forks: int


class McpCategory(TypedDict):
    id: int
    name: str
    order: int
    emoji: str
    description: str
    created_at: datetime


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    order = Column(Integer)
    emoji = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self) -> McpCategory:
        return {
            "id": self.id,
            "name": self.name,
            "order": self.order,
            "emoji": self.emoji,
            "description": self.description,
            "created_at": self.created_at
        }


class ServerFeature(Base):
    __tablename__ = "server_features"

    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("servers.id"))
    feature = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    author = Column(String)
    package_name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    github_url = Column(String, unique=True, index=True)
    stars = Column(Integer, nullable=True)
    watchers = Column(Integer, nullable=True)
    forks = Column(Integer, nullable=True)
    github_stats_updated_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    config = Column(String, nullable=True)

    # Relationships
    features = relationship("ServerFeature", backref="server")
    category = relationship("Category")

    @staticmethod
    def create(
            name: str,
            author: str,
            package_name: str,
            description: str,
            category: str,
            features: List[str],
            github_url: str
    ) -> McpServer:
        return {
            "name": name,
            "author": author,
            "package_name": package_name,
            "slug": slugify(name),
            "description": description,
            "category": category,
            "features": features,
            "github_url": github_url,
            "created_at": datetime.utcnow(),
            "config": None,
            "stars": None,
        }

    def to_dict(self) -> McpServer:
        return {
            "name": self.name,
            "author": self.author,
            "package_name": self.package_name,
            "slug": self.slug,
            "description": self.description,
            "category": self.category.name if self.category else None,
            "features": [f.feature for f in self.features],
            "github_url": self.github_url,
            "stars": self.stars,
            "watchers": self.watchers,
            "forks": self.forks,
            "created_at": self.created_at,
            "config": self.config
        }


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    frequency = Column(String)  # daily, weekly, monthly, custom
    cron_expression = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    # Relationships
    executions = relationship("TaskExecution", backref="task")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "frequency": self.frequency,
            "cron_expression": self.cron_expression,
            "created_at": self.created_at,
            "is_active": self.is_active
        }


class TaskExecution(Base):
    __tablename__ = "task_executions"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"))
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(String, default="pending")  # pending, success, failed
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    error_message = Column(String, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "scheduled_time": self.scheduled_time,
            "status": self.status,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "error_message": self.error_message
        }
