# Python Agent Runtime

可扩展的 Python Agent Runtime。当前处于 Phase 0，提供工程骨架和确定性的离线模型替身。

## 本地验证

在项目根目录使用 PowerShell 和 Python 3.11 或以上版本。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e '.[dev]'
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m mypy
```

macOS 或 Linux 可将解释器路径替换为 `.venv/bin/python`。依赖安装完成后，测试可离线运行。环境变量示例供未来的真实模型适配器使用。

## 试用 Mock LLM

```python
from adapters.llm_mock import MockLLM

model = MockLLM[str, str](["服务正常"])
assert model.complete("检查服务状态") == "服务正常"
assert model.requests == ("检查服务状态",)
```

Mock 按顺序消耗预设响应，支持注入异常，并保存请求快照。请求与响应的类型由测试指定，便于将来接入负责人确认的核心接口。

## 项目文档

- [架构与首个函数的验收标准](docs/architecture.md)
- [设计决策记录模板](docs/design_decisions.md)
- [学习日志模板](docs/learning_log.md)
- [阶段任务](task_plan.md)
- [工程日志](progress.md)
