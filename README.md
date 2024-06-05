
# 项目运行指南

## 前端项目运行

首先，确保你的系统已经安装了 Node.js 和 npm。

1. **安装依赖**：
    ```bash
    npm install
    ```

2. **运行开发服务器**：
    ```bash
    npm run dev
    ```

## 后端项目运行

确保你的系统已经安装了 Python 和 pip。

1. **安装依赖**：
    ```bash
    pip install -r requirements.txt
    ```

2. **运行 Django 服务器**：
    ```bash
    python manage.py runserver
    ```

## 注意事项

- 确保在运行以上命令之前，已经进入到项目的根目录。
- 如果在安装依赖或运行服务器过程中遇到问题，请检查相应的错误信息并进行调试。
- 在生产环境中，建议使用 `npm run build` 生成前端的静态文件，并使用合适的 Web 服务器（如 Nginx、Apache）和 WSGI 服务器（如 Gunicorn、uWSGI）来部署后端项目。