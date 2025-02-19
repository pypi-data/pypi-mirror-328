import logging
import os
from typing import List, Optional

import requests
from mcp.server import FastMCP
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.mcp_database_server.types import McpServer, McpCategory, Category

logger = logging.getLogger(__name__)

mcp = FastMCP()

@mcp.tool()
def get_server_by_slug(slug: str) -> Optional[McpServer]:
    """
    Retrieve a server from the database by its URL slug.
    
    Args:
        slug (str): The URL-friendly identifier of the server
            
    Returns:
        Optional[McpServer]: A dictionary containing server information if found, None if not found:
            - id: Unique identifier
            - name: Server name
            - author: Server author
            - package_name: Python package name
            - slug: URL-friendly identifier
            - description: Server description
            - category: Category information
            - features: List of server features
            - github_url: GitHub repository URL
            - created_at: Creation timestamp
            
    Example:
        >>> server = get_server_by_slug("my-cool-server")
        >>> print(server)
        {
            "id": 1,
            "name": "My Cool Server",
            "author": "john_doe",
            "package_name": "my_cool_server",
            "slug": "my-cool-server",
            "description": "A cool MCP server",
            "category": {"id": 1, "name": "web"},
            "features": ["feature1", "feature2"],
            "github_url": "https://github.com/user/repo",
            "created_at": "2024-01-15T10:00:00"
        }
    """
    from .database import get_session
    from .types import Server
    session = get_session()
    server = session.query(Server).filter(Server.slug == slug).first()
    return server.to_dict() if server else None


@mcp.tool()
def get_all_categories() -> List[McpCategory]:
    """
    Retrieve all available MCP server categories from the database.
    
    Returns:
        List[McpCategory]: A list of category dictionaries, each containing:
            - id: Unique identifier for the category
            - name: Category name
            - description: Category description
            - order: Display order of the category
            
    Example:
        >>> categories = get_all_categories()
        >>> print(categories)
        [
            {
                "id": 1,
                "name": "web",
                "description": "Web servers and frameworks",
                "order": 1
            },
            {
                "id": 2,
                "name": "database",
                "description": "Database servers",
                "order": 2
            }
        ]
    """
    from .database import get_session
    session = get_session()
    categories = session.query(Category).order_by(Category.order).all()
    return [category.to_dict() for category in categories]


@mcp.tool()
def save_mcp_sever(server_data: McpServer) -> Optional[McpServer]:
    """
    Save a new MCP server to the database.
    
    Args:
        server_data (McpServer): A dictionary containing server information with the following fields:
            - name: Server name
            - author: Server author
            - package_name: Python package name
            - slug: URL-friendly identifier
            - description: Server description
            - category: Server category name
            - features: List of server features
            - github_url: GitHub repository URL
            
    Returns:
        Optional[McpServer]: Dictionary containing the saved server data if successful, None if failed
        
    Example:
        >>> server_data = {
        ...     "name": "My Server",
        ...     "author": "john_doe",
        ...     "package_name": "my_server",
        ...     "slug": "my-server",
        ...     "description": "A cool server",
        ...     "category": "web",
        ...     "features": ["feature1", "feature2"],
        ...     "github_url": "https://github.com/user/repo"
        ... }
        >>> result = save_mcp_sever(server_data)
    """
    # Use existing database session
    from .database import get_session
    from .types import Server, Category, ServerFeature
    session = get_session()

    # 检查分类是否存在
    category = session.query(Category).filter(Category.name == server_data["category"]).first()
    if not category:
        logger.error(f"Category {server_data['category']} not found for server {server_data['name']}")
        return None

    # 检查 slug 是否存在
    existing_server = get_server_by_slug(server_data["slug"])
    if existing_server:
        logger.info(f"Server slug {server_data['slug']} already exists, adding author prefix")
        server_data["slug"] = f"{server_data['author']}-{server_data['slug']}"

    # 创建服务器
    server = Server(
        name=server_data["name"],
        author=server_data["author"],
        package_name=server_data["package_name"],
        slug=server_data["slug"],
        description=server_data["description"],
        category_id=category.id,
        github_url=server_data["github_url"]
    )
    session.add(server)
    session.flush()  # 获取 server.id

    # 添加特性
    for feature in server_data["features"]:
        server_feature = ServerFeature(
            server_id=server.id,
            feature=feature
        )
        session.add(server_feature)

    session.commit()
    session.refresh(server)
    return server.to_dict()


@mcp.tool()
def fetch_readme_content(github_url: str) -> str:
    """
    Fetch README content from a GitHub repository.
    
    Args:
        github_url (str): GitHub repository URL. Can be in formats:
            - https://github.com/user/repo
            - https://github.com/user/repo/
            - https://github.com/user/repo/tree/main/src/
            
    Returns:
        str: Content of the README.md file from the repository
        
    Raises:
        Exception: If README cannot be fetched from both main and master branches
        
    Example:
        >>> content = fetch_readme_content("https://github.com/user/repo")
        >>> print(content)
        '# Project Name\nProject description...'
    """
    # 移除末尾的斜杠(如果有)
    clean_url = github_url.rstrip('/')
    logger.info(f"Fetching README from {clean_url}")

    def build_readme_url(branch: str) -> str:
        """构建不同分支的README URL"""
        if f'/tree/{branch}/src/' in clean_url:
            return (clean_url
                    .replace('github.com', 'raw.githubusercontent.com')
                    .replace('/tree/', '/refs/heads/')
                    + '/README.md')
        return (clean_url
                .replace('github.com', 'raw.githubusercontent.com')
                + f'/refs/heads/{branch}/README.md')

    # 首先尝试 main 分支
    try:
        main_url = build_readme_url('main')
        logger.info(f"Building README URL for main branch: {main_url}")
        logger.info(f"Fetching README from {main_url}")
        response = requests.get(main_url)
        if response.ok:
            return response.text
    except Exception as error:
        logger.error(f"Failed to fetch README from main branch: {error}")

    # 如果 main 分支失败，尝试 master 分支
    try:
        master_url = build_readme_url('master')
        logger.info(f"Fetching README from {master_url}")
        response = requests.get(master_url)
        if response.ok:
            return response.text
        raise Exception(f"Failed to fetch README: {response.status_code}")
    except Exception as error:
        raise Exception(f"Failed to fetch README from both main and master branches: {error}")


@mcp.tool()
def get_mcp_servers(server_created_date: str) -> List[dict]:
    """
    Query the MCP servers database and return servers created on the specified date.
    
    Args:
        server_created_date (str): The date to filter servers by (format: 'YYYY-MM-DD')
        
    Returns:
        List[dict]: A list of dictionaries containing server information
        
    Example:
        >>> servers = get_mcp_servers("2024-01-15")
        >>> print(servers)
        [
            {
                "id": 1,
                "name": "Server1",
                "description": "Description1",
                "created_at": "2024-01-15T10:00:00",
                "features": ["feature1", "feature2"],
                "github_url": "https://github.com/user/repo"
            },
            ...
        ]
    """
    try:
        # Use existing database session
        from .database import get_session
        from .types import Server

        session = get_session()

        # Query using SQLAlchemy ORM
        servers = (
            session.query(Server)
            .filter(text("DATE(created_at) = DATE(:created_date)"))
            .params(created_date=server_created_date)
            .order_by(Server.created_at.desc())
            .limit(10)
            .all()
        )

        # Convert to list of dictionaries using existing to_dict method
        result = []
        for server in servers:
            server_dict = server.to_dict()
            server_dict['README'] = fetch_readme_content(github_url=server.github_url)
            server_dict['internal_link'] = "https://mcpserver.cloud/server/" + server.slug
            result.append(server_dict)

        return result

    except SQLAlchemyError as e:
        return {"error": f"Database error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


def run_server():
    if not os.getenv('POSTGRES_URL'):
        error_msg = "Error: POSTGRES_URL environment variable is not set"
        logger.error(error_msg)
        raise SystemExit(error_msg)

    mcp.run(transport='stdio')
