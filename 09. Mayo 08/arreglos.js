/*let arreglo = [1, 2, 3, 4, 5];
console.log(arreglo);
arreglo = ["manzana", "pera", "fresa"];
console.log(arreglo);*/
//arreglo = ["manzana", 1, true, [1, 2, 2, 4, 3, ["Uno", "Dos", [1, 9, 8]]]];
/*
console.log(arreglo);
for (const element of arreglo) {
  console.log(element);  
}
console.log(arreglo[2]);*/
//imprimir el numero 3 del cuarto elemento
//console.log(arreglo[3][5][2][1]);


let arreglo2D = [[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]];
/*console.log(arreglo2D[2][2]);//9
console.log(arreglo2D[1][1]);//5*/


let arreglo3D = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]];
/*//imprimir el 6
console.log(arreglo3D[1][0][1]);
//imprimir el 3
console.log(arreglo3D[0][1][0]);
//imprimir el 8
console.log(arreglo3D[1][1][1]);*/

//recorrer los elementos
/*
for (let i = 0; i < arreglo2D.length; i++) {
  for (let j = 0; j < arreglo2D[i].length; j++) {
    console.log(arreglo2D[i][j]);
  }
}*/

for (let i = 0; i < arreglo3D.length; i++) {
  for (let j = 0; j < arreglo3D[i].length; j++) {
    for (let k = 0; k < arreglo3D[j].length; k++) {
      console.log(arreglo3D[i][j][k]);
    }
  }
}
console.log(arreglo3D[0][0]);



