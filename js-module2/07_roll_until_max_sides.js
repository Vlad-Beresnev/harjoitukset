'use strict';

function rollDie(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

const sides = Number(prompt('Enter number of sides on the dice:'));
const rolls = [];
let roll;

do {
  roll = rollDie(sides);
  rolls.push(roll);
} while (roll !== sides);

const target = document.getElementById('target');
const ul = document.createElement('ul');

for (const value of rolls) {
  const li = document.createElement('li');
  li.textContent = value;
  ul.appendChild(li);
}

target.appendChild(ul);
