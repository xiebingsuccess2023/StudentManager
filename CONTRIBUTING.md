# 参与项目开发

## 分支命名

- `feature/功能名称`：新功能
- `fix/问题名称`：错误修复
- `docs/内容`：文档修改

## 提交信息示例

- `feat: add student search`
- `fix: validate student age`
- `docs: update README`

## 提交 PR 前

1. 确认代码可以运行：`python main.py`
2. 运行测试：`python -m unittest discover -s tests -v`
3. 检查差异：`git diff`
4. 确认没有提交 `.env`、虚拟环境、缓存和本地数据
5. 在 PR 中说明修改内容、测试结果和风险
