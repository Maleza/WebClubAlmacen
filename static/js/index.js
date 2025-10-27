// menú móvil
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('menu-toggle');
  const sidebar = document.getElementById('sidebar');

  toggle?.addEventListener('click', () => {
    sidebar.classList.toggle('open');
  });

  // búsqueda simple por título (filtra tarjetas)
  const search = document.getElementById('search-input');
  const cards = Array.from(document.querySelectorAll('.card'));

  function filtrar(term){
    const q = term.trim().toLowerCase();
    cards.forEach(card => {
      const title = (card.dataset.title || card.querySelector('h3')?.innerText || '').toLowerCase();
      card.style.display = title.includes(q) ? '' : 'none';
    });
  }

  search?.addEventListener('input', (e) => filtrar(e.target.value));
});
