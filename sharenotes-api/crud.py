from sqlalchemy.orm import Session
import models
import schemas


def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.note_id == note_id).first()


def create_note(db: Session, note_id: int, note: schemas.NoteCreate):
    db_note = models.Note(note_id=note_id, title=note.title,
                          content=note.content, parent_explorer_id=note.parent_explorer_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
