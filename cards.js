/* Shared script for index.html.
   Expects a global PROJECTS array to be defined in an inline <script> before this file loads. */
(function(){
  const grid = document.getElementById('grid');
  const filters = document.getElementById('filters');
  if(!grid || !filters || typeof PROJECTS === 'undefined') return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function mediaMarkup(p){
    return `<img src="media/${p.slug}-1.jpg" alt="${p.title}" loading="lazy" onerror="this.replaceWith(Object.assign(document.createElement('span'),{className:'placeholder-label',innerHTML:'DROP IMAGE NAMED &quot;${p.slug}-1.jpg&quot; INTO /media FOR<br>— ${p.title} —'}))">`;
  }

  function attachTilt(card){
    if(reduceMotion) return;
    const MAX_TILT = 9;
    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width;
      const py = (e.clientY - r.top) / r.height;
      const rotateY = (px - 0.5) * MAX_TILT * 2;
      const rotateX = (0.5 - py) * MAX_TILT * 2;
      card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
      card.style.setProperty('--mx', `${px * 100}%`);
      card.style.setProperty('--my', `${py * 100}%`);
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg) translateY(0)';
    });
  }

  function render(filter){
    grid.innerHTML = '';
    PROJECTS.forEach((p, i) => {
      if(filter !== 'all' && p.category !== filter) return;
      const card = document.createElement('a');
      card.className = 'card';
      card.href = `projects/${p.slug}.html`;
      card.innerHTML = `
        <div class="card-media">
          ${mediaMarkup(p)}
          <span class="sheet-tag mono">SHEET ${String(i+1).padStart(2,'0')}/${String(PROJECTS.length).padStart(2,'0')}</span>
        </div>
        <div class="card-body">
          <div class="card-cat">${p.catLabel}</div>
          <h3 class="card-title">${p.title}</h3>
          <p class="card-desc">${p.desc}</p>
          <div class="chip-row">${p.tools.map(t => `<span class="chip">${t}</span>`).join('')}</div>
        </div>
        <div class="tick-tl"></div><div class="tick-tr"></div><div class="tick-bl"></div><div class="tick-br"></div>
      `;
      attachTilt(card);
      grid.appendChild(card);
    });
  }

  filters.addEventListener('click', e => {
    if(!e.target.classList.contains('filter-btn')) return;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    e.target.classList.add('active');
    render(e.target.dataset.filter);
  });

  render('all');
})();
