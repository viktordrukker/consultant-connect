import os
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, validator
from typing import Optional, Dict, Any

class Settings(BaseSettings):
    """
    Application settings using Pydantic BaseSettings.
    Reads environment variables automatically.
    """
    PROJECT_NAME: str = "Consultant Connect"
    API_V1_STR: str = "/api/v1"

    # Database settings
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: Optional[PostgresDsn] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        """
        Assemble the database connection string from individual components
        if it's not provided directly.
        """
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    # JWT Settings
    SECRET_KEY: str  # Needs to be set in environment
    # 60 minutes * 24 hours * 7 days = 7 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        # Specifies the file to load environment variables from
        env_file = ".env"
        # Makes Pydantic Settings case-insensitive regarding environment variables
        case_sensitive = False

# Instantiate settings
settings = Settings()
