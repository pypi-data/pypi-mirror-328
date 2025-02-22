"""Configuration module for DevOpsAI."""

import os
import logging

def get_api_url():
    """Get the API URL from environment variables."""
    api_url = os.environ.get("DEVOPSAI_API_URL")
    if not api_url:
        logging.error("DEVOPSAI_API_URL environment variable is not set")
        raise ValueError("API URL not configured. Set the DEVOPSAI_API_URL environment variable.")
    return api_url

def get_api_key():
    """Get the API key from environment variables (optional)."""
    return os.environ.get("DEVOPSAI_API_KEY")