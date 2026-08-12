from dataclasses import asdict, dataclass
from typing import ClassVar
from datetime import datetime
from typing import Any


VALID_STATUSES = {"待投递", "已投递", "笔试", "面试", "已拒绝", "已入职"}


@dataclass
class Job:
    VALID_STATUSES: ClassVar[set[str]] = {
        "待投递",
        "已投递",
        "笔试",
        "面试",
        "已拒绝",
        "已入职",
    }
    id: int
    company: str
    title: str
    city: str
    url: str = ""
    status: str = "待投递"
    note: str = ""
    created_at: str = ""

    def __post_init__(self) -> None:
        if not self.company.strip():
            raise ValueError("公司名称不能为空")

        if not self.title.strip():
            raise ValueError("岗位名称不能为空")

        if self.status not in VALID_STATUSES:
            raise ValueError(f"不支持的投递状态：{self.status}")

        if not self.created_at:
            self.created_at = self.now()

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Job":
        return cls(**data)

    @staticmethod
    def now() -> str:
        return datetime.now().isoformat(timespec="seconds")