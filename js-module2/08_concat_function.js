'use strict';

function concat(arr) {
  let result = '';

  for (const item of arr) {
    result += item;
  }

  return result;
}

const names = ['Johnny', 'DeeDee', 'Joey', 'Marky'];
const combined = concat(names);

document.getElementById('target').textContent = combined;
