from pydantic import BaseModel


class Note(BaseModel):
    note_id: int
    title: str
    content: str
    parent_explorer_id: int

    class Config:
        orm_mode = True
