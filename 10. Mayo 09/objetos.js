const productos = {
  nombre: "Manzana",
  precio: 5,
  codigo: "01",
  disponible: true,
  incremarValor: function (valor) {
    this.precio += valor;
  }
}
console.log(productos);

productos.cantidad=5;
console.log(productos);

console.log(productos.precio);
console.log(productos.nombre);
console.log(productos.disponible);
console.log(productos.codigo);
productos.incremarValor(5);
console.log(productos["precio"]);

