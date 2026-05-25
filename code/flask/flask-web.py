from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
# 允许所有来源的跨域请求
CORS(app)

# 获取当前脚本所在的目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 定义一个路由，用于提供静态文件服务
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(BASE_DIR, path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)