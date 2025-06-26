const obtenerClimaBtn = document.getElementById('obtenerClimaBtn'); 
const resultadoClimaDiv = document.getElementById('resultadoClima');
async function obtenerClimaPorUbicacion() {
    resultadoClimaDiv.innerHTML = '<p class="loading">Buscando tu ubicación...</p>';

    if (!navigator.geolocation) {
        resultadoClimaDiv.innerHTML = '<p class="error">Tu navegador no soporta la geolocalización.</p>';
        return;
    }

    try {
        const position = await new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(resolve, reject, { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 });
        });
        console.log(position);
        
        const latitud = position.coords.latitude;
        const longitud = position.coords.longitude;

        resultadoClimaDiv.innerHTML = `<p class="loading">Ubicación encontrada (${latitud.toFixed(2)}, ${longitud.toFixed(2)}). Obteniendo clima...</p>`;

        const climaUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitud}&longitude=${longitud}&current_weather=true&forecast_days=1`;
        const climaResponse = await fetch(climaUrl);

        if (!climaResponse.ok) {
            throw new Error(`Error al obtener datos del clima: ${climaResponse.status}`);
        }

        const climaData = await climaResponse.json();

        if (!climaData.current_weather) {
            resultadoClimaDiv.innerHTML = `<p class="error">No se pudo obtener el clima actual para esta ubicación.</p>`;
            return;
        }

        const temperatura = climaData.current_weather.temperature;
        const velocidadViento = climaData.current_weather.windspeed;
        const weatherCode = climaData.current_weather.weathercode;

        function obtenerDescripcionClima(code) {
            if (code >= 0 && code <= 3) return 'Soleado / Parcialmente Nublado';
            if (code >= 45 && code <= 48) return 'Niebla';
            if (code >= 51 && code <= 55) return 'Llovizna';
            if (code >= 61 && code <= 65) return 'Lluvia';
            if (code >= 71 && code <= 75) return 'Nieve';
            if (code >= 95 && code <= 99) return 'Tormenta';
            return 'Condición Desconocida';
        }

        const descripcionClima = obtenerDescripcionClima(weatherCode);

        const geoReverseUrl = `https://nominatim.openstreetmap.org/reverse?lat=${latitud}&lon=${longitud}&format=json&zoom=10`;
        const geoReverseResponse = await fetch(geoReverseUrl);
        const geoReverseData = await geoReverseResponse.json();

        let nombreCiudad = "Tu ubicación";
        if (geoReverseData.address && (geoReverseData.address.city || geoReverseData.address.town || geoReverseData.address.village)) {
            nombreCiudad = geoReverseData.address.city || geoReverseData.address.town || geoReverseData.address.village;
        } else if (geoReverseData.display_name) {
             nombreCiudad = geoReverseData.display_name;
        }


        resultadoClimaDiv.innerHTML = `
            <p><strong>Ubicación:</strong> ${nombreCiudad}</p>
            <p><strong>Temperatura:</strong> ${temperatura}°C</p>
            <p><strong>Condición:</strong> ${descripcionClima}</p>
            <p><strong>Viento:</strong> ${velocidadViento} km/h</p>
        `;

    } catch (error) {
        console.error('Hubo un error al obtener la ubicación o el clima:', error);
        let mensajeError = 'No se pudo obtener el clima de tu ubicación.';
        if (error.code === error.PERMISSION_DENIED) {
            mensajeError = 'Necesitamos tu permiso para acceder a la ubicación. Por favor, permítelo en la configuración de tu navegador.';
        } else if (error.code === error.POSITION_UNAVAILABLE) {
            mensajeError = 'La información de ubicación no está disponible.';
        } else if (error.code === error.TIMEOUT) {
            mensajeError = 'Tiempo de espera agotado al intentar obtener la ubicación.';
        } else {
            mensajeError += ` Error: ${error.message}`;
        }
        resultadoClimaDiv.innerHTML = `<p class="error">${mensajeError}</p>`;
    }
}


obtenerClimaPorUbicacion();

