from __future__ import annotations

import ctypes
from pathlib import Path
import subprocess
import sys


def _show_error(message: str) -> None:
    try:
        ctypes.windll.user32.MessageBoxW(0, message, "306 launcher", 0x10)
    except Exception:
        pass


def _app_root() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / "app"
    return Path(__file__).resolve().parent / "app"


def main() -> int:
    app_root = _app_root()
    target = app_root / "jdgc721.exe"

    if not target.exists():
        _show_error(f"Missing target executable:\n{target}")
        return 1

    try:
        proc = subprocess.Popen([str(target), *sys.argv[1:]], cwd=str(app_root))
        return proc.wait()
    except Exception as exc:
        _show_error(f"Failed to launch bundled app:\n{exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
