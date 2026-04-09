'use strict';

const dogs = [];

for (let i = 1; i <= 6; i++) {
  const name = prompt(`Enter name for dog ${i}:`) || '';
  dogs.push(name);
}

dogs.sort((a, b) => b.localeCompare(a));

const target = document.getElementById('target');
const ul = document.createElement('ul');

for (const name of dogs) {
  const li = document.createElement('li');
  li.textContent = name;
  ul.appendChild(li);
}

target.appendChild(ul);
