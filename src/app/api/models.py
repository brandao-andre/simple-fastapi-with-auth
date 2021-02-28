from pydantic import BaseModel, Field, EmailStr


class NoteSchema(BaseModel):
   title: str = Field(..., min_length=3, max_length=50)
   description: str = Field(..., min_length=3, max_length=50)


class NoteDB(NoteSchema):
    id: int


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

