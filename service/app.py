from fastapi import FastAPI
from dotenv import load_dotenv

# Load .env configuration
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Load views
from . import views

"""
uvicorn service.app:app --port=5004 --reload
"""
