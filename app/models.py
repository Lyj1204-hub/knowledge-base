from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, ClassVar


@dataclass
class Note:
    """A learning note stored by the application."""

    VALID_STATUSES: ClassVar[set[str]] = {"未开始", "学习中", "已掌握", "待复习"}

    id: int
    title: str
    content: str
    category: str
    source_url: str = ""
    status: str = "未开始"
    summary: str = ""
    created_at: str = ""

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("笔记标题不能为空")
        if not self.content.strip():
            raise ValueError("笔记内容不能为空")
        if not self.category.strip():
            raise ValueError("笔记分类不能为空")
        if self.status not in self.VALID_STATUSES:
            raise ValueError(f"不支持的学习状态：{self.status}")
        if not self.created_at:
            self.created_at = datetime.now().isoformat(timespec="seconds")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Note":
        return cls(**data)
