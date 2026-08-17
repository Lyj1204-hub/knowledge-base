import pytest

from app.models import Note
from app.storage import NoteStorage


def test_storage_creates_file(tmp_path):
    storage = NoteStorage(tmp_path / "notes.json")
    assert storage.load() == []


def test_save_and_load(tmp_path):
    storage = NoteStorage(tmp_path / "notes.json")
    note = Note(1, "FastAPI", "学习路由", "后端")
    storage.save([note])
    assert storage.load() == [note]


def test_empty_file_returns_empty_list(tmp_path):
    path = tmp_path / "notes.json"
    path.write_text("", encoding="utf-8")
    assert NoteStorage(path).load() == []


def test_invalid_json_has_clear_error(tmp_path):
    path = tmp_path / "notes.json"
    path.write_text("not json", encoding="utf-8")
    with pytest.raises(ValueError, match="格式错误"):
        NoteStorage(path).load()


def test_next_id(tmp_path):
    storage = NoteStorage(tmp_path / "notes.json")
    notes = [Note(1, "A", "a", "Python"), Note(3, "B", "b", "Python")]
    assert storage.next_id(notes) == 4
