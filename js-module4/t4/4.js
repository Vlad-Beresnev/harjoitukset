'use strict';

const FALLBACK_IMAGE = 'https://placehold.co/210x295?text=Not%20Found';

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
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);

    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    const data = await response.json();

    if (data.length === 0) {
      statusEl.textContent = 'No results found.';
      return;
    }

    for (const item of data) {
      const show = item.show;

      const article = document.createElement('article');

      const title = document.createElement('h2');
      title.textContent = show.name;

      const link = document.createElement('a');
      link.href = show.url;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.textContent = 'Show details';

      const image = document.createElement('img');
      const mediumImage = show.image && show.image.medium ? show.image.medium : FALLBACK_IMAGE;
      image.src = mediumImage;
      image.alt = show.name;

      const summary = document.createElement('div');
      summary.innerHTML = show.summary || 'No summary available.';

      article.append(title, link, image, summary);
      resultsEl.appendChild(article);
    }

    statusEl.textContent = `Found ${data.length} result(s).`;
  } catch (error) {
    console.error(error);
    statusEl.textContent = 'Failed to fetch data. See console for details.';
    resultsEl.innerHTML = '';
  }
});
