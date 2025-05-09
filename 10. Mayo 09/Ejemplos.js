// ejemplo declaracion variable tipo de dato primitivo permite cambiar valores

let Equipo = "Nacional";
Equipo = "Junior";
console.log(Equipo);

// ejemplo declaracion variable tipo de dato estructurado permite cambiar valores

let Frutas = ["manzana","pera"];
Frutas.push("Banana")
console.log(Frutas);


// ejemplo declaracion constante tipo de dato estructurado permite cambiar valores

const edades = [52,36,39];
edades.push(12);
console.log(edades);


// ejemplo declaracion constante tipo de dato primitivo permite cambiar valores
/*
const nombre = "Hever";
nombre = "Hever Torres Delanoys";*/

//ejemplo llenado de vector

const estratos = [];
let n=0;

console.log(estratos);
while(n<10){
  estratos.push(parseInt(Math.random()*10))
  n++;
}
console.log(estratos);

// recorrer un arreglo con su propio metodo sin un ciclo externo

estratos.forEach(function(estrato, indice){
  console.log(estrato + " " + indice + " desde forEach");  
})


// ejemplo copiar arreglo

let paises = ["Colombia","Ecuador","Panama","Perú","Argentina","USA"];
console.log(paises);
let paisesConIdiomaEspañol=paises.slice(1,3);
console.log(paisesConIdiomaEspañol);