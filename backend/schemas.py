from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict

class ContactCreate(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        from_attributes=True 
    )

    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone: str = Field(..., min_length=10)
    # subject: str
    message: str = Field(..., min_length=5)

    @field_validator('first_name', 'last_name', 'message')
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Поле не може містити лише пробіли')
        return v

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        digits = "".join(filter(str.isdigit, v))
        if len(digits) < 7:
            raise ValueError('Номер телефону занадто короткий')
        return digits
