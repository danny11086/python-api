#!/bin/bash

# 设置虚拟环境名称
VENV_NAME="alarm_callback_env"

# 激活虚拟环境
source $VENV_NAME/bin/activate

# 启动应用
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080
