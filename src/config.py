
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    MODEL_NAME = os.getenv('MODEL_NAME', 'gemini-2.5-flash')
    
    # Persona Details
    PERSON_NAME = "Aman Gupta"
    PERSON_TITLE = "Co-Founder & CMO"
    COMPANY = "boAt Lifestyle"
    COMPANY_PROFILE = "Consumer Electronics, 500+ employees"
    
    # Paths
    DATA_DIR = "data"
    OUTPUT_DIR = "outputs"
    
    # DSPy Optimizer Settings
    MAX_BOOTSTRAPPED_DEMOS = 2
    NUM_CANDIDATE_PROGRAMS = 6
    
    @classmethod
    def validate(cls):
        if not cls.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        print("✓ Configuration validated")
