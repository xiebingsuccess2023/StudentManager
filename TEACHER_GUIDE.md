# 教师操作指导：将 StudentManager 发布到 GitHub 并完成案例3

## A. 在 GitHub 创建远程仓库

1. 登录 https://github.com
2. 点击右上角 `+` → `New repository`
3. Repository name 填 `StudentManager`
4. 选择 Public（便于学生互相查看）或 Private
5. **不要勾选** Add a README、.gitignore、license（本工程已经包含这些文件）
6. 点击 Create repository

## B. 将本地工程推送到 GitHub

先解压工程 ZIP，在工程目录打开 PowerShell：

```powershell
cd 路径\\StudentManager
git init
git branch -M main
git add .
git commit -m "chore: initialize student manager project"
git remote add origin https://github.com/你的用户名/StudentManager.git
git push -u origin main
```

如果 Git 提示设置身份，执行：

```powershell
git config --global user.name "你的名字"
git config --global user.email "你的 GitHub 邮箱"
```

再次执行 commit。GitHub 可能要求浏览器登录或使用凭据管理器完成认证。

## C. 验证项目

```powershell
python --version
python main.py
python -m unittest discover -s tests -v
git status
```

第一次添加学生后会生成 `data/students.json`；该运行数据被 `.gitignore` 忽略。

## D. 标准功能分支流程

```powershell
git switch -c feature/student-search
```

学生可以在 `student_manager.py` 中练习增加姓名关键词查询等功能。完成后：

```powershell
git diff
git add .
git commit -m "feat: add student search"
git push -u origin feature/student-search
```

在 GitHub 页面创建 PR：base 选择 `main`，compare 选择 `feature/student-search`。完成 Review 后再合并。

## E. Fork 协作流程

1. 学生打开教师的公开仓库，点击 Fork。
2. Clone 自己账号下的 Fork 仓库。
3. 创建功能分支，修改、测试、commit、push。
4. 在 GitHub 创建 PR，目标选择教师的原始仓库 `main`。
5. 教师 Review 后合并。

## F. 可重复的冲突演示（建议两名学生各用一份独立 Clone）

前提：两份工作副本都从同一个最新 main 开始，且都没有先同步对方的提交。

张三的副本：

```powershell
git switch -c feature/student-search
```

将 README 中这一行：
`项目状态：基础版本，等待功能开发。`

改为：
`项目状态：已增加学生查询功能。`

然后：

```powershell
git add README.md
git commit -m "docs: describe student search"
git push -u origin feature/student-search
```

李四的副本（仍从原来的 main 起点创建分支，不先 pull 张三的提交）：

```powershell
git switch -c feature/student-update
```

将同一行改为：
`项目状态：已增加学生修改功能。`

然后：

```powershell
git add README.md
git commit -m "docs: describe student update"
git push -u origin feature/student-update
```

在张三的本地副本中模拟合并：

```powershell
git switch main
git pull origin main
git merge feature/student-search
git merge feature/student-update
```

第二次 merge 应产生冲突。编辑 README，手动改为同时保留两项功能，例如：
`项目状态：已增加学生查询和修改功能。`

删除 `<<<<<<<`、`=======`、`>>>>>>>` 标记后：

```powershell
git add README.md
git commit -m "merge: resolve README conflict"
```

注意：如果两人使用 GitHub PR 协作，也可以让第二个 PR 在第一个 PR 合并后出现冲突，再由开发者更新分支并解决。课堂本地演示更容易控制和复现。

## G. reset / revert 演示（仅在练习分支操作）

先制造一个可撤销的提交：

```powershell
git switch -c practice/undo
# 修改 README 并保存
git add README.md
git commit -m "test: make an incorrect change"
```

撤销最近提交但保留工作区修改：

```powershell
git reset --mixed HEAD~1
```

再重新提交后，演示安全撤销提交：

```powershell
git add README.md
git commit -m "test: add a change to revert"
git revert HEAD
```

不要在多人共用的 main 分支上演示 `reset --hard`，不要对已共享历史随意强制推送。

## H. Tag 发布演示

在 main 已包含稳定代码且测试通过后：

```powershell
git switch main
git pull origin main
python -m unittest discover -s tests -v
git tag -a v1.0 -m "StudentManager version 1.0"
git push origin v1.0
```

GitHub 仓库的 Tags 页面可以看到 `v1.0`。

## I. AI 辅助提示词

### 生成提交信息
“请分析以下 git diff，概括实际修改内容，并生成一条简洁、准确的 Conventional Commits 风格提交信息。不要夸大未实现的功能。”

### 分析冲突
“下面是两个分支的冲突内容。请分别说明双方意图，判断哪些修改可以同时保留，给出合并后的建议文本，并指出需要人工确认的业务规则。”

### 审查 PR
“请审查这段 PR，按可读性、正确性、边界条件、安全性分类指出问题。每个问题请给出位置、风险、复现方式和修改建议。区分确定的问题与需要进一步验证的疑点。”

## 教学提醒

- `.gitignore` 只影响未被跟踪的文件；已经跟踪的敏感文件需要 `git rm --cached 文件名`，并且已经泄露的密钥必须更换。
- PR 是协作评审流程，不是 `git push` 的同义词。
- GitHub 默认分支、权限、仓库保护规则可能因账号设置而不同。
- 先在练习分支演示 `reset`、`revert`，避免误操作正式仓库。
