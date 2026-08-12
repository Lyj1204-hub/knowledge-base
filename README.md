# Job Assistant

## 项目简介

Job Assistant 是一个使用 Python 编写的命令行求职岗位管理工具。

它可以帮助用户记录投递过或准备投递的岗位，并支持查看、筛选、修改投递状态和删除岗位。岗位数据保存在本地 JSON 文件中，程序关闭后数据不会丢失。

## 已实现功能

- 新增岗位信息
- 查看全部岗位
- 按投递状态筛选岗位
- 修改岗位投递状态
- 删除岗位
- 使用 JSON 文件保存岗位数据
- 自动生成岗位编号
- 公司名称和岗位名称不能为空
- 校验投递状态是否合法
- 处理不存在的岗位编号
- 处理非数字岗位编号等错误输入
- 使用 pytest 进行自动化测试

## 支持的投递状态

```text
待投递
已投递
笔试
面试
已拒绝
已入职
```

## 项目结构

```text
github-project/
├─ app/
│  ├─ __init__.py
│  ├─ main.py          # 命令行程序入口和菜单交互
│  ├─ models.py        # Job 岗位数据模型和数据校验
│  ├─ services.py      # 岗位新增、查询、修改、删除等业务逻辑
│  └─ storage.py       # JSON 文件读写和数据持久化
├─ data/
│  └─ jobs.json        # 本地岗位数据文件
├─ tests/
│  ├─ test_models.py   # 数据模型测试
│  ├─ test_services.py # 业务逻辑测试
│  └─ test_storage.py  # 数据存储测试
├─ .gitignore
├─ README.md
└─ requirements.txt
```

## 环境要求

- Python 3.10 或更高版本
- Git（可选，用于下载和提交项目）

## 安装步骤

### 1. 克隆项目

```powershell
git clone <你的 GitHub 仓库地址>
cd github-project
```

### 2. 创建虚拟环境

```powershell
python -m venv .venv
```

### 3. 激活虚拟环境

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. 安装依赖

```powershell
pip install -r requirements.txt
```

## 运行方式

在项目根目录运行：

```powershell
python -m app.main
```

程序启动后会显示菜单：

```text
====== Job Assistant ======
1. 新增岗位
2. 查看全部岗位
3. 按状态查看
4. 修改投递状态
5. 删除岗位
0. 退出
```

根据提示输入数字即可操作。

## 测试方式

运行全部自动化测试：

```powershell
python -m pytest -q
```

测试覆盖以下内容：

- 创建岗位
- 默认投递状态
- 公司名称不能为空
- 岗位名称不能为空
- 非法投递状态
- JSON 文件保存和读取
- 空文件处理
- 错误 JSON 文件处理
- 岗位编号自动递增
- 修改岗位状态
- 删除岗位
- 修改或删除不存在的岗位

## 数据保存说明

岗位数据默认保存到：

```text
data/jobs.json
```

程序重新启动后，之前保存的岗位数据仍然可以读取。

该文件仅建议保存示例数据，不建议上传真实岗位链接、个人联系方式或其他隐私信息。

## 技术栈

- Python
- dataclass
- JSON
- pathlib
- pytest
- Git 和 GitHub

## 后续计划

- 使用 MySQL 替换 JSON 文件存储
- 使用 FastAPI 提供 Web API
- 增加用户注册、登录和权限管理
- 增加岗位搜索、分页和统计功能
- 增加 Docker 部署
- 将项目升级为 AI 求职助手或岗位信息研究 Agent