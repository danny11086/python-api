# 使用官方 Python 作为基础镜像
FROM python:3.12.3-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到容器的 /app 目录
COPY . .

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露应用运行的端口（根据需要修改）
EXPOSE 8080

# 运行应用（根据您的应用入口点进行修改） 
CMD ["gunicorn", "-b", "0.0.0.0:8080","-k", "uvicorn.workers.UvicornWorker", "--reload", "app.main:app"]

