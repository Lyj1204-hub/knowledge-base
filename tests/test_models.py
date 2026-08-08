import pytest

from app.models import Job


def test_create_job():
    job = Job(
        id=1,
        company="测试公司",
        title="Python后端实习生",
        city="北京",
    )

    assert job.id == 1
    assert job.company == "测试公司"
    assert job.title == "Python后端实习生"
    assert job.status == "待投递"
    assert job.created_at != ""


def test_job_to_dict_and_from_dict():
    job = Job(
        id=1,
        company="测试公司",
        title="Python后端实习生",
        city="北京",
    )

    data = job.to_dict()
    restored_job = Job.from_dict(data)

    assert restored_job == job


def test_empty_company_is_rejected():
    with pytest.raises(ValueError):
        Job(
            id=1,
            company="",
            title="Python后端实习生",
            city="北京",
        )


def test_empty_title_is_rejected():
    with pytest.raises(ValueError):
        Job(
            id=1,
            company="测试公司",
            title="",
            city="北京",
        )


def test_invalid_status_is_rejected():
    with pytest.raises(ValueError):
        Job(
            id=1,
            company="测试公司",
            title="Python后端实习生",
            city="北京",
            status="错误状态",
        )