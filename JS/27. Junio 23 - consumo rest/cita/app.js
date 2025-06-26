const citaTextoDiv = document.getElementById('citaTexto');
const citaAutorDiv = document.getElementById('citaAutor');
const idiomaOriginalSpan = document.getElementById('idiomaOriginal');
const nuevaCitaBtn = document.getElementById('nuevaCitaBtn');
const citaContainer = document.getElementById('citaContainer');

let citaOriginalTexto = '';
let citaOriginalAutor = '';

const CITA_API_URL = 'https://api.quotable.io/random';
const TRADUCCION_API_URL = 'https://api.mymemory.translated.net/get';

async function obtenerCitaAleatoria() {
    citaTextoDiv.textContent = 'Cargando cita...';
    citaAutorDiv.textContent = '';
    idiomaOriginalSpan.style.display = 'none';
    citaContainer.classList.add('loading');
    citaContainer.classList.remove('error');

    try {
        const respuesta = await fetch(CITA_API_URL);

        if (!respuesta.ok) {
            throw new Error(`Error HTTP: ${respuesta.status} - ${respuesta.statusText}`);
        }

        const data = await respuesta.json();

        citaOriginalTexto = data.content;
        citaOriginalAutor = data.author;

        citaTextoDiv.textContent = `"${citaOriginalTexto}"`;
        citaAutorDiv.textContent = `- ${citaOriginalAutor}`;
        idiomaOriginalSpan.style.display = 'block';
        citaContainer.classList.remove('loading');

        await traducirCitaAutomatica();

    } catch (error) {
        console.error('Hubo un problema al obtener la cita:', error);
        citaTextoDiv.textContent = 'Lo sentimos, no pudimos cargar una cita.';
        citaAutorDiv.textContent = 'Por favor, inténtalo de nuevo.';
        idiomaOriginalSpan.style.display = 'none';
        citaContainer.classList.add('error');
        citaContainer.classList.remove('loading');
    }
}

async function traducirCitaAutomatica() {
    if (!citaOriginalTexto) {
        return;
    }

    const textoATraducir = citaOriginalTexto;
    citaTextoDiv.textContent = 'Traduciendo...';
    citaContainer.classList.add('loading'); 

    try {
        const traduccionUrlCompleta = `${TRADUCCION_API_URL}?langpair=en|es&q=${encodeURIComponent(textoATraducir)}`;
        
        const response = await fetch(traduccionUrlCompleta);
        console.log(traduccionUrlCompleta);
        
        if (!response.ok) {
            throw new Error(`Error al traducir: ${response.status} - ${response.statusText}`);
        }

        const data = await response.json();
        
        const citaTraducida = data.responseData.translatedText;

        citaTextoDiv.textContent = `"${citaTraducida}"`;
        citaAutorDiv.textContent = `- ${citaOriginalAutor}`;
        idiomaOriginalSpan.style.display = 'none'; 
        citaContainer.classList.remove('loading');

    } catch (error) {
        console.error('Error al traducir la cita:', error);
        citaTextoDiv.textContent = `"${citaOriginalTexto}"`;
        citaAutorDiv.textContent = `- ${citaOriginalAutor}`;
        idiomaOriginalSpan.textContent = '(Error al traducir - Original en inglés)';
        idiomaOriginalSpan.style.display = 'block';
        citaContainer.classList.add('error');
        citaContainer.classList.remove('loading');
    }
}

obtenerCitaAleatoria();

nuevaCitaBtn.addEventListener('click', obtenerCitaAleatoria);