app.get('/api/search', (req, res) => {
  const keyword = req.query.q;
  const query = 'SELECT * FROM artifacts WHERE name LIKE ? OR description LIKE ?';
  db.query(query, [`%${keyword}%`, `%${keyword}%`], (err, results) => {
    if (err) {
      return res.status(500).json({ error: '数据库查询失败' });
    }
    res.json(results);
  });
});