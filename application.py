from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="book Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_address_book', response_model=List[schema.Book])
def retrieve_all_book_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    book = crud.get_book(db=db, skip=skip, limit=limit)
    return book


@app.post('/add_new_book', response_model=schema.BookAdd)
def add_new_book(movie: schema.BookAdd, db: Session = Depends(get_db)):
    book_id = crud.get_book_by_book_id(db=db, book_id=book.book_id)
    if book_id:
        raise HTTPException(status_code=400, detail=f"book id {book.book_id} already exist in database: {book_id}")
    return crud.add_book_details_to_db(db=db, book=book)


@app.delete('/delete_book_by_id')
def delete_book_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_book_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_book_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_book_details', response_model=schema.Book)
def update_movie_details(sl_id: int, update_param: schema.UpdateBook, db: Session = Depends(get_db)):
    details = crud.get_book_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_book_details(db=db, details=update_param, sl_id=sl_id)