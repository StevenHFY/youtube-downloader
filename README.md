# YouTube 视频下载器

这是一个功能强大的 YouTube 视频下载工具，使用 Python 编写，基于 yt-dlp 库实现。支持多种视频格式和质量选项，提供友好的命令行界面。

## 功能特点

- 支持多种视频格式和质量选项
  - 从 144p 到 1080p 的多种分辨率
  - MP4、WebM 等多种文件格式
  - 音频单独下载选项
- 显示详细的视频信息
  - 视频标题
  - 时长
  - 文件大小
  - 可用格式列表
- 实时下载进度显示
  - 进度条
  - 下载速度
  - 剩余时间
- 自定义下载选项
  - 可选择特定视频质量
  - 可自定义保存路径
  - 默认使用最佳质量
- 高级功能
  - 自动使用浏览器 Cookies
  - 支持代理设置
  - 智能反反爬虫机制

## 系统要求

- Python 3.8 或更高版本
- FFmpeg（用于视频处理和音视频合并）
- Chrome 浏览器（用于 Cookies 同步，可选）
- 网络连接
- 足够的磁盘空间

## 安装

1. 克隆或下载此仓库：

GitHub:
```bash
git clone git@github.com:StevenHFY/youtube-downloader.git
```

JihuLab:
```bash
git clone git@jihulab.com:Steven6880/youtube-downloader.git
```

cd youtube-downloader

2. 安装 Python 依赖：
```bash
pip install -r requirements.txt
```

3. 安装 FFmpeg：

macOS（使用 Homebrew）：
```bash
brew install ffmpeg
```

Windows（使用 Chocolatey）：
```bash
choco install ffmpeg
```

Linux（Ubuntu/Debian）：
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

## 使用方法

1. 运行程序：
```bash
python youtube_downloader.py
```

2. 输入 YouTube 视频链接
   - 格式示例：https://www.youtube.com/watch?v=XXXXXXXXXXX
   - 输入 'q' 退出程序

3. 选择视频格式
   - 程序会显示所有可用的视频格式
   - 可以通过格式代码选择特定质量
   - 直接回车使用最佳质量
   - 格式信息会显示是否包含视频和音频

4. 选择保存路径
   - 可以指定自定义路径
   - 直接回车使用默认路径（./downloads/）

## 高级使用说明

### Cookies 设置
1. 在 Chrome 浏览器中登录 YouTube
2. 程序会自动使用浏览器的 Cookies
3. 这样可以：
   - 下载会员视频
   - 避免反爬虫检测
   - 使用您的 YouTube 设置

### 代理设置
如果需要使用代理，可以：
1. 设置系统代理
2. 使用环境变量：
   ```bash
   export HTTP_PROXY="http://127.0.0.1:7890"
   export HTTPS_PROXY="http://127.0.0.1:7890"
   ```
3. 在代码中直接配置代理

### 反爬虫处理
如果遇到 "Sign in to confirm you're not a bot" 错误：
1. 在浏览器中登录 YouTube
2. 完成人机验证
3. 确保使用最新版本的程序
4. 等待几分钟后重试
5. 必要时使用代理

## 格式代码说明

下载时显示的格式代码含义：
- `[数字]p`：表示视频分辨率（如 720p、1080p）
- `mp4`/`webm`：视频文件格式
- `audio only`：仅音频文件
- `[视频]`：仅包含视频流
- `[音频]`：仅包含音频流
- `[视频+音频]`：包含完整的视频和音频
- 文件大小：预计的下载文件大小

## 注意事项

1. 下载限制
   - 请遵守 YouTube 的服务条款
   - 注意视频的版权限制
   - 某些视频可能有地区限制

2. 网络要求
   - 需要稳定的网络连接
   - 下载速度取决于网络状况
   - 部分视频可能需要代理访问

3. 存储空间
   - 确保有足够的磁盘空间
   - 高质量视频文件可能较大

## 常见问题

1. 如果出现 "视频不可用" 错误
   - 检查视频链接是否正确
   - 确认视频在您的地区是否可用
   - 某些视频可能需要登录才能访问

2. 下载速度慢
   - 检查网络连接
   - 尝试选择较低的视频质量
   - 考虑使用代理服务器

3. 格式选择建议
   - MP4 格式兼容性最好
   - WebM 格式文件较小
   - 选择合适的分辨率以平衡质量和文件大小

4. 视频没有声音
   - 确保已安装 FFmpeg
   - 检查 FFmpeg 是否在系统路径中
   - 尝试重新安装 FFmpeg
   - 选择不同的视频格式

5. FFmpeg 相关问题
   - 确保 FFmpeg 版本最新
   - 检查系统环境变量设置
   - Windows 用户需要重启终端
   - 如遇到权限问题，以管理员身份运行

6. 反爬虫相关问题
   - 确保使用最新版本的程序
   - 在浏览器中登录 YouTube
   - 完成人机验证后重试
   - 使用代理服务器
   - 等待一段时间后再试

## 更新日志

- 2024.03: 
  - 使用 yt-dlp 重写下载核心
  - 添加格式选择功能
  - 改进进度显示
  - 添加 FFmpeg 支持，解决视频无声音问题
  - 优化视频合并和转码功能
  - 更新依赖要求
  - 添加浏览器 Cookies 支持
  - 增强反反爬虫能力
  - 改进格式显示，清晰区分视频和音频流

## 依赖说明

主要依赖包：
- yt-dlp >= 2023.11.16：YouTube 视频下载核心
- tqdm == 4.66.1：进度条显示
- requests >= 2.31.0：网络请求处理
- colorama >= 0.4.6：终端颜色输出
- ffmpeg-python >= 0.2.0：FFmpeg 接口
- rich >= 13.7.0：终端美化

系统依赖：
- FFmpeg：用于视频处理
  - 音视频流合并
  - 格式转换
  - 视频编码
  - 元数据处理
- Chrome：用于 Cookies 同步（可选）

## 许可证

MIT License 