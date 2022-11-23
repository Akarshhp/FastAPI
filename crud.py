from sqlalchemy.orm import Session
import model
import schema


def get_book_by_book_id(db: Session, book_id: str):
    return db.query(model.Book).filter(model.Book.book_id == book_id).first()


def get_book_by_id(db: Session, sl_id: int):
    return db.query(model.Book).filter(model.Book.id == sl_id).first()

def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Book).offset(skip).limit(limit).all()


def add_book_details_to_db(db: Session, book: schema.BookAdd):

    book_details = model.Book(
        book_id=book.book_id,
        book_name=book.book_name,
        author= book.author,
        geners=book.geners,
        location=book.location,
        price=book.price,
        membership_required=book.membership_required,

    )
    db.add(book_details)
    db.commit()
    db.refresh(book_details)
    return model.Book(**book.dict())


def update_book_details(db: Session, sl_id: int, details: schema.UpdateBook):
    # book_details = db.query(model.Book).filter(model.Book.id == sl_id).firsta()
    #
    # if book_details is None:
    #     return None

    db.query(model.Book).filter(model.Book.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Book).filter(model.Book.id == sl_id).first()


def delete_book_details_by_id(db: Session, sl_id: int):

    try:
        db.query(model.Book).filter(model.Book.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
