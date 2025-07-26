#!/usr/bin/env python3
"""
AugmentCode-Free 简化构建脚本
用于快速本地构建和测试
"""

import os
import sys
import shutil
import subprocess
import platform
from pathlib import Path

def run_command(cmd, check=True):
    """运行命令并处理错误"""
    print(f"执行: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"警告: {result.stderr}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"错误: 命令执行失败: {cmd}")
        print(f"返回码: {e.returncode}")
        if e.stdout:
            print(f"输出: {e.stdout}")
        if e.stderr:
            print(f"错误: {e.stderr}")
        return None

def main():
    """主构建函数"""
    print("=" * 60)
    print("AugmentCode-Free 简化构建脚本")
    print("=" * 60)
    
    # 检查Python版本
    if sys.version_info < (3, 7):
        print("错误: 需要Python 3.7或更高版本")
        return 1
    
    print(f"Python版本: {sys.version}")
    print(f"平台: {platform.platform()}")
    
    # 创建dist目录
    dist_dir = Path("dist")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    # 安装依赖
    print("\n1. 安装构建依赖...")
    python_cmd = sys.executable
    
    deps = ["pyinstaller", "setuptools", "wheel"]
    for dep in deps:
        result = run_command(f'"{python_cmd}" -m pip install {dep}')
        if result is None:
            print(f"警告: 无法安装 {dep}")
    
    # 构建可执行文件
    print("\n2. 构建可执行文件...")
    
    system = platform.system()
    if system == "Windows":
        exe_name = "AugmentCode-Free-v1.0.5-Windows.exe"
        data_sep = ";"
        windowed = "--windowed"
    elif system == "Darwin":
        exe_name = "AugmentCode-Free-v1.0.5-macOS"
        data_sep = ":"
        windowed = "--windowed"
    else:
        exe_name = "AugmentCode-Free-v1.0.5-Linux"
        data_sep = ":"
        windowed = ""
    
    pyinstaller_cmd = f'''"{python_cmd}" -m PyInstaller --onefile {windowed} \\
        --name "{exe_name}" \\
        --distpath dist \\
        --add-data "augment_tools_core{data_sep}augment_tools_core" \\
        --add-data "gui_qt6{data_sep}gui_qt6" \\
        --add-data "languages{data_sep}languages" \\
        --add-data "config{data_sep}config" \\
        --hidden-import PyQt6 \\
        --hidden-import PyQt6.QtWidgets \\
        --hidden-import PyQt6.QtCore \\
        --hidden-import PyQt6.QtGui \\
        --hidden-import psutil \\
        --hidden-import xml.etree.ElementTree \\
        main.py'''
    
    result = run_command(pyinstaller_cmd)
    if result is None:
        print("错误: PyInstaller构建失败")
        return 1
    
    # 创建便携版
    print("\n3. 创建便携版...")
    portable_dir = Path("portable")
    if portable_dir.exists():
        shutil.rmtree(portable_dir)
    portable_dir.mkdir()
    
    # 复制文件
    for item in ["augment_tools_core", "gui_qt6", "languages", "config", "main.py", "requirements.txt", "README.md", "LICENSE"]:
        src = Path(item)
        if src.exists():
            if src.is_dir():
                shutil.copytree(src, portable_dir / item)
            else:
                shutil.copy2(src, portable_dir / item)
    
    # 创建启动脚本
    if system == "Windows":
        start_script = portable_dir / "start.bat"
        with open(start_script, "w", encoding="utf-8") as f:
            f.write("""@echo off
chcp 65001 >nul
echo Starting AugmentCode-Free...
python main.py
pause
""")
    else:
        start_script = portable_dir / "start.sh"
        with open(start_script, "w", encoding="utf-8") as f:
            f.write("""#!/bin/bash
echo "Starting AugmentCode-Free..."
python3 main.py
""")
        start_script.chmod(0o755)
    
    # 创建压缩包
    print("\n4. 创建压缩包...")
    if system == "Windows":
        archive_name = "AugmentCode-Free-v1.0.5-Portable-Windows.zip"
        run_command(f'powershell Compress-Archive -Path portable\\* -DestinationPath {archive_name}')
    else:
        archive_name = f"AugmentCode-Free-v1.0.5-Portable-{system}.tar.gz"
        run_command(f"tar -czf {archive_name} -C portable .")
    
    # 生成校验和
    print("\n5. 生成校验和...")
    checksums_file = dist_dir / "checksums.txt"
    
    if system == "Windows":
        exe_path = dist_dir / f"{exe_name}"
        if exe_path.exists():
            run_command(f'certutil -hashfile "{exe_path}" SHA256 > "{checksums_file}"')
            run_command(f'certutil -hashfile "{archive_name}" SHA256 >> "{checksums_file}"')
    else:
        exe_path = dist_dir / exe_name
        if exe_path.exists():
            run_command(f'shasum -a 256 "{exe_path}" > "{checksums_file}"')
            run_command(f'shasum -a 256 "{archive_name}" >> "{checksums_file}"')
    
    # 显示结果
    print("\n" + "=" * 60)
    print("构建完成!")
    print("=" * 60)
    
    print("\n生成的文件:")
    for item in dist_dir.iterdir():
        size = item.stat().st_size
        print(f"  {item.name} ({size:,} bytes)")
    
    if Path(archive_name).exists():
        size = Path(archive_name).stat().st_size
        print(f"  {archive_name} ({size:,} bytes)")
    
    print(f"\n可执行文件位置: {dist_dir / exe_name}")
    print(f"便携版位置: {archive_name}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
