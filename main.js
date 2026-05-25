 function initArtifactPopup() {
            const artifactItems = document.querySelectorAll('.artifact-item');
            const popupWindow = document.getElementById('popup-window');
            const popupImage = document.getElementById('popup-image');
            const popupVideo = document.getElementById('popup-video');
            const closePopup = document.getElementById('close-popup');

            // 为每个文物项添加点击事件监听器
            artifactItems.forEach((item) => {
                item.addEventListener('click', () => {
                    const imageSrc = item.dataset.image;
                    const videoSrc = item.dataset.video;

                    popupImage.src = imageSrc;
                    popupVideo.src = videoSrc;

                    // 加载视频
                    popupVideo.load();

                    // 显示弹出窗口
                    popupWindow.classList.remove('hidden');
                });
            });

            // 为关闭按钮添加点击事件监听器
            closePopup.addEventListener('click', () => {
                popupWindow.classList.add('hidden');
            });

            // 为弹出窗口添加点击事件监听器，点击窗口外部关闭窗口
            popupWindow.addEventListener('click', (event) => {
                if (event.target === popupWindow) {
                    popupWindow.classList.add('hidden');
                }
            });
        }

        // 在页面加载完成后调用初始化函数
        window.addEventListener('load', () => {
            initArtifactPopup();
        });