from sqlalchemy import Boolean,Column,Integer,String
from db_handler import Base

class Book(Base):

    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    book_id = Column(String, unique=True, index=True, nullable=False)
    book_name = Column(String(255), index=True, nullable=False)
    author = Column(String(255),index=True,nullable=False
    geners = Column(String, index=True, nullable=False)
    location = Column(String, index=True, nullable=False)
    price = Column(Integer, index=True, nullable=False)
    membership_required = Column(Boolean, nullable=False, default=True)
