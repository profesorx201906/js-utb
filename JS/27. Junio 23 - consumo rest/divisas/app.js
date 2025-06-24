const rateDisplayDiv = document.getElementById('rateDisplay');
const updateRatesBtn = document.getElementById('updateRatesBtn');
const lastUpdatedP = document.getElementById('lastUpdated');

const API_KEY = 'e89661359afd81c452308024'; 
const BASE_CURRENCY = 'USD';
const API_URL = `https://v6.exchangerate-api.com/v6/${API_KEY}/latest/${BASE_CURRENCY}`;

async function obtenerTasasDeCambio() {
    rateDisplayDiv.innerHTML = '<p class="loading">Cargando tasas...</p>';
    lastUpdatedP.textContent = ''; 

    if (API_KEY === 'YOUR_API_KEY' || API_KEY === '') {
        rateDisplayDiv.innerHTML = '<p class="error">Por favor, reemplaza "YOUR_API_KEY" en app.js con tu clave obtenida de exchangerate-api.com.</p>';
        return;
    }

    try {
        const respuesta = await fetch(API_URL);

        if (!respuesta.ok) {
            const errorData = await respuesta.json(); 
            let errorMessage = `Error HTTP: ${respuesta.status}`;
            if (errorData && errorData.error_type) {
                errorMessage += ` - Tipo: ${errorData.error_type}. Mensaje: ${errorData.result}`; 
            } else {
                errorMessage += ` - ${respuesta.statusText}`;
            }
            throw new Error(errorMessage);
        }

        const data = await respuesta.json();
        console.log(API_URL);
        
        if (data.result === 'error') {
            throw new Error(`Error de la API: ${data.error_type}. Por favor, verifica tu clave o los límites de uso.`);
        }

        const tasas = data.conversion_rates;
        const usdToCop = tasas.COP; 
        const eurToUsd = tasas.EUR; 

        const eurToCop = eurToUsd * usdToCop;

        const formatter = new Intl.NumberFormat('es-CO', {
            style: 'currency',
            currency: 'COP',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });

        rateDisplayDiv.innerHTML = `
            <p>1 ${BASE_CURRENCY} = <span>${formatter.format(usdToCop)}</span></p>
            <p>1 EUR = <span>${formatter.format(eurToCop)}</span></p>
        `;

        const ultimaActualizacionTimestamp = data.time_last_update_unix * 1000; 
        const fechaActualizacion = new Date(ultimaActualizacionTimestamp);
        lastUpdatedP.textContent = `Última actualización: ${fechaActualizacion.toLocaleString('es-CO')}`;

    } catch (error) {
        console.error('Hubo un problema al obtener las tasas de cambio:', error);
        rateDisplayDiv.innerHTML = `<p class="error">Error al cargar las tasas: ${error.message}. Por favor, inténtalo de nuevo.</p>`;
        lastUpdatedP.textContent = '';
    }
}

obtenerTasasDeCambio();

updateRatesBtn.addEventListener('click', obtenerTasasDeCambio);