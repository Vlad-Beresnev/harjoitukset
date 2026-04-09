'use strict';

function even(arr) {
  const evenNumbers = [];

  for (const value of arr) {
    if (value % 2 === 0) {
      evenNumbers.push(value);
    }
  }

  return evenNumbers;
}

const numbers = [2, 7, 4];
const onlyEven = even(numbers);

console.log('Original array:', numbers);
console.log('Even numbers:', onlyEven);
