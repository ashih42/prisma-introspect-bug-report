from sqlalchemy import *


DATABASE_URL = "sqlite:///doge.db"
engine = create_engine(DATABASE_URL, echo=True)
