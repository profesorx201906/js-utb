console.log("Antes de crear la funcion");

//función -> retorna valor
function sumar (a,b){
  return a+b;//tiene metodo return
}

console.log(sumar(5,6));
let suma = sumar(10,20);
console.log(suma);
console.log(sumar(8,6));
console.log(sumar(5,45));
console.log(sumar(51,3));
console.log(sumar(50,60));
console.log(sumar(15,26));

console.log("después de crear la funcion");

//procedimiento -> No Retorna Valor
function saludar(nombre){
  console.log(`Hola ${nombre} Bienvenido`);  
}
saludar("Jose")
let saludo = saludar("Dayana")
console.log(saludo);



