'use strict';

const form = document.querySelector('#search-form');
const queryInput = document.querySelector('#query');
const statusEl = document.querySelector('#status');
const resultsEl = document.querySelector('#results');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const query = queryInput.value.trim();
  if (!query) {
    statusEl.textContent = 'Please enter a search term.';
    resultsEl.innerHTML = '';
    return;
  }

  statusEl.textContent = 'Loading...';
  resultsEl.innerHTML = '';

  try {
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(query)}`);

    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    const data = await response.json();

    if (!data.result || data.result.length === 0) {
      statusEl.textContent = 'No results found.';
      return;
    }

    for (const joke of data.result) {
      const article = document.createElement('article');
      const paragraph = document.createElement('p');
      paragraph.textContent = joke.value;
      article.appendChild(paragraph);
      resultsEl.appendChild(article);
    }

    statusEl.textContent = `Found ${data.result.length} joke(s).`;
  } catch (error) {
    console.error(error);
    statusEl.textContent = 'Failed to fetch jokes. See console for details.';
    resultsEl.innerHTML = '';
  }
});
