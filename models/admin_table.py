from database import Base
from sqlalchemy import Integer,String,Column

class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    age = Column(Integer)