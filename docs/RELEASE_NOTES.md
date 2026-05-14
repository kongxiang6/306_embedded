# 发布说明

## 当前发布形态

本项目是面向《三角洲行动》倒子弹流程的 Windows 桌面自动化辅助工具，当前包含两种可交付形态：

- 目录版：保留完整运行目录，直接运行 `jdgc721.exe`。
- 单文件版：使用 PyInstaller 打包启动器和完整运行目录，启动后自动解压并运行内部的 `jdgc721.exe`。

## 发布前检查

- 确认 `jdgc721.exe`、`dm.dll`、`DmReg.dll`、`python312.dll` 存在。
- 确认所有 `*.bmp` 模板文件存在。
- 确认 `ziku.txt`、`ziku1.txt`、`newpeizhuang.txt`、`new余额.txt`、`房卡.txt` 存在。
- 确认 `USER_GUIDE.md`、`README.md`、`THIRD_PARTY_NOTICES.md` 随包发布。
- 确认 `operation_tutorial.mp4` 随包发布。
- 确认 `wegame_official_launcher_dual_open_tutorial.pdf` 随包发布。
- 确认 Windows 显示环境建议写明：`1920 x 1080`、`100%` 缩放、横向显示。
- 确认单文件版和目录版都要求管理员权限运行。
- 确认发布包没有误带本机账号、私密路径、聊天记录、录屏文件或调试日志。

## 已知注意事项

- 主程序和部分依赖未进行代码签名，安全软件可能出现误报。
- 软件必须以管理员身份运行，启动时会出现 Windows UAC 提权提示。
- 单文件版首次启动较慢，因为需要解压内部运行目录。
- 单文件版包含操作视频后体积会明显增大，首次启动解压时间也会更长。
- 当前目录是已编译发布包，不包含主程序源码。
- 如果要真正开源，需要补充源码、构建说明和明确的开源许可证。

## 建议发布文件

- `306_single.exe`：单文件成品，只包含软件运行所需文件
- `operation_tutorial.mp4`：操作视频教程
- `wegame_official_launcher_dual_open_tutorial.pdf`：WeGame 和官方启动器双开 PDF 教程
- `USER_GUIDE.md`：操作说明

GitHub Release 页面会显示附件 digest，当前不再单独上传 `SHA256SUMS.txt`。
