# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path
import os


project_root = Path.cwd()
source_root = Path(os.environ.get("APP_PAYLOAD_DIR", project_root / "app_payload")).resolve()
launcher_path = project_root / "src" / "launcher.py"
exclude_names = {"新建 文本文档.txt", "temp_ocr_region.bmp", "temp_ocr_region_processed.bmp"}

if not source_root.exists():
    raise SystemExit(
        "Missing app payload directory. Set APP_PAYLOAD_DIR to the unpacked "
        "runtime directory that contains jdgc721.exe."
    )

datas = []

for path in source_root.rglob("*"):
    if path.is_file() and path.name not in exclude_names:
        rel = path.relative_to(source_root)
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
