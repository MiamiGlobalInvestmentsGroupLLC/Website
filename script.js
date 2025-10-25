// Header shadow on scroll
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 10);
});

// Mobile menu
const menuBtn = document.getElementById('menu');
const nav = document.getElementById('nav');
menuBtn?.addEventListener('click', ()=>{
  const open = nav.style.display === 'block';
  nav.style.display = open ? 'none' : 'block';
  menuBtn.setAttribute('aria-expanded', String(!open));
});

// Year
document.querySelectorAll('#year').forEach(el=> el.textContent = new Date().getFullYear());

// Reveal on scroll (IntersectionObserver)
const observer = new IntersectionObserver((entries)=>{
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
},{threshold:0.2});
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// Audio control (no autoplay to respect browser policies)
const btn = document.getElementById('audioBtn');
const bgm = document.getElementById('bgm');
btn?.addEventListener('click', ()=>{
  if (bgm.paused) { bgm.play(); btn.classList.add('playing'); }
  else { bgm.pause(); btn.classList.remove('playing'); }
});
