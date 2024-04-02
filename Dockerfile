# 基于Python的官方镜像作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用程序的端口（如果需要）
EXPOSE 8080

# 定义启动应用程序的命令
CMD ["python", "chatbot.py"]