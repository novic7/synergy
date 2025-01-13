const images = [
    'images/image1.jpg',
    'images/image2.jpg',
    'images/image3.jpg',
    'images/image4.jpg',
    'images/image5.jpg'
];

let currentIndex = 0;

const sliderImage = document.getElementById('slider-image');
const imageCounter = document.getElementById('image-counter');

function updateImage() {
    sliderImage.src = images[currentIndex];
    imageCounter.textContent = `Изображение ${currentIndex + 1} из ${images.length}`;
}

document.getElementById('next-button').addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % images.length;
    updateImage();
});

document.getElementById('prev-button').addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateImage();
});

// Инициализация
updateImage();
