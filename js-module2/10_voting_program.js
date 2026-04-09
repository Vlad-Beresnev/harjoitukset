'use strict';

const candidateCount = Number(prompt('Enter number of candidates:'));
const candidates = [];

for (let i = 1; i <= candidateCount; i++) {
  const name = prompt(`Name for candidate ${i}:`) || '';
  candidates.push({
    name,
    votes: 0,
  });
}

const voterCount = Number(prompt('Enter number of voters:'));

for (let i = 1; i <= voterCount; i++) {
  const vote = prompt(`Voter ${i}, enter candidate name (empty for empty vote):`) || '';

  if (vote.trim() === '') {
    continue;
  }

  const candidate = candidates.find((item) => item.name === vote);
  if (candidate) {
    candidate.votes += 1;
  }
}

candidates.sort((a, b) => b.votes - a.votes);

if (candidates.length > 0) {
  console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
}

console.log('results:');
for (const candidate of candidates) {
  console.log(`${candidate.name}: ${candidate.votes} votes`);
}
