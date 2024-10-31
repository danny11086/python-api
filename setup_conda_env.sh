#!/bin/bash

# 设置环境名称
ENV_NAME="fastapi_alarm_callback"

# 创建新的 Conda 环境
conda create -n $ENV_NAME python=3.12 -y

# 激活环境
source activate $ENV_NAME

# 升级 pip
pip install --upgrade pip

# 安装项目依赖
pip install -r requirements.txt

echo "Conda 环境 '$ENV_NAME' 已创建并设置完成。使用 'conda activate $ENV_NAME' 来激活它。"
