from sqlalchemy.orm import Session
import models


def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.note_id == note_id).first()
