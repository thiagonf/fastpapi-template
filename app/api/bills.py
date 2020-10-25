from fastapi import APIRouter, Depends
from typing import List
from app import models, schemas, database
from sqlalchemy.orm import Session
from app.auth.user import oauth2_scheme


router = APIRouter()


@router.get("/bills", response_model=List[schemas.bill.Bill])
def get_bills(skip: int = 0, limit: int = 100,
              db: Session = Depends(database.get_db),
              token: str = Depends(oauth2_scheme)):
    """
    Create an item with all the information:

    - **CPF**: CPF by owner bill
    - **value**: value R$ bill
    - **type_bill**: type of bill
    - **was_paid**: boolean if bill was paid
    - **date_created**: datetime when bill was create
    - **date_paid**: datetime when bill was paid

    **Parameters**:
    - **skip**: number of page
    """
    return db.query(models.bill.Bill).offset(skip).limit(limit).all()


@router.post("/bills", response_model=schemas.bill.Bill, response_description="The created bill",)
async def post_bills(bill: schemas.bill.Bill, db: Session = Depends(database.get_db)):
    db_item = models.bill.Bill(**bill.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return bill
