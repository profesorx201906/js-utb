console.log("Antes de crear la funcion");

//función -> retorna valor
/*function sumar(a, b) {
  return a + b;//tiene metodo return
}*/

//cambiar la funcion sumar por una funcion flecha
const sumar = (a, b) => {
  return a + b;
}
console.log(sumar(5, 6));
let suma = sumar(10, 20);
console.log(suma);
console.log(sumar(8, 6));
console.log(sumar(5, 45));
console.log(sumar(51, 3));
console.log(sumar(50, 60));
console.log(sumar(15, 26));

console.log("después de crear la funcion");

//procedimiento -> No Retorna Valor
function saludar(nombre) {
  console.log(`Hola ${nombre} Bienvenido`);
}
saludar("Jose")
let saludo = saludar("Dayana")
console.log(saludo);


//crear una funcion que haye el mayor de 3 numeros
function numeroMayor(num1, num2, num3) {
  let mayor;
  if (num1 > num2 && num1 > num3) {
    mayor = num1;
  } else if (num2 > num1 && num2 > num3) {
    mayor = num2;
  } else {
    mayor = num3
  }
  return mayor;
}
console.log(numeroMayor(10, 5, 14));
//otra forma de declarar funcion asignando a una constante o variable
const numeroMayorV1 = function (num1, num2, num3) {
  let mayor;
  if (num1 > num2 && num1 > num3) {
    mayor = num1;
  } else if (num2 > num1 && num2 > num3) {
    mayor = num2;
  } else {
    mayor = num3
  }
  return mayor;
}
console.log(numeroMayorV1(10, 50, 14));

//declar una funcion flecha
const numeroMayorV2 = (num1, num2, num3) => {
  let mayor;
  if (num1 > num2 && num1 > num3) {
    mayor = num1;
  } else if (num2 > num1 && num2 > num3) {
    mayor = num2;
  } else {
    mayor = num3
  }
  return mayor;
}
console.log(numeroMayorV2(100, 50, 14));


//ejemplo de parametro o argumento tipo array

const imprimirArreglo = (array) => {
  for (const element of array) {
    console.log(element);
  }
}
function imprimirArregloV2(array) {
  for (const element of array) {
    console.log(element);
  }
}
let frutas = ["manzana","pera","banana"];
let numeros = [5,6,9,3];
imprimirArreglo(frutas);
imprimirArregloV2(numeros);