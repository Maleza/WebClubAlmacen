let page = 1;
let loading = false;

window.addEventListener('scroll', async () => {
    if (loading) return;

    // Si llegamos al fondo
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 200) {
        loading = true;
        page++;

        const response = await fetch(`/api/index-items/?page=${page}`);
        const data = await response.json();

        const container = document.getElementById("cards-grid");

        data.items.forEach(item => {
            container.innerHTML += `
                <article class="card">
                  <div class="thumb" style="background-image:url('${item.imagen}')"></div>
                  <div class="card-body">
                    <h3>${item.titulo}</h3>
                    <p class="excerpt">${item.descripcion}</p>
                    <div class="card-meta">
                      <span class="tag">${item.categoria}</span>
                      <a class="readmore" href="${item.link}">Leer</a>
                    </div>
                  </div>
                </article>
            `;
        });

        loading = false;
    }
});
