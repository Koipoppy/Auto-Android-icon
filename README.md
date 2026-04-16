# Auto-Android-icon

根据指定的 1024×1024 `icon.png` 文件，自动生成 Android 项目所需的各种密度和类型的启动图标。

## 功能特点

- 自动创建标准的 Android mipmap 目录结构
- 生成三种类型的图标：
  - `ic_launcher.png` (标准启动图标)
  - `ic_launcher_foreground.png` (前景图标，用于自适应图标)
  - `ic_launcher_round.png` (圆形启动图标)
- 支持 5 种屏幕密度：
  - mdpi (1x)
  - hdpi (1.5x)
  - xhdpi (2x)
  - xxhdpi (3x)
  - xxxhdpi (4x)

## 前置要求

- Python 3.6+
- Pillow 库

## 安装依赖

```bash
pip install Pillow
```

## 使用方法

### 基本用法

1. 修改脚本中的输入和输出路径配置（位于脚本开头）：

```python
# ==================== 配置区域 ====================
# 在此处修改输入和输出路径

# 输入的源图片路径 (应为 1024x1024 的 PNG 文件)
INPUT_PATH = 'icon.png'

# 输出目录路径 (将在此目录下创建 res 文件夹)
OUTPUT_PATH = './output'
# =================================================
```

2. 运行脚本：

```bash
python generate_icons.py
```

### 配置说明

| 配置项 | 说明 | 示例 |
|--------|------|------|
| `INPUT_PATH` | 输入的 1024×1024 PNG 图标文件路径 | `'icon.png'`, `'/path/to/your/icon.png'` |
| `OUTPUT_PATH` | 输出目录路径 | `'./output'`, `'./android_app/res'` |

### 示例

```bash
# 使用默认配置（当前目录下的 icon.png，输出到 ./output）
python generate_icons.py

# 或者先修改脚本中的 INPUT_PATH 和 OUTPUT_PATH，然后直接运行
```

## 输出结构

生成的文件将按照以下结构组织：

```
output/
└── res/
    ├── mipmap-mdpi/
    │   ├── ic_launcher.png
    │   ├── ic_launcher_foreground.png
    │   └── ic_launcher_round.png
    ├── mipmap-hdpi/
    │   ├── ic_launcher.png
    │   ├── ic_launcher_foreground.png
    │   └── ic_launcher_round.png
    ├── mipmap-xhdpi/
    │   ├── ic_launcher.png
    │   ├── ic_launcher_foreground.png
    │   └── ic_launcher_round.png
    ├── mipmap-xxhdpi/
    │   ├── ic_launcher.png
    │   ├── ic_launcher_foreground.png
    │   └── ic_launcher_round.png
    └── mipmap-xxxhdpi/
        ├── ic_launcher.png
        ├── ic_launcher_foreground.png
        └── ic_launcher_round.png
```

## 图标尺寸规格

| 密度 | 倍数 | 生成尺寸 |
|------|------|----------|
| mdpi | 1x | 48×48 |
| hdpi | 1.5x | 72×72 |
| xhdpi | 2x | 96×96 |
| xxhdpi | 3x | 144×144 |
| xxxhdpi | 4x | 192×192 |

## 注意事项

1. **输入图片要求**：
   - 必须是 PNG 格式
   - 分辨率必须为 1024×1024 像素
   - 建议背景透明（特别是对于自适应图标）

2. **输出目录**：
   - 如果输出目录已存在，脚本会自动覆盖其中的文件
   - `res` 文件夹会在输出目录下自动创建

3. **自适应图标**：
   - 生成的 `ic_launcher_foreground.png` 可直接用于 Android 8.0+ 的自适应图标
   - 如需完整的自适应图标配置，还需创建 `ic_launcher_background.xml` 和 `ic_launcher.xml`

## 许可证

MIT License
