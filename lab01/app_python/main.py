from abc import ABC, abstractmethod
from fastapi import APIRouter, FastAPI, Depends, Response
import uvicorn
import argparse
from datetime import datetime, timezone
from pydantic import BaseModel
from uuid import UUID, uuid4
from functools import lru_cache
# zd2


app = FastAPI()


class Note(BaseModel):
    id: UUID
    text: str
    created_at: datetime

    @classmethod
    def new(cls, text: str):
        return Note(
            id=uuid4(),
            text=text,
            created_at=datetime.now(tz=timezone.utc),
        )



class NoteRepo(ABC):
    @abstractmethod
    def store_note(self, note: Note):
        """"""

    @abstractmethod
    def get_note(self, id_: UUID) -> Note | None:
        """"""

    @abstractmethod
    def get_all(self) -> list[Note]:
        """"""


class InMemoryNoteRepo(NoteRepo):
    def __init__(self):
        self.notes: dict[UUID, Note] = {}

    def store_note(self, note: Note):
        self.notes[note.id] = note

    def get_note(self, id_: UUID) -> Note | None:
        return self.notes.get(id_)

    def get_all(self) -> list[Note]:
        return list(self.notes.values())


def get_note(
    note_repo: NoteRepo,
    uid: UUID
) -> Note | None:
    return note_repo.get_note(uid)


def store_note(
    note_repo: NoteRepo,
    note_text: str,
) -> UUID:
    note = Note.new(text=note_text)
    note_repo.store_note(note)
    return note.id


def get_all(note_repo: NoteRepo) -> list[Note]:
    return note_repo.get_all()


@lru_cache(maxsize=1)
def note_repo():
    return InMemoryNoteRepo()


@app.get('/health')
def healthcheck():
    return 'OK'


class StoreNoteRequest(BaseModel):
    text: str


class StoreNoteResponse(BaseModel):
    uuid: str


notes_router = APIRouter()


@notes_router.post('/', response_model=StoreNoteResponse)
def store_note_endpoint(
    __root__: StoreNoteRequest,
    note_repo: NoteRepo = Depends(note_repo),
):
    uid = store_note(note_repo, __root__.text)
    return StoreNoteResponse(uuid=str(uid))


@notes_router.get('/{note_id}')
def get_note_endpoint(note_id: str, note_repo: NoteRepo = Depends(note_repo)):
    try:
        uid = UUID(note_id)
    except ValueError:
        return Response(status_code=400)

    note = get_note(note_repo, uid)
    if note is None:
        return Response(status_code=404)

    return note


@notes_router.get('/')
def get_all_endpoint(note_repo: NoteRepo = Depends(note_repo)):
    print(id(note_repo))
    return note_repo.get_all()


app.include_router(prefix='/notes', router=notes_router)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--host',
        type=str,
        default='0.0.0.0',
        help='Interface to listen'
    )
    parser.add_argument('--port', type=int, default=8000, help='Port to listen')
    args = parser.parse_args()
    uvicorn.run(app, host=args.host, port=args.port)
