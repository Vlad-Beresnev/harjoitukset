'use strict';

const target = document.querySelector('#target');
const items = ['First item', 'Second item', 'Third item'];

for (let i = 0; i < items.length; i++) {
  const li = document.createElement('li');
  li.textContent = items[i];

  if (i === 1) {
    li.classList.add('my-item');
  }

  target.appendChild(li);
}
