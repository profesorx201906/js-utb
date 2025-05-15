// ---- Ejemplo básico
/*
let numero = 0;

while (numero < 90) {
  console.log(numero);
  numero=parseInt(Math.random()*100);  
}
console.log("Finalizó ciclo While");*/

// ---- Ejemplo recorrer cadena hasta caracter ,

/*
let cadena = "Este es un ejemplo de cadena, para el ciclo while";
let i = 0;
while (cadena[i] !== ",") {
  console.log(cadena[i]);
  i++;
}
*/

// ---- Ejemplo do while
/*
let n = 0;
console.log("Inicio Ciclo while");
while (n !== 0) {
  console.log("el valor de n =" + n);
  n=0;
}
console.log("Fin Ciclo while");
console.log("Inicio Ciclo  do while");
do {
  console.log("el valor de n =" + n);
  n=0;
} while (n !== 0);
console.log("Fin Ciclo do while");

*/
let n=0;
do {
  console.log(n);
  n++;
} while (n<5);
