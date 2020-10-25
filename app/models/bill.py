from sqlalchemy import Boolean, Column, Integer, String, DateTime, Float
from datetime import datetime
from app.database import Base


class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float)
    type_bill = Column(String)
    was_paid = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.now())
    date_paid = Column(DateTime, default=None)
    CPF = Column(String, unique=True)