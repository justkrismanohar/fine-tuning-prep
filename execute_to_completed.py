"""Run PREP notebooks; save executed copies under completed/."""
from __future__ import annotations

import io
import json
import os
import traceback
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent


def cell_source(cell: dict) -> str:
    src = cell.get("source", "")
    return "".join(src) if isinstance(src, list) else (src or "")


def execute_notebook(path: Path) -> dict:
    nb = json.loads(path.read_text(encoding="utf-8"))
    env: dict = {"__name__": "__main__"}
    count = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        count += 1
        cell["execution_count"] = count
        src = cell_source(cell)
        out_buf, err_buf = io.StringIO(), io.StringIO()
        outputs: list[dict] = []
        try:
            with redirect_stdout(out_buf), redirect_stderr(err_buf):
                exec(compile(src, str(path), "exec"), env, env)
        except Exception as exc:
            tb = traceback.format_exc()
            raise RuntimeError(f"{path.name} cell {count} failed:\n{src[:400]}\n{exc}\n{tb}") from exc
        if out_buf.getvalue():
            outputs.append({"output_type": "stream", "name": "stdout", "text": out_buf.getvalue()})
        if err_buf.getvalue():
            outputs.append({"output_type": "stream", "name": "stderr", "text": err_buf.getvalue()})
        cell["outputs"] = outputs
    nb.setdefault("metadata", {})
    nb["metadata"]["civicdesk_executed"] = True
    return nb


def main() -> None:
    completed = HERE / "completed"
    completed.mkdir(exist_ok=True)
    old = Path.cwd()
    os.chdir(HERE)
    try:
        for src in sorted(HERE.glob("PREP-*.ipynb")):
            print("executing", src.name)
            executed = execute_notebook(src)
            dest = completed / src.name
            dest.write_text(json.dumps(executed, indent=1, ensure_ascii=False), encoding="utf-8")
            print("  saved", dest.relative_to(HERE))
    finally:
        os.chdir(old)
    print("done")


if __name__ == "__main__":
    main()
