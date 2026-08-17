import pytest

from app.services import NoteService
from app.storage import NoteStorage


def service(tmp_path):
    return NoteService(NoteStorage(tmp_path / "notes.json"))


def test_add_and_list(tmp_path):
    item = service(tmp_path).add_note("Python", "学习函数", "Python")
    assert item.id == 1
    assert len(service(tmp_path).list_notes()) == 1


def test_filter_by_category_and_status(tmp_path):
    s = service(tmp_path)
    s.add_note("Python", "函数", "Python", status="学习中")
    s.add_note("Git", "提交", "工具")
    assert len(s.list_notes(category="Python")) == 1
    assert len(s.list_notes(status="学习中")) == 1


def test_update_status_and_missing_id(tmp_path):
    s = service(tmp_path)
    item = s.add_note("SQL", "查询", "数据库")
    assert s.update_status(item.id, "已掌握").status == "已掌握"
    assert s.update_status(999, "已掌握") is None


def test_invalid_status_rejected(tmp_path):
    with pytest.raises(ValueError, match="学习状态"):
        service(tmp_path).add_note("标题", "内容", "Python", status="错误状态")


def test_delete_job_and_missing_id(tmp_path):
    s = service(tmp_path)
    item = s.add_note("Docker", "容器", "后端")
    assert s.delete_note(item.id) is True
    assert s.delete_note(999) is False
