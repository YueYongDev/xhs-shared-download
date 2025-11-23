# 小红书图片下载工具

一个简单易用的小红书图片批量下载工具，支持去水印，适配移动端和桌面端。

## 功能特点

- 📱 完美适配移动端和桌面端
- 🚀 简单易用，粘贴分享文本即可使用
- 💫 支持长按（移动端）/ 右键（桌面端）保存图片

## 在线体验

访问地址：[xhs.dashuaibi.monster](https://xhs.dashuaibi.monster)

## 使用说明

1. 打开小红书APP，点击分享按钮
2. 选择"复制链接"
3. 将复制的内容粘贴到输入框
4. 点击获取图片
5. 长按(手机)或右键(电脑)保存图片

## 部署说明

### Docker 部署（推荐）

克隆项目
```bash
git clone https://github.com/your-username/xiaohongshu-downloader.git
```

进入项目目录
```bash
cd xiaohongshu-downloader
```

启动服务
```bash
docker compose up --build -d
```

默认端口：10010，如需修改请编辑 docker-compose.yaml 文件

### 手动部署

1. 确保已安装 Python 3.7+
2. 安装依赖：`pip install -r requirements.txt`
3. 运行服务：`python app.py`

## API 调用示例

### 图片下载 API
获取小红书帖子中的所有图片URL列表
```bash
curl -X POST http://localhost:10010/api/images \
  -H "Content-Type: application/json" \
  -d '{"shareUrl": "复制的小红书分享文本或链接"}'
```

响应示例：
```json
{
  "code": 200,
  "message": "",
  "data": [
    "https://img.xiaohongshu.com/xxx1.jpg",
    "https://img.xiaohongshu.com/xxx2.jpg"
  ]
}
```

### 视频下载 API
获取小红书视频信息和下载链接
```bash
curl -X POST http://localhost:10010/api/video \
  -H "Content-Type: application/json" \
  -d '{"shareUrl": "复制的小红书分享文本或链接"}'
```

响应示例：
```json
{
  "code": 200,
  "message": "",
  "data": {
    "keyword": "视频关键词",
    "link": "https://video.xiaohongshu.com/xxx.mp4",
    "time": "120"
  }
}
```

### 图片代理下载
通过代理服务器下载图片（解决跨域问题）
```bash
curl "http://localhost:10010/proxy_image?url=https://img.xiaohongshu.com/xxx.jpg"
```

### 直接下载图片
直接下载并保存图片文件
```bash
curl "http://localhost:10010/api/download?url=https://img.xiaohongshu.com/xxx.jpg" -o image.jpg
```

## Docker 运行说明

### 基本命令
构建并启动容器：
```bash
docker compose up --build -d
```

查看容器日志：
```bash
docker compose logs -f
```

停止服务：
```bash
docker compose down
```

### 常见问题解决

如果遇到Docker构建失败（如网络问题），可以尝试以下解决方案：

1. **更换Python基础镜像**：Dockerfile已更新为使用`python:3.11-slim`，如果仍有问题可手动修改Dockerfile中的基础镜像版本。

2. **配置Docker镜像源**：在国内可能需要配置Docker镜像加速器。

3. **手动部署作为备选**：如果Docker无法正常工作，推荐使用手动部署方式。

## 项目截图

![移动端效果](https://github.com/user-attachments/assets/6efc5a4c-a65b-40ec-8d7f-110e53d2cd2f)

![桌面端效果](https://github.com/user-attachments/assets/984e0731-e140-4d9b-a317-16c13841b497)

## 技术栈

- 前端：HTML5 + CSS3 + JavaScript
- 后端：Python
- 部署：Docker

## 注意事项

- 本工具仅供学习交流使用
- 请勿用于商业用途
