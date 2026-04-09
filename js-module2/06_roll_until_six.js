'use strict';

function rollDie() {
  return Math.floor(Math.random() * 6) + 1;
}

const rolls = [];
let roll;

do {
  roll = rollDie();
  rolls.push(roll);
} while (roll !== 6);

const target = document.getElementById('target');
const ul = document.createElement('ul');

for (const value of rolls) {
  const li = document.createElement('li');
  li.textContent = value;
  ul.appendChild(li);
}

target.appendChild(ul);
