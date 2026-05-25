// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', () => {
  // 加载所有文物数据
  loadArtifacts();

  // 搜索功能
  setupSearch();
});

// 加载所有文物数据
function loadArtifacts() {
  fetch('http://localhost:3000/api/artifacts')
    .then(response => response.json())
    .then(data => {
      const galleryGrid = document.getElementById('gallery-grid');
      galleryGrid.innerHTML = ''; // 清空现有内容

      // 遍历数据并生成文物卡片
      data.forEach(artifact => {
        const card = createArtifactCard(artifact);
        galleryGrid.appendChild(card);

        // 初始化 3D 模型查看器
        new UniversalModelViewer(card.querySelector('.threejs-canvas'));
      });
    })
    .catch(error => {
      console.error('获取数据失败:', error);
    });
}

// 创建文物卡片
function createArtifactCard(artifact) {
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
  return card;
}

// 设置搜索功能
function setupSearch() {
  const searchButton = document.querySelector('.search-button');
  const searchInput = document.querySelector('.search-input');

  // 点击搜索按钮
  searchButton.addEventListener('click', () => {
    const keyword = searchInput.value.trim();
    if (keyword) {
      searchArtifacts(keyword);
    }
  });

  // 按下回车键
  searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      const keyword = searchInput.value.trim();
      if (keyword) {
        searchArtifacts(keyword);
      }
    }
  });
}

// 搜索文物数据
function searchArtifacts(keyword) {
  fetch(`http://localhost:3000/api/search?q=${encodeURIComponent(keyword)}`)
    .then(response => response.json())
    .then(data => {
      const galleryGrid = document.getElementById('gallery-grid');
      galleryGrid.innerHTML = ''; // 清空现有内容

      // 遍历搜索结果并生成文物卡片
      data.forEach(artifact => {
        const card = createArtifactCard(artifact);
        galleryGrid.appendChild(card);

        // 初始化 3D 模型查看器
        new UniversalModelViewer(card.querySelector('.threejs-canvas'));
      });
    })
    .catch(error => {
      console.error('搜索失败:', error);
    });
}

// Three.js 模型查看器
class UniversalModelViewer {
  constructor(canvasElement) {
    if (!canvasElement.dataset.model) {
      console.error('未指定模型路径');
      return;
    }

    this.canvas = canvasElement;
    this.modelPath = canvasElement.dataset.model;
    this.format = this.detectFormat();
    this.isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    this.initThree();
  }

  // 检测模型格式
  detectFormat() {
    const ext = this.modelPath.split('.').pop().toLowerCase();
    return ['glb', 'gltf'].includes(ext) ? 'glb' : ext;
  }

  // 初始化 Three.js
  initThree() {
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(
      45,
      this.canvas.clientWidth / this.canvas.clientHeight,
      0.1,
      1000
    );

    this.renderer = new THREE.WebGLRenderer({
      canvas: this.canvas,
      antialias: true,
      alpha: true
    });
    this.renderer.setPixelRatio(window.devicePixelRatio);

    this.initLights();
    this.loadModel();
  }

  // 初始化灯光
  initLights() {
    const ambient = new THREE.AmbientLight(0xffffff, 0.8);
    const directional = new THREE.DirectionalLight(0xffffff, 1);
    directional.position.set(5, 5, 5);
    this.scene.add(ambient, directional);
  }

  // 加载模型
  loadModel() {
    let loader;
    switch (this.format) {
      case 'fbx':
        loader = new THREE.FBXLoader();
        break;
      case 'glb':
      case 'gltf':
        loader = new THREE.GLTFLoader();
        break;
      default:
        console.error('不支持的格式:', this.format);
        return;
    }

    loader.load(
      this.modelPath,
      (model) => this.onModelLoaded(model),
      (xhr) => console.log(`加载进度: ${(xhr.loaded / xhr.total * 100).toFixed(1)}%`),
      (error) => {
        console.error('模型加载失败:', error);
        this.showErrorFallback();
      }
    );
  }

  // 模型加载完成后的处理
  onModelLoaded(model) {
    const model3D = this.format === 'glb' ? model.scene : model;

    model3D.traverse(child => {
      if (child.isMesh) {
        if (this.format === 'glb') {
          child.material.metalness = 0.5;
          child.material.roughness = 0.6;
        } else {
          child.material = new THREE.MeshStandardMaterial({
            map: child.material.map,
            metalness: 0.4,
            roughness: 0.5
          });
        }
      }
    });

    const box = new THREE.Box3().setFromObject(model3D);
    const size = box.getSize(new THREE.Vector3());
    const maxDim = Math.max(size.x, size.y, size.z);
    const scale = (this.canvas.dataset.scale || 1) / maxDim;

    model3D.scale.set(scale, scale, scale);
    this.scene.add(model3D);

    const center = box.getCenter(new THREE.Vector3());
    this.camera.position.set(center.x, center.y, center.z + maxDim * 1.5);
    this.camera.lookAt(center);

    if (model.animations?.length > 0) {
      this.mixer = new THREE.AnimationMixer(model3D);
      this.mixer.clipAction(model.animations[0]).play();
    }

    this.animate();
  }

  // 动画循环
  animate() {
    requestAnimationFrame(() => this.animate());
    if (this.mixer) this.mixer.update(0.016);
    this.renderer.render(this.scene, this.camera);
  }

  // 模型加载失败时的回退显示
  showErrorFallback() {
    this.canvas.parentElement.innerHTML = `
      <div class="model-error">
        <img src="./assets/error-icon.svg" alt="加载失败">
        <p>文物模型暂时无法呈现</p>
      </div>
    `;
  }
}