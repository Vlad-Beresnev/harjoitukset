'use strict';

const statusEl = document.querySelector('#status');

(async () => {
  statusEl.textContent = 'Loading...';

  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');

    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    const data = await response.json();
    console.log(data.value);
    statusEl.textContent = 'Joke logged to console.';
  } catch (error) {
    console.error(error);
    statusEl.textContent = 'Failed to fetch joke. See console for details.';
  }
})();
