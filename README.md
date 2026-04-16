# Auto Android icon

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

```bash
python generate_icons.py -i icon.png -o ./output
```

### 参数说明

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--input` | `-i` | 输入的 1024×1024 PNG 图标文件路径 | **必填** |
| `--output` | `-o` | 输出目录路径 | `./res_output` |

### 示例

```bash
# 使用当前目录下的 icon.png，输出到 ./my_app_res
python generate_icons.py -i icon.png -o ./my_app_res

# 使用指定路径的图标文件
python generate_icons.py -i /path/to/your/icon.png -o ./android_app/res
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
