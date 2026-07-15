/* Shared script for project detail pages.
   Auto-detects photos by trying media/{slug}-1.jpg, {slug}-2.jpg, {slug}-3.jpg ...
   Just drop numbered files into /media named after the project's slug — no code edits needed.
   Expects a global PROJECT_SLUG string (and PROJECT_TITLE) defined inline before this file loads. */
(function(){
  const frame = document.getElementById('carouselFrame');
  const thumbs = document.getElementById('carouselThumbs');
  const counter = document.getElementById('carouselCounter');
  if(!frame) return;

  const slug = (typeof PROJECT_SLUG !== 'undefined') ? PROJECT_SLUG : '';
  const title = (typeof PROJECT_TITLE !== 'undefined') ? PROJECT_TITLE : '';
  const MAX_PROBE = 30;
  let images = [];
  let current = 0;

  function probe(n){
    return new Promise(resolve => {
      const src = `../media/${slug}-${n}.jpg`;
      const img = new Image();
      img.onload = () => resolve(src);
      img.onerror = () => resolve(null);
      img.src = src;
    });
  }

  async function detectImages(){
    for(let n = 1; n <= MAX_PROBE; n++){
      const src = await probe(n);
      if(!src) break; // stop at first gap in numbering
      images.push(src);
    }
    renderFrame();
  }

  function renderFrame(){
    if(images.length === 0){
      frame.innerHTML = `<div class="carousel-placeholder">DROP PHOTOS NAMED "${slug}-1.jpg", "${slug}-2.jpg"... INTO /media FOR<br>— ${title} —</div>`;
      if(counter) counter.style.display = 'none';
      return;
    }
    frame.innerHTML = `
      <img src="${images[current]}" alt="${title} — image ${current + 1}">
      ${images.length > 1 ? `
        <div class="carousel-arrow prev" id="prevBtn" aria-label="Previous photo">&#8249;</div>
        <div class="carousel-arrow next" id="nextBtn" aria-label="Next photo">&#8250;</div>
      ` : ''}
    `;
    if(counter){
      counter.style.display = images.length > 1 ? 'block' : 'none';
      counter.textContent = `${current + 1} / ${images.length}`;
    }
    if(images.length > 1){
      document.getElementById('prevBtn').addEventListener('click', () => go(current - 1));
      document.getElementById('nextBtn').addEventListener('click', () => go(current + 1));
    }
    if(thumbs){
      if(images.length > 1){
        thumbs.innerHTML = images.map((src, i) =>
          `<img src="${src}" class="carousel-thumb${i === current ? ' active' : ''}" data-i="${i}" alt="${title} thumbnail ${i+1}">`
        ).join('');
        thumbs.querySelectorAll('.carousel-thumb').forEach(t => {
          t.addEventListener('click', () => go(parseInt(t.dataset.i, 10)));
        });
      } else {
        thumbs.innerHTML = '';
      }
    }
  }

  function go(i){
    current = (i + images.length) % images.length;
    renderFrame();
  }

  document.addEventListener('keydown', e => {
    if(images.length <= 1) return;
    if(e.key === 'ArrowLeft') go(current - 1);
    if(e.key === 'ArrowRight') go(current + 1);
  });

  detectImages();
})();

