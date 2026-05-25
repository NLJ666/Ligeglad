const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mysql = require('mysql2');

// 创建 Express 应用
const app = express();
const port = 3000;

// 允许跨域请求
app.use(cors());

// 解析 JSON 请求体
app.use(bodyParser.json());

// 创建 MySQL 数据库连接
const db = mysql.createConnection({
  host: 'localhost', // 数据库主机名
  user: 'root', // 数据库用户名
  password: 'wh123', // 数据库密码
  database: 'CulturalHeritageDB' // 数据库名称
});

// 测试数据库连接
db.connect((err) => {
  if (err) {
    console.error('数据库连接失败:', err);
  } else {
    console.log('数据库连接成功');
  }
});

// 获取所有文物数据的 API
app.get('/api/artifacts', (req, res) => {
  const query = 'SELECT * FROM artifacts'; // 查询所有文物数据
  db.query(query, (err, results) => {
    if (err) {
      return res.status(500).json({ error: '数据库查询失败' });
    }
    res.json(results); // 返回查询结果
  });
});

// 搜索文物数据的 API
app.get('/api/search', (req, res) => {
  const keyword = req.query.q; // 获取搜索关键词
  if (!keyword) {
    return res.status(400).json({ error: '请输入搜索关键词' });
  }

  const query = `
    SELECT * FROM artifacts
    WHERE name LIKE ? OR description LIKE ?
  `;
  const searchTerm = `%${keyword}%`;

  db.query(query, [searchTerm, searchTerm], (err, results) => {
    if (err) {
      return res.status(500).json({ error: '数据库查询失败' });
    }
    res.json(results); // 返回搜索结果
  });
});

// 添加新文物数据的 API
app.post('/api/artifacts', (req, res) => {
  const { name, description, model_path, image_path } = req.body;

  if (!name || !description || !model_path) {
    return res.status(400).json({ error: '缺少必填字段' });
  }

  const query = `
    INSERT INTO artifacts (name, description, model_path, image_path)
    VALUES (?, ?, ?, ?)
  `;
  const values = [name, description, model_path, image_path];

  db.query(query, values, (err, results) => {
    if (err) {
      return res.status(500).json({ error: '数据库插入失败' });
    }
    res.status(201).json({ message: '文物添加成功', id: results.insertId });
  });
});

// 启动服务器
app.listen(port, () => {
  console.log(`服务器运行在 http://localhost:${port}`);
});