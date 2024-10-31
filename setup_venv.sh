#!/bin/bash

# 设置虚拟环境名称
VENV_NAME="alarm_callback_env"

# 检查虚拟环境是否已存在
if [ ! -d "$VENV_NAME" ]; then
    echo "创建虚拟环境 $VENV_NAME..."
    python3 -m venv $VENV_NAME
else
    echo "虚拟环境 $VENV_NAME 已存在."
fi

# 激活虚拟环境
source $VENV_NAME/bin/activate

# 升级 pip
pip install --upgrade pip

# 安装依赖
pip install -r requirements.txt

echo "虚拟环境设置完成。使用 'source $VENV_NAME/bin/activate' 来激活它。"
