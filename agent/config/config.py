from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv(override=True)

class Settings(BaseSettings):
    """
    A class to manage application settings using Pydantic's BaseSettings.

    Attributes:
        GROQ_API_KEY (str): The API key for Groq API service.
        GROQ_MODEL (str): The model identifier for Groq API.
    """
    GROQ_API_KEY: str = Field(..., env="GROQ_API_KEY")
    GROQ_MODEL: str = Field(..., env="GROQ_MODEL")
    TAVILY_API_KEY: str = Field(..., env="TAVILY_API_KEY")
    LANGSMITH_API_KEY: str = Field(..., env="LANGSMITH_API_KEY")
    LANGSMITH_TRACING : bool = Field(..., env="LANGSMITH_TRACING")
    LANGSMITH_ENDPOINT : str = Field(..., env="LANGSMITH_ENDPOINT")
    LANGSMITH_PROJECT : str = Field(..., env="LANGSMITH_PROJECT")
    class Config:
        """
        Configuration for the Settings class.

        Attributes:
            env_file (str): Path to the environment file (.env) containing configuration values.
        """
        env_file = ".env"

settings = Settings()