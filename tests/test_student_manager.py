"""学生管理业务逻辑单元测试。"""
import tempfile
import unittest
from pathlib import Path

from student_manager import StudentManager
from storage import JsonStorage


class StudentManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        data_file = Path(self.temp_dir.name) / "students.json"
        self.manager = StudentManager(JsonStorage(data_file))

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_get_student(self):
        self.manager.add_student("S001", "张三", 20, "人工智能1班")
        student = self.manager.get_student("S001")
        self.assertEqual(student["name"], "张三")
        self.assertEqual(student["age"], 20)

    def test_duplicate_student_id_is_rejected(self):
        self.manager.add_student("S001", "张三", 20, "人工智能1班")
        with self.assertRaises(ValueError):
            self.manager.add_student("S001", "李四", 21, "人工智能2班")

    def test_update_student(self):
        self.manager.add_student("S001", "张三", 20, "人工智能1班")
        updated = self.manager.update_student("S001", name="张三丰")
        self.assertEqual(updated["name"], "张三丰")

    def test_delete_student(self):
        self.manager.add_student("S001", "张三", 20, "人工智能1班")
        self.assertTrue(self.manager.delete_student("S001"))
        self.assertIsNone(self.manager.get_student("S001"))

    def test_invalid_age_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student("S001", "张三", 0, "人工智能1班")


if __name__ == "__main__":
    unittest.main()
