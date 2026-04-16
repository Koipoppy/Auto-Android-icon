#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-Android-icon
自动生成 Android 应用图标（mipmap）的脚本。
根据指定的 1024*1024 icon.png 文件，生成不同密度下的三种图标文件。
"""

import os
from PIL import Image

# ================= 配置区域 =================
# 输入图片路径 (必须是 1024x1024 的 png 文件)
INPUT_IMAGE_PATH = "icon.png"

# 输出根目录路径 (生成的 res 文件夹将保存在此目录下)
OUTPUT_ROOT_PATH = "./output_res"
# ===========================================

# Android mipmap 密度配置 (目标尺寸)
# 标准启动图标尺寸：mdpi(48x48), hdpi(72x72), xhdpi(96x96), xxhdpi(144x144), xxxhdpi(192x192)
DENSITIES = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192,
}

# 需要生成的图标文件名
ICON_FILES = [
    'ic_launcher.png',
    'ic_launcher_foreground.png',
    'ic_launcher_round.png',
]


def resize_icon(source_image, size):
    """
    调整图片大小，使用 LANCZOS 滤镜保证质量
    """
    return source_image.resize((size, size), Image.LANCZOS)


def generate_icons():
    """
    生成所有密度的图标
    
    Returns:
        bool: 成功返回 True，失败返回 False
    """
    # 检查源文件是否存在
    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"错误：源文件不存在 - {INPUT_IMAGE_PATH}")
        print("请确保该文件在当前目录下，或修改脚本中的 INPUT_IMAGE_PATH 变量。")
        return False
    
    # 打开源图片并验证尺寸
    try:
        source_image = Image.open(INPUT_IMAGE_PATH)
        width, height = source_image.size
        if width != 1024 or height != 1024:
            print(f"警告：源图片尺寸为 {width}x{height}，期望 1024x1024")
            print("将继续处理，但结果可能不符合预期")
    except Exception as e:
        print(f"错误：无法打开源文件 - {e}")
        return False
    
    # 创建输出目录结构
    res_dir = os.path.join(OUTPUT_ROOT_PATH, 'res')
    
    for density_folder, size in DENSITIES.items():
        folder_path = os.path.join(res_dir, density_folder)
        
        # 创建文件夹
        os.makedirs(folder_path, exist_ok=True)
        print(f"创建目录：{folder_path}")
        
        # 为每个图标文件生成对应尺寸的图片
        for icon_file in ICON_FILES:
            # 调整图片大小
            resized_image = resize_icon(source_image, size)
            
            # 保存到新位置
            output_path = os.path.join(folder_path, icon_file)
            resized_image.save(output_path, 'PNG')
            print(f"  ✓ 生成：{output_path} ({size}x{size})")
    
    print(f"\n完成！所有图标已生成到：{os.path.abspath(res_dir)}")
    return True


def main():
    """
    主函数
    """
    print("=" * 60)
    print("Auto-Android-icon")
    print("=" * 60)
    print(f"源文件：{INPUT_IMAGE_PATH}")
    print(f"输出目录：{OUTPUT_ROOT_PATH}")
    print("-" * 60)
    
    success = generate_icons()
    
    if success:
        print("\n✓ 图标生成成功!")
    else:
        print("\n✗ 图标生成失败!")


if __name__ == '__main__':
    main()
