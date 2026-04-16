# Auto-Android-icon

自动生成 Android 应用图标（mipmap）的 Python 脚本。根据指定的 1024×1024 像素的 `icon.png` 文件，自动生成不同密度下的三种图标文件，并按照 Android 标准目录结构保存。

## 功能特点

- ✅ 支持生成 5 种密度的图标：mdpi、hdpi、xhdpi、xxhdpi、xxxhdpi
- ✅ 自动生成三种图标文件：
  - `ic_launcher.png` - 标准启动图标
  - `ic_launcher_foreground.png` - 自适应图标前景层
  - `ic_launcher_round.png` - 圆形启动图标
- ✅ 按照 Android 标准目录结构输出（`res/mipmap-*/`）
- ✅ 使用高质量 LANCZOS 滤镜进行图片缩放

## 前置要求

- Python 3.6 或更高版本
- Pillow 库（Python 图像处理库）

## 安装依赖

```bash
pip install Pillow
```

## 使用方法

### 1. 配置输入输出路径

打开 `Auto-Android-icon.py` 脚本，在文件顶部的**配置区域**修改输入和输出路径：

```python
# ================= 配置区域 =================
# 输入图片路径 (必须是 1024x1024 的 png 文件)
INPUT_IMAGE_PATH = "icon.png"

# 输出根目录路径 (生成的 res 文件夹将保存在此目录下)
OUTPUT_ROOT_PATH = "./output_res"
# ===========================================
```

**参数说明：**
| 参数 | 说明 | 默认值 |
|------|------|--------|
| `INPUT_IMAGE_PATH` | 输入的 1024×1024 PNG 图标文件路径 | `icon.png` |
| `OUTPUT_ROOT_PATH` | 输出目录路径，脚本会在此目录下创建 `res` 文件夹 | `./output_res` |

### 2. 准备源图片

将你的 1024×1024 像素的 PNG 图标文件命名为 `icon.png`，并放置在脚本所在目录（或你在 `INPUT_IMAGE_PATH` 中指定的路径）。

### 3. 运行脚本

```bash
python Auto-Android-icon.py
```

### 示例

假设你的项目结构如下：

```
my_project/
├── Auto-Android-icon.py
├── icon.png          # 你的 1024x1024 源图标
└── app/              # 输出到这里
```

修改脚本配置：

```python
INPUT_IMAGE_PATH = "icon.png"
OUTPUT_ROOT_PATH = "./app"
```

运行脚本后，会在 `app/res/` 目录下生成所有图标。

## 输出结构

脚本执行成功后，会生成以下目录结构：

```
output_res/
└── res/
    ├── mipmap-mdpi/
    │   ├── ic_launcher.png (48x48)
    │   ├── ic_launcher_foreground.png (48x48)
    │   └── ic_launcher_round.png (48x48)
    ├── mipmap-hdpi/
    │   ├── ic_launcher.png (72x72)
    │   ├── ic_launcher_foreground.png (72x72)
    │   └── ic_launcher_round.png (72x72)
    ├── mipmap-xhdpi/
    │   ├── ic_launcher.png (96x96)
    │   ├── ic_launcher_foreground.png (96x96)
    │   └── ic_launcher_round.png (96x96)
    ├── mipmap-xxhdpi/
    │   ├── ic_launcher.png (144x144)
    │   ├── ic_launcher_foreground.png (144x144)
    │   └── ic_launcher_round.png (144x144)
    └── mipmap-xxxhdpi/
        ├── ic_launcher.png (192x192)
        ├── ic_launcher_foreground.png (192x192)
        └── ic_launcher_round.png (192x192)
```

## 图标尺寸规格

| 密度 | 文件夹名称 | 图标尺寸 | 缩放比例 |
|------|-----------|---------|---------|
| mdpi | mipmap-mdpi | 48×48 | 1x |
| hdpi | mipmap-hdpi | 72×72 | 1.5x |
| xhdpi | mipmap-xhdpi | 96×96 | 2x |
| xxhdpi | mipmap-xxhdpi | 144×144 | 3x |
| xxxhdpi | mipmap-xxxhdpi | 192×192 | 4x |

## 注意事项

1. **输入图片要求**：
   - 推荐尺寸为 1024×1024 像素
   - 格式必须为 PNG（支持透明度）
   - 如果尺寸不是 1024×1024，脚本会发出警告但仍会继续处理

2. **输出目录**：
   - 如果输出目录不存在，脚本会自动创建
   - 如果目录已存在，新生成的图标会覆盖同名文件

3. **自适应图标**：
   - Android 8.0 (API 26+) 支持自适应启动图标
   - `ic_launcher_foreground.png` 用于自适应图标的前景层
   - 你可能还需要准备一个背景层 (`ic_launcher_background.png`)

4. **直接使用**：
   - 将生成的 `res` 文件夹整个复制到你的 Android 项目的 `app/src/main/` 目录下即可

## 许可证

MIT License
