/* Shared background: diagonal drifting L/S/T/R letters.
   Included on every page so the animated backdrop stays consistent site-wide. */
(function initDriftLetters(){
  function run(){
    const container = document.getElementById('bgLetters');
    if(!container) return;
    const CHARS = ['L','S','T','R'];
    const COUNT = 13;
    const letters = [];
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function rand(min, max){ return Math.random() * (max - min) + min; }

    function spawn(fresh){
      const size = rand(56, 132);
      const el = document.createElement('span');
      el.className = 'drift-letter';
      el.textContent = CHARS[Math.floor(rand(0, CHARS.length))];
      el.style.fontSize = size + 'px';
      container.appendChild(el);

      const vw = window.innerWidth, vh = window.innerHeight;
      const speed = rand(0.10, 0.26);
      const state = {
        el, size,
        x: fresh ? rand(0, vw) : rand(vw * 0.6, vw + 200),
        y: fresh ? rand(0, vh) : rand(-200, vh * 0.4),
        vx: -speed,
        vy: speed * rand(0.7, 1.1),
        rot: rand(0, 360),
        vr: rand(-0.05, 0.05) || 0.02,
        opacity: rand(0.14, 0.34)
      };
      el.style.opacity = state.opacity;
      letters.push(state);
    }

    for(let i = 0; i < COUNT; i++) spawn(true);

    function place(s){
      s.el.style.transform = `translate(${s.x}px, ${s.y}px) rotate(${s.rot}deg)`;
    }

    if(reduceMotion){
      letters.forEach(place);
      return;
    }

    function tick(){
      const vw = window.innerWidth, vh = window.innerHeight;
      letters.forEach(s => {
        s.x += s.vx;
        s.y += s.vy;
        s.rot += s.vr;
        if(s.x < -s.size - 40 || s.y > vh + s.size + 40){
          s.x = rand(vw * 0.55, vw + 200);
          s.y = rand(-200, vh * 0.25);
        }
        place(s);
      });
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
