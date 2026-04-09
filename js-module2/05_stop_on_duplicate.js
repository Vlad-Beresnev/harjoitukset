'use strict';

const numbers = [];

while (true) {
  const value = Number(prompt('Enter a number:'));

  if (numbers.includes(value)) {
    alert('The number has already been given. Program stops.');
    break;
  }

  numbers.push(value);
}

numbers.sort((a, b) => a - b);
console.log(numbers);
