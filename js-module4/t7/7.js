'use strict';

const DESTINATION = {
  lat: 60.2231,
  lon: 24.7587,
  label: 'Karaportti 2, Espoo'
};

const OSRM_ROUTE_API = 'https://router.project-osrm.org/route/v1/driving';

const statusEl = document.querySelector('#status');
const tripTimesEl = document.querySelector('#trip-times');

let map;
let mapLayerGroup;

function initMap() {
  map = L.map('map').setView([60.22, 24.8], 11);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  mapLayerGroup = L.layerGroup().addTo(map);
}

async function fetchRoute(origin, destination) {
  const url = `${OSRM_ROUTE_API}/${origin.lon},${origin.lat};${destination.lon},${destination.lat}?overview=full&geometries=geojson`;
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Routing failed with status ${response.status}`);
  }

  const data = await response.json();

  if (!data.routes || data.routes.length === 0) {
    return null;
  }

  return data.routes[0];
}

function clearRoute() {
  mapLayerGroup.clearLayers();
  tripTimesEl.textContent = '';
}

function renderRoute(origin, destination, route) {
  clearRoute();

  const coords = route.geometry.coordinates.map((point) => [point[1], point[0]]);
  const polyline = L.polyline(coords, {color: 'blue', weight: 5}).addTo(mapLayerGroup);

  L.marker([origin.lat, origin.lon]).addTo(mapLayerGroup).bindPopup('Start: Your location');
  L.marker([destination.lat, destination.lon]).addTo(mapLayerGroup).bindPopup(`End: ${destination.label}`);

  map.fitBounds(polyline.getBounds(), {padding: [25, 25]});

  const startDate = new Date();
  const endDate = new Date(startDate.getTime() + route.duration * 1000);
  const startTime = startDate.toLocaleTimeString('fi-FI', {hour: '2-digit', minute: '2-digit'});
  const endTime = endDate.toLocaleTimeString('fi-FI', {hour: '2-digit', minute: '2-digit'});

  tripTimesEl.textContent = `Trip starts at ${startTime} and ends at about ${endTime}.`;
}

function getCurrentPosition() {
  return new Promise((resolve, reject) => {
    navigator.geolocation.getCurrentPosition(resolve, reject, {
      enableHighAccuracy: true,
      timeout: 15000,
      maximumAge: 0
    });
  });
}

async function loadRouteFromCurrentLocation() {
  if (!navigator.geolocation) {
    statusEl.textContent = 'Geolocation is not supported by this browser.';
    return;
  }

  statusEl.textContent = 'Requesting current location...';
  clearRoute();

  try {
    const position = await getCurrentPosition();
    const origin = {
      lat: position.coords.latitude,
      lon: position.coords.longitude,
      label: 'Your location'
    };

    statusEl.textContent = 'Loading route...';

    const route = await fetchRoute(origin, DESTINATION);

    if (!route) {
      statusEl.textContent = 'No route found from your location.';
      return;
    }

    renderRoute(origin, DESTINATION, route);
    statusEl.textContent = 'Route loaded.';
  } catch (error) {
    console.error(error);

    if (error.code === 1) {
      statusEl.textContent = 'Location permission denied.';
      return;
    }

    if (error.code === 2) {
      statusEl.textContent = 'Location unavailable.';
      return;
    }

    if (error.code === 3) {
      statusEl.textContent = 'Location request timed out.';
      return;
    }

    statusEl.textContent = 'Failed to load route. See console for details.';
    clearRoute();
  }
}

window.addEventListener('DOMContentLoaded', async () => {
  initMap();
  await loadRouteFromCurrentLocation();
});
