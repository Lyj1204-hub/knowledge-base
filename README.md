# Personal Knowledge Base

一个使用 Python 编写的个人知识库与学习笔记管理系统。

## 功能

- 新增、查看和删除学习笔记
- 按分类或学习状态筛选
- 修改学习状态
- JSON 持久化保存
- 输入校验、异常处理和自动化测试

## 项目结构

```text
app/models.py    笔记数据模型和校验
app/storage.py   JSON 持久化
app/services.py  笔记业务逻辑
app/main.py      命令行交互
tests/           自动化测试
data/notes.json  示例数据
```

## 安装和运行

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m app.main
```

## 测试

```powershell
python -m pytest -q
```

## 后续计划

- 使用 FastAPI 提供 REST API
- 使用 MySQL 替换 JSON 存储
- 增加搜索、分页和用户权限
- 接入向量检索和 RAG 问答
