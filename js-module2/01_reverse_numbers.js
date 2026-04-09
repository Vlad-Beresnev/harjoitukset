'use strict';

const numbers = [];

for (let i = 1; i <= 5; i++) {
  const value = Number(prompt(`Enter number ${i}/5:`));
  numbers.push(value);
}

for (let i = numbers.length - 1; i >= 0; i--) {
  console.log(numbers[i]);
}
