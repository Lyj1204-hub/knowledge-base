import json
from pathlib import Path
from typing import Any

from .models import Job


class JobStorage:
    def __init__(self, file_path: str | Path = "data/jobs.json"):
        self.file_path = Path(file_path)

        # 如果 data 文件夹不存在，就自动创建
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        # 如果 JSON 文件不存在，就创建一个空列表
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def load(self) -> list[Job]:
        content = self.file_path.read_text(encoding="utf-8").strip()

        if not content:
            return []

        try:
            data = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError("岗位数据文件格式错误，请检查 data/jobs.json") from exc

        if not isinstance(data, list):
            raise ValueError("JSON文件内容必须是列表")

        return [Job.from_dict(item) for item in data]

    def save(self, jobs: list[Job]) -> None:
        data = [job.to_dict() for job in jobs]

        self.file_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def next_id(self, jobs: list[Job]) -> int:
        return max(
            (job.id for job in jobs),
            default=0,
        ) + 1