'use strict';

const numbers = [];

while (true) {
  const value = Number(prompt('Enter a number (0 to stop):'));

  if (value === 0) {
    break;
  }

  numbers.push(value);
}

numbers.sort((a, b) => b - a);
console.log(numbers);
