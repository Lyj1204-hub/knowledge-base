from app.models import Note


def test_note_has_created_at():
    note = Note(1, "Python", "学习 Python 基础", "Python")
    assert note.created_at
