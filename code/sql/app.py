"""
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# 数据库配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password':'wh123'
    'database':'CulturalHeritageDB'
}

# 搜索接口
@app.route('/api/search', methods=['GET'])
def search_artifacts():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': '请输入搜索内容'}), 400

    try:
        # 连接数据库
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # 执行查询
        sql = "SELECT * FROM ArtifactInfo WHERE Name LIKE %s"
        cursor.execute(sql, (f'%{query}%',))
        results = cursor.fetchall()

        # 关闭连接
        cursor.close()
        connection.close()

        # 返回结果
        return jsonify(results)
    except Exception as e:
        print(f"数据库查询失败: {e}")
        return jsonify({'error': '数据库查询失败'}), 500

# 启动服务
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)"""