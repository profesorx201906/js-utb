const cargarPeliculasBtn = document.getElementById('cargarPeliculasBtn');
const peliculasContainer = document.getElementById('peliculas-container');
const mensajeCarga = document.getElementById('mensaje-carga');

const API_URL = 'https://jsonplaceholder.typicode.com/posts'; 


async function obtenerPeliculas() {

    mensajeCarga.textContent = 'Cargando películas...';
    peliculasContainer.innerHTML = ''; 

    try {
        const respuesta = await fetch(API_URL);

        if (!respuesta.ok) {
            throw new Error(`Error HTTP: ${respuesta.status}`);
        }
        const data = await respuesta.json();
        mensajeCarga.style.display = 'none';
        mostrarPeliculas(data);

    } catch (error) {
        console.error('Hubo un problema al obtener las películas:', error);
        peliculasContainer.innerHTML = '<p>Lo sentimos, no pudimos cargar las películas. Inténtalo de nuevo más tarde.</p>';
        mensajeCarga.style.display = 'none';     }
}

function mostrarPeliculas(peliculas) {
    const peliculasAMostrar = peliculas.slice(0, 10);

    peliculasAMostrar.forEach(pelicula => {
        const peliculaCard = document.createElement('div');
        peliculaCard.classList.add('pelicula-card');
        const titulo = pelicula.title;
        const cuerpo = pelicula.body.substring(0, 100) + '...'; 
        const imagenUrl = `https://picsum.photos/200/300?random=${pelicula.id}`; 

        peliculaCard.innerHTML = `
            <img src="${imagenUrl}" alt="Poster de ${titulo}">
            <h2>${titulo}</h2>
            <p>${cuerpo}</p>
        `;
        peliculasContainer.appendChild(peliculaCard);
    });
}

cargarPeliculasBtn.addEventListener('click', obtenerPeliculas);

