from app.models import Job
from app.storage import JobStorage


class JobService:
    def __init__(self, storage: JobStorage):
        self.storage = storage

    def add_job(
        self,
        company: str,
        title: str,
        city: str,
        url: str,
        status: str = "待投递",
        note: str = "",
    ) -> Job:
        jobs = self.storage.load()

        job = Job(
            id=self.storage.next_id(jobs),
            company=company,
            title=title,
            city=city,
            url=url,
            status=status,
            note=note,
        )

        jobs.append(job)
        self.storage.save(jobs)
        return job

    def list_jobs(self, status: str | None = None) -> list[Job]:
        jobs = self.storage.load()

        if status is None:
            return jobs

        return [job for job in jobs if job.status == status]

    def update_status(self, job_id: int, status: str) -> Job | None:
        jobs = self.storage.load()

        for job in jobs:
            if job.id == job_id:
                job.status = status
                self.storage.save(jobs)
                return job

        return None

    def delete_job(self, job_id: int) -> bool:
        jobs = self.storage.load()
        new_jobs = [job for job in jobs if job.id != job_id]

        if len(new_jobs) == len(jobs):
            return False

        self.storage.save(new_jobs)
        return True