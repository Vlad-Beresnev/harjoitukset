'use strict';

const calculationInput = document.querySelector('#calculation');
const button = document.querySelector('#start');
const resultElement = document.querySelector('#result');

button.addEventListener('click', () => {
  const calculation = calculationInput.value.replaceAll(' ', '');
  let operator = '';

  if (calculation.includes('+')) {
    operator = '+';
  } else if (calculation.includes('-')) {
    operator = '-';
  } else if (calculation.includes('*')) {
    operator = '*';
  } else if (calculation.includes('/')) {
    operator = '/';
  } else {
    resultElement.textContent = 'Invalid expression';
    return;
  }

  const parts = calculation.split(operator);

  if (parts.length !== 2) {
    resultElement.textContent = 'Invalid expression';
    return;
  }

  const left = parseInt(parts[0], 10);
  const right = parseInt(parts[1], 10);

  if (Number.isNaN(left) || Number.isNaN(right)) {
    resultElement.textContent = 'Invalid expression';
    return;
  }

  let result;

  if (operator === '+') {
    result = left + right;
  } else if (operator === '-') {
    result = left - right;
  } else if (operator === '*') {
    result = left * right;
  } else {
    if (right === 0) {
      resultElement.textContent = 'Cannot divide by zero';
      return;
    }

    result = left / right;
  }

  resultElement.textContent = `Result: ${result}`;
});
