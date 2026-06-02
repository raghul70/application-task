from database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    completed = Column(Boolean,default=False)