import models
import schemas
import crud
import uvicorn
from typing import Annotated, Union

from fastapi import Depends, FastAPI, Path, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/notes/{note_id}", response_model=schemas.Note)
async def get_note_by_id(note_id: int, db: Session = Depends(get_db)) -> models.Note:
    db_note = crud.get_note(db, note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note note found")
    return db_note


@app.post("/notes", response_model=schemas.Note)
async def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)


@app.put("/notes", response_model=schemas.Note)
async def updat_note(note: schemas.Note, db: Session = Depends(get_db)):
    return crud.update_note(db, note)


@app.delete("/notes/{note_id}")
async def delete_note(note_id: Annotated[int, Path(title="The ID of the note to get")], db: Session = Depends(get_db)):
    crud.delete_note(db, note_id)


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
