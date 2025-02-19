import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from the env file
package_root = Path(__file__).parent
env_path = package_root / 'env'
load_dotenv(env_path)

class Settings:
    """Gateway SDK settings loaded from environment variables"""
    
    @property
    def base_url(self) -> str:
        """Get the base URL from environment variable or use default"""
        base_url = os.getenv("KOSMOY_API_BASE_URL")
        if not base_url:
            raise ValueError("KOSMOY_API_BASE_URL is not set")
        return base_url.rstrip("/")

# Global settings instance
settings = Settings()
