from .engine import engine
from .Base import Base

from .Tables import *


def create_tables():
    Base.metadata.create_all(engine)
