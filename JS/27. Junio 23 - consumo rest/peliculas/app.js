//Se accede a los elementos del DOM
const cargarPeliculasBtn = document.getElementById('cargarPeliculasBtn');
const peliculasContainer = document.getElementById('peliculas-container');
const mensajeCarga = document.getElementById('mensaje-carga');
//url del servicio rest 
const API_URL = 'https://jsonplaceholder.typicode.com/posts';

//peticiones asincronas
async function obtenerPeliculas() {

    mensajeCarga.textContent = 'Cargando películas...';

    peliculasContainer.innerHTML = '';

    try {
        //accedo al endpoint(direccion url de api rest para este caso API_URL)
        const respuesta = await fetch(API_URL);
        
        //verifico si la respuesta fue positiva, si es negativa muestro un error
        if (!respuesta.ok) {
            throw new Error(`Error HTTP: ${respuesta.status}`);
        }
        //si no hay error convierto la información a formato json
        const data = await respuesta.json();
        
        mensajeCarga.style.display = 'none';
        mostrarPeliculas(data);

    } catch (error) {
        //si se presenta un error en las sentencias anteriores se lanza esta excepción
        console.error('Hubo un problema al obtener las películas:', error);
        peliculasContainer.innerHTML = '<p>Lo sentimos, no pudimos cargar las películas. Inténtalo de nuevo más tarde.</p>';
        mensajeCarga.style.display = 'none';
    }
}

function mostrarPeliculas(peliculas) {
    
    
    //se extrae un numero de elementos del la data recibida para mostrala
    const peliculasAMostrar = peliculas.slice(0, 10);

    peliculasAMostrar.forEach(pelicula => {
        const peliculaCard = document.createElement('div');
        peliculaCard.classList.add('pelicula-card');
        const titulo = pelicula.title;
        const cuerpo = pelicula.body.substring(0, 100) + '...';
        const imagenUrl = `https://picsum.photos/200/300?random=${pelicula.id}`;
        console.log(imagenUrl);
        
        peliculaCard.innerHTML = `
            <img src="${imagenUrl}" alt="Poster de ${titulo}">
            <h2>${titulo}</h2>
            <p>${cuerpo}</p>
        `;
        peliculasContainer.appendChild(peliculaCard);
    });
}

//simular demora en la ejecución del script
function lanzar() {
    mensajeCarga.textContent = 'Cargando películas...';
    setTimeout(function () {
        obtenerPeliculas()
    }, 1)

}
cargarPeliculasBtn.addEventListener('click', lanzar);

