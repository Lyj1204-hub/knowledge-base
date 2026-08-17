from .models import Note
from .storage import NoteStorage


class NoteService:
    def __init__(self, storage: NoteStorage) -> None:
        self.storage = storage

    def add_note(
        self,
        title: str,
        content: str,
        category: str,
        source_url: str = "",
        status: str = "未开始",
        summary: str = "",
    ) -> Note:
        notes = self.storage.load()
        note = Note(
            id=self.storage.next_id(notes),
            title=title,
            content=content,
            category=category,
            source_url=source_url,
            status=status,
            summary=summary,
        )
        notes.append(note)
        self.storage.save(notes)
        return note

    def list_notes(self, category: str | None = None, status: str | None = None) -> list[Note]:
        notes = self.storage.load()
        if category is not None:
            notes = [note for note in notes if note.category == category]
        if status is not None:
            if status not in Note.VALID_STATUSES:
                raise ValueError(f"不支持的学习状态：{status}")
            notes = [note for note in notes if note.status == status]
        return notes

    def get_note(self, note_id: int) -> Note | None:
        return next((note for note in self.storage.load() if note.id == note_id), None)

    def update_status(self, note_id: int, status: str) -> Note | None:
        if status not in Note.VALID_STATUSES:
            raise ValueError(f"不支持的学习状态：{status}")
        notes = self.storage.load()
        for note in notes:
            if note.id == note_id:
                note.status = status
                self.storage.save(notes)
                return note
        return None

    def delete_note(self, note_id: int) -> bool:
        notes = self.storage.load()
        remaining = [note for note in notes if note.id != note_id]
        if len(remaining) == len(notes):
            return False
        self.storage.save(remaining)
        return True
