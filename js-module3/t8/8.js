'use strict';

const num1Input = document.querySelector('#num1');
const num2Input = document.querySelector('#num2');
const operationSelect = document.querySelector('#operation');
const button = document.querySelector('#start');
const resultElement = document.querySelector('#result');

button.addEventListener('click', () => {
  const num1 = parseInt(num1Input.value, 10);
  const num2 = parseInt(num2Input.value, 10);

  if (Number.isNaN(num1) || Number.isNaN(num2)) {
    resultElement.textContent = 'Please enter valid integers';
    return;
  }

  const operation = operationSelect.value;
  let result;

  if (operation === 'add') {
    result = num1 + num2;
  } else if (operation === 'sub') {
    result = num1 - num2;
  } else if (operation === 'multi') {
    result = num1 * num2;
  } else if (operation === 'div') {
    if (num2 === 0) {
      resultElement.textContent = 'Cannot divide by zero';
      return;
    }

    result = num1 / num2;
  }

  resultElement.textContent = `Result: ${result}`;
});
