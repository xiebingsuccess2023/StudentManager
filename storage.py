"""JSON 文件存储。"""
import json
from pathlib import Path


class JsonStorage:
    """负责从 JSON 文件读取和保存学生数据。"""

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load(self):
        if not self.file_path.exists():
            return []
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError(f"学生数据文件格式错误：{error}") from error

        if not isinstance(data, list):
            raise ValueError("学生数据文件必须保存为列表格式。")
        return data

    def save(self, students):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = self.file_path.with_suffix(".tmp")
        with temporary_path.open("w", encoding="utf-8") as file:
            json.dump(students, file, ensure_ascii=False, indent=4)
        temporary_path.replace(self.file_path)
