// leer información de 100 personas
// su numero de identificación
// al ganador de la loteria cuyo numero identificacion = 123456
for (let index = 0; index < 100; index++) {
  if (index > 5) {
    break;// "convierte" un ciclo for en un ciclo while
  }
  console.log(index);
}
let tiempo = Date.now();
let tiempo1;
console.log(tiempo);

while (true) {
  tiempo1 = Date.now();
  if (Date.now() > tiempo + 1000) {
    break;
  }
}
console.log(tiempo1)