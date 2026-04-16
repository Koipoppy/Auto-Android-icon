#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Android Launcher Icon Generator
根据1024*1024的icon.png自动生成不同密度的启动器图标
"""

import os
import sys
from PIL import Image

# Android各密度对应的尺寸（基于1024x1024的源图）
# 标准比例：mdpi(1x), hdpi(1.5x), xhdpi(2x), xxhdpi(3x), xxxhdpi(4x)
# 启动器图标标准尺寸：mdpi(48x48), hdpi(72x72), xhdpi(96x96), xxhdpi(144x144), xxxhdpi(192x192)
DENSITIES = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192,
}

# 需要生成的图标文件列表
ICON_FILES = [
    'ic_launcher.png',
    'ic_launcher_foreground.png',
    'ic_launcher_round.png',
]


def resize_icon(source_image, size):
    """
    调整图片大小，使用LANCZOS滤镜保证质量
    """
    return source_image.resize((size, size), Image.LANCZOS)


def generate_icons(source_path, output_dir):
    """
    生成所有密度的图标
    
    Args:
        source_path: 源图片路径 (1024x1024)
        output_dir: 输出目录
    """
    # 检查源文件是否存在
    if not os.path.exists(source_path):
        print(f"错误：源文件不存在 - {source_path}")
        return False
    
    # 打开源图片并验证尺寸
    try:
        source_image = Image.open(source_path)
        width, height = source_image.size
        if width != 1024 or height != 1024:
            print(f"警告：源图片尺寸为 {width}x{height}，期望 1024x1024")
            print("将继续处理，但结果可能不符合预期")
    except Exception as e:
        print(f"错误：无法打开源文件 - {e}")
        return False
    
    # 创建输出目录结构
    res_dir = os.path.join(output_dir, 'res')
    
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
    
    print(f"\n完成！所有图标已生成到：{res_dir}")
    return True


def main():
    """
    主函数
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description='根据1024x1024的icon.png生成Android启动器图标',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python generate_icons.py -i icon.png -o ./output
  python generate_icons.py --input /path/to/icon.png --output /path/to/output
        """
    )
    
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='输入的icon.png文件路径 (应为1024x1024)'
    )
    
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='输出目录路径 (将在此目录下创建res文件夹)'
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Android Launcher Icon Generator")
    print("=" * 60)
    print(f"源文件：{args.input}")
    print(f"输出目录：{args.output}")
    print("-" * 60)
    
    success = generate_icons(args.input, args.output)
    
    if success:
        print("\n✓ 图标生成成功!")
        sys.exit(0)
    else:
        print("\n✗ 图标生成失败!")
        sys.exit(1)


if __name__ == '__main__':
    main()
