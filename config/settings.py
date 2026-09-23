import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env file."""

    # API Keys
    openai_api_key: str = Field(..., description="OpenAI API Key for agents")
    serpapi_api_key: str | None = Field(None, description="SerpAPI Key for Google Search")
    tavily_api_key: str | None = Field(None, description="Tavily API Key for web search")

    # Storage Settings
    database_url: str = Field("sqlite:///./internships.db", description="Database Connection String")

    # Execution Thresholds
    log_level: str = Field("INFO", description="Logging verbosity level")
    max_search_results: int = Field(10, description="Max search results fetched per run")
    min_match_score_threshold: float = Field(75.0, description="Minimum score to trigger drafting")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


# Instantiate global settings object
try:
    settings = Settings()
except Exception as e:
    print(f"Configuration Error: Ensure your .env file is properly set up.\nDetails: {e}")