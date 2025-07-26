# AugmentCode-Free v1.0.5 Release Notes

## 🎉 新版本发布

AugmentCode-Free v1.0.5 现已发布！这是一个多IDE维护工具包，支持 VS Code、Cursor、Windsurf 和 JetBrains 系列产品。

## 📦 下载

### Windows 用户
- **可执行文件**: `AugmentCode-Free-v1.0.5-Windows.exe` (推荐)
  - 无需安装Python环境
  - 双击即可运行
  - 包含所有依赖

### macOS 用户
- **可执行文件**: `AugmentCode-Free-v1.0.5-macOS`
  - 适用于 Intel 和 Apple Silicon Mac
  - 无需安装Python环境
  - 双击即可运行

### Linux 用户
- **可执行文件**: `AugmentCode-Free-v1.0.5-Linux`
  - 适用于大多数Linux发行版
  - 无需安装Python环境
  - 在终端中运行

### 便携版 (所有平台)
- **Windows**: `AugmentCode-Free-v1.0.5-Portable-Windows.zip`
- **macOS**: `AugmentCode-Free-v1.0.5-Portable-macos-latest.tar.gz`
- **Linux**: `AugmentCode-Free-v1.0.5-Portable-ubuntu-latest.tar.gz`

便携版需要Python 3.7+环境，但提供了更好的兼容性。

## ✨ 主要功能

### 核心功能
- **多IDE数据库清理**: 清理 VS Code、Cursor、Windsurf 本地数据库中的特定条目
- **多IDE遥测ID修改**: 重置或更改支持的IDE存储的遥测标识符
- **JetBrains SessionID管理**: 自动修改 JetBrains 系列产品的 SessionID
- **智能进程检测**: 自动检测和管理正在运行的IDE进程

### 支持的IDE
- **VS Code** (Visual Studio Code)
- **Cursor** (AI代码编辑器)
- **Windsurf** (Codeium IDE)
- **JetBrains系列**: PyCharm、IntelliJ IDEA、WebStorm、PhpStorm、CLion、DataGrip、GoLand、RubyMine、AppCode、AndroidStudio、Rider、DataSpell

### 界面特性
- **现代化GUI**: 基于PyQt6的用户友好界面
- **多语言支持**: 支持中文和英文
- **一键操作**: 简单的点击操作完成复杂任务
- **实时日志**: 详细的操作日志和状态反馈

## 🔧 系统要求

### 可执行文件版本
- **Windows**: Windows 7/10/11
- **macOS**: macOS 10.14 或更高版本
- **Linux**: 大多数现代Linux发行版
- **内存**: 最少100MB RAM
- **存储**: 50MB可用空间

### 便携版
- **Python**: 3.7 或更高版本
- **依赖包**: PyQt6, psutil, click, colorama (自动安装)

## 🚀 使用方法

### 可执行文件版本
1. 下载对应平台的可执行文件
2. 双击运行 (Windows/macOS) 或在终端中执行 (Linux)
3. 选择要操作的IDE
4. 点击相应的功能按钮
5. 按照提示完成操作

### 便携版
1. 下载并解压便携版压缩包
2. **Windows**: 双击 `start.bat`
3. **macOS/Linux**: 运行 `./start.sh`
4. 如果缺少依赖，运行 `pip install -r requirements.txt`

## ⚠️ 重要提醒

**使用前请务必：**
- 退出 AugmentCode 账号登录
- 关闭所有相关IDE进程
- 备份重要数据（工具会自动创建备份）

**安全提示：**
- 本项目完全开源免费
- 如有人向您收费，请立即举报诈骗行为
- 仅从官方渠道下载，确保软件安全

## 🔐 文件校验

每个发布文件都提供了SHA256校验和，请在下载后验证文件完整性：

```bash
# Windows
certutil -hashfile filename.exe SHA256

# macOS/Linux
shasum -a 256 filename
# 或
sha256sum filename
```

## 📝 更新日志

### v1.0.5 (当前版本)
- 移除了界面中的作者信息和版本显示
- 简化了用户界面，专注于核心功能
- 优化了多平台构建流程
- 改进了错误处理和用户反馈

### 历史版本
- v1.0.4: 修复了macOS兼容性问题
- v1.0.3: 修复了About对话框显示问题
- v1.0.2: 增加了JetBrains支持
- v1.0.1: 初始GUI版本
- v1.0.0: 命令行版本

## 🐛 问题反馈

如果您遇到任何问题，请：
1. 检查系统要求是否满足
2. 确认按照使用说明正确操作
3. 查看程序日志中的错误信息
4. 在GitHub Issues中报告问题

## 📄 许可证

本项目采用 MIT 许可证开源。详见 [LICENSE](LICENSE) 文件。

---

**感谢使用 AugmentCode-Free！**
