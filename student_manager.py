"""学生信息管理业务逻辑。"""


class StudentManager:
    """提供学生信息的增删改查功能。"""

    def __init__(self, storage):
        self.storage = storage
        self.students = self.storage.load()

    @staticmethod
    def _validate(student_id, name, age, class_name):
        if not student_id or not student_id.strip():
            raise ValueError("学号不能为空。")
        if not name or not name.strip():
            raise ValueError("姓名不能为空。")
        if not class_name or not class_name.strip():
            raise ValueError("班级不能为空。")

        try:
            age_value = int(age)
        except (TypeError, ValueError):
            raise ValueError("年龄必须是整数。")

        if not 1 <= age_value <= 120:
            raise ValueError("年龄必须在 1～120 之间。")

        return {
            "student_id": student_id.strip(),
            "name": name.strip(),
            "age": age_value,
            "class_name": class_name.strip(),
        }

    def add_student(self, student_id, name, age, class_name):
        student = self._validate(student_id, name, age, class_name)
        if self.get_student(student["student_id"]):
            raise ValueError("该学号已经存在。")
        self.students.append(student)
        self.storage.save(self.students)
        return student.copy()

    def get_student(self, student_id):
        for student in self.students:
            if student["student_id"] == student_id:
                return student.copy()
        return None

    def list_students(self):
        return [student.copy() for student in self.students]

    def update_student(self, student_id, name=None, age=None, class_name=None):
        for index, old_student in enumerate(self.students):
            if old_student["student_id"] == student_id:
                updated = self._validate(
                    student_id,
                    name if name is not None else old_student["name"],
                    age if age is not None else old_student["age"],
                    class_name if class_name is not None else old_student["class_name"],
                )
                self.students[index] = updated
                self.storage.save(self.students)
                return updated.copy()
        raise ValueError("要修改的学生不存在。")

    def delete_student(self, student_id):
        for index, student in enumerate(self.students):
            if student["student_id"] == student_id:
                del self.students[index]
                self.storage.save(self.students)
                return True
        return False
