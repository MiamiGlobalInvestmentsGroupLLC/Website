// Basic interactions + year stamp
const menuBtn = document.getElementById('menu');
const nav = document.getElementById('nav');
menuBtn?.addEventListener('click', ()=>{
  const open = nav.style.display === 'block';
  nav.style.display = open ? 'none' : 'block';
  menuBtn.setAttribute('aria-expanded', String(!open));
});
document.querySelectorAll('#year').forEach(el=> el.textContent = new Date().getFullYear());
