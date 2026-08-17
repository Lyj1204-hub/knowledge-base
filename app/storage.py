import json
from pathlib import Path

from .models import Note


class NoteStorage:
    def __init__(self, file_path: str | Path = "data/notes.json") -> None:
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def load(self) -> list[Note]:
        content = self.file_path.read_text(encoding="utf-8").strip()
        if not content:
            return []
        try:
            data = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError("笔记数据文件格式错误，请检查 data/notes.json") from exc
        if not isinstance(data, list):
            raise ValueError("笔记数据文件必须是 JSON 列表")
        try:
            return [Note.from_dict(item) for item in data]
        except (TypeError, ValueError) as exc:
            raise ValueError("笔记数据文件包含无效记录") from exc

    def save(self, notes: list[Note]) -> None:
        data = [note.to_dict() for note in notes]
        self.file_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def next_id(self, notes: list[Note]) -> int:
        return max((note.id for note in notes), default=0) + 1
