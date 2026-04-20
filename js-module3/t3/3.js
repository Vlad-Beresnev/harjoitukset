'use strict';
const names = ['John', 'Paul', 'Jones'];

const target = document.querySelector('#target');
let listHtml = '';

for (const name of names) {
  listHtml += `<li>${name}</li>`;
}

target.innerHTML = listHtml;
