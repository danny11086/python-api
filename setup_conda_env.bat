@echo off

REM 设置环境名称
set ENV_NAME=fastapi_alarm_callback

REM 创建新的 Conda 环境
call conda create -n %ENV_NAME% python=3.12 -y

REM 激活环境
call conda activate %ENV_NAME%

REM 升级 pip
python -m pip install --upgrade pip

REM 安装项目依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

echo Conda 环境 '%ENV_NAME%' 已创建并设置完成。使用 'conda activate %ENV_NAME%' 来激活它。
