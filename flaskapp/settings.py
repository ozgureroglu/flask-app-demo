import os
from dotenv import load_dotenv

load_dotenv()

VERSION = os.getenv("VERSION", "1.0.0")
SECRET_KEY = os.getenv("SECRET_KEY", "dev")
DATABASE = os.getenv("DATABASE", "flaskapp.sqlite")
TESTING = os.getenv("TESTING", False)