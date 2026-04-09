'use strict';

const participantCount = Number(prompt('Enter the number of participants:'));
const participants = [];

for (let i = 1; i <= participantCount; i++) {
  const name = prompt(`Enter name for participant ${i}:`) || '';
  participants.push(name);
}

participants.sort((a, b) => a.localeCompare(b));

const target = document.getElementById('target');
const ol = document.createElement('ol');

for (const name of participants) {
  const li = document.createElement('li');
  li.textContent = name;
  ol.appendChild(li);
}

target.appendChild(ol);
