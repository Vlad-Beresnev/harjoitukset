'use strict';

const form = document.querySelector('#search-form');
const queryInput = document.querySelector('#query');
const statusEl = document.querySelector('#results');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const query = queryInput.value.trim();
  if (!query) {
    statusEl.textContent = 'Please enter a search term.';
    return;
  }

  statusEl.textContent = 'Loading...';

  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);

    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
    statusEl.textContent = `Fetched ${data.length} result(s). Check console.`;
  } catch (error) {
    console.error(error);
    statusEl.textContent = 'Failed to fetch data. See console for details.';
  }
});
