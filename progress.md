# 开发日志

## 2026-11-06 · Phase 0

- 已检查目录和环境，开始搭建工程。
- 已建立扁平包结构、核心 TODO、离线 Mock、测试和 CI 配置，并补充接口草案。
- Windows Python 3.12.10 的 `.venv` 已安装可编辑项目及开发依赖。Pydantic 2.14.3、pytest 9.2.0、Ruff 0.17.4、mypy 1.20.2。
- `python -m pytest -q` 通过 3 项测试。Ruff lint、Ruff 格式、mypy 和 `pip check` 均通过。
- GitHub Actions 配置覆盖 Python 3.11 和 3.12。实际验证环境为本机 Python 3.12。
