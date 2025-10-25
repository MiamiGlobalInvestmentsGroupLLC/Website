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
