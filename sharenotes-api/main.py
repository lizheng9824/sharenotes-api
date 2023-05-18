import models
import schemas
import crud
import uvicorn

from fastapi import Depends, FastAPI, HTTPException
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


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
