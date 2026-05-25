document.querySelector('.search-button').addEventListener('click', () => {
  const keyword = document.querySelector('.search-input').value.trim();
  if (keyword) {
    fetch(`http://localhost:3000/api/search?q=${keyword}`)
      .then(response => response.json())
      .then(data => {
        const galleryGrid = document.getElementById('gallery-grid');
        galleryGrid.innerHTML = ''; // 清空现有内容
        data.forEach(artifact => {
          const card = document.createElement('article');
          card.className = 'exhibit-card';
          card.innerHTML = `
            <div class="model-container">
              <canvas class="threejs-canvas" data-model="${artifact.model_path}"></canvas>
            </div>
            <div class="card-content">
              <h3>${artifact.name}</h3><br>
              <p>${artifact.description}</p>
            </div>
          `;
          galleryGrid.appendChild(card);
          new UniversalModelViewer(card.querySelector('.threejs-canvas'));
        });
      })
      .catch(error => {
        console.error('搜索失败:', error);
      });
  }
});