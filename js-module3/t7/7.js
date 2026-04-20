'use strict';

const trigger = document.querySelector('#trigger');
const targetImage = document.querySelector('#target');

trigger.addEventListener('mouseenter', () => {
  targetImage.src = 'img/picB.jpg';
});

trigger.addEventListener('mouseleave', () => {
  targetImage.src = 'img/picA.jpg';
});
