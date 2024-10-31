# 告警数据回调服务

这是一个使用 FastAPI 框架实现的 Python 服务，用于处理告警数据的回调流程。

## 功能

- 提供 `/callback/alarm` 接口，接受 JSON 格式的订阅告警数据
- 将接收到的数据写入 Markdown 文件
- 提供 `/view_alarms` 接口，以卡片式布局展示所有告警数据

## 安装

### 使用虚拟环境（不使用 conda）

1. 克隆此仓库
2. 进入项目目录
3. 运行设置脚本：
   ```
   chmod +x setup_venv.sh
   ./setup_venv.sh
   ```
4. 激活虚拟环境：
   ```
   source alarm_callback_env/bin/activate
   ```

### Linux 服务器部署

1. 将代码复制到服务器
2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```
3. 配置 `app/config.py` 文件，根据需要调整设置
4. 确保 `run.sh` 脚本中的虚拟环境路径正确
5. 给予 `run.sh` 执行权限：
   ```
   chmod +x run.sh
   ```

## 运行

### 使用虚拟环境

1. 确保你已经激活了虚拟环境
2. 运行启动脚本：
   ```
   ./run.sh
   ```

## 调试

1. 在 VS Code 中打开项目文件夹。
2. 确保已安装 Python 扩展。
3. 在 VS Code 的调试视图中，选择 "Python: FastAPI" 配置。
4. 按 F5 或点击 "开始调试" 按钮来启动调试会话。

## API 文档

运行服务后，访问 `http://your_server_ip:8080/docs` 查看 Swagger UI API 文档。

## 查看告警数据

访问 `http://your_server_ip:8080/view_alarms` 查看以卡片式布局展示的所有告警数据。

## 注意事项

- 确保服务器防火墙允许访问 8080 端口（或您配置的其他端口）。
- 在生产环境中，建议使用 Nginx 作为反向代理，并配置 HTTPS。
- 定期备份 `alarm_data.md` 文件以防数据丢失。

## 贡献

欢迎提交 Pull Requests 来改进这个项目。对于重大更改，请先开 issue 讨论您想要改变的内容。

## 许可

[MIT](https://choosealicense.com/licenses/mit/)
