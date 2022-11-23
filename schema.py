from typing import Optional
from pydantic import BaseModel

class BookBase(BaseModel):
    book_name: str
    author: str
    geners: str
    location: str
    price: int

class BookAdd(BookBase):
    book_id: str

    streaming_platform: Optional[str] = None
    membership_required: bool

    class Config:
        orm_mode = True

class Book(BookAdd):
    id: int

    class Config:
        orm_mode = True

class UpdateBook(BaseModel):

    streaming_platform: Optional[str] = None
    membership_required: bool

    class Config:
        orm_mode = True