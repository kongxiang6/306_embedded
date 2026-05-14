# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path
import os


project_root = Path.cwd()
source_root = Path(os.environ.get("APP_PAYLOAD_DIR", project_root / "app_payload")).resolve()
launcher_path = project_root / "src" / "launcher.py"

# Only bundle files needed by the application at runtime. Tutorials, guides,
# release notes, and other user-facing documents are published as Release
# assets instead of being embedded into the single-file executable.
exclude_names = {
    ".gitignore",
    "LICENSE",
    "README.md",
    "RELEASE_NOTES.md",
    "THIRD_PARTY_NOTICES.md",
    "USER_GUIDE.md",
    "使用说明.md",
    "发布说明.md",
    "新建 文本文档.txt",
    "temp_ocr_region.bmp",
    "temp_ocr_region_processed.bmp",
}
exclude_suffixes = {".mp4", ".pdf", ".bak"}
exclude_dirs = {"tutorials", "__pycache__"}

if not source_root.exists():
    raise SystemExit(
        "Missing app payload directory. Set APP_PAYLOAD_DIR to the unpacked "
        "runtime directory that contains jdgc721.exe."
    )

datas = []

for path in source_root.rglob("*"):
    rel = path.relative_to(source_root)
    if any(part in exclude_dirs for part in rel.parts):
        continue
    if path.is_file() and path.name not in exclude_names and path.suffix.lower() not in exclude_suffixes:
        parent = rel.parent
        dest = str(Path("app") / parent) if str(parent) != "." else "app"
        datas.append((str(path), dest))

a = Analysis(
    [str(launcher_path)],
    pathex=[str(project_root)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="306_single",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    uac_admin=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
