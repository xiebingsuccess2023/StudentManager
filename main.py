"""学生信息管理系统命令行入口。"""
from student_manager import StudentManager
from storage import JsonStorage

DATA_FILE = "data/students.json"


def show_menu():
    print("\n========== 学生信息管理系统 ==========")
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 修改学生")
    print("4. 删除学生")
    print("5. 显示全部学生")
    print("0. 退出系统")
    print("======================================")


def print_student(student):
    print(
        f"学号：{student['student_id']} | "
        f"姓名：{student['name']} | "
        f"年龄：{student['age']} | "
        f"班级：{student['class_name']}"
    )


def main():
    manager = StudentManager(JsonStorage(DATA_FILE))
    print("欢迎使用学生信息管理系统！")

    while True:
        show_menu()
        choice = input("请选择操作：").strip()

        try:
            if choice == "1":
                student_id = input("学号：").strip()
                name = input("姓名：").strip()
                age = input("年龄：").strip()
                class_name = input("班级：").strip()
                student = manager.add_student(student_id, name, age, class_name)
                print("添加成功：")
                print_student(student)

            elif choice == "2":
                student_id = input("请输入要查询的学号：").strip()
                student = manager.get_student(student_id)
                if student:
                    print_student(student)
                else:
                    print("没有找到该学生。")

            elif choice == "3":
                student_id = input("请输入要修改的学号：").strip()
                current = manager.get_student(student_id)
                if not current:
                    print("没有找到该学生。")
                    continue
                print("直接回车表示保留原值。")
                name = input(f"姓名（{current['name']}）：").strip() or current["name"]
                age = input(f"年龄（{current['age']}）：").strip() or current["age"]
                class_name = input(
                    f"班级（{current['class_name']}）："
                ).strip() or current["class_name"]
                student = manager.update_student(
                    student_id, name=name, age=age, class_name=class_name
                )
                print("修改成功：")
                print_student(student)

            elif choice == "4":
                student_id = input("请输入要删除的学号：").strip()
                if manager.delete_student(student_id):
                    print("删除成功。")
                else:
                    print("没有找到该学生。")

            elif choice == "5":
                students = manager.list_students()
                if not students:
                    print("当前没有学生记录。")
                for student in students:
                    print_student(student)

            elif choice == "0":
                print("已退出系统，再见！")
                break
            else:
                print("无效选项，请输入 0～5。")

        except (ValueError, OSError) as error:
            print(f"操作失败：{error}")


if __name__ == "__main__":
    main()
