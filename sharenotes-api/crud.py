from sqlalchemy.orm import Session
import models
import schemas


def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.note_id == note_id).first()


def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(title=note.title,
                          content=note.content, parent_explorer_id=note.parent_explorer_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def update_note(db: Session, note: schemas.Note):
    db_note = get_note(db, note.note_id)
    # TODO: 存在しない場合、エラーをraiseする。
    db_note.update_dict(note.dict())
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, note_id: int):
    db_note = get_note(db, note_id)
    db.delete(db_note)
    db.commit()
