//---- ciclo for recorrer cadena

//Ejemplo básico

/*
let cadena = "hola campistas bienvenidos";
for (let letra of cadena){
  console.log(letra);  
}
*/

//-----------------------
// ejemplo eliminar espacios en blanco letra a letra
/*
for (let letra of cadena) {
  if (letra !== " ") {
    console.log(letra);
  }
}*/

//-----------------------
// ejemplo eliminar espacios en blanco nueva cadena
/*
let nuevaCadena = "";
for (let letra of cadena) {
  if (letra !== " ") {
    nuevaCadena += letra;
  }
}
console.log(nuevaCadena);
*/


//-----------------------
// ejemplo for of con arreglos
/*
let frutas = ["Manzana", "Pera", "Banana", "Kiwi", "Guanabana"];
for (let fruta of frutas) {
  console.log(fruta);
}*/

//-----------------------
// ejemplo for of con arreglos creando cadena a partir de los elementos
/*
let frutas = ["Manzana", "Pera", "Banana", "Kiwi", "Guanabana"];
let cadena = "";
for (let fruta of frutas) {
  cadena += fruta + " ";
}
console.log(cadena);
*/

//-----------------------
//dado un arreglo que contiene elementos del hogar determinar
// 1. cuantos elementos comienzan por la letra t
// 2. imprimir la longitud de cada uno de los elementos 
// 3. imprimir la totalidad de la longitud de todos los elementos
/*
let elementosHogar = [
  "televisor",
  "silla",
  "mesa",
  "tostadora",
  "cama",
  "lámpara",
  "refrigerador",
  "alfombra",
  "toalla",
  "espejo"
];

let contador = 0    
let acumuladorLetras=0
for (let i = 0; i < elementosHogar.length; i++) {
    if (elementosHogar[i].charAt(0) == "t") {
        contador++
    }
    console.log(elementosHogar[i] + " tiene " + elementosHogar[i].length + " caracteres")
    acumuladorLetras+=elementosHogar[i].length;
}
console.log("La cantidad de elementos que empiezan con t es: " + contador)
console.log("La cantidad de elementos es: " + elementosHogar.length)
 
console.log("La cantidad de caracteres de todos los elementos es: " + acumuladorLetras)
*/


const elementos = ["televisor", "toalla", "tostadora", "silla", "mesa", "cama", "lámpara", "refrigerador", "alfombra", "espejo"];

let count = 0;
let longitud = 0;
for (const elemento of elementos) {
  if (elemento[0] === "t") {
    count++; // Cantidad
  }
  console.log(`el elemento ${elemento} tiene una longitud de ${elemento.length}`)
  longitud += elemento.length;
}

console.log(`${count} elemento comienzan con t`);
console.log(`la total de logitud de todos los elementos es : ${longitud}`);
