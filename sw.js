const CACHE_NAME = 'bus-eta-v1';
const ASSETS = [
  '/',
  '/bus-eta/',
  '/bus-eta/23m.html',
  '/bus-eta/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
