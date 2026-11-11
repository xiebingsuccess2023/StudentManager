# StudentManager 学生信息管理系统

> Git + GitHub + AI 综合实践教学项目。项目使用 Python 标准库，无需安装第三方依赖。

## 项目简介

这是一个基于 Python 开发的学生信息管理系统，支持学生信息管理和数据持久化。

## 1. 项目功能

- 添加、查询、修改、删除学生信息
- 显示全部学生
- 使用 JSON 文件保存数据，程序退出后数据仍然保留
- 检查学号重复、姓名为空、年龄范围等常见输入问题
- 提供单元测试

## 2. 环境要求

- Python 3.9 或更高版本
- Git
- GitHub 账号

## 3. 下载与运行

```bash
git clone https://github.com/你的用户名/StudentManager.git
cd StudentManager
python main.py
```

Windows 如果 `python` 命令不可用，可以尝试 `py main.py`。

## 4. 运行测试

```bash
python -m unittest discover -s tests -v
```

## 5. 数据保存位置

第一次添加学生后，程序会自动创建 `data/students.json`。该文件属于运行数据，默认不提交到 Git。

## 6. Git 日常协作流程

```bash
git switch -c feature/student-search
# 修改代码
git status
git diff
git add .
git commit -m "feat: add student search"
git push -u origin feature/student-search
```

然后在 GitHub 上创建 Pull Request，目标分支选择 `main`。

## 7. 案例3冲突演示

本项目 README 中有一行专门用于课堂冲突演示：

`项目状态：基础版本，等待功能开发。`

请让两个同学分别从同一个 `main` 起点创建分支，并分别将这一行改成不同内容，然后按教师实践指导合并两个分支，即可产生冲突。不要让第二位同学先拉取第一位同学的修改，否则可能不会产生冲突。

## 8. 安全提醒

- 不要把真实密码、API Key 或数据库密钥提交到 GitHub。
- `.env` 已加入 `.gitignore`；`.env.example` 只放变量名称和示例占位值。
- `.gitignore` 不会自动取消已经被 Git 跟踪的文件。
