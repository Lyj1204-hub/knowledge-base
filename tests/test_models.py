import pytest

from app.models import Note


def test_note_creation_and_default_status():
    note = Note(1, "Python 类型注解", "记录类型注解的作用", "Python")
    assert note.status == "未开始"


def test_note_to_dict_and_from_dict():
    note = Note(1, "Git", "记录常用命令", "工具")
    assert Note.from_dict(note.to_dict()) == note


def test_empty_title_rejected():
    with pytest.raises(ValueError, match="标题"):
        Note(1, "", "内容", "Python")


def test_empty_content_rejected():
    with pytest.raises(ValueError, match="内容"):
        Note(1, "标题", "", "Python")


def test_invalid_status_rejected():
    with pytest.raises(ValueError, match="学习状态"):
        Note(1, "标题", "内容", "Python", status="错误状态")
