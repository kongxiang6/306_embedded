# 306 Embedded

这是一个 Windows 桌面自动化辅助工具发布包，主要用于窗口绑定、图像模板识别、OCR 数字识别、自动点击和运行日志展示。

> 当前仓库保存可公开的启动器源码、打包配置和文档。主程序 `jdgc721.exe` 的业务源码目前未包含，详见 [SOURCE_STATUS.md](./SOURCE_STATUS.md)。

## 功能概览

- 绑定目标游戏窗口和购买窗口
- 基于 BMP 模板识别大厅、配装、交易行、购买状态等页面
- 通过 OCR 字库识别价格、余额、数量等数字信息
- 根据配置执行购买、出售、收取等自动化流程
- 支持配装选择、延迟配置、定时启动和定时关闭
- 在运行日志中输出窗口绑定、识别、停止和线程退出等状态

## 运行环境

- 操作系统：Windows 10/11
- 推荐分辨率：`1920 x 1080`
- 推荐缩放：`100%`
- 显示方向：横向
- 运行权限：建议软件和目标窗口使用相同权限，必要时以管理员身份运行

## 快速启动

Release 成品：

1. 到 GitHub Releases 下载 `306_single.exe`。
2. 同时下载 `新手肉蛋教程.mp4` 和 `USER_GUIDE.md`。
3. 双击 `306_single.exe` 启动。
4. 第一次使用建议先看视频教程，再按说明书绑定窗口并设置参数。

本地重新打包：

1. 准备包含 `jdgc721.exe` 的完整运行目录。
2. 安装 PyInstaller。
3. 执行 `scripts/build_single.ps1 -PayloadDir <完整运行目录>`。
4. 生成文件位于 `dist/306_single.exe`。

## 文件结构

- `src/launcher.py`：单文件启动器源码
- `packaging/306_single.spec`：PyInstaller 打包配置
- `scripts/build_single.ps1`：本地打包脚本
- `docs/USER_GUIDE.md`：面向用户的操作说明
- `docs/RELEASE_NOTES.md`：发布说明
- `docs/THIRD_PARTY_NOTICES.md`：第三方依赖说明

## 分发说明

Release 中的 `306_single.exe` 会把运行目录打包到内部，并在运行时解压后启动主程序。请不要把 Release 附件直接提交到源码仓库。

## 风险提示

本软件会模拟窗口识别、OCR 和点击操作。请只在你有权限操作的环境中使用，并自行确认目标软件或游戏的使用规则。自动化工具可能导致误操作、账号风险或被安全软件拦截。

## 开源说明

如果准备发布到 GitHub，请优先补充完整源码、构建脚本、依赖来源说明和第三方许可。当前发布包内包含多个第三方运行库和主题资源，详见 [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)。
