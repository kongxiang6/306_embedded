# Source Status

This repository contains the source files that are currently available for publication:

- PyInstaller launcher source in `src/launcher.py`
- Single-file packaging configuration in `packaging/306_single.spec`
- Build helper script in `scripts/build_single.ps1`
- User documentation and release notes under `docs/`

The compiled application payload `jdgc721.exe` is not available as source code in this repository. The current release artifact is built by bundling that compiled payload together with the launcher and runtime resources.

Because the main application source is not present, this repository should be treated as a release/packaging source repository until the original application source is added.
