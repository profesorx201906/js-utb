/* ejemplo básico
let n = 0;
for (let i = 0; i < 9; i++) {
  n += i;
  //n=n+i;
}
console.log(n);
*/

//-----------------------
/*hacer un ciclo que imprima los numeros pares desde el numero 10 hasta el numero 30 inclusives

for (let i = 10; i <= 30; i+=2) {
  console.log(i);
}*/

//-----------------------

/* hacer una modificacion para imprimir los numeros pares del 30 al 10 sin incluirlos

for (let i = 28; i > 10; i -= 2) {
  console.log(i);
}*/


//-----------------------


/*imprimir una a una las letras de la cadena
let cadena = "hola campistas bienvenidos";
for (let i = 0; i < cadena.length; i++) {
    console.log(cadena[i]);    
}*/

//-----------------------

/*
//modificar el codigo para imprimir la cadena al reves
let cadena = "hola campistas bienvenidos";
let cadenaInvertida=""
for (let i = cadena.length-1; i >= 0; i--) {
  //console.log(cadena[i]);
  cadenaInvertida+=cadena[i];
}
console.log(cadenaInvertida);
*/

//-----------------------

//modificar para que imprima la cadena sin espacios 
/*
let cadena = "hola campistas bienvenidos";
let cadenaInvertida = ""
for (let i = cadena.length - 1; i >= 0; i--) {
  if (cadena[i] !== " ") {
    cadenaInvertida += cadena[i];
  }
}
console.log(cadenaInvertida);
*/

//-----------------------

//modificar para imprimir la cadena e imprimir el carater # en lugar de las vocales

let cadena = "hola campistas bienvenidos";
let cadenaInvertida = ""
for (let i = cadena.length - 1; i >= 0; i--) {
  if (cadena[i] !== " ") {
    if (cadena[i] !== "a" && cadena[i] !== "e" && cadena[i] !== "i" && cadena[i] !== "o" && cadena[i] !== "u") {
      cadenaInvertida += cadena[i];
    } else {
      cadenaInvertida += "#";
    }

  }
}
console.log(cadenaInvertida);

/*
let cadena = "hola campistas bienvendios";
let resultado = "";

for (let i = cadena.length - 1; i >= 0; i--) {
  let caracter = cadena[i];
  if (cadena[i] !== " ") {
    if ("aeiou".includes(cadena[i])) {
      resultado += "#"; // Reemplaza vocal por #
    } else {
      resultado += caracter; // Mantiene consonantes
    }
  }
}

console.log(resultado);
*/
