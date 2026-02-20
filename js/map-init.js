// Leaflet map initialization extracted from main.js
// Keep behavior identical; only move code for readability.

export function setTileTheme({ isDark, baseLayer, DARK_TILES, LIGHT_TILES }) {
  if (isDark) {
    document.body.classList.remove('light-mode');
    if (baseLayer) baseLayer.setUrl(DARK_TILES);
  } else {
    document.body.classList.add('light-mode');
    if (baseLayer) baseLayer.setUrl(LIGHT_TILES);
  }
}

export function initLeafletMap({ L, mapEl, appEl, isDark, DARK_TILES, LIGHT_TILES }) {
  const map = L.map(mapEl, { zoomControl: false }).setView([52.5200, 13.4050], 13);

  const baseLayer = L.tileLayer(isDark ? DARK_TILES : LIGHT_TILES, {
    attribution: '&copy; OpenStreetMap &copy; CARTO'
  }).addTo(map);

  // Create panes for layering
  map.createPane('customRouteLinePane');
  map.getPane('customRouteLinePane').style.zIndex = 450;

  map.createPane('customRouteStopsPane');
  map.getPane('customRouteStopsPane').style.zIndex = 500;

  const routeLayer = L.layerGroup().addTo(map);

  // Clear route when clicking on map background
  map.on('click', () => {
    if (routeLayer) routeLayer.clearLayers();
  });

  map.on('zoomstart', () => {
    document.querySelectorAll('.leaflet-marker-icon').forEach(el => { el.classList.add('no-transition'); });
  });
  map.on('zoomend', () => {
    setTimeout(() => {
      document.querySelectorAll('.leaflet-marker-icon').forEach(el => { el.classList.remove('no-transition'); });
    }, 100);
  });

  const resizeObserver = new ResizeObserver(() => {
    if (map) map.invalidateSize();
  });
  if (appEl) resizeObserver.observe(appEl);

  return { map, baseLayer, routeLayer, resizeObserver };
}
