from database import Base
from sqlalchemy import Column, Integer, Float, String


class Note(Base):
    __tablename__ = "notes"
    note_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=False)
    content = Column(String, unique=False)
    parent_explorer_id = Column(Integer, unique=False)

    def __init__(self, note_id=None, title=None, content=None, parent_explorer_id=None):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.parent_explorer_id = parent_explorer_id

    def update_dict(self, dict):
        for name, value in dict.items():
            setattr(self, name, value)
