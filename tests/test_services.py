from app.services import JobService
from app.storage import JobStorage


def create_service(tmp_path):
    file_path = tmp_path / "jobs.json"
    storage = JobStorage(file_path)
    return JobService(storage)


def test_add_job(tmp_path):
    service = create_service(tmp_path)

    job = service.add_job(
        company="字节跳动",
        title="Python开发实习生",
        city="北京",
        url="https://example.com",
        note="测试岗位",
    )

    assert job.id == 1
    assert job.company == "字节跳动"

    jobs = service.list_jobs()
    assert len(jobs) == 1


def test_list_jobs_by_status(tmp_path):
    service = create_service(tmp_path)

    service.add_job(
        company="腾讯",
        title="后端开发实习生",
        city="深圳",
        url="https://example.com",
        status="待投递",
    )

    service.add_job(
        company="阿里巴巴",
        title="Python实习生",
        city="杭州",
        url="https://example.com",
        status="已投递",
    )

    jobs = service.list_jobs("已投递")

    assert len(jobs) == 1
    assert jobs[0].company == "阿里巴巴"


def test_update_status(tmp_path):
    service = create_service(tmp_path)

    job = service.add_job(
        company="百度",
        title="算法实习生",
        city="北京",
        url="https://example.com",
    )

    updated_job = service.update_status(job.id, "已投递")

    assert updated_job is not None
    assert updated_job.status == "已投递"


def test_delete_job(tmp_path):
    service = create_service(tmp_path)

    job = service.add_job(
        company="京东",
        title="后端实习生",
        city="北京",
        url="https://example.com",
    )

    result = service.delete_job(job.id)

    assert result is True
    assert service.list_jobs() == []


def test_delete_nonexistent_job(tmp_path):
    service = create_service(tmp_path)

    result = service.delete_job(999)

    assert result is False