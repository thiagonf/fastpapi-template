from pydantic import BaseModel, ValidationError, validator
from enum import Enum
from datetime import datetime
from typing import Optional


class TypeBill(str, Enum):
    IPTU = "IPTU"
    IPVA = "IPVA"
    MULTA = "MULTA"


class Bill(BaseModel):
    CPF: str
    value: float
    type_bill: TypeBill
    was_paid: bool = False
    date_created: datetime = datetime.now()
    date_paid: Optional[datetime] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "value": 10.5,
                "type_bill": "IPTU",
                "was_paid": False,
                "date_created": "2020-10-20T16:47:36.145000",
                "date_paid": "2020-10-20T16:47:36.145000",
                "CPF": "111.111.111-11"
            }
        }

    @validator('CPF')
    def validate_cpf(cls, v):
        cpf = v.replace(".", "").replace("-", "")
        if check_number_cpf(int(cpf)):
            return cpf
        else:
            raise ValueError('invalid CPF')


def check_number_cpf(numbers):
    # Verifica se o CPF possui 11 números:
    if len(numbers) != 11:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True
