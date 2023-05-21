from typing import Union
from pydantic import BaseModel, Field


class NoteBase(BaseModel):
    title: str = Field(max_length=10)
    content: Union[str, None] = Field(default=None, max_length=10)
    parent_explorer_id: int


class Note(NoteBase):
    note_id: int

    class Config:
        orm_mode = True


class NoteCreate(NoteBase):
    pass
