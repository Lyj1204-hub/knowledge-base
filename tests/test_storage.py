from app.models import Job
from app.storage import JobStorage
import pytest


def create_job() -> Job:
    return Job(
        id=1,
        company="测试公司",
        title="Python后端实习生",
        city="北京",
    )


def test_storage_creates_file(tmp_path):
    file_path = tmp_path / "jobs.json"
    storage = JobStorage(file_path)

    assert file_path.exists()
    assert storage.load() == []


def test_save_and_load_jobs(tmp_path):
    file_path = tmp_path / "jobs.json"
    storage = JobStorage(file_path)

    job = create_job()
    storage.save([job])

    jobs = storage.load()

    assert len(jobs) == 1
    assert jobs[0] == job


def test_next_id(tmp_path):
    file_path = tmp_path / "jobs.json"
    storage = JobStorage(file_path)

    jobs = [
        Job(1, "公司A", "后端实习生", "北京"),
        Job(3, "公司B", "AI应用实习生", "上海"),
    ]

    assert storage.next_id(jobs) == 4


def test_empty_file_returns_empty_list(tmp_path):
    file_path = tmp_path / "jobs.json"
    file_path.write_text("", encoding="utf-8")

    storage = JobStorage(file_path)

    assert storage.load() == []


def test_invalid_json_has_clear_error(tmp_path):
    file_path = tmp_path / "jobs.json"
    file_path.write_text("这不是合法的 JSON", encoding="utf-8")

    storage = JobStorage(file_path)

    with pytest.raises(ValueError, match="格式错误"):
        storage.load()